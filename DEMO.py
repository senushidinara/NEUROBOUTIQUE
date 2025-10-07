# =================================================================
# NEUROBOUTIQUE AI DEMO SCRIPT
# This script contains the data models, AI recommendation logic,
# the predictive simulation engine, and visualization code.
#
# Execution: Run this script directly in a Google Colab notebook
# or locally with 'python neuroboutique_demo.py'
# Dependencies: pandas, matplotlib
# =================================================================
import json
import random
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. DATA STRUCTURES ---

class Product:
    """Defines a product in the NeuroBoutique marketplace."""
    def __init__(self, name: str, category: str, price: float, description: str):
        self.name = name
        self.category = category
        self.price = price
        self.description = description

class UserProfile:
    """
    Defines the user profile and contains the simulated multi-modal
    tracked data (scores from 0.0 to 1.0).
    """
    def __init__(self, user_id: int, goals: list[str], sleep_score: float, focus_score: float, recent_mood_score: float):
        self.user_id = user_id
        self.goals = goals
        self.sleep_score = sleep_score
        self.focus_score = focus_score
        self.recent_mood_score = recent_mood_score

# --- 2. LOAD DATA ---

# Load mock product data from the external JSON file
try:
    with open('product_data.json', 'r') as f:
        PRODUCT_DATA = json.load(f)
except FileNotFoundError:
    print("WARNING: 'product_data.json' not found. Using hardcoded backup data.")
    PRODUCT_DATA = [
        {"name": "NeuroFocus Capsules", "category": "Focus", "price": 39.99, "description": "Nootropic for focus."},
        {"name": "Cogniva Gummies", "category": "Memory", "price": 24.99, "description": "Vitamins for recall."},
        {"name": "CalmNeuro Drops", "category": "Calm", "price": 29.99, "description": "Drops for restful states."},
        {"name": "NeuroTrainer Handheld", "category": "Gadget", "price": 149.00, "description": "Cognitive trainer."},
        {"name": "SleepSync Eye Mask", "category": "Sleep", "price": 34.99, "description": "Smart mask for sleep."},
        {"name": "HappyMind Chews", "category": "Mood", "price": 14.99, "description": "Chews to support mood."},
        {"name": "NeuroCharge", "category": "Energy", "price": 19.99, "description": "Effervescent drink for quick cognitive lift."},
    ]

ALL_PRODUCTS = [Product(**p) for p in PRODUCT_DATA]

# Define a Mock User (Simulating Multi-modal Tracking Data)
MOCK_USER_DATA = UserProfile(
    user_id=4021,
    goals=["Focus"],
    sleep_score=0.6,    # Medium Sleep Score (Needs minor improvement)
    focus_score=0.35,   # LOW Focus Score (High priority intervention)
    recent_mood_score=0.55 # Neutral Mood Score
)
print(f"--- Initial Tracking Data Loaded for User ID: {MOCK_USER_DATA.user_id} ---")
print(f"Current Focus Score: {MOCK_USER_DATA.focus_score:.2f} (Low)")
print(f"Current Sleep Score: {MOCK_USER_DATA.sleep_score:.2f}")


# --- 3. AI RECOMMENDER AGENT ---

def get_goal_bundle(user: UserProfile, goal: str) -> list[Product]:
    """
    AI Agent 1: Determines the optimal product bundle based on user profile and goal.
    This uses rule-based logic to simulate complex AI personalization.
    """
    print(f"\n--- AI Agent 1: Generating Bundle for Goal: {goal} ---")

    # 1. Base Recommendation (The core product for the goal)
    bundle_products = []
    
    # 2. Apply Rule-Based Personalization and Auto-Optimization
    
    if goal == "Focus":
        # Base: Always recommend a Nootropic for Focus
        bundle_products.append(next(p for p in ALL_PRODUCTS if p.name == "NeuroFocus Capsules"))
        
        # Optimization 1: If Focus is severely low (<0.5), recommend a training device.
        if user.focus_score < 0.5:
            print("  [Auto-Optimization]: Focus deficit detected. Adding NeuroTrainer Handheld.")
            bundle_products.append(next(p for p in ALL_PRODUCTS if p.name == "NeuroTrainer Handheld"))
            
        # Optimization 2: Check for upstream causes (e.g., poor sleep hurts focus).
        if user.sleep_score < 0.7:
            print("  [Auto-Optimization]: Sub-optimal sleep detected. Adding SleepSync Eye Mask.")
            bundle_products.append(next(p for p in ALL_PRODUCTS if p.name == "SleepSync Eye Mask"))
            
    # Other goal logic (e.g., if goal == "Sleep", recommend CalmNeuro Drops + SleepSync Eye Mask)
    # ...

    return bundle_products

