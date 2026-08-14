"""
Όλα τα IDs / ρυθμίσεις του bot σε ένα σημείο.
Συμπλήρωσε τα με τα πραγματικά IDs του server σου πριν το τρέξεις.
"""

# ─── Βασικά ────────────────────────────────────────────────
GUILD_ID = 1511471695758626818

OWNER_ID = 1531030511970025664       # ID του αρχηγού (για !dmall)
ADMIN_ROLE_ID = 1531030518076932327  
AUTOROLE_ID = 1531030573647139008

# ─── Ticket System ─────────────────────────────────────────
TICKET_CATEGORY_ID = 1534475446492860426 
# Ρόλοι που βλέπουν κάθε τύπο ticket
STAFF_ROLE_ID =  1531030566479335426       # βλέπει τα "Support" tickets
ANOTATH_DIOIKISI_ROLE_ID = 1534468753968988190  # βλέπει τα "Επικοινωνία Διοίκησης" tickets

# Emoji (placeholders — αντικατέστησέ τα με τα δικά σου custom emojis)
EMOJI_SUPPORT = "<a:support:1534476690108186665>"
EMOJI_CONTACT = "<:contact:1534476798824415262>"
EMOJI_CLOSE = "<:close:1534476941594202243>"
EMOJI_PING = "<a:ping:1534477033017704529>"
EMOJI_TICKET = "<:ticket:1534477079377084536>"
EMOJI_DUTY_ON = "<a:duty_on:1534477124843475114>"
EMOJI_DUTY_OFF = "<a:duty_off:1534477144271360130>"
EMOJI_LIST = "<:list:1534477214047801344>"
EMOJI_LEADERBOARD = "<:leaderboard:1534480843274194954>"
EMOJI_CLOCK = "<:clock:1534480904637120545>"

# Thumbnail/εικόνα για τα panels (URLs — άλλαξέ τα)
TICKET_PANEL_THUMBNAIL = "https://i.imgur.com/0Vc7sWw.gif"
DUTY_PANEL_THUMBNAIL = "https://i.imgur.com/0Vc7sWw.gif"

# Banner που εμφανίζεται πάνω-πάνω στο ticket panel
TICKET_PANEL_BANNER = "https://i.imgur.com/jiBdco2.jpeg"

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

EMBED_COLOR = 0x3498db
# ─── Database (Turso) ───────────────────────────────────────
# Βάζονται μέσω environment variables (.env / Render):
# TURSO_DATABASE_URL=libsql://xxxx.turso.io
# TURSO_AUTH_TOKEN=xxxxx
