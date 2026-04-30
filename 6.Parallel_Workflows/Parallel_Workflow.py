# ============================================================
# 🧠 PARALLEL WORKFLOWS IN LANGGRAPH
# ============================================================

# Definition:
# Parallel workflows allow multiple independent tasks to run
# simultaneously instead of sequentially.

# Key Benefits:
# - Faster execution (performance optimization)
# - Efficient resource utilization
# - Suitable for independent computations

# Use Cases:
# - Data analysis pipelines
# - Multi-aspect evaluation (e.g., essay scoring)
# - Content moderation (multiple checks at once)
# - Multi-agent systems


# ============================================================
# ⚙️ SIMPLE PARALLEL WORKFLOW — CRICKET DATA ANALYSIS
# ============================================================

# Task:
# Analyze a batsman’s performance using input statistics

# Input:
# - runs (int)
# - balls (int)
# - fours (int)
# - sixes (int)

# Output Metrics (computed in parallel):
# 1. Strike Rate = (runs / balls) * 100
# 2. Boundary Percentage = % of runs from fours and sixes
# 3. Boundaries per Ball = balls per boundary


# ------------------------------------------------------------
# 🔹 Workflow Structure
# ------------------------------------------------------------

# start
#   ↓
# ┌───────────────┬──────────────────────┬──────────────────────┐
# │ strike_rate   │ boundary_percentage  │ boundaries_per_ball  │
# └───────────────┴──────────────────────┴──────────────────────┘
#   ↓ (parallel outputs merged)
# summary_node
#   ↓
# end


# ------------------------------------------------------------
# 🔹 State Definition
# ------------------------------------------------------------

# Input:
# - runs: int
# - balls: int
# - fours: int
# - sixes: int

# Output:
# - strike_rate: float
# - boundary_percentage: float
# - boundaries_per_ball: float
# - summary: string


# ------------------------------------------------------------
# 🔹 Implementation Highlights
# ------------------------------------------------------------

# - Each metric is calculated in a separate node
# - All nodes execute simultaneously (parallel execution)
# - Results are passed to a summary node

# ⚠️ Important Rule:
# - Each parallel node must return ONLY its partial state update
#   Example:
#   return {"strike_rate": value}
#
# - Do NOT return full state in parallel workflows
# - This prevents overwriting conflicts during execution

# Debug Note:
# - Ensure correct formula:
#   strike_rate = (runs / balls) * 100


# ============================================================
# 🤖  COMPLEX PARALLEL WORKFLOW — LLM ESSAY EVALUATION
# ============================================================

# Task:
# Evaluate an essay using multiple LLMs in parallel

# Evaluation Aspects:
# - Clarity of thought
# - Depth of analysis
# - Language quality

# Each LLM returns:
# - Textual feedback
# - Score (0–10)


# ------------------------------------------------------------
# 🔹 Workflow Structure
# ------------------------------------------------------------

# start
#   ↓
# ┌────────────┬────────────┬────────────┐
# │ clarity    │ depth      │ language   │
# └────────────┴────────────┴────────────┘
#   ↓ (parallel outputs)
# final_evaluation_node
#   ↓
# end


# ------------------------------------------------------------
# 🔹 Final Evaluation Node Responsibilities
# ------------------------------------------------------------

# - Merge feedback from all nodes
# - Generate summarized feedback (using LLM)
# - Calculate average score


# ------------------------------------------------------------
# 🔹 State Definition
# ------------------------------------------------------------

# - essay: string
# - clarity_feedback: string
# - depth_feedback: string
# - language_feedback: string
# - final_feedback: string
# - scores: list[int]
# - average_score: float


# ------------------------------------------------------------
# 🔹 Key Concepts & Challenges
# ------------------------------------------------------------

# 1. Structured Output from LLMs:
# - Use schema (e.g., Pydantic models)
# - Ensures numeric outputs (avoid "seven" instead of 7)

# 2. Reducers:
# - Required to merge parallel outputs safely

# Example:
# - scores from multiple nodes → combined into one list
# - Use operator.add to concatenate lists

# 3. Parallel State Updates:
# - Each node updates only its own part of the state
# - Reducers handle merging of shared fields

# 4. Graph Construction:
# - Define nodes (LLM evaluators)
# - Define edges (parallel connections)
# - Compile and execute graph


# ------------------------------------------------------------
# 🔹 Execution Result
# ------------------------------------------------------------

# - Essay is evaluated across multiple dimensions
# - Provides:
#   → Detailed feedback
#   → Individual scores
#   → Final aggregated score


# ============================================================
# 📌 SUMMARY & KEY TAKEAWAYS
# ============================================================

# - LangGraph supports efficient parallel workflows
# - Suitable for independent and multi-task execution

# Key Practices:
# - Return partial state updates in parallel nodes
# - Use structured outputs for LLM reliability
# - Apply reducers to merge parallel results safely

# Insight:
# - Parallel workflows significantly improve performance
# - Essential for building scalable, real-world AI systems

# ============================================================
