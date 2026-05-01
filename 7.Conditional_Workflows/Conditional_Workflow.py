# ============================================================
# 🧠  CONDITIONAL WORKFLOWS IN LANGGRAPH
# ============================================================

# Definition:
# Conditional workflows enable decision-based execution where
# only ONE path is executed based on a condition.

# Key Concepts:
# - Dynamic branching (if-else logic)
# - Only one branch runs (unlike parallel workflows)
# - Used to handle different scenarios intelligently

# Comparison:
# - Parallel Workflow → runs ALL branches simultaneously
# - Conditional Workflow → runs ONLY one branch based on condition

# Importance:
# - Essential for building adaptive and intelligent workflows
# - Mimics real-world decision-making systems


# ============================================================
# ⚙️  NON-LLM WORKFLOW — QUADRATIC EQUATION SOLVER
# ============================================================

# Problem:
# Solve quadratic equation:
# ax^2 + bx + c = 0

# Input:
# - a, b, c (coefficients)

# Key Formula:
# Discriminant:
# d = b^2 - 4ac

# Root Conditions:
# - d > 0 → Two distinct real roots
# - d = 0 → One repeated root
# - d < 0 → No real roots


# ------------------------------------------------------------
# 🔹 Workflow Steps
# ------------------------------------------------------------

# 1. Take input values (a, b, c)
# 2. Display equation
# 3. Calculate discriminant
# 4. Apply conditional branching:
#    → If d > 0 → calculate two roots
#    → If d = 0 → calculate one root
#    → If d < 0 → no real roots


# ------------------------------------------------------------
# 🔹 State Definition
# ------------------------------------------------------------

# - a: float
# - b: float
# - c: float
# - equation: string
# - discriminant: float
# - result: string


# ------------------------------------------------------------
# 🔹 Nodes (Functions)
# ------------------------------------------------------------

# - show_equation
# - calculate_discriminant
# - calculate_two_roots
# - calculate_single_root
# - handle_no_roots


# ------------------------------------------------------------
# 🔹 Conditional Function
# ------------------------------------------------------------

# Function: check_condition

# Logic:
# if d > 0:
#     return "calculate_two_roots"
# elif d == 0:
#     return "calculate_single_root"
# else:
#     return "handle_no_roots"


# ------------------------------------------------------------
# 🔹 Graph Construction
# ------------------------------------------------------------

# - Use add_conditional_edges()
# - Connect discriminant node to multiple possible next nodes
# - Only one branch executes based on condition

# Flow:
# start → show_equation → calculate_discriminant
#        → (conditional branching) → appropriate node → end


# ------------------------------------------------------------
# 🔹 Result
# ------------------------------------------------------------

# - Correct root calculation based on discriminant
# - Demonstrates dynamic branching clearly


# ============================================================
# 🤖  LLM-BASED CONDITIONAL WORKFLOW — CUSTOMER SUPPORT
# ============================================================

# Goal:
# Automatically respond to customer reviews

# Input:
# - Customer review text

# Output:
# - Appropriate response based on sentiment


# ------------------------------------------------------------
# 🔹 Workflow Steps
# ------------------------------------------------------------

# 1. Detect sentiment (positive or negative)
# 2. Conditional branching:
#    → Positive → generate thank-you response
#    → Negative → perform diagnosis + generate response


# ------------------------------------------------------------
# 🔹 State Definition
# ------------------------------------------------------------

# - review: string
# - sentiment: string ("positive" or "negative")
# - diagnosis: dict
# - response: string


# ------------------------------------------------------------
# 🔹 Nodes (Functions)
# ------------------------------------------------------------

# - find_sentiment
# - generate_positive_response
# - run_diagnosis
# - generate_negative_response


# ------------------------------------------------------------
# 🔹 Structured Output (Important)
# ------------------------------------------------------------

# Sentiment Schema:
# - Only allows "positive" or "negative"

# Diagnosis Schema:
# - issue_type (UI, performance, bug, support)
# - tone (frustration, anger, etc.)
# - urgency (low, medium, high)

# Purpose:
# - Ensures consistent and reliable LLM outputs


# ------------------------------------------------------------
# 🔹 Conditional Function
# ------------------------------------------------------------

# Function: check_sentiment

# Logic:
# if sentiment == "positive":
#     return "generate_positive_response"
# else:
#     return "run_diagnosis"


# ------------------------------------------------------------
# 🔹 Workflow Flow
# ------------------------------------------------------------

# start → find_sentiment
#        → (conditional branching)
#            → positive → generate_positive_response → end
#            → negative → run_diagnosis → generate_negative_response → end


# ------------------------------------------------------------
# 🔹 Execution Result
# ------------------------------------------------------------

# - Positive reviews → warm and thankful replies
# - Negative reviews → diagnostic + empathetic response


# ============================================================
# 📌  KEY CONCEPTS & TAKEAWAYS
# ============================================================

# - Conditional workflows enable intelligent decision-making
# - Only one branch executes based on evaluated condition

# Implementation:
# - Use condition-checking functions
# - Use add_conditional_edges() for branching

# Best Practices:
# - Use structured outputs for LLM reliability
# - Clearly define state and branching logic

# Insight:
# - Combines traditional logic (quadratic solver)
#   with AI-powered reasoning (customer support system)

# ============================================================
