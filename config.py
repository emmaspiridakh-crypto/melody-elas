"""
Όλα τα IDs / ρυθμίσεις του bot σε ένα σημείο.
Συμπλήρωσε τα με τα πραγματικά IDs του server σου πριν το τρέξεις.
"""

# ─── Βασικά ────────────────────────────────────────────────
GUILD_ID = 1511471695758626818

OWNER_ID = 1531030511970025664       # ID του αρχηγού (για !dmall)
ADMIN_ROLE_ID = 1531030518076932327     # role του διοικητή που έχει δικαίωμα !dmall

# ─── Ticket System ─────────────────────────────────────────
TICKET_CATEGORY_ID = 1534475446492860426  # κατηγορία μέσα στην οποία θα ανοίγουν τα tickets

# Ρόλοι που βλέπουν κάθε τύπο ticket
STAFF_ROLE_ID =  1531030566479335426       # βλέπει τα "Support" tickets
ANOTATH_DIOIKISI_ROLE_ID = 1534468753968988190  # βλέπει τα "Επικοινωνία Διοίκησης" tickets

# Emoji (placeholders — αντικατέστησέ τα με τα δικά σου custom emojis)
EMOJI_SUPPORT = "<:support:>"
EMOJI_CONTACT = "<:contact:>"
EMOJI_CLOSE = "<:close:>"
EMOJI_PING = "<:ping:>"
EMOJI_TICKET = "<:ticket:>"
EMOJI_DUTY_ON = "<:duty_on:>"
EMOJI_DUTY_OFF = "<:duty_off:>"
EMOJI_LIST = "<:list:>"
EMOJI_LEADERBOARD = "<:leaderboard:>"
EMOJI_CLOCK = "<:clock:>"

# Thumbnail/εικόνα για τα panels (URLs — άλλαξέ τα)
TICKET_PANEL_THUMBNAIL = ""
DUTY_PANEL_THUMBNAIL = ""

# Banner που εμφανίζεται πάνω-πάνω στο ticket panel
TICKET_PANEL_BANNER = ""

# ─── Duty System ────────────────────────────────────────────
ON_DUTY_ROLE_ID = 1534475721920090193   # ο role που παίρνει κάποιος όταν πατάει ON

# ─── Logs — βάλε το ID του αντίστοιχου text channel για κάθε κατηγορία ──────
LOG_CHANNELS = {
    "join_leave": 1531030862169243849,
    "role": 1531030872415797288,
    "voice": 1531030865407377540,
    "message": 1531030863809220760,
    "channel": 1531030874135462111,
    "commands": 1531030859321180344,
    "dmall": 1531030859321180344,
    "ticket": 1531030867106074674,
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
