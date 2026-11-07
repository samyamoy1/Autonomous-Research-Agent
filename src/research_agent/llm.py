
import os
from dotenv import load_dotenv
from google import genai
from groq import Groq
from ollama import Client

load_dotenv()


def generate_response(system_prompt, user_prompt):

    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0,
            max_tokens=2048
        )

        return response.choices[0].message.content

    elif provider == "ollama":

        client = Client(host="http://localhost:11434")

        response = client.chat(
            model="qwen2.5:1.5b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            options={
                "temperature": 0,
                "num_predict": 600,
                "num_ctx": 2048
            }
        )

        return response["message"]["content"]

    elif provider == "gemini":

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        client = genai.Client(api_key=api_key)

        response = client.interactions.create(
            model="gemini-3.8-flash",
            system_instruction=system_prompt,
            input=user_prompt,
            generation_config={
                "max_output_tokens": 4096,
                "thinking_level": "low"
            }
        )

        if response.status != "completed":
            raise RuntimeError("Gemini response incomplete")

        return response.output_text

    else:
        raise ValueError(f"Unknown LLM provider: {provider}")
