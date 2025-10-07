# 🧠 NeuroBoutique – Personalized AI Wellness, Redefined

**Tagline:**  
A smart platform combining multi-modal user tracking, an AI-driven marketplace, and predictive simulation to create dynamically optimized wellness bundles.

---

## Hackathon Track

| Track | Status | Core Innovation |
|---|---|---|
| Health & Wellness | Primary | AI-driven Predictive Outcomes (Simulation) |
| Open Innovation | Secondary | Multi-Agent System for Dynamic Personalization |

---

## ✨ Core Innovation: AI Simulation Engine

NeuroBoutique moves beyond simple recommendation by leveraging **two collaborating AI agents** to offer validated outcomes:

- **AI Recommender:** Analyzes tracked data (Sleep Score, Focus Score, Mood) to diagnose deficiencies and select a tailored product bundle.  
- **AI Simulator:** Runs a predictive model to forecast the week-by-week cognitive and physical metric changes if the user uses the recommended products.  

This answers the fundamental user question:  
*"What will this purchase do for me?"*

---

## 📈 Demo Visualization: Predicted Outcomes

The core technical output is the **predicted metric increase visualized over time**.  

*(CRITICAL: Upload the chart image to `assets/demo_screenshot.png` and it will display here once the repo is live!)*

---

## 🛠️ Project Setup & Execution Guide (Google Colab MVP)

The entire AI logic, data handling, and visualization are contained in the **`neuroboutique_demo.py`** script, ensuring zero setup time for judging.

### Prerequisites
- A web browser  
- A Google Account (required to run code in Colab)

### 🚀 Step-by-Step Demo Instructions

Follow these steps to experience the complete personalized wellness flow:

1. **Launch the Script in Colab**  
   - Go to the Google Colab environment and upload the `neuroboutique_demo.py` file.  
   - Alternatively, open a new notebook and paste the contents of `neuroboutique_demo.py` into the first code cell.  

2. **Install Dependencies (If needed)**  
   Run this command in a code cell if using a fresh Colab instance:  
   ```python
   !pip install pandas matplotlib
   ```

3. **Execute the Code**  
   - Run all cells (or execute the single cell containing the script).  

---

### 🔍 Expected Output (3 Key Feature Demos)

Observe the console output and generated chart:

- **Multi-Modal Tracking:** Initial printout confirms the user's low focus score (e.g., Focus Score: 0.35).  
- **AI Personalized Bundle:** Console shows Auto-Optimization messages (e.g., "Sub-optimal sleep detected. Adding SleepSync Eye Mask.") followed by the final recommended product list.  
- **AI Simulation:** Generates a **line chart** showing predicted trends for Focus, Sleep, and Mood metrics over time, followed by the final projected scores in the console.  

---

## 📚 Technical Stack

- **Core Logic & AI:** Python 3.x  
- **Platform:** Google Colab / Jupyter Notebook (Simulating a backend API)  
- **Libraries:** pandas, matplotlib  

---

## 🛒 Mock Product Catalog

| Product | Category | Price | Purpose |
|---|---|---|---|
| NeuroFocus Capsules | Focus | $39.99 | Premium nootropic for mental clarity |
| NeuroTrainer Handheld | Gadget | $149.00 | Cognitive trainer for attention & speed |
| SleepSync Eye Mask | Sleep | $34.99 | Smart mask for restorative sleep |
| HappyMind Chews | Mood | $14.99 | Supports resilience and positive mood |

---

## ⚡ Challenges & Solutions

- **Simulation Accuracy:** Modeling incremental changes in metrics over time.  
- **AI Agent Collaboration:** Coordinating multiple agents for coherent recommendations.  
- **User Interface in Colab:** Designing a clear, intuitive workflow within a notebook.  

---

## 🏆 Accomplishments

- Functional AI recommendation engine for personalized bundles  
- Interactive simulation charts showing predicted outcomes  
- Zero-setup Google Colab MVP ready for judging  
- Integrated mock product catalog for dynamic recommendations

---

## 📖 Lessons Learned

- Multi-modal data integration is crucial for accurate personalization  
- Visualization makes predictive insights actionable and engaging  
- Cloud-based notebooks simplify hackathon demos and sharing

---

## 🌟 Future Plans

- Expand catalog to include more supplements, gadgets, and services  
- Enhance predictive models with real-world user data  
- Add community features, goal tracking, and notifications  
- Integrate wearable devices for real-time biofeedback and continuous personalization

---

## 🚀 Mission Statement

**NeuroBoutique turns data into actionable wellness insights, empowering individuals to optimize focus, mood, energy, and sleep — predictably and intelligently.**
