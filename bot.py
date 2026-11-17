import os
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from wzgram import Client, filters, enums
from wzgram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

MESSAGE = os.environ.get(
    "MESSAGE", "<b>Use my alt:</b>\n<i>@xyzbot</i>"
).replace("\\n", "\n")
PICS = os.environ.get("PIC", "").split()
BUTTON_TEXT = os.environ.get("BUTTON_TEXT", "")
BUTTON_LINK = os.environ.get("BUTTON_LINK", "")


def get_markup():
    if not BUTTON_TEXT or not BUTTON_LINK:
        return None
    btn = InlineKeyboardButton(
        BUTTON_TEXT, url=BUTTON_LINK, style=enums.ButtonStyle.DANGER
    )
    return InlineKeyboardMarkup([[btn]])


class Health(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, *args):
        pass


def run_web():
    HTTPServer(("0.0.0.0", int(os.environ.get("PORT", 8080))), Health).serve_forever()


app = Client("FallbackBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(
    filters.text & filters.incoming & (filters.private | filters.group) & ~filters.bot
)
async def notice(c, m):
    markup = get_markup()
    try:
        if PICS:
            await m.reply_photo(
                random.choice(PICS),
                caption=MESSAGE,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=markup,
            )
        else:
            await m.reply_text(
                MESSAGE,
                parse_mode=enums.ParseMode.HTML,
                disable_web_page_preview=True,
                reply_markup=markup,
            )
    except Exception as e:
        print(e)


threading.Thread(target=run_web, daemon=True).start()
app.run()
