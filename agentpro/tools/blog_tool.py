from .base_tool import Tool
from agentpro.tools.duckduckgo_tool import QuickInternetTool
from typing import Any

class BlogRecommendationTool(Tool):
    name: str = "Blog Recommendation"
    description: str = "Finds latest blog articles for a topic using internet search."
    action_type: str = "blog_recommendation"
    input_format: str = "A string with the topic name."

    def run(self, input_text: Any) -> str:
        topic = str(input_text)
        search_query = f"best blogs about {topic} programming"
        search_tool = QuickInternetTool()
        web_results = search_tool.run(search_query)
        return web_results
