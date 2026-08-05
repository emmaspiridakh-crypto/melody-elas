"""
Όλα τα IDs / ρυθμίσεις του bot σε ένα σημείο.
Συμπλήρωσε τα με τα πραγματικά IDs του server σου πριν το τρέξεις.
"""

# ─── Βασικά ────────────────────────────────────────────────
GUILD_ID = 000000000000000000

OWNER_ID = 000000000000000000          # ID του αρχηγού (για !dmall)
ADMIN_ROLE_ID = 000000000000000000     # role του διοικητή που έχει δικαίωμα !dmall

# ─── Ticket System ─────────────────────────────────────────
TICKET_CATEGORY_ID = 000000000000000000   # κατηγορία μέσα στην οποία θα ανοίγουν τα tickets

# Ρόλοι που βλέπουν κάθε τύπο ticket
STAFF_ROLE_ID = 000000000000000000        # βλέπει τα "Support" tickets
ANOTATH_DIOIKISI_ROLE_ID = 000000000000000000  # βλέπει τα "Επικοινωνία Διοίκησης" tickets

# Emoji (placeholders — αντικατέστησέ τα με τα δικά σου custom emojis)
EMOJI_SUPPORT = "<:support:0000000000000000>"
EMOJI_CONTACT = "<:contact:0000000000000000>"
EMOJI_CLOSE = "<:close:0000000000000000>"
EMOJI_PING = "<:ping:0000000000000000>"
EMOJI_TICKET = "<:ticket:0000000000000000>"
EMOJI_DUTY_ON = "<:duty_on:0000000000000000>"
EMOJI_DUTY_OFF = "<:duty_off:0000000000000000>"
EMOJI_LIST = "<:list:0000000000000000>"
EMOJI_LEADERBOARD = "<:leaderboard:0000000000000000>"
EMOJI_CLOCK = "<:clock:0000000000000000>"

# Thumbnail/εικόνα για τα panels (URLs — άλλαξέ τα)
TICKET_PANEL_THUMBNAIL = "https://i.imgur.com/placeholder1.png"
DUTY_PANEL_THUMBNAIL = "https://i.imgur.com/placeholder2.png"

# Banner που εμφανίζεται πάνω-πάνω στο ticket panel
TICKET_PANEL_BANNER = "https://i.imgur.com/placeholder_banner.png"

# ─── Duty System ────────────────────────────────────────────
ON_DUTY_ROLE_ID = 000000000000000000   # ο role που παίρνει κάποιος όταν πατάει ON

# ─── Logs — βάλε το ID του αντίστοιχου text channel για κάθε κατηγορία ──────
LOG_CHANNELS = {
    "join_leave": 000000000000000000,
    "role": 000000000000000000,
    "voice": 000000000000000000,
    "message": 000000000000000000,
    "channel": 000000000000000000,
    "commands": 000000000000000000,
    "dmall": 000000000000000000,
    "ticket": 000000000000000000,
}

# Χρώματα embeds (μπορείς να τα αλλάξεις ελεύθερα)
COLOR_JOIN = 0x57F287
COLOR_LEAVE = 0xED4245
COLOR_ROLE = 0xFEE75C
COLOR_VOICE = 0x5865F2
COLOR_MESSAGE = 0xEB459E
COLOR_CHANNEL = 0xF57C00
COLOR_COMMAND = 0x99AAB5
COLOR_DMALL = 0x2ECC71
COLOR_TICKET = 0x3498DB

# ─── Database (Turso) ───────────────────────────────────────
# Βάζονται μέσω environment variables (.env / Render):
# TURSO_DATABASE_URL=libsql://xxxx.turso.io
# TURSO_AUTH_TOKEN=xxxxx
