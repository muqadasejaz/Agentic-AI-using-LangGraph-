# =============================================================================
#                    SHORT-TERM MEMORY IN LANGGRAPH
# =============================================================================

# =============================================================================
# 1. INTRODUCTION TO SHORT-TERM MEMORY
# =============================================================================
# Large Language Models (LLMs) are stateless by nature.
#
# This means:
# - LLMs do not intrinsically remember past messages
# - Every API call is independent
# - Previous interactions are forgotten automatically
#
# Example:
#
# User: "My name is John."
# AI: "Nice to meet you, John."
#
# Later:
#
# User: "What is my name?"
#
# Without memory:
# - the model cannot remember the earlier message
#
# To solve this problem:
# - conversation history is maintained externally
#
# This creates the illusion of memory.
#
# This type of temporary conversational memory is called:
#
#     Short-Term Memory
#
# Short-term memory enables:
# - conversation continuity
# - context retention
# - session awareness
# - active workflow tracking
# =============================================================================


# =============================================================================
# 2. CONVERSATION CONTEXT HANDLING
# =============================================================================
# To maintain context across multiple interactions:
# - previous user and AI messages are stored
# - these messages are repeatedly passed back to the LLM
#
# This process is called:
#
#     Conversation Context Handling
#
# The model receives:
# - current query
# - previous conversation history
#
# Example:
#
# messages = [
#     {"role": "user", "content": "My name is John"},
#     {"role": "assistant", "content": "Nice to meet you"},
#     {"role": "user", "content": "What is my name?"}
# ]
#
# Because previous messages are included:
# - the LLM can answer correctly
#
# This creates conversational continuity.
# =============================================================================


# =============================================================================
# 3. SESSION-BASED MEMORY
# =============================================================================
# Short-term memory is generally session-based.
#
# Each conversation session:
# - has isolated memory
# - stores independent message history
#
# In LangGraph:
# - sessions are managed using Thread IDs
#
# Thread IDs help:
# - separate conversations
# - isolate user sessions
# - manage workflow state independently
#
# Example:
#
# Thread ID: 1001
# -> Conversation about AI
#
# Thread ID: 1002
# -> Conversation about travel
#
# Each thread maintains separate memory.
#
# Switching thread IDs:
# - starts a completely fresh conversation
#
# This is extremely important in:
# - chatbots
# - customer support systems
# - enterprise AI agents
# =============================================================================


# =============================================================================
# 4. IMPLEMENTING SHORT-TERM MEMORY IN LANGGRAPH
# =============================================================================

# -----------------------------------------------------------------------------
# Core Concepts
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# A. Checkpoints
# -----------------------------------------------------------------------------
# LangGraph uses checkpoints to store workflow state.
#
# A checkpoint:
# - saves state at every superstep
# - tracks graph execution progress
# - enables memory persistence
#
# Checkpoints store:
# - messages
# - workflow variables
# - intermediate states
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# B. Thread IDs
# -----------------------------------------------------------------------------
# Every conversation is associated with:
#
#     thread_id
#
# The thread ID:
# - identifies conversation sessions
# - isolates memory between users
# - retrieves previous conversation history
#
# Example:
#
# config = {
#     "configurable": {
#         "thread_id": "user_101"
#     }
# }
# -----------------------------------------------------------------------------


# =============================================================================
# 5. IN-MEMORY SHORT-TERM MEMORY
# =============================================================================
# Initially, memory can be stored in RAM.
#
# LangGraph provides:
#
#     InMemorySaver
#
# This saver:
# - stores conversation state temporarily
# - maintains active workflow memory
# - supports session continuity
#
# Example Flow:
#
# 1. User sends message
# 2. Message stored in checkpoint
# 3. Thread ID linked to checkpoint
# 4. Entire conversation retrieved during next call
#
# Result:
# The model appears to remember earlier messages.
#
# Important Limitation:
# RAM is volatile.
#
# If application restarts:
# - all memory is lost
# =============================================================================


