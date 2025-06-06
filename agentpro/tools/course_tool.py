from .base_tool import Tool
from agentpro.tools.duckduckgo_tool import QuickInternetTool
from typing import Any

class CourseRecommendationTool(Tool):
    name: str = "Course Recommendation"
    description: str = "Finds latest online courses (free and paid) for a topic using internet search."
    action_type: str = "course_recommendation"
    input_format: str = "A string with the topic name. Example: 'Python', 'Data Science'."

    def run(self, input_text: Any) -> str:
        topic = str(input_text)
        search_query = f"best online courses {topic} free paid"
        search_tool = QuickInternetTool()
        web_results = search_tool.run(search_query)
        # Summarize/clean results if needed (here: return directly for demonstration)
        return web_results
