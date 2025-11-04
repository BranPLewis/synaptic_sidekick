# **Assignment: ReAct Agent with Tools and Retrieval**

## **Description**

In this assignment, you will create a **ReAct agent** that uses tools and retrieval to answer questions about **Machine Learning**.
Your agent will be called **Synaptic Sidekick**.

You will begin referencing your ReAct agent from the previous assignment, and the demo code from class and adapt them to serve as the Synaptic Sidekick.
This will involve redesigning the tools, modifying the prompts, collecting and ingesting relevant data, and ensuring the agent can meaningfully respond to machine learning related questions.

## **Learning Outcomes**

By completing this assignment, you will be able to:

- Implement a ReAct agent
- Collect relevant information sources
- Index sources in a vector database
- Retrieve relevant sources from a vector database
- Design and integrate agent tools
- Direct an agent to use tools effectively
- Customize an agent’s system prompt

## **Resources**

- **Starter Code:**
  Use your previous assignment's ReAct agent as a starter. Additionally, download the vector database related
  code from the class demo.
  
- **Specific Data:**
  Identify at least 10 relevant papers from [Machine Learning at arXiv](https://arxiv.org/list/cs.LG/recent).
  Download them and use them to populate your knowledge base.

## **Requirements**

- Running
  ```bash
  python3 run.py "My question about machine learning."
  ```  
  must trigger your agent to generate a response.

- Your agent should be able to handle a wide range of questions, such as:
  - "Describe reinforcement learning?"
  - "What is the variance-bias trade-off?"

- You *must* have a knowledge base implemented as a vector store with a tool
  for your agent to access the content. The agent *must* actually use the
  tool.
  

## **Deliverables**

Submit a single **.zip file** containing the following:

- Your project directory, named `synaptic-sidekick`, which includes:
  - All source files
  - `requirements.txt`
  - Any supporting data files
  *(Exclude API keys, compiled files, and virtual environments.)*

- A **report file** (`.pdf` or `.md`) that includes:
  - **Knowledge Added:** describe the content of the papers you selected
  - **Tools Added:** describe each tool, its purpose, and how it is used
  - **Prompts Modified:** outline any system or tool prompt changes
  - **Example Results:** show example user queries and responses
