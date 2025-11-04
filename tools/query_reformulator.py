"""Simple query reformulator tool for Synaptic Sidekick.

This tool generates a small set of query reformulations/paraphrases intended to
expand recall for the retriever. It implements lightweight, deterministic
heuristics (no external LLM calls) so it can be used offline and cheaply.

The generated queries include the original query plus common research-focused
reformulations (e.g., adding 'overview', 'recent advances', citation/source
filters like site:arxiv.org). Keep the output small (3-6 rewrites) to avoid
excessive downstream retrieval costs.
"""

from typing import List

from smolagents import Tool


class QueryReformulator(Tool):
    name = "query_reformulator"
    description = (
        "Generate a small list of reformulations / paraphrases for a natural-language query. "
        "Useful to expand retrieval recall when searching academic sources."
    )
    inputs = {
        "query": {"type": "string", "description": "Original user query."},
        "num_rewrites": {
            "type": "integer",
            "description": "Maximum number of reformulations to return (excluding original).",
            "default": 3,
            "nullable": True,
        },
    }
    output_type = "array"

    def __init__(self) -> None:
        super().__init__()

    def forward(self, query: str, num_rewrites: int = 3) -> List[str]:
        """Return a list of reformulated queries.

        The return list always includes the original query as the first element
        followed by up to `num_rewrites` variations.
        """
         # Normalize num_rewrites
        try:
            n = int(num_rewrites) if num_rewrites is not None else 3
        except Exception:
            n = 3
        n = max(0, min(10, n))  # cap to reasonable range

        base = query.strip()
        variations: List[str] = [base]

        # Heuristic reformulations useful for academic/research retrieval
        candidates = [
            f"{base} overview",
            f"{base} review",
            f"recent advances in {base}",
            f"{base} tutorial",
            f"{base} site:arxiv.org",
            f"{base} site:paperswithcode.com",
            f"{base} 2023..2025",
            f"{base} survey",
            f"{base} methods results",
            f"{base} applications",
        ]

        # Add candidates that are not duplicates and not identical to base
        for cand in candidates:
            if len(variations) - 1 >= n:
                break
            if cand not in variations:
                variations.append(cand)

        return variations
