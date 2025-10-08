
import json
import os

import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Walmart AI Platform — Prototype",
    page_icon="🛒",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        color-scheme: light;
    }
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #f5f7fb 0%, #e6ecf8 45%, #f5f7fb 100%);
        padding-top: 1.5rem;
    }
    .hero-card {
        background: linear-gradient(135deg, #0046be, #0069ff);
        color: white;
        padding: 2.4rem;
        border-radius: 1.4rem;
        box-shadow: 0 20px 50px rgba(0, 60, 172, 0.22);
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
    }
    .hero-card::after {
        content: "";
        position: absolute;
        right: -10rem;
        top: -6rem;
        width: 22rem;
        height: 22rem;
        background: rgba(255, 255, 255, 0.18);
        filter: blur(0.5px);
        border-radius: 50%;
    }
    .hero-card h1 {
        font-size: clamp(2rem, 4vw, 2.8rem);
        margin-bottom: 0.4rem;
    }
    .hero-card p {
        font-size: 1.05rem;
        opacity: 0.92;
        max-width: 720px;
    }
    div[data-testid="metric-container"] {
        background: white;
        border-radius: 1rem;
        padding: 1.1rem 1.25rem;
        box-shadow: 0 12px 32px rgba(15, 40, 125, 0.1);
        border: 1px solid rgba(0, 70, 190, 0.08);
    }
    div[data-testid="metric-container"] > label {
        font-weight: 600;
        color: #0f1a3a;
    }
    div[data-testid="metric-container"] span[data-testid="stMetricDelta"] {
        font-weight: 600;
    }
    .section-label {
        font-size: 0.9rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #3d4a75;
        font-weight: 600;
        margin-bottom: -0.6rem;
    }
    .quick-links {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .quick-links a {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.9rem 1.1rem;
        background: white;
        border-radius: 1rem;
        text-decoration: none;
        color: #0f1a3a;
        font-weight: 600;
        box-shadow: 0 8px 20px rgba(15, 40, 125, 0.08);
        border: 1px solid rgba(0, 70, 190, 0.08);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .quick-links a:hover {
        transform: translateY(-4px);
        box-shadow: 0 14px 30px rgba(0, 60, 172, 0.16);
    }
    .quick-links span.icon {
        font-size: 1.4rem;
    }
    .use-case-card {
        background: white;
        border-radius: 1.2rem;
        padding: 1.4rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        gap: 0.7rem;
        box-shadow: 0 16px 36px rgba(15, 40, 125, 0.12);
        border: 1px solid rgba(0, 70, 190, 0.08);
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }
    .use-case-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 22px 46px rgba(0, 60, 172, 0.18);
    }
    .use-case-card .title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #10224d;
    }
    .use-case-card .desc {
        font-size: 0.95rem;
        color: #475987;
        flex: 1;
    }
    .use-case-card a {
        font-weight: 600;
        color: #0056ff;
        text-decoration: none;
    }
    .use-case-card a:hover {
        text-decoration: underline;
    }
    @media (max-width: 1024px) {
        .hero-card {
            padding: 2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <h1>Walmart AI Platform — Prototype</h1>
        <p>Vertical slice across the Model Catalog, Prompt Studio, Guardrails, Cost Insights, Deployment, and Feedback pillars. Explore how the platform unifies governance with delightful builder ergonomics.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-label">Platform health</div>
    """,
    unsafe_allow_html=True,
)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Active Apps", 4, delta="+1 WoW")
with col2:
    st.metric("Total Cost (7d)", "$7,877", delta="-6%")
with col3:
    st.metric("Median Latency", "409 ms", delta="-4%")
with col4:
    st.metric("Guardrail Blocks (7d)", 37, delta="-12%")

st.markdown("""<div class="section-label" style="margin-top:2rem;">Navigation</div>""", unsafe_allow_html=True)
st.markdown("""### Quick Links""")

quick_links = [
    {"icon": "🔍", "label": "Model Catalog", "page": "Model_Catalog"},
    {"icon": "🎯", "label": "Prompt Studio", "page": "Prompt_Studio"},
    {"icon": "🔒", "label": "Guardrails Config", "page": "Guardrails_Config"},
    {"icon": "📊", "label": "Cost & Telemetry", "page": "Cost_&_Telemetry"},
    {"icon": "🚀", "label": "Deployment", "page": "Deployment_SDK"},
    {"icon": "📝", "label": "Feedback Loop", "page": "Feedback_Loop"},
]

st.markdown("<div class='quick-links'>", unsafe_allow_html=True)
for link in quick_links:
    st.markdown(
        f"<a href='/{link['page']}'><span class='icon'>{link['icon']}</span><span>{link['label']}</span></a>",
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""<div class="section-label" style="margin-top:1.8rem;">Featured journeys</div>""", unsafe_allow_html=True)
st.markdown("### Featured Use Cases")
uc_cols = st.columns(4)
use_cases = [
    ("Seller Assistant", "Summarize GMV, flag anomalies, recommend actions", "UseCase_Seller_Assistant.py", "🤝"),
    ("Shopper Assistant", "Conversational shopping with size fit & availability", "UseCase_Shopper_Assistant.py", "🛍️"),
    ("Catalog Enrichment", "Rewrite titles, normalize attributes, ground to policy", "UseCase_Catalog_Enrichment.py", "🗂️"),
    ("Returns Agent", "Policy-aware returns with empathy and fraud checks", "UseCase_Returns_Agent.py", "📦"),
]

for col, (title, desc, page, icon) in zip(uc_cols, use_cases):
    with col:
        st.markdown(
            f"""
            <div class="use-case-card">
                <div class="title">{icon} {title}</div>
                <div class="desc">{desc}</div>
            """,
            unsafe_allow_html=True,
        )
        st.page_link(f"pages/{page}", label="Open Journey →")
        st.markdown("</div>", unsafe_allow_html=True)

st.divider()

telemetry_path = os.path.join("data", "telemetry.json")
if os.path.exists(telemetry_path):
    with open(telemetry_path) as f:
        telemetry = pd.DataFrame(json.load(f))

    telemetry["date"] = pd.to_datetime(telemetry["date"])
    chart_data = (
        telemetry.groupby(["date", "app"], as_index=False)["cost_usd"].sum()
    )

    st.markdown("### Cost by App Over Time")
    st.caption("Aggregated daily cost across active applications, sourced from the telemetry feed.")

    line_chart = (
        alt.Chart(chart_data)
        .mark_line(point=True)
        .encode(
            x=alt.X("date:T", title="Date"),
            y=alt.Y("cost_usd:Q", title="USD"),
            color=alt.Color("app:N", title="Application"),
            tooltip=[
                alt.Tooltip("app:N", title="Application"),
                alt.Tooltip("date:T", title="Date", format="%b %d"),
                alt.Tooltip("cost_usd:Q", title="Cost", format="$.2f"),
            ],
        )
        .properties(height=360)
        .interactive()
    )

    st.altair_chart(line_chart, use_container_width=True)
else:
    st.warning("Telemetry not found")
