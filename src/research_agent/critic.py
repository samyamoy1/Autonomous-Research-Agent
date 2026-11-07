
import json
from research_agent.llm import generate_response
import re


CRITIC_SYSTEM_PROMPT = """
You are a research quality evaluator.

Your job is to evaluate whether the collected research
is sufficient to answer the given research topic.

Evaluate these criteria:
1. Topic coverage
2. Completeness of information
3. Reliability and relevance of sources
4. Presence of useful evidence and explanations
5. Important missing areas

Be strict. Do not mark research as sufficient
if important information is missing.

Return ONLY valid JSON in this exact structure:

{
    "research_quality": "sufficient or insufficient",
    "missing_areas": [],
    "feedback": "Your evaluation",
    "additional_search_queries": []
}
"""


def evaluate_research(topic, sources):

    research_content = ""

    for i, source in enumerate(sources[:10], start=1):
        research_content += f"""
Source {i}:
Title: {source['title']}
URL: {source['url']}
Content: {source['content'][:500]}

"""

    user_prompt = f"""
Research Topic:
{topic}

Collected Research:
{research_content}

Evaluate the quality and completeness of this research.

Important:
- If important information is missing, mark it insufficient.
- If research is sufficient, use an empty missing_areas list.
- If insufficient, suggest additional search queries.
- Return only valid JSON.
"""
    response = generate_response(
       CRITIC_SYSTEM_PROMPT,
       user_prompt
    )

    print("\n========== RAW CRITIC RESPONSE ==========")
    print(response)
    
    # Remove Markdown code block markers if present.
    response = response.strip()

    response = re.sub(
        r"^```(?:json)?\s*",
        "",
        response,
        flags=re.IGNORECASE
    )

    response = re.sub(
        r"\s*```$",
        "",
        response
    )

    try:
        evaluation = json.loads(response)

    except json.JSONDecodeError:
        raise ValueError(
            "Critic returned invalid JSON:\n" + response
        )

    required_keys = [
        "research_quality",
        "missing_areas",
        "feedback",
        "additional_search_queries"
    ]

    for key in required_keys:
        if key not in evaluation:
            raise ValueError(
                f"Critic response is missing key: {key}"
            )

    if evaluation["research_quality"] not in [
        "sufficient",
        "insufficient"
    ]:
        raise ValueError("Invalid research_quality value")

    return evaluation
