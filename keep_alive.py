"""
Keep-alive Flask server.
Render χρειάζεται ένα open port για να θεωρήσει το service "healthy" (Web Service),
και το UptimeRobot θα κάνει ping σε αυτό το endpoint κάθε λίγα λεπτά ώστε
να μην κοιμάται/σβήνει το process.
"""

import os
import logging
from threading import Thread
from flask import Flask

log = logging.getLogger("keep_alive")

app = Flask(__name__)

# Απενεργοποιούμε τα logs του Flask/werkzeug για να μη γεμίζει το console
werkzeug_log = logging.getLogger("werkzeug")
werkzeug_log.setLevel(logging.ERROR)


@app.route("/")
def home():
    return "Bot is alive!", 200


@app.route("/ping")
def ping():
    # Endpoint ειδικά για UptimeRobot
    return "pong", 200


@app.route("/health")
def health():
    return {"status": "ok"}, 200


def run():
    # Render δίνει το πραγματικό port μέσω env var PORT.
    # Αν δεν υπάρχει (π.χ. τοπικά), πέφτουμε σε ένα "fake" port 10000
    # μόνο και μόνο για να ανοίγει κάτι και να μη killάρει το Render το container.
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
    log.info("Keep-alive Flask server started.")
