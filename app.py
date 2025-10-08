
import streamlit as st
from datetime import datetime
import json, os, pandas as pd
from urllib.parse import quote
import matplotlib.pyplot as plt

st.set_page_config(page_title="Walmart AI Platform — Prototype", layout="wide")

st.markdown(
    """
    <style>
        .hero-card {
            background: radial-gradient(circle at 0% 0%, #1e88e5 0%, #0d47a1 60%, #041e42 100%);
            padding: 2.8rem 3rem;
            border-radius: 24px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 20px 40px rgba(4, 30, 66, 0.35);
        }
        .hero-card h1 {
            font-size: 2.3rem;
            margin-bottom: 0.4rem;
        }
        .hero-card p {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        .metric-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1.1rem;
            margin-bottom: 2rem;
        }
        .metric-card {
            background: white;
            border-radius: 18px;
            padding: 1.4rem 1.6rem;
            box-shadow: 0 12px 24px rgba(4, 30, 66, 0.08);
            border: 1px solid rgba(4, 30, 66, 0.08);
        }
        .metric-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 600;
            color: #041e42;
            opacity: 0.75;
        }
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #041e42;
            margin: 0.4rem 0;
        }
        .metric-delta {
            font-size: 0.9rem;
            font-weight: 600;
        }
        .metric-delta.positive { color: #0f9d58; }
        .metric-delta.negative { color: #d93025; }
        .quick-link-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
            margin-bottom: 2.5rem;
        }
        .quick-link {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-start;
            gap: 0.35rem;
            padding: 1.2rem 1.4rem;
            border-radius: 16px;
            background: linear-gradient(140deg, rgba(255,255,255,0.94), rgba(236, 244, 255, 0.94));
            border: 1px solid rgba(4, 30, 66, 0.1);
            box-shadow: 0 10px 22px rgba(4, 30, 66, 0.08);
            transition: transform 150ms ease, box-shadow 150ms ease;
            text-decoration: none;
            color: inherit;
        }
        .quick-link:hover {
            transform: translateY(-4px);
            box-shadow: 0 18px 30px rgba(4, 30, 66, 0.12);
        }
        .quick-link span:first-child {
            font-size: 1.8rem;
        }
        .quick-link span:last-child {
            font-size: 1.05rem;
            font-weight: 600;
            color: #041e42;
        }
        .use-case-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
        }
        .use-case-card {
            background: white;
            border-radius: 18px;
            padding: 1.5rem 1.6rem;
            border: 1px solid rgba(4, 30, 66, 0.1);
            box-shadow: 0 12px 24px rgba(4, 30, 66, 0.08);
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            transition: transform 150ms ease, box-shadow 150ms ease;
        }
        .use-case-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 18px 32px rgba(4, 30, 66, 0.12);
        }
        .use-case-card h3 {
            margin: 0;
            font-size: 1.25rem;
            color: #041e42;
        }
        .use-case-card p {
            margin: 0;
            color: rgba(4, 30, 66, 0.75);
            min-height: 56px;
        }
        .use-case-card a {
            font-weight: 600;
            color: #1e88e5;
            text-decoration: none;
        }
        .use-case-card a:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <h1>Walmart AI Platform — Prototype</h1>
        <p>Unified workspace to design, deploy, and govern generative AI applications across the Walmart ecosystem.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Vertical slice: Model Catalog • Prompt Studio • Guardrails • Cost Insights • Deployment • Feedback")

st.info("This is a UI **mockup** with simulated data to demonstrate the experience and architecture pattern.")

metric_data = [
    ("Active Apps", "4", "+1 WoW"),
    ("Total Cost (7d)", "$7,877", "-6%"),
    ("Median Latency", "409 ms", "-4%"),
    ("Guardrail Blocks (7d)", "37", "-12%"),
]

metric_html = "<div class='metric-grid'>"
for label, value, delta in metric_data:
    trend_class = "positive" if "+" in delta else "negative"
    metric_html += f"""
        <div class='metric-card'>
            <div class='metric-label'>{label}</div>
            <div class='metric-value'>{value}</div>
            <div class='metric-delta {trend_class}'>{delta}</div>
        </div>
    """
metric_html += "</div>"
st.markdown(metric_html, unsafe_allow_html=True)

st.markdown("### Quick Links")

quick_links = [
    ("🔍", "Model Catalog", "Model_Catalog"),
    ("🎯", "Prompt Studio", "Prompt_Studio"),
    ("🔒", "Guardrails Config", "Guardrails_Config"),
    ("📊", "Cost & Telemetry", "Cost_&_Telemetry"),
    ("🚀", "Deployment", "Deployment_SDK"),
    ("📝", "Feedback Loop", "Feedback_Loop"),
]

quick_link_html = "<div class='quick-link-grid'>"
for emoji, label, page in quick_links:
    quick_link_html += f"<a class='quick-link' href='/?page={quote(page)}'><span>{emoji}</span><span>{label}</span></a>"
quick_link_html += "</div>"
st.markdown(quick_link_html, unsafe_allow_html=True)

st.markdown("### Featured Use Cases")

use_case_html = "<div class='use-case-grid'>"
for title, desc in [
    ("Seller Assistant", "Summarize GMV, flag anomalies, recommend actions"),
    ("Shopper Assistant", "Conversational shopping with size fit & availability"),
    ("Catalog Enrichment", "Rewrite titles, normalize attributes, ground to policy"),
    ("Returns Agent", "Policy-aware returns with empathy and fraud checks"),
]:
    page_name = f"UseCase_{title.replace(' ', '_')}"
    use_case_html += f"""
        <div class='use-case-card'>
            <h3>{title}</h3>
            <p>{desc}</p>
            <a href='/?page={quote(page_name)}'>Open use case →</a>
        </div>
    """
use_case_html += "</div>"
st.markdown(use_case_html, unsafe_allow_html=True)

# Simple cost trend chart (matplotlib, single plot)
telemetry_path = os.path.join("data","telemetry.json")
if os.path.exists(telemetry_path):
    with open(telemetry_path) as f:
        t = pd.DataFrame(json.load(f))
    t["date"] = pd.to_datetime(t["date"])
    fig = plt.figure()
    for app in t["app"].unique():
        subset = t[t["app"]==app].groupby("date").sum(numeric_only=True)["cost_usd"]
        plt.plot(subset.index, subset.values, label=app)
    plt.title("Cost by App Over Time")
    plt.xlabel("Date")
    plt.ylabel("USD")
    plt.legend()
    st.pyplot(fig)
else:
    st.warning("Telemetry not found")
