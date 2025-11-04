from smolagents import ToolCallingAgent
import utilities, sys
from tools.vector_store import ChromaRetriever 
from tools.retrieval_tool import RetrieveDocumentsTool
from tools.web_tools import MachineLearningWebSearchTool
from tools.query_reformulator import QueryReformulator

retriever = ChromaRetriever(
    persist_directory="data/vector_store",
    collection_name="machine_learning_pdfs"
)
retrieval_tool = RetrieveDocumentsTool(retriever)

def build_agent()->ToolCallingAgent:
    model = utilities.google_build_reasoning_model()

    tools = [
        retrieval_tool,
        MachineLearningWebSearchTool(),
        QueryReformulator(),
    ]

    agent = ToolCallingAgent(
        tools = tools,
        model = model,
        verbosity_level = 2,
        stream_outputs = False,
        planning_interval = 2,
        instructions = """You are an agent programmed
        simply to help users learn about Machine Learning 
        concepts, topics, tools, and libraries."""
    )
    return agent

def main():
    if len(sys.argv)<2:
        print("Usage: python run_agent.py \"<your question about Machine Learning.>\"")
        return
    query = sys.argv[1]
    agent = build_agent()
    print("Query:", query)
    result = agent.run(query)
    print("\n-----------Final Answer-----------\n", result)

if __name__ == "__main__":
    main()