# Run the Recommender Agent
RECOMMENDED_BUNDLE = get_goal_bundle(MOCK_USER_DATA, "Focus")

print("\n🤖 NeuroBoutique Personalized Recommendation:")
for i, p in enumerate(RECOMMENDED_BUNDLE):
    print(f"{i+1}. {p.name} ({p.category}) - ${p.price:.2f}")


# --- 4. AI SIMULATION ENGINE AGENT ---

def run_simulation(current_metrics: dict, bundle: list[Product], duration_weeks: int = 8) -> pd.DataFrame:
    """
    AI Agent 2: Predicts week-by-week outcome of a product bundle over time.
    """
    print(f"\n--- AI Agent 2: Running {duration_weeks}-Week Predictive Simulation ---")

    # Define how each product category impacts a metric
    IMPACT_MAP = {
        "Focus": {'focus': 0.15, 'mood': 0.05},
        "Gadget": {'focus': 0.1, 'processing_speed': 0.1},
        "Sleep": {'sleep': 0.2, 'mood': 0.05},
        "Calm": {'mood': 0.1, 'sleep': 0.05},
        "Energy": {'focus': 0.05, 'energy': 0.1},
    }

    # Calculate the total potential impact of the whole bundle
    total_impact = {metric: 0 for metric in current_metrics}
    for product in bundle:
        # Sum up boosts for all relevant metrics
        for metric, boost in IMPACT_MAP.get(product.category, {}).items():
            if metric in total_impact:
                total_impact[metric] += boost

    # Initialize simulation data
    simulation_data = {metric: [value] for metric, value in current_metrics.items()}
    current_metrics_copy = current_metrics.copy()

    # Simulate week-by-week progression
    for week in range(1, duration_weeks + 1):
        for metric in current_metrics_copy:
            base_increase = total_impact.get(metric, 0)
            noise = random.uniform(-0.01, 0.03) # Small weekly randomness

            # Improvement model: boost is higher when the score is low (diminishing returns)
            new_value = min(1.0, current_metrics_copy[metric] + (base_increase * (1 - current_metrics_copy[metric])) + noise)

            current_metrics_copy[metric] = new_value
            simulation_data[metric].append(new_value)

    # Return data as a Pandas DataFrame for easy charting
    return pd.DataFrame(simulation_data, index=[f'Week {i}' for i in range(duration_weeks + 1)])


# Run the Simulation Agent
CURRENT_METRICS = {
    'focus': MOCK_USER_DATA.focus_score,
    'sleep': MOCK_USER_DATA.sleep_score,
    'mood': MOCK_USER_DATA.recent_mood_score
}
PREDICTED_OUTCOMES_DF = run_simulation(CURRENT_METRICS, RECOMMENDED_BUNDLE, duration_weeks=8)


# --- 5. VISUALIZATION ---
print("\n--- Generating Visualization ---")

plt.figure(figsize=(10, 6))
for column in PREDICTED_OUTCOMES_DF.columns:
    plt.plot(PREDICTED_OUTCOMES_DF.index, PREDICTED_OUTCOMES_DF[column],
             label=column.capitalize(), marker='o', markersize=4, linewidth=2)

plt.title('NeuroBoutique AI Simulation: Predicted Outcomes over 8 Weeks', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Metric Score (0.0 to 1.0)', fontsize=12)
plt.legend(title="Metrics", loc='lower right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(0.0, 1.0)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n--- Final Projected Scores (After 8 Weeks) ---")
print(PREDICTED_OUTCOMES_DF.iloc[-1].round(3))

# Final note for screenshot guidance
print("\n*** IMPORTANT: Please save the chart above as 'assets/demo_screenshot.png' for the README. ***")

