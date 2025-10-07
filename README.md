# 🧠 NeuroBoutique – Personalized AI Wellness, Redefined

**Tagline:**  
A smart platform combining multi-modal user tracking, an AI-driven marketplace, and predictive simulation to create dynamically optimized wellness bundles for individuals.

---

## Hackathon Track

| Track | Status | Core Innovation |
|---|---|---|
| Health & Wellness | Primary | AI-driven Predictive Outcomes (Simulation) |
| Open Innovation | Secondary | Multi-Agent System for Dynamic Personalization |

---

## ✨ Core Innovation: AI Simulation Engine

NeuroBoutique is not just a marketplace; it’s a **predictive, personalized wellness platform**. Its core innovation lies in combining **multi-modal user tracking**, **AI-driven recommendations**, and **simulation-based predictive modeling** to deliver personalized wellness plans.  

We achieve this with **two collaborating AI agents**:

- **AI Recommender:** This agent analyzes data from multiple sources — including sleep patterns, activity levels, focus scores, and mood metrics — to diagnose potential deficiencies. Based on this analysis, it selects a tailored product bundle designed specifically for the user’s goals.  
- **AI Simulator:** Once the recommended bundle is generated, the AI Simulator forecasts the week-by-week changes in cognitive, physical, and mood-related metrics. This allows users to **visualize the potential impact of their choices over time**.

Together, these agents answer the fundamental user question:  
*"What will this purchase do for me?"*

---

## 📈 Demo Visualization: Predicted Outcomes

The output of NeuroBoutique is **actionable and visualizable**. Users can see predicted metric improvements over weeks or months in clear charts. These simulations help users make **informed decisions** about their wellness journey, empowering them with data-driven insights.  

![Predicted Metric Improvement over 8 Weeks](assets/demo_screenshot.png)

---

## 🛠️ Project Setup & Execution Guide (Google Colab MVP)

To simplify judging and execution, the entire **AI logic, data handling, and visualization** is packaged in a **single Google Colab Notebook**. This eliminates setup barriers and ensures anyone can experience the platform immediately.  

### Prerequisites
- A web browser  
- A Google Account (required to run code in Colab)

### Step-by-Step Demo Instructions
1. **Open the Notebook** in Google Colab.  
2. **Run All Cells:** Go to **Runtime → Run all** in the top menu.  
3. **Observe Outputs:** The notebook demonstrates the full NeuroBoutique workflow:  
   - Multi-modal tracking of user metrics  
   - AI-driven personalized bundle recommendations  
   - Predictive simulations visualizing potential outcomes

---

## 🔍 Expected Outputs (Key Demos)

| Cell # | Feature Demonstrated | Expected Output |
|---|---|---|
| Cell 2 | Multi-Modal Tracking | Confirmation of the user’s metrics (e.g., Focus Score: 0.4, Sleep Score: 0.6) |
| Cell 3 | AI-Driven Personalized Bundle | Prints the optimization reasoning (e.g., "Focus score is low. Adding Cognitive Trainer.") and final product list |
| Cell 4 | Interactive Simulation | Line charts showing predicted trends for Focus, Sleep, and Mood metrics, with final projected scores displayed below the chart |

---

## 📚 Technical Stack & Implementation Details

NeuroBoutique leverages a combination of modern technologies:

- **Programming Language:** Python 3.x for AI logic and data processing  
- **Platform:** Google Colab / Jupyter Notebook for zero-install, cloud-executable code  
- **Data Handling:** pandas for structured dataset manipulation  
- **Visualization:** matplotlib to create dynamic, interactive charts for predicted metrics  
- **AI/ML Techniques:** Multi-agent system for recommendation + predictive modeling for outcome simulation  

The architecture allows **scalability** — additional wellness metrics, product categories, and AI agents can be integrated seamlessly in future versions.

---

## 🛒 Mock Product Catalog

The AI Recommender uses a curated set of wellness products to personalize bundles:

| Product | Category | Price | Purpose |
|---|---|---|---|
| NeuroFocus Capsules | Focus | $39.99 | Premium nootropic for mental clarity and sustained attention |
| NeuroTrainer Handheld | Gadget | $149.00 | Cognitive trainer to improve processing speed and focus |
| SleepSync Eye Mask | Sleep | $34.99 | Smart mask to enhance restorative sleep |
| HappyMind Chews | Mood | $14.99 | Supplements to support resilience and positive mood |

These products are combined dynamically based on user goals and tracked metrics to **create optimized bundles** for individual needs.

---

## ⚡ Challenges We Overcame

During development, we faced several technical and design challenges:

- **Realistic Outcome Simulations:** Simulating cognitive and mood improvements over weeks required modeling incremental changes and making them visually intuitive.  
- **AI Agent Collaboration:** Coordinating multiple AI agents to produce coherent, personalized recommendations and predictions was complex.  
- **User Interface Design:** Creating a smooth, intuitive workflow for tracking, recommendations, and simulations within a single notebook demanded careful planning.  

---

## 🏆 Key Accomplishments

- Developed a **fully functional AI recommendation engine** capable of personalizing wellness bundles.  
- Created **interactive simulation charts** showing predicted outcomes over multiple weeks.  
- Built a **demo-ready Google Colab MVP** that requires zero installation and runs directly in the cloud.  
- Showcased a **mock product catalog** integrated with AI for real-time recommendations.  

---

## 📖 Lessons Learned

- The importance of **multi-modal data integration** for accurate personalized recommendations.  
- How to create **intuitive, visually engaging simulations** that communicate predictive insights clearly.  
- Practical strategies for **deploying AI in a lightweight, accessible platform** for hackathon-ready demos.  

---

## 🌟 Future Plans

NeuroBoutique is a **foundation for next-generation wellness platforms**. Future developments include:

- Expanding the product catalog to include additional supplements, gadgets, and wellness services.  
- Improving predictive models using **real-world user data and clinical research**.  
- Adding **community features, goal tracking, and notifications** to enhance engagement.  
- Integrating with **wearable devices** for real-time biofeedback and continuous personalization.  

---

## 🚀 Mission Statement

**NeuroBoutique turns data into actionable wellness insights, empowering individuals to optimize their focus, mood, energy, and sleep — predictably and intelligently.**
