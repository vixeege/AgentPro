from .base_tool import Tool
import openai
import os
from typing import Any

class RoadmapTool(Tool):
    name: str = "Roadmap Generator"
    description: str = "Uses OpenAI to generate a learning roadmap for a topic."
    action_type: str = "roadmap"
    input_format: str = "A string with the topic name."

    def run(self, input_text: Any) -> str:
        topic = str(input_text)
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ARES_KEY")
        if not api_key:
            return "No OpenAI API key found in environment. Please set OPENAI_API_KEY or ARES_KEY."
        client = openai.OpenAI(api_key=api_key)
        prompt = (
            f"Create a detailed, step-by-step learning roadmap for mastering {topic} from beginner to advanced. "
            "Include suggested online courses, key concepts, and practical project ideas for each stage. Format with clear steps."
        )
        response = client.chat.completions.create(
            model="gpt-4o",  # Use "gpt-4" or "gpt-3.5-turbo" if "gpt-4o" is unavailable for your key
            messages=[
                {"role": "system", "content": "You are an expert career and curriculum advisor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
        )
        roadmap = response.choices[0].message.content
        return roadmap
