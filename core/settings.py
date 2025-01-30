from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramBotSettings(BaseModel):
    """Class which contains all settings for telegram bot."""

    telegram_bot_token: str = "Your_telegram_bot_token"
    white_list_user_ids: str = "Your_white_list_user_ids, separated by comma"


class Settings(BaseSettings):
    """Class which contains all the app settings."""

    model_config = SettingsConfigDict(env_file=".env", extra="allow")
    api_token: str = "your_api_token"
    imeicheck_url: str = "https://api.imeicheck.net/v1/checks"
    imeicheck_token: str = "your_imeicheck_token"
    imeicheck_service_id: int = 12
    bot_config: TelegramBotSettings = TelegramBotSettings()


settings = Settings()
