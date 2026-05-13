# ============================================================
# SUBGRAPHS IN LANGGRAPH
# ============================================================

# ------------------------------------------------------------
# Introduction to SubGraphs
# ------------------------------------------------------------

# Definition:
# A SubGraph is a graph embedded inside another graph.
# In LangGraph, a node inside a parent graph can itself
# contain multiple nodes and edges forming a smaller graph.

# Simple Understanding:
# Instead of every node performing a single small task,
# some nodes can represent complete workflows internally.
# These internal workflows are called SubGraphs.

# Parent Graph:
# Main workflow graph.

# SubGraph:
# Smaller graph executed as part of the parent graph.

# Concept:
# Large Workflow
# ├── Node A
# ├── Node B
# ├── SubGraph Node
# │      ├── Internal Node 1
# │      ├── Internal Node 2
# │      └── Internal Node 3
# └── Node C


# ============================================================
# WHY SUBGRAPHS ARE IMPORTANT
# ============================================================

# ------------------------------------------------------------
# Handling Workflow Complexity
# ------------------------------------------------------------

# Modern AI systems are highly complex.
# They may contain:
# - Multiple tools
# - Memory systems
# - Retry mechanisms
# - Evaluation systems
# - Guardrails
# - Multi-agent collaboration

# Managing everything inside one giant graph becomes difficult.

# SubGraphs solve this problem by dividing workflows
# into smaller modular systems.


# ------------------------------------------------------------
# Example Use Case
# ------------------------------------------------------------

# Example:
# AI Software Development Company

# Main AI System:
# ├── Backend Team Agent
# ├── Frontend Team Agent
# ├── Testing Team Agent
# ├── Code Review Agent
# └── DevOps Agent

# Each team itself can be implemented as a SubGraph.


# ============================================================
# BENEFITS OF SUBGRAPHS
# ============================================================

# ------------------------------------------------------------
# 1. Modularity
# ------------------------------------------------------------

# Large workflows are divided into smaller reusable modules.

# Benefits:
# - Easier to understand
# - Easier to maintain
# - Easier to scale


# ------------------------------------------------------------
# 2. Reusability
# ------------------------------------------------------------

# Same SubGraph can be reused in multiple places.

# Example:
# Coding agent SubGraph can be reused for:
# - Backend coding
# - Frontend coding
# - API development


# ------------------------------------------------------------
# 3. Maintainability
# ------------------------------------------------------------

# Bugs can be isolated inside specific SubGraphs.

# Instead of debugging the entire workflow,
# developers only debug the affected SubGraph.


# ------------------------------------------------------------
# 4. Failure Isolation
# ------------------------------------------------------------

# If one SubGraph fails:
# - Entire workflow may continue
# - Parent graph can handle failure gracefully

# This improves robustness of enterprise AI systems.


# ------------------------------------------------------------
# 5. State Separation
# ------------------------------------------------------------

# Different SubGraphs can maintain different states.

# This prevents:
# - State conflicts
# - Variable overwriting
# - Memory confusion


# ------------------------------------------------------------
# 6. Observability
# ------------------------------------------------------------

# LangGraph supports monitoring SubGraphs independently.

# Developers can track:
# - Token usage
# - Latency
# - Errors
# - Performance metrics

# This is useful for production-grade AI systems.


# ============================================================
# TYPES OF SUBGRAPHS
# ============================================================

# LangGraph mainly supports two types of SubGraphs.


# ============================================================
# TYPE 1: SHARED STATE SUBGRAPHS
# ============================================================

# ------------------------------------------------------------
# Shared State SubGraphs
# ------------------------------------------------------------

# In this approach:
# - Parent graph and SubGraph share the same state.
# - Both can directly access and modify common variables.

# Characteristics:
# - Tight integration
# - Faster communication
# - Direct state updates

# Useful For:
# - Closely connected workflows
# - Shared memory systems
# - Collaborative multi-agent workflows


# ------------------------------------------------------------
# Shared State Example
# ------------------------------------------------------------

# Shared State:
# {
#     "question": "...",
#     "answer": "...",
#     "translated_answer": "..."
# }

# Parent graph creates answer.
# Translation SubGraph directly updates translated_answer.


# ------------------------------------------------------------
# Advantages
# ------------------------------------------------------------

# - Simple communication
# - No manual state mapping required
# - Faster workflow integration


# ------------------------------------------------------------
# Limitations
# ------------------------------------------------------------

# - Risk of state conflicts
# - Tight coupling between components
# - Harder to isolate independent modules


# ============================================================
# TYPE 2: INDEPENDENT STATE SUBGRAPHS
# ============================================================

# ------------------------------------------------------------
# Independent State SubGraphs
# ------------------------------------------------------------

# In this approach:
# - Parent graph and SubGraph maintain separate states.
# - Communication happens through inputs and outputs.

# Characteristics:
# - Loose coupling
# - Better modularity
# - Reusable architecture


