from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    api_token: str = "your_api_token"
    white_list_user_ids: list[int] = None


settings = Settings()