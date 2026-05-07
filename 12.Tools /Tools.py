# ============================================================
# TOOLS IN LANGGRAPH
# ============================================================

# ============================================================
# 1. INTRODUCTION TO TOOLS IN LANGGRAPH
# ============================================================

# In real-world AI applications, chatbots and agents must do more
# than just generate text.
#
# A normal Large Language Model (LLM):
# - Can answer conversational questions
# - Can explain concepts
# - Can generate text
#
# But it CANNOT:
# - Perform real calculations reliably
# - Search the internet in real time
# - Fetch live stock prices
# - Access APIs or databases directly
# - Execute external actions automatically
#
# This limitation creates the need for TOOL CALLING.

# ------------------------------------------------------------
# Definition:
# ------------------------------------------------------------

# Tool Calling in LangGraph allows AI agents to interact with:
# - APIs
# - Databases
# - Python functions
# - External services
# - Search engines
# - Custom utilities
#
# This transforms a normal chatbot into a TOOL-ENABLED AI AGENT.


# ============================================================
# 2. CURRENT PROBLEM BEFORE ADDING TOOLS
# ============================================================

# Existing chatbot architecture:
#
# User ---> OpenAI LLM ---> Response
#
# The chatbot can:
# - Answer conversational queries
# - Explain topics
# - Generate content
#
# But it cannot:
# - Calculate 654 * 713
# - Search latest news
# - Fetch live stock prices
# - Perform external tasks
#
# Example:
#
# User: "What is Tesla stock price?"
#
# Without tools:
# - LLM may hallucinate
# - Information may be outdated
#
# With tools:
# - AI fetches real-time data from APIs
# - Returns accurate results


# ============================================================
# 3. GOAL OF TOOL-ENABLED AGENTS
# ============================================================

# The main goal is:
#
# Build AI agents that can:
# - Think
# - Decide
# - Choose tools dynamically
# - Execute actions
# - Return intelligent responses
#
# Instead of only generating text,
# the AI becomes capable of TAKING ACTIONS.


# ============================================================
# 4. TOOLS USED IN THE WORKFLOW
# ============================================================

# Three example tools are integrated:

# ------------------------------------------------------------
# 4.1 Calculator Tool
# ------------------------------------------------------------

# Purpose:
# - Perform mathematical calculations
#
# Example:
# User: "What is 654 * 713?"
#
# AI Agent:
# - Detects calculation request
# - Calls calculator tool
# - Returns accurate result

# ------------------------------------------------------------
# 4.2 Internet Search Tool
# ------------------------------------------------------------

# Purpose:
# - Search real-time information from the internet
#
# Tool used:
# - DuckDuckGo Search
#
# Example:
# User: "Latest AI news today"
#
# AI Agent:
# - Uses internet search tool
# - Retrieves fresh information
# - Summarises results

# ------------------------------------------------------------
# 4.3 Stock Price Tool
# ------------------------------------------------------------

# Purpose:
# - Fetch live stock prices
#
# API used:
# - Alpha Vantage API
#
# Example:
# User: "What is Tesla stock price?"
#
# AI Agent:
# - Calls stock API
# - Retrieves live market data
# - Returns formatted response


# ============================================================
# 5. HOW TOOL-ENABLED AGENTS WORK
# ============================================================

# Example interaction flow:

# ------------------------------------------------------------
# Scenario 1: Normal Conversation
# ------------------------------------------------------------

# User: "Hi"
#
# AI:
# - Handles query normally
# - No tool required

# ------------------------------------------------------------
# Scenario 2: Calculation Request
# ------------------------------------------------------------

# User: "What is 654 * 713?"
#
# AI:
# - Detects mathematical operation
# - Calls calculator tool
# - Returns result

# ------------------------------------------------------------
# Scenario 3: Internet Search
# ------------------------------------------------------------

# User: "Who won yesterday's cricket match?"
#
# AI:
# - Detects real-time information need
# - Calls internet search tool
# - Returns updated answer

# ------------------------------------------------------------
# Scenario 4: Stock Price Query
# ------------------------------------------------------------

# User: "Tesla stock price"
#
# AI:
# - Calls stock price API
# - Retrieves live data
# - Returns formatted response


# ============================================================
# 6. LANGGRAPH ARCHITECTURE FOR TOOLS
# ============================================================

# The workflow contains two major nodes:

# ------------------------------------------------------------
# 6.1 Chat Node
# ------------------------------------------------------------

