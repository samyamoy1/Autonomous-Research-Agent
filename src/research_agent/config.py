
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "Autonomous Research Agent"
    max_research_rounds: int = 3
    max_sources: int = 10
    output_directory: str = "reports"


settings = Settings()
