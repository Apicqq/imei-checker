from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Class which contains all the app settings."""

    model_config = SettingsConfigDict(env_file=".env")
    api_token: str = "your_api_token"
    white_list_user_ids: list[int] = None
    imeicheck_url: str = "https://api.imeicheck.net/v1/checks"
    imeicheck_token: str = "your_imeicheck_token"
    imeicheck_service_id: int = 12


settings = Settings()