"""Module for starting the bot."""

import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from configs import settings

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler.

    Args:
        update (Update): Telegram update.
        context (ContextTypes.DEFAULT_TYPE): Telegram context.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!",
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(settings.telegram.token).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    if settings.telegram.webhook_mode:
        logger.info("Starting bot (webhook mode)...")
        application.run_webhook(
            host=settings.telegram.webhook_host,
            port=settings.telegram.webhook_port,
            webhook_url=settings.telegram.webhook_url,
            secret_token=settings.telegram.secret_token,
        )

    logger.info("Starting bot (polling mode)...")
    application.run_polling()