# =============================================================================
# 6. TEMPORARY STATE TRACKING DURING EXECUTION
# =============================================================================
# Short-term memory also tracks temporary workflow state.
#
# Example:
#
# AI Travel Agent Workflow:
#
# Step 1 -> User selects destination
# Step 2 -> User selects flight
# Step 3 -> User confirms payment
#
# During execution:
# - workflow state changes continuously
# - temporary values are stored
#
# Example State:
#
# state = {
#     "destination": "Dubai",
#     "flight": "Emirates EK612",
#     "payment_status": "pending"
# }
#
# This active workflow memory helps:
# - maintain execution continuity
# - resume interrupted tasks
# - manage multi-step workflows
# =============================================================================


# =============================================================================
# 7. PERSISTENT SHORT-TERM MEMORY USING POSTGRESQL
# =============================================================================

# -----------------------------------------------------------------------------
# Problem with In-Memory Saver
# -----------------------------------------------------------------------------
# RAM-based storage is temporary.
#
# Problems:
# - data lost after restart
# - no durable memory
# - unsuitable for production systems
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Solution: PostgreSQL Persistence
# -----------------------------------------------------------------------------
# LangGraph supports persistent checkpoint storage using databases.
#
# Common Choice:
#
#     PostgreSQL
#
# Benefits:
# - durable storage
# - survives restarts
# - scalable
# - production-ready
#
# Conversation history is permanently stored.
#
# Even after restarting the application:
# - previous conversations remain accessible
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Docker-Based PostgreSQL Setup
# -----------------------------------------------------------------------------
# Recommended approach:
# - use Docker
#
# Benefits:
# - easier setup
# - avoids installation issues
# - portable environment
#
# Typical Setup Includes:
# - username
# - password
# - database name
# - port mapping
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Required Libraries
# -----------------------------------------------------------------------------
# Common dependencies:
#
# - langgraph-checkpoint-postgres
# - psycopg
# - langchain
# - openai
# - sqlalchemy
# -----------------------------------------------------------------------------


# =============================================================================
# 8. CONTEXT WINDOW MANAGEMENT
# =============================================================================
# Every LLM has a maximum context window.
#
# Example Limits:
# - 8K tokens
# - 32K tokens
# - 128K tokens
#
# If too many messages are sent:
# - token overflow occurs
# - latency increases
# - hallucinations increase
# - performance degrades
#
# Therefore:
# conversation memory must be managed carefully.
# =============================================================================


# =============================================================================
# 9. TECHNIQUES FOR CONTEXT WINDOW MANAGEMENT
# =============================================================================

# -----------------------------------------------------------------------------
# A. Trimming
# -----------------------------------------------------------------------------
# Trimming keeps only recent messages within token limits.
#
# Process:
#
# 1. Count total tokens
# 2. Compare against limit
# 3. Remove oldest messages temporarily
#
# Example:
#
# Max Token Limit = 500
#
# Keep:
# - newest messages
#
# Exclude:
# - oldest messages
#
# Important:
# Messages are NOT deleted from storage.
# They are only excluded from the current prompt.
#
# LangChain provides:
#
#     trim_messages()
#
# Benefits:
# - reduces token usage
# - maintains recent context
#
# Drawback:
# - older context may become unavailable temporarily
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# B. Deletion
# -----------------------------------------------------------------------------
# Deletion permanently removes old messages.
#
# Example Logic:
#
# If message count > 10:
#     delete oldest 6 messages
#
# Benefits:
# - reduces memory size
# - prevents storage bloat
# - improves scalability
#
# LangGraph provides:
#
#     remove_messages()
#
# Used heavily in:
# - enterprise systems
# - long-running chat agents
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# C. Summarization
# -----------------------------------------------------------------------------
# Summarization is a more advanced memory management technique.
#
# Instead of deleting old messages:
# - summarize them using an LLM
#
# Process:
#
# Step 1:
# Keep recent messages unchanged
#
# Step 2:
# Summarize older messages
#
# Step 3:
# Store summary in state
#
# Step 4:
# Delete detailed old messages
#
# Result:
# - essential context preserved
# - token usage reduced
#
# Example:
#
# Instead of storing:
# - 100 detailed messages
#
# Store:
# - 1 summarized memory block
#
# Benefits:
# - long-term conversation coherence
# - efficient context retention
# - scalable memory handling
# -----------------------------------------------------------------------------


