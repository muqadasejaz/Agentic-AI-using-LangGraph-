# 🤖 Agentic AI with LangGraph

This repository documents my journey into **Agentic AI and workflow-based AI systems** using **LangGraph**.  
It covers the transition from **Generative AI to autonomous AI agents**, focusing on **system design, workflows, and real-world applications**.

The repository emphasizes both **conceptual clarity and practical understanding**, helping build intelligent systems that can **plan, reason, and execute tasks autonomously**.

---

# 🗂️ Table of Contents

### 01: Generative AI vs Agentic AI
- What is Generative AI?  
- Limitations of Generative AI (reactive nature)  
- Introduction to Agentic AI  
- Key differences and evolution  

### 02: What is Agentic AI?
- Definition and core idea  
- Characteristics: autonomy, proactivity, adaptability  
- Components of an AI agent  
- Real-world examples (e.g., AI recruiter, automation agents)  

### 03: LangChain vs LangGraph
- Overview of LangChain  
- Limitations of linear chains  
- Introduction to LangGraph  
- When to use LangChain vs LangGraph  

### 04: LangGraph Core Concepts
- Nodes (tasks/functions)  
- Edges (flow control)  
- State management  
- Graph-based execution model  

### 05: Sequential Workflows in LangGraph
- Step-by-step execution  
- Linear pipelines  
- Use cases and implementation logic  

### 06: Parallel Workflows in LangGraph
- Running multiple tasks simultaneously  
- Performance optimization  
- Use cases and examples  

### 07: Conditional Workflows in LangGraph
- Decision-based execution  
- Dynamic branching  
- Handling different scenarios  

### 08: Iterative Workflows in LangGraph
- Loops and repeated execution  
- Feedback-driven improvements  
- Self-correcting agents  

### 09: Persistence in LangGraph
- Saving and restoring workflow state  
- Checkpointing execution progress  
- Resuming workflows after failure or interruption  
- Long-running agent support (multi-step processes over time)  
- Real-world use cases (HR pipelines, approvals, long research tasks)  

### 10: Streaming in LangGraph
- Real-time output generation during execution  
- Step-by-step response streaming to users  
- Improving user experience in agent applications  
- Debugging and monitoring intermediate states  
- Use cases: chat agents, live assistants, interactive workflows  

### 11: Observability in LangGraph
- Tracking execution of nodes and edges  
- Monitoring state transitions  
- Debugging complex workflows  
- Logging and tracing agent decisions  
- Integration with observability tools for production systems  
- Essential for enterprise-grade AI agents  

### 12: Tools in LangGraph
- Tool calling and external integrations  
- Using APIs, databases, and Python functions  
- Tool-enabled AI agents  
- Dynamic decision-making using tools  
- Real-world examples of tool-augmented agents  

### 13: MCP Client using LangGraph
- Introduction to Model Context Protocol (MCP)  
- Connecting AI agents with external MCP servers  
- Accessing tools, resources, and prompts dynamically  
- Building interoperable AI systems using MCP clients  
- Real-world integrations and workflows  

### 14: Retrieval-Augmented Generation (RAG)
- Introduction to RAG architecture  
- Combining retrieval systems with LLMs  
- Vector databases and embeddings  
- Context-aware question answering  
- Building document-aware AI agents  

### 15: Human-in-the-Loop (HITL)
- Human approval and intervention workflows  
- Interrupting and resuming execution  
- AI-human collaborative systems  
- Risk control and safety mechanisms  
- Enterprise approval pipelines and review systems  

### 16: SubGraphs in LangGraph
- Modular workflow architecture  
- Breaking large workflows into reusable components  
- Nested graphs and graph composition  
- Multi-agent coordination using subgraphs  
- Building scalable enterprise AI systems

 #### Types of SubGraphs
- Shared State SubGraphs  
  - Parent graph and subgraph share the same state  
  - Useful for tightly connected workflows  
  - Enables direct state updates across components  

- Independent State SubGraphs  
  - Subgraph maintains its own isolated state  
  - Parent and subgraph communicate through input/output mappings  
  - Useful for modular and reusable workflow components

### 17: Memory in LLM Applications
- Importance of memory in AI agents  
- Stateless vs stateful AI systems  
- Context retention in workflows  
- Personalized and adaptive AI agents  
- Memory-driven reasoning systems  

### 18: Short-Term Memory
- Conversation context handling  
- Session-based memory  
- Context window management  
- Temporary state tracking during execution  
- Chat history and active workflow memory  

### 19: Long-Term Memory
- Persistent memory storage  
- User preference retention  
- Cross-session continuity  
- Knowledge accumulation over time  
- Long-term personalization in AI systems  

### 20: Advanced RAG: Corrective RAG (CRAG)
- Introduction to Corrective RAG architecture  
- Detecting retrieval quality issues  
- Correcting irrelevant or weak retrieval results  
- Improving factual accuracy and reliability  
- Self-correction pipelines for AI agents  

### 21: Self-RAG
- Self-reflective retrieval systems  
- AI agents deciding when retrieval is needed  
- Reflection tokens and reasoning loops  
- Adaptive retrieval and generation workflows  
- Building autonomous self-improving RAG agents  

---

# 🚀 Key Learning Outcomes

- Understand the shift from **Generative AI → Agentic AI**  
- Learn how to design **AI systems with memory and decision-making**  
- Build **workflow-based AI agents using LangGraph**  
- Implement **sequential, parallel, conditional, and iterative flows**  
- Gain production-level understanding with **persistence, streaming, and observability**  
- Learn **tool integration, MCP, RAG, and HITL workflows**  
- Understand **memory architectures in AI systems**  
- Explore **advanced retrieval systems like CRAG and Self-RAG**  
- Apply concepts to **real-world automation and intelligent systems**  

---

# 🛠️ Tools & Technologies

- Python  
- LangChain  
- LangGraph  
- Large Language Models (LLMs)  
- APIs & Tool Integrations  
- Vector Databases  
- MCP (Model Context Protocol)  
- LangSmith  
- FAISS / ChromaDB  
- OpenAI APIs  
- PostgreSQL / Redis  

---

# 📌 Conclusion

This repository provides a structured approach to learning **Agentic AI**, combining  
**theory, workflows, and system design** to build intelligent, autonomous agents.

It goes beyond basic LLM usage by covering **production-level concepts like persistence, streaming, observability, RAG, MCP, HITL, memory systems, and advanced retrieval architectures**, making it suitable for real-world AI system development.

The repository is designed to help learners transition from simple LLM applications to building **scalable, production-ready AI agents and multi-agent systems**.

---

> ⚡ **Note:** This repository focuses on **practical system design and real-world applications**, making it ideal for learners who want to go beyond basic LLM usage and build **next-generation AI systems**.
