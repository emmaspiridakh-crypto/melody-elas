import asyncio
import logging
import discord
from discord.ext import commands

import config

log = logging.getLogger("dmall")


def is_owner_or_admin():
    async def predicate(ctx: commands.Context) -> bool:
        if ctx.author.id == config.OWNER_ID:
            return True
        role = ctx.guild.get_role(config.ADMIN_ROLE_ID) if ctx.guild else None
        return role is not None and role in ctx.author.roles
    return commands.check(predicate)


class DMAll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="dmall")
    @is_owner_or_admin()
    async def dmall(self, ctx: commands.Context, *, message: str):
        guild = ctx.guild
        sent, failed = 0, 0

        status_msg = await ctx.send(f"Στέλνετε περίμενε μπαγάσα")

        embed = discord.Embed(
            title=f"📢 Μήνυμα από {guild.name}",
            description=message,
            color=config.COLOR_DMALL,
        )

        for member in guild.members:
            if member.bot:
                continue
            try:
                await member.send(embed=embed)
                sent += 1
            except discord.Forbidden:
                failed += 1
            except discord.HTTPException:
                failed += 1
            await asyncio.sleep(0.7) 

        await status_msg.edit(content=f"✅ Ολοκληρώθηκε. Στάλθηκαν: **{sent}** | Απέτυχαν: **{failed}**")

        self.bot.dispatch("dmall_sent", ctx, sent, failed, message)

    @dmall.error
    async def dmall_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("❌ Δεν έχεις δικαίωμα να χρησιμοποιήσεις αυτή την εντολή.")
        else:
            log.error(f"dmall error: {error}")


async def setup(bot: commands.Bot):
    await bot.add_cog(DMAll(bot))
