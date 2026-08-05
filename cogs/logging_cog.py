import discord
from discord.ext import commands

import config


def log_channel(guild: discord.Guild, key: str):
    return guild.get_channel(config.LOG_CHANNELS.get(key))


class LoggingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ── Join / Leave ─────────────────────────────────────────
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        ch = log_channel(member.guild, "join_leave")
        if not ch:
            return
        embed = discord.Embed(
            title="📥 Νέο Μέλος",
            description=f"{member.mention} ({member})",
            color=config.COLOR_JOIN,
        )
        embed.add_field(name="Λογαριασμός δημιουργήθηκε", value=discord.utils.format_dt(member.created_at, "R"))
        embed.add_field(name="Μέλη τώρα", value=str(member.guild.member_count))
        embed.set_thumbnail(url=member.display_avatar.url)
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        ch = log_channel(member.guild, "join_leave")
        if not ch:
            return
        embed = discord.Embed(
            title="📤 Αποχώρησε Μέλος",
            description=f"{member.mention} ({member})",
            color=config.COLOR_LEAVE,
        )
        roles = [r.mention for r in member.roles if r != member.guild.default_role]
        embed.add_field(name="Ρόλοι", value=", ".join(roles) if roles else "—", inline=False)
        embed.add_field(name="Μέλη τώρα", value=str(member.guild.member_count))
        embed.set_thumbnail(url=member.display_avatar.url)
        await ch.send(embed=embed)

    # ── Role changes ─────────────────────────────────────────
    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        ch = log_channel(after.guild, "role")
        if not ch:
            return

        before_roles = set(before.roles)
        after_roles = set(after.roles)

        added = after_roles - before_roles
        removed = before_roles - after_roles

        if not added and not removed:
            return

        embed = discord.Embed(title="🎭 Αλλαγή Ρόλων", description=f"{after.mention} ({after})", color=config.COLOR_ROLE)
        if added:
            embed.add_field(name="➕ Προστέθηκαν", value=", ".join(r.mention for r in added), inline=False)
        if removed:
            embed.add_field(name="➖ Αφαιρέθηκαν", value=", ".join(r.mention for r in removed), inline=False)
        await ch.send(embed=embed)

    # ── Voice ─────────────────────────────────────────────────
    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        ch = log_channel(member.guild, "voice")
        if not ch:
            return

        if before.channel is None and after.channel is not None:
            embed = discord.Embed(
                title="🔊 Μπήκε σε Voice",
                description=f"{member.mention} → {after.channel.mention}",
                color=config.COLOR_VOICE,
            )
            await ch.send(embed=embed)
        elif before.channel is not None and after.channel is None:
            embed = discord.Embed(
                title="🔇 Βγήκε από Voice",
                description=f"{member.mention} ← {before.channel.mention}",
                color=config.COLOR_VOICE,
            )
            await ch.send(embed=embed)
        elif before.channel != after.channel and before.channel and after.channel:
            embed = discord.Embed(
                title="🔀 Άλλαξε Voice Κανάλι",
                description=f"{member.mention}: {before.channel.mention} → {after.channel.mention}",
                color=config.COLOR_VOICE,
            )
            await ch.send(embed=embed)

    # ── Messages ─────────────────────────────────────────────
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author.bot or not message.guild:
            return
        ch = log_channel(message.guild, "message")
        if not ch:
            return
        embed = discord.Embed(
            title="🗑️ Διαγράφηκε Μήνυμα",
            description=f"**Κανάλι:** {message.channel.mention}\n**Χρήστης:** {message.author.mention}",
            color=config.COLOR_MESSAGE,
        )
        if message.content:
            embed.add_field(name="Περιεχόμενο", value=message.content[:1024], inline=False)
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.author.bot or not before.guild or before.content == after.content:
            return
        ch = log_channel(before.guild, "message")
        if not ch:
            return
        embed = discord.Embed(
            title="✏️ Επεξεργάστηκε Μήνυμα",
            description=f"**Κανάλι:** {before.channel.mention}\n**Χρήστης:** {before.author.mention}\n[Μετάβαση στο μήνυμα]({after.jump_url})",
            color=config.COLOR_MESSAGE,
        )
        embed.add_field(name="Πριν", value=(before.content or "—")[:1024], inline=False)
        embed.add_field(name="Μετά", value=(after.content or "—")[:1024], inline=False)
        await ch.send(embed=embed)

    # ── Channels ─────────────────────────────────────────────
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        ch = log_channel(channel.guild, "channel")
        if not ch:
            return
        embed = discord.Embed(title="➕ Νέο Κανάλι", description=f"{channel.mention} ({channel.type})", color=config.COLOR_CHANNEL)
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        ch = log_channel(channel.guild, "channel")
        if not ch:
            return
        embed = discord.Embed(title="➖ Διαγράφηκε Κανάλι", description=f"#{channel.name} ({channel.type})", color=config.COLOR_CHANNEL)
        await ch.send(embed=embed)

    # ── Commands ─────────────────────────────────────────────
    @commands.Cog.listener()
    async def on_command_completion(self, ctx: commands.Context):
        if not ctx.guild:
            return
        ch = log_channel(ctx.guild, "commands")
        if not ch:
            return
        embed = discord.Embed(
            title="⚙️ Εντολή Χρησιμοποιήθηκε",
            description=f"**Χρήστης:** {ctx.author.mention}\n**Εντολή:** `{ctx.message.content}`\n**Κανάλι:** {ctx.channel.mention}",
            color=config.COLOR_COMMAND,
        )
        await ch.send(embed=embed)

    @commands.Cog.listener()
    async def on_app_command_completion(self, interaction: discord.Interaction, command):
        if not interaction.guild:
            return
        ch = log_channel(interaction.guild, "commands")
        if not ch:
            return
        embed = discord.Embed(
            title="⚙️ Slash Command Χρησιμοποιήθηκε",
            description=f"**Χρήστης:** {interaction.user.mention}\n**Εντολή:** `/{command.qualified_name}`\n**Κανάλι:** {interaction.channel.mention}",
            color=config.COLOR_COMMAND,
        )
        await ch.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(LoggingCog(bot))
