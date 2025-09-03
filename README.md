# Maximizing-Section-Throughput-Using-Al-Powered-Precise-Train-Traffic-Control
SIH 2025
# AI-Powered Train Traffic Scheduling & Simulation

It is a prototype system that demonstrates **AI-powered train traffic scheduling** using a combination of **heuristics, OR-Tools optimization, simulation, and interactive dashboards**.  
It allows users to **simulate train delays, section blockages, and re-optimize schedules** in real-time while visualizing KPIs and train movements.

---

## 🔹 Project Workflow

1. **Data Modeling & Simulation (Shashwat)**
   - Define input schemas for trains, stations, and track sections (JSON/CSV).
   - Create simulation environment to introduce delays and disruptions.
   - Generate synthetic datasets for testing (10–20 trains, 3–5 stations).

2. **Optimization Engine (Vandan)**
   - Implement scheduling logic with constraints (headway, station dwell times, priorities).
   - Prototype greedy heuristic, then implement OR-Tools CP-SAT solver.
   - Ensure re-scheduling works dynamically when disruptions are introduced.

3. **Visualization & Dashboard (Aksh)**
   - Build Gantt chart timelines of train schedules.
   - Show train movements before/after disruptions.
   - Add KPI cards for avg. delay, throughput, and utilization.

4. **Frontend & UI/UX (Apurva)**
   - Design interactive interface (buttons: `Delay Train`, `Block Section`, `Reschedule`).
   - Provide explanation panel for solver decisions.
   - Polish UI for demo-readiness.

5. **System Integration (Shlok)**
   - Connect solver + simulation + UI layers.
   - Build APIs (Flask/FastAPI if needed) to trigger re-optimization.
   - Ensure seamless live rescheduling during disruptions.

6. **Pitch & Documentation (Prathamesh)**
   - Prepare final presentation slides (Problem → Solution → Demo → Impact → Future Scope).
   - Create system architecture diagrams.
   - Document assumptions, workflow, and usage.

---

## 📂 Folder Structure
Full Project File Structure:
train-scheduler-ai/
│── README.md                 # Project overview, setup, usage
│── requirements.txt          # Python dependencies
│── main.py                   # Entry point (CLI / Orchestrator)
│── server.py                 # (Optional) REST API for demo
│── config.yaml               # Global configs (timings, headway defaults, etc.)
│
├── core/                     # Shared utilities (used by all members)
│   ├── __init__.py
│   ├── models.py             # Train, Section, Station classes
│   ├── utils.py              # Common helpers (time handling, JSON I/O)
│   ├── logger.py             # Custom logging + explanation logs
│   └── sample_input.json     # Example dataset for quick testing
│
├── member1_optimization_engine/   # Member 1 – Scheduling & Optimization
│   ├── __init__.py
│   ├── greedy_scheduler.py        # Heuristic baseline scheduler
│   ├── ortools_scheduler.py       # CP-SAT constraint solver
│   ├── reopt_engine.py            # Re-optimization under disruptions
│   └── tests/                     # Unit tests
│       └── test_scheduler.py
│
├── member2_disruption_sim/        # Member 2 – Disruption Simulator
│   ├── __init__.py
│   ├── disruption_generator.py    # Random delay, section blockages
│   ├── scenario_loader.py         # Load pre-made disruption scenarios
│   └── tests/
│       └── test_disruptions.py
│
├── member3_visualization/         # Member 3 – Visualization (Gantt/Graph)
│   ├── __init__.py
│   ├── gantt_plot.py              # Matplotlib/Plotly Gantt chart
│   ├── network_graph.py           # NetworkX/Graph visualization of routes
│   ├── dashboard.py               # Streamlit/Dash UI for demo
│   └── tests/
│       └── test_visuals.py
│
├── member4_ai_explanations/       # Member 4 – AI Explanations
│   ├── __init__.py
│   ├── llm_explainer.py           # Calls OpenAI/Gemini/Claude
│   ├── rule_based_explainer.py    # Fallback simple explanations
│   ├── prompt_templates/          # Pre-built prompt templates for LLMs
│   │   ├── conflict_explanation.txt
│   │   └── delay_explanation.txt
│   └── tests/
│       └── test_explainer.py
│
├── member5_orchestration/         # Member 5 – Integration & Pipeline
│   ├── __init__.py
│   ├── orchestrator.py            # Calls Member1→2→3→4 in pipeline
│   ├── api_handler.py             # Converts inputs/outputs to JSON
│   └── tests/
│       └── test_pipeline.py
│
├── data/                          # Input/Output Data
│   ├── inputs/                    # Train timetables, station layouts
│   │   └── sample_trains.json
│   ├── disruptions/               # Disruption datasets
│   │   └── scenario1.json
│   ├── outputs/                   # Generated schedules + logs
│   │   ├── schedule.json
│   │   ├── logs.txt
│   │   └── explanations.json
│   └── visuals/                   # Saved charts for reports
│       └── gantt_chart.png
│
└── docs/                          # Documentation
    ├── architecture.md            # High-level architecture diagram
    ├── member_roles.md            # Responsibility breakdown
    └── api_spec.md                # REST API specs if server is used

