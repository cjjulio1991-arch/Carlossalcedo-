import streamlit as st
import asyncio
import pandas as pd
import time
from nexus6.core.engine.kernel import IntelligenceEngine

# Configure page
st.set_page_config(page_title="NEXUS-6 Ω | Admin Console", layout="wide")

# Custom CSS for Nexus UI
st.markdown("""
    <style>
    .main { background-color: #050505; color: #00d4ff; font-family: 'Inter', sans-serif; }
    .stMetric { background: rgba(0, 212, 255, 0.05); border: 1px solid #00d4ff; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #ffffff !important; text-transform: uppercase; letter-spacing: 2px; }
    .stButton>button { width: 100%; background-color: #00d4ff; color: black; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

if 'engine' not in st.session_state:
    st.session_state.engine = IntelligenceEngine()

st.title("💠 NEXUS-6 Ω : System Intelligence")

# Sidebar Metrics
with st.sidebar:
    st.header("Core Metrics")
    health = st.session_state.engine.immune_system.health_metrics
    st.metric("System Integrity", f"{health['integrity']*100:.1f}%")
    st.metric("Cognitive Noise", f"{health['noise_level']*100:.1f}%")

    if st.button("Manual Self-Healing"):
        st.session_state.engine.immune_system.update_health()
        st.success("Immune system optimized.")

# Main Interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Problem Submission")
    problem = st.text_area("Enter complex problem or objective:", height=150, placeholder="Example: Optimize global supply chain resilience using first principles...")

    if st.button("INITIATE REASONING CYCLE"):
        if problem:
            with st.status("Reasoning in progress...", expanded=True) as status:
                st.write("Decomposing via First Principles...")
                # Run async solve in sync streamlit
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(st.session_state.engine.solve_problem(problem))

                st.write("Synthesizing solutions...")
                time.sleep(0.5)
                st.write("Auditing safety...")

                status.update(label="Reasoning Cycle Complete", state="complete", expanded=False)

            st.success("Task Resolved")
            st.json(result)
        else:
            st.warning("Please enter a problem description.")

with col2:
    st.subheader("Real-time Observability")
    # Simulate some log activity
    logs = st.session_state.engine.memory.short_term
    if logs:
        st.write("Recent Activity Log")
        st.table(pd.DataFrame(logs).tail(5))
    else:
        st.info("Waiting for activity data...")

    st.subheader("Memory Tier Status")
    st.write(f"Experience Memory: {len(st.session_state.engine.memory.experience.collection.get()['ids'])} records")
    st.write(f"Knowledge Base: {len(st.session_state.engine.memory.long_term.collection.get()['ids'])} records")

st.divider()
st.caption("NEXUS-6 Ω | Cognitive Architecture | Production Ready")
