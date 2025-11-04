from smolagents import Tool, DuckDuckGoSearchTool
from typing import List
        
class MachineLearningWebSearchTool(Tool):
    name = "Utah_Tech_University_website_search"
    description = (
        "Searches through all Utah Tech University's website for a query."
        "Course titles, URL's."
    )
    inputs = {"query": {"type":"string","description":"HTTP/HTTPS URL to fetch"}}
    output_type = "string"

    def __init__(self, sites: List[str] = None):
        super().__init__()
        self._ddgs = DuckDuckGoSearchTool()
        if sites is None:
            sites = ["https://www.kaggle.com", "https://www.kdnuggets.com", "https://www.deeplearning.ai", "https://huggingface.co", "https://arxiv.org/list/cs.LG/recent"]
            self.sites = sites
        else:
            self.sites = sites

    def forward(self, query: str) -> str:
        site_filter = [f"site:{site}" for site in self.sites]
        site_query = f"({' OR '.join(site_filter)})"
        query = f"{site_query} {query}"
        return self._ddgs(query)