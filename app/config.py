from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Settings(BaseSettings):
    bot_token: str = Field(alias="BOT_TOKEN")
    admin_ids_raw: str = Field(default="", alias="ADMIN_IDS")
    db_path: str = Field(default=str(BASE_DIR / "bot.db"), alias="DB_PATH")
    results_chat_id: int | None = Field(default=None, alias="RESULTS_CHAT_ID")
    port: int = Field(default=10000, alias="PORT")
    webhook_base_url: str = Field(default="", alias="WEBHOOK_BASE_URL")
    webhook_path: str = Field(default="/webhook", alias="WEBHOOK_PATH")
    webhook_secret: str = Field(default="proweb-exam-secret", alias="WEBHOOK_SECRET")

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def admin_ids(self) -> set[int]:
        if not self.admin_ids_raw.strip():
            return set()
        return {
            int(item.strip())
            for item in self.admin_ids_raw.split(",")
            if item.strip().isdigit()
        }

    @property
    def webhook_enabled(self) -> bool:
        return bool(self.webhook_base_url.strip())

    @property
    def webhook_url(self) -> str:
        return f"{self.webhook_base_url.rstrip('/')}{self.webhook_path}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
