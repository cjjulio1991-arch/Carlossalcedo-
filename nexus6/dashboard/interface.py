import streamlit as st
import time
import json
import os
import threading
from nexus6.core.hive import HiveKernel

def run_dashboard():
    st.set_page_config(page_title="NEXUS-6 Ω Command Center", layout="wide")

    # Custom Cyberpunk CSS
    st.markdown("""
        <style>
        .main { background-color: #0d0221; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
        .stMetric { background: rgba(0, 255, 65, 0.1); border: 1px solid #00ff41; padding: 10px; border-radius: 5px; }
        .agent-grid { display: grid; grid-template-columns: repeat(10, 1fr); gap: 5px; margin-top: 20px; }
        .agent-node { width: 100%; aspect-ratio: 1; border-radius: 2px; }
        </style>
    """, unsafe_allow_html=True)

    st.title("⚡ NEXUS-6 Ω: SWARM INTELLIGENCE MONITOR")

    # Start Kernel if not running globally in the process
    if 'kernel' not in st.session_state:
        # Check if a kernel thread is already running to avoid duplicates
        kernel_running = False
        for t in threading.enumerate():
            if t.name == "NexusHiveKernel":
                kernel_running = True
                break

        if not kernel_running:
            kernel = HiveKernel(100)
            kernel_thread = threading.Thread(target=kernel.run, daemon=True, name="NexusHiveKernel")
            kernel_thread.start()

        st.session_state['kernel'] = True

    placeholder = st.empty()

    while True:
        if os.path.exists("agi_state.log"):
            try:
                with open("agi_state.log", "r") as f:
                    data = json.load(f)

                with placeholder.container():
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Coherencia Cognitiva", data['coherence'])
                    col2.metric("Índice de Evolución", data['evolution'])
                    col3.metric("Salud del Enjambre", f"{data['health']*100:.1f}%")
                    col4.metric("Mythos Guard Hash", data['security_hash'][:8] + "...")

                    st.write("### Swarm Load Heatmap (100 Agents)")

                    # Manual grid for the heatmap
                    loads = data['agent_loads']
                    cols = st.columns(10)
                    for i in range(100):
                        load = loads[i]
                        color = f"rgba(0, 255, 65, {load})" # Green intensity based on load
                        with cols[i % 10]:
                            st.markdown(f'<div style="background-color: {color}; height: 30px; border: 1px solid #00ff41; margin-bottom: 5px;" title="Agent {i}: {load*100:.1f}%"></div>', unsafe_allow_html=True)

                    with st.expander("Telemetry JSON Raw Feed"):
                        st.json(data)
            except Exception as e:
                st.error(f"Sync error: {e}")

        time.sleep(1)

if __name__ == "__main__":
    run_dashboard()
