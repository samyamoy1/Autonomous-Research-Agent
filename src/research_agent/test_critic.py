
from research_agent.critic import evaluate_research


topic = "Future of Generative AI"

sources = [
    {
        "title": "Generative AI Overview",
        "url": "https://example.com/overview",
        "content": """
        Generative AI creates new content such as text,
        images, audio and video. Large language models
        are widely used in chatbots and content generation.
        """
    },
    {
        "title": "Applications of Generative AI",
        "url": "https://example.com/applications",
        "content": """
        Generative AI is used in content creation,
        software development, education and business.
        """
    }
]


result = evaluate_research(topic, sources)

print("\n========== CRITIC EVALUATION ==========")
print("Quality:", result["research_quality"])
print("Missing Areas:", result["missing_areas"])
print("Feedback:", result["feedback"])
print("Additional Queries:", result["additional_search_queries"])
