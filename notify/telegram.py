import telegram
import logging
import keyring

logger = logging.getLogger(__name__)

def fetch_user():
    return keyring.get_credential("TelegramUser", "User").password


def fetch_apitoken():
    return keyring.get_credential("TelegramAPIToken", "Token").password


async def send_once(message_text):
    try:
        bot = telegram.Bot(token=fetch_apitoken())
        await bot.send_message(chat_id=fetch_user(), text=message_text)
        logger.info("Message sent successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")