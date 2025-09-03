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
<img width="649" height="707" alt="image" src="https://github.com/user-attachments/assets/89fc2c52-3f3c-492e-b988-72401c673550" />

