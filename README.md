
# Walmart AI Platform — Streamlit Prototype

**What this is:** A UI mockup (with mocked data) that demonstrates the *experience* of a unified AI platform: Model Catalog, Prompt Studio, Guardrails, Cost & Telemetry, Deployment, Feedback Loop, and 4 Walmart use cases.

## Quickstart
```bash
pip install streamlit pandas matplotlib
streamlit run app.py
```
The app is multi-page; use the left sidebar or "Quick Links" on Home.

## Structure
- `app.py` — Home dashboard
- `pages/Model_Catalog.py`
- `pages/Prompt_Studio.py`
- `pages/Guardrails_Config.py`
- `pages/Cost_&_Telemetry.py`
- `pages/Deployment_SDK.py`
- `pages/Feedback_Loop.py`
- `pages/UseCase_*.py` — Seller Assistant, Shopper Assistant, Catalog Enrichment, Returns Agent
- `data/` — Mock JSON for catalog, guardrails, telemetry, prompts

## Notes
- Charts use matplotlib per constraints.
- Replace mock calls with your preferred LLM SDKs and internal APIs for a live demo.
