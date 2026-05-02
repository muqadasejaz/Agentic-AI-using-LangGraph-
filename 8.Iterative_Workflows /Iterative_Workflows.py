# ============================================================
# 🔁  ITERATIVE WORKFLOWS IN LANGGRAPH
# ============================================================

# Definition:
# Iterative (looping) workflows repeatedly execute a set of steps
# until a condition is met.

# Core Ideas:
# - Loops and repeated execution
# - Feedback-driven improvements
# - Self-correcting agents

# Importance:
# - Enables gradual refinement of outputs
# - Essential for building intelligent, adaptive AI systems


# ============================================================
# 💡  USE CASE — AUTOMATED SOCIAL MEDIA POSTING
# ============================================================

# Problem:
# - Maintaining presence across platforms (LinkedIn, X, Instagram)
# - Manual posting is time-consuming

# Solution:
# - Build an automated AI workflow to generate and post content

# Challenge:
# - LLM-generated posts may lack quality or become repetitive

# Goal:
# - Use iterative workflow to improve post quality until acceptable


# ============================================================
# ⚙️ HIGH-LEVEL WORKFLOW DESIGN
# ============================================================

# Input:
# - Topic (e.g., "AI in India")

# Workflow Loop:
# Generate → Evaluate → Optimize → Evaluate → ... → End

# Logic:
# - Generate post using LLM
# - Evaluate quality using strict criteria
# - If approved → End
# - If rejected → Optimize using feedback → repeat loop

# Stops when:
# - Approved OR
# - Maximum iterations reached


# ============================================================
# 🧩  CORE COMPONENTS
# ============================================================

# 1. Generator:
# - Creates content based on topic
# - Requires strong writing capability

# 2. Evaluator:
# - Evaluates quality (strict criteria)
# - Returns approval + feedback

# 3. Optimizer:
# - Improves content using feedback
# - Refines output iteratively

# Note:
# - Different LLMs can be used for each role in production


# ============================================================
# 🗂️  STATE DEFINITION (TWEET WORKFLOW)
# ============================================================

# State Variables:

# - topic: string
# - tweet: string
# - evaluation: "approved" or "needs improvement"
# - feedback: string
# - iteration: int
# - max_iterations: int (e.g., 5)

# Additional (for tracking history):

# - tweet_history: list[string]
# - feedback_history: list[string]

# Purpose:
# - Prevent infinite loops
# - Track improvement over iterations


# ============================================================
# 🔧  GRAPH & NODES
# ============================================================

# Nodes:
# - generate_tweet
# - evaluate_tweet
# - optimise_tweet

# Flow:
# start → generate → evaluate → (conditional) → end / optimise
# optimise → evaluate (loop back)


# ============================================================
# ✍️  GENERATE FUNCTION
# ============================================================

# Input:
# - topic

# Prompt Instructions:
# - Funny, original tweet
# - Max 280 characters
# - No Q&A format
# - Use humour (sarcasm, irony, cultural references)

# Output:
# - Generated tweet

# Also:
# - Append tweet to tweet_history


# ============================================================
# 🔍  EVALUATE FUNCTION
# ============================================================

# Input:
# - tweet

# Evaluation Criteria:
# - Originality
# - Humour
# - Virality
# - Format compliance

# Output (Structured):
# - evaluation: "approved" / "needs improvement"
# - feedback: explanation

# Use schema to enforce structured output


# ============================================================
# 🔄  OPTIMIZE FUNCTION
# ============================================================

# Input:
# - tweet + feedback

# Task:
# - Improve tweet based on feedback

# Constraints:
# - Keep under 280 characters
# - Maintain humour and clarity

# Output:
# - Improved tweet

# Also:
# - Increment iteration count
# - Append new tweet and feedback to history


# ============================================================
# 🔀 LOOP & CONDITIONAL ROUTING
# ============================================================

# Function: route_evaluation

# Logic:
# if evaluation == "approved" OR iteration >= max_iterations:
#     return "end"
# else:
#     return "optimise"

# This creates loop:
# optimise → evaluate → optimise → ... until condition met


# ============================================================
# 🧪  WORKFLOW EXECUTION EXAMPLE
# ============================================================

# Initial State:
# - topic: "Indian Railways"
# - iteration: 1
# - max_iterations: 5

# Execution:
# - Tweet generated
# - If approved → ends immediately
# - Else → improved and re-evaluated

# Observation:
# - Sometimes 1 iteration is enough
# - Sometimes multiple loops required


# ============================================================
# 📊  HISTORY TRACKING
# ============================================================

# Added:
# - tweet_history
# - feedback_history

# Purpose:
# - Track all iterations
# - Analyze improvements

# Implementation:
# - Use reducer (operator.add)
# - Append new values instead of replacing


# ============================================================
# 📌  KEY INSIGHTS
# ============================================================

# - Iterative workflows enable self-correcting systems
# - Feedback loops improve output quality over time
# - Structured outputs ensure reliable decision-making
# - Iteration limits prevent infinite loops
# - History tracking helps debugging and analysis


# ============================================================
# 🧾 SUMMARY
# ============================================================

# - LangGraph supports looping via conditional edges
# - Enables complex workflows with repeated execution
# - Combines:
#   → Generation
#   → Evaluation
#   → Optimization

# Final Outcome:
# - High-quality, refined outputs
# - Autonomous, adaptive AI behavior

# ============================================================