# =============================================================================
# 10. SUMMARIZATION WORKFLOW IN LANGGRAPH
# =============================================================================
# A summarization-based workflow usually contains:
#
# -----------------------------------------------------------------------------
# Chat Node
# -----------------------------------------------------------------------------
# Handles:
# - normal user interaction
# - message generation
# - conversation flow
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Summary Node
# -----------------------------------------------------------------------------
# Handles:
# - summarization of old messages
# - deletion of unnecessary details
# - compression of chat history
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Conditional Flow
# -----------------------------------------------------------------------------
# Example Logic:
#
# If message_count <= 6:
#     continue normal chat
#
# Else:
#     trigger summarization node
#
# This dynamic routing:
# - optimizes memory usage
# - prevents token overflow
# -----------------------------------------------------------------------------


# =============================================================================
# 11. CHAT HISTORY AND ACTIVE WORKFLOW MEMORY
# =============================================================================
# Short-term memory maintains:
#
# -----------------------------------------------------------------------------
# Chat History
# -----------------------------------------------------------------------------
# Stores:
# - user messages
# - assistant replies
# - interaction flow
#
# Enables:
# - conversational continuity
# - contextual understanding
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Active Workflow Memory
# -----------------------------------------------------------------------------
# Stores:
# - temporary execution state
# - intermediate workflow variables
# - pending actions
#
# Example:
#
# AI Order Agent:
#
# state = {
#     "selected_product": "Laptop",
#     "payment_status": "pending",
#     "shipping_address": "Islamabad"
# }
#
# This helps:
# - resume workflows
# - manage interruptions
# - track execution progress
# -----------------------------------------------------------------------------


# =============================================================================
# 12. REAL-WORLD USE CASES
# =============================================================================

# -----------------------------------------------------------------------------
# AI Customer Support Agent
# -----------------------------------------------------------------------------
# - remembers conversation history
# - tracks unresolved issues
# - maintains session continuity
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# AI Tutor
# -----------------------------------------------------------------------------
# - remembers recent learning topics
# - tracks active exercises
# - maintains teaching flow
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# AI Travel Booking Agent
# -----------------------------------------------------------------------------
# - tracks selected flights
# - remembers booking progress
# - handles multi-step workflows
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# AI Healthcare Assistant
# -----------------------------------------------------------------------------
# - remembers current symptoms
# - tracks ongoing diagnosis
# - maintains consultation context
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Enterprise Workflow Agents
# -----------------------------------------------------------------------------
# - maintain approval status
# - track pending actions
# - preserve temporary execution state
# -----------------------------------------------------------------------------


# =============================================================================
# 13. KEY BENEFITS OF SHORT-TERM MEMORY
# =============================================================================
# Short-term memory enables:
#
# - conversational continuity
# - workflow tracking
# - temporary state management
# - session-based interactions
# - context-aware reasoning
#
# It dramatically improves:
# - user experience
# - coherence
# - personalization
# - reliability
# =============================================================================


# =============================================================================
# 14. FINAL SUMMARY
# =============================================================================
# Short-term memory is essential for modern AI systems.
#
# Key Concepts:
#
# - LLMs are stateless
# - memory is externally maintained
# - conversation history simulates memory
# - thread IDs isolate sessions
# - checkpoints track workflow state
#
# Memory Management Techniques:
#
# 1. Trimming
# 2. Deletion
# 3. Summarization
#
# Storage Options:
#
# - In-Memory Saver
# - PostgreSQL Persistence
#
# Short-term memory supports:
#
# - chatbots
# - AI assistants
# - workflow agents
# - enterprise systems
# - multi-step AI applications
#
# LangGraph provides powerful tools for:
#
# - session management
# - workflow state tracking
# - context retention
# - scalable memory systems
#
# These concepts form the foundation for building
# intelligent and stateful AI agents.
# =============================================================================