# Responsibilities:
# - Handle normal conversations
# - Understand user intent
# - Decide whether tools are required

# ------------------------------------------------------------
# 6.2 Tool Node
# ------------------------------------------------------------

# Responsibilities:
# - Execute external tools
# - Manage APIs/functions
# - Return tool outputs

# ------------------------------------------------------------
# Workflow Structure
# ------------------------------------------------------------

# START
#   |
#   v
# CHAT NODE
#   |
#   |-----> If no tool needed -----> END
#   |
#   |-----> If tool required
#                     |
#                     v
#                 TOOL NODE
#                     |
#                     v
#                 CHAT NODE
#                     |
#                     v
#                    END


# ============================================================
# 7. TOOLS CONDITION IN LANGGRAPH
# ============================================================

# LangGraph provides a built-in mechanism called:

# ------------------------------------------------------------
# Tools Condition
# ------------------------------------------------------------

# Purpose:
# - Decide whether a query needs tool execution
#
# It acts like:
#
# IF tool required:
#     route to tool node
# ELSE:
#     return normal response

# This creates DYNAMIC DECISION-MAKING.


# ============================================================
# 8. DYNAMIC DECISION-MAKING USING TOOLS
# ============================================================

# Dynamic decision-making means:
#
# The AI agent intelligently decides:
# - Which tool to use
# - When to use it
# - What input to send
# - How to process outputs

# Example:
#
# User:
# "If Tesla stock is 240 dollars,
# what will be the price of 15 shares?"
#
# Agent workflow:
#
# Step 1:
# Use stock price tool
#
# Step 2:
# Use calculator tool
#
# Step 3:
# Generate final response
#
# This demonstrates MULTI-STEP TOOL REASONING.


# ============================================================
# 9. PROBLEM WITH RAW TOOL OUTPUTS
# ============================================================

# Tools often return:
# - JSON
# - API responses
# - Raw text
# - Unformatted data
#
# Example:
#
# {
#   "symbol": "TSLA",
#   "price": 240.17
# }
#
# This is not user-friendly.


# ============================================================
# 10. FEEDBACK LOOP SOLUTION
# ============================================================

# Solution:
#
# TOOL NODE ---> CHAT NODE ---> USER
#
# Instead of sending raw outputs directly:
#
# Step 1:
# Tool executes
#
# Step 2:
# Output sent back to chat node
#
# Step 3:
# LLM refines the response
#
# Final Result:
#
# "Tesla stock is currently trading around $240.17 per share."

# Benefits:
# - Cleaner responses
# - Better UX
# - Multi-step reasoning support
# - Better formatting


# ============================================================
# 11. USING APIS IN LANGGRAPH
# ============================================================

# APIs allow agents to interact with external systems.

# Common API integrations:
#
# - Weather APIs
# - Stock market APIs
# - Google Maps APIs
# - Payment APIs
# - Email APIs
# - Calendar APIs

# Example:
#
# User:
# "Book a meeting tomorrow"
#
# AI Agent:
# - Calls calendar API
# - Checks availability
# - Schedules event


# ============================================================
# 12. USING DATABASES IN LANGGRAPH
# ============================================================

# AI agents can connect to databases to:
#
# - Fetch records
# - Store memory
# - Retrieve user history
# - Analyse business data

# Example:
#
# Customer Support Agent:
#
# - Reads customer history
# - Retrieves previous tickets
# - Generates contextual responses

# Common databases:
#
# - PostgreSQL
# - MySQL
# - MongoDB
# - Redis
# - Vector Databases


# ============================================================
# 13. USING PYTHON FUNCTIONS AS TOOLS
# ============================================================

# LangGraph allows converting Python functions into tools.

# Example:
#
# @tool
# def calculator(expression):
#     return eval(expression)

# Benefits:
# - Easy customization
# - Fast development
# - Unlimited flexibility

# Custom tools can perform:
#
# - File processing
# - Calculations
# - Data cleaning
# - Automation
# - ML inference


# ============================================================
# 14. PREBUILT VS CUSTOM TOOLS
# ============================================================

# ------------------------------------------------------------
# Prebuilt Tools
# ------------------------------------------------------------

# Provided by LangChain/LangGraph ecosystem.

# Examples:
# - DuckDuckGo Search
# - Wikipedia Search
# - Web Browsers

# ------------------------------------------------------------
# Custom Tools
# ------------------------------------------------------------

# Created by developers for specific tasks.

