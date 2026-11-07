
from research_agent.config import settings


def test_app_name():
    assert settings.app_name == "Autonomous Research Agent"


def test_max_research_rounds():
    assert settings.max_research_rounds > 0


def test_max_sources():
    assert settings.max_sources > 0
