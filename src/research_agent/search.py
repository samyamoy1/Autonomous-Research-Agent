import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def get_search_client():
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        raise ValueError("TAVILY_API_KEY not found in .env")

    return TavilyClient(api_key=api_key)


def search_web(query, max_results=5):
    client = get_search_client()

    response = client.search(
        query=query,
        max_results=max_results
    )

    return response["results"]
