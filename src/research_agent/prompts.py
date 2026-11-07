SYSTEM_PROMPT = """
You are an Autonomous Research Agent.

Your responsibilities:
1. Understand the research topic.
2. Explain complex topics clearly.
3. Be accurate and avoid inventing facts.
4. Admit when information is unavailable.
5. Organize your answers properly.
"""

def build_user_prompt(topic):
    return f"""
Research the following topic:

{topic}

Provide:
1. Introduction
2. Key concepts
3. Important findings
4. Conclusion
"""