# ------------------------------------------------------------
# Independent State Example
# ------------------------------------------------------------

# Parent State:
# {
#     "question": "..."
# }

# SubGraph State:
# {
#     "english_answer": "...",
#     "hindi_answer": "..."
# }

# Parent graph sends input to SubGraph.
# SubGraph processes internally and returns output.


# ------------------------------------------------------------
# Advantages
# ------------------------------------------------------------

# - Better isolation
# - Cleaner architecture
# - Easier debugging
# - Highly reusable


# ------------------------------------------------------------
# Limitations
# ------------------------------------------------------------

# - Requires input/output mapping
# - Slightly more complex integration


# ============================================================
# IMPLEMENTING SUBGRAPHS IN LANGGRAPH
# ============================================================

# There are two main mechanisms.


# ============================================================
# MECHANISM 1:
# INVOKING A SUBGRAPH FROM A NODE
# ============================================================

# ------------------------------------------------------------
# Concept
# ------------------------------------------------------------

# Parent graph contains a node.
# That node invokes another graph internally.

# States remain isolated.


# ------------------------------------------------------------
# Workflow Example
# ------------------------------------------------------------

# Parent Graph
# ├── Question Node
# ├── Answer Generation Node
# ├── Translation Node
# │      └── Invokes Translation SubGraph
# └── End


# ------------------------------------------------------------
# Characteristics
# ------------------------------------------------------------

# - Independent states
# - Better modularity
# - Cleaner separation


# ============================================================
# MECHANISM 2:
# ADDING SUBGRAPH AS A NODE
# ============================================================

# ------------------------------------------------------------
# Concept
# ------------------------------------------------------------

# SubGraph is directly inserted into parent graph as a node.

# Both share same state structure.


# ------------------------------------------------------------
# Workflow Example
# ------------------------------------------------------------

# Parent Graph
# ├── Question Node
# ├── Answer Node
# ├── Translation SubGraph Node
# └── End

# Translation SubGraph internally:
# ├── Translate Text
# ├── Refine Translation
# └── Final Output


# ------------------------------------------------------------
# Characteristics
# ------------------------------------------------------------

# - Shared state
# - Tight integration
# - Easier direct communication


# ============================================================
# PRACTICAL EXAMPLE:
# ENGLISH TO HINDI TRANSLATION WORKFLOW
# ============================================================

# ------------------------------------------------------------
# Scenario
# ------------------------------------------------------------

# User asks a question.
# LLM generates answer in English.
# Translation SubGraph converts answer into Hindi.


# ============================================================
# IMPLEMENTATION USING INDEPENDENT STATE SUBGRAPH
# ============================================================

# Parent Graph Responsibilities:
# - Receive question
# - Generate English answer

# Translation SubGraph Responsibilities:
# - Translate answer into Hindi
# - Return translated output

# States remain separate.


# ============================================================
# IMPLEMENTATION USING SHARED STATE SUBGRAPH
# ============================================================

# Parent graph and Translation SubGraph
# share same state dictionary.

# Translation directly updates:
# state["translated_answer"]


# ============================================================
# MULTI-AGENT COORDINATION USING SUBGRAPHS
# ============================================================

# SubGraphs are extremely useful for:
# - Multi-agent systems
# - Enterprise AI platforms
# - Team-based AI workflows

# Example:
# Enterprise AI Assistant

# Main Graph:
# ├── Research Agent SubGraph
# ├── Planning Agent SubGraph
# ├── Coding Agent SubGraph
# ├── Testing Agent SubGraph
# └── Deployment Agent SubGraph


# ============================================================
# BUILDING SCALABLE ENTERPRISE AI SYSTEMS
# ============================================================

# SubGraphs help build scalable systems because:
# - Teams can independently develop modules
# - Components are reusable
# - Failures are isolated
# - Monitoring becomes easier
# - Systems become maintainable

# Common Enterprise Use Cases:
# - AI software development agents
# - Customer support automation
# - HR workflow systems
# - Financial analysis pipelines
# - Autonomous research systems


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# SubGraphs are graphs inside larger graphs.

# They provide:
# - Modularity
# - Reusability
# - Maintainability
# - Failure isolation
# - Better observability

# Two Main Types:
# 1. Shared State SubGraphs
# 2. Independent State SubGraphs

# Two Main Integration Mechanisms:
# 1. Invoke SubGraph from node
# 2. Add SubGraph directly as node

# SubGraphs are essential for:
# - Multi-agent AI systems
# - Enterprise-grade workflows
# - Scalable agentic AI architectures


# ============================================================
# CONCLUSION
# ============================================================

# SubGraphs are one of the most powerful concepts
# in LangGraph for building modular and scalable
# AI systems.

# They allow developers to divide large workflows
# into smaller specialised components, making
# complex agentic AI systems easier to build,
# maintain, debug, and scale.

# SubGraphs are heavily used in:
# - Multi-agent systems
# - Enterprise AI platforms
# - Autonomous AI workflows
# - Production-grade AI architectures
