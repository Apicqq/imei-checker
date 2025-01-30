import logging
import json
import os

from telegram import ForceReply, Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

from utils.http_client import HttpClient
from utils.imei_verification import check_imei, Response

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

load_dotenv()

http_client = HttpClient()


def format_message(message: dict) -> str:
    """Format a dictionary into JSON dictionary with indentation."""
    formatted_json = json.dumps(message, indent=2, ensure_ascii=False)
    return f"```\n{formatted_json}\n```"


async def post_init(_: Application) -> None:
    """Initiate aiohttp session."""
    http_client.start()


async def post_stop(_: Application) -> None:
    """Stop aiohttp session after bot is stopped."""
    await http_client.stop()


async def verify_imei(update: Update, _: ContextTypes.DEFAULT_TYPE):
    """
    Check the IMEI of the device.

    before proceeding, checks, whether user is allowed to use the bot.
    """
    if update.effective_user.id not in map(
        int,
        os.getenv("WHITE_LIST_USER_IDS").split(","),
    ):
        await update.message.reply_html(
            "You are not allowed to use this bot.",
            reply_markup=ForceReply(selective=True),
        )
        return
    result: Response = await check_imei(
        update.message.text,
        http_client.session,
    )
    await update.message.reply_markdown(format_message(result.json))


def main() -> None:
    app = (
        Application.builder()
        .token(os.getenv("TELEGRAM_BOT_TOKEN"))
        .post_init(post_init)
        .post_stop(post_stop)
        .build()
    )
    app.add_handler(MessageHandler(filters.TEXT, verify_imei))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