# Examples:
# - Internal company database access
# - Financial analysis tool
# - Resume scoring engine
# - Medical data parser


# ============================================================
# 15. TECHNICAL IMPLEMENTATION HIGHLIGHTS
# ============================================================

# Main implementation steps:

# Step 1:
# Import ToolNode and tools_condition

# Step 2:
# Create tools
#
# - Calculator tool
# - Search tool
# - Stock tool

# Step 3:
# Bind tools with LLM

# Step 4:
# Create state graph

# Step 5:
# Add:
# - Chat node
# - Tool node

# Step 6:
# Add conditional edges

# Step 7:
# Compile graph

# Step 8:
# Stream responses to frontend


# ============================================================
# 16. USER EXPERIENCE IMPROVEMENTS
# ============================================================

# Additional frontend improvements include:

# ------------------------------------------------------------
# Streaming Responses
# ------------------------------------------------------------

# Responses appear token-by-token.

# ------------------------------------------------------------
# Tool Status Indicators
# ------------------------------------------------------------

# Example:
#
# "Searching internet..."
# "Calculating result..."
# "Fetching stock price..."

# This improves:
# - Transparency
# - User trust
# - Interactivity


# ============================================================
# 17. REAL-WORLD USE CASES OF TOOL-AUGMENTED AGENTS
# ============================================================

# ------------------------------------------------------------
# 17.1 AI Financial Assistant
# ------------------------------------------------------------

# Tools:
# - Stock APIs
# - Financial databases
# - Calculator tools

# Tasks:
# - Portfolio analysis
# - Risk estimation
# - Investment summaries

# ------------------------------------------------------------
# 17.2 Customer Support Agent
# ------------------------------------------------------------

# Tools:
# - CRM database
# - Ticketing systems
# - Knowledge bases

# Tasks:
# - Retrieve customer history
# - Resolve tickets
# - Escalate issues

# ------------------------------------------------------------
# 17.3 AI Research Assistant
# ------------------------------------------------------------

# Tools:
# - Web search
# - Research databases
# - PDF readers

# Tasks:
# - Literature review
# - Summarisation
# - Citation generation

# ------------------------------------------------------------
# 17.4 AI Hiring Agent
# ------------------------------------------------------------

# Tools:
# - Resume parser
# - LinkedIn APIs
# - Email APIs
# - Scheduling systems

# Tasks:
# - Candidate screening
# - Interview scheduling
# - Offer generation

# ------------------------------------------------------------
# 17.5 Autonomous Business Intelligence Agent
# ------------------------------------------------------------

# Tools:
# - SQL databases
# - Dashboards
# - Analytics APIs

# Tasks:
# - Generate reports
# - Analyse KPIs
# - Detect trends


# ============================================================
# 18. KEY CONCEPTS SUMMARY
# ============================================================

# ------------------------------------------------------------
# Tool Node
# ------------------------------------------------------------

# A predefined LangGraph node that:
# - Manages tools
# - Executes tools
# - Returns outputs

# ------------------------------------------------------------
# Tools Condition
# ------------------------------------------------------------

# A conditional routing mechanism that:
# - Detects tool usage requirements
# - Routes workflow dynamically

# ------------------------------------------------------------
# Tool-Enabled Agent
# ------------------------------------------------------------

# An AI system capable of:
# - Reasoning
# - Using tools
# - Executing actions
# - Solving real-world tasks


# ============================================================
# 19. BENEFITS OF TOOL CALLING IN LANGGRAPH
# ============================================================

# Tool calling enables:
#
# - Real-time information retrieval
# - Accurate calculations
# - Dynamic workflows
# - API integrations
# - Multi-step reasoning
# - Action-taking AI systems
# - Production-ready intelligent agents


# ============================================================
# 20. CONCLUSION
# ============================================================

# Tools are one of the most important concepts in LangGraph
# and Agentic AI.
#
# They transform passive conversational chatbots into:
#
# - Intelligent assistants
# - Autonomous agents
# - Action-taking systems
#
# By integrating:
# - APIs
# - Databases
# - Python functions
# - External services
#
# LangGraph agents can solve real-world business problems
# and execute complex workflows dynamically.
#
# Tool calling forms the foundation for advanced AI systems
# such as:
#
# - AI hiring agents
# - Research assistants
# - Financial intelligence systems
# - Customer support automation
# - Autonomous enterprise workflows
#
# This makes LangGraph a powerful framework for building
# production-grade Agentic AI applications.
# ============================================================
