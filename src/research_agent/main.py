
from research_agent.logger import setup_logger

logger = setup_logger()


def display_banner():
    print("=" * 55)
    print("          AUTONOMOUS RESEARCH AGENT")
    print("=" * 55)
    print("Your AI-powered research assistant")
    print("=" * 55)


def get_research_topic():
    topic = input("\nEnter a research topic: ").strip()

    if not topic:
        print("\n[ERROR] Please enter a valid topic.")
        logger.warning("Empty research topic received.")
        return None

    return topic


def main():
    display_banner()

    logger.info("Application started.")

    topic = get_research_topic()

    if topic is None:
        return

    logger.info("Research topic received: %s", topic)

    print("\n[Agent] Research topic received!")
    print(f"[Agent] Topic: {topic}")

    print("\n[Agent] Research functionality will be added in later phases.")

    logger.info("Application completed.")


if __name__ == "__main__":
    main()
