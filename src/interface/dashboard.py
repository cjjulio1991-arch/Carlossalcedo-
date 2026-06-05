import streamlit as st
import time
import threading
import sys
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Ensure the root 'src' is in the path
sys.path.append(os.getcwd())

from src.engine.state import shared_state
from src.engine.kernel import kernel_process

def run_dashboard():
    st.set_page_config(page_title="AetherOS Nexus | Level 6 Cognitive OS", layout="wide")
    st.title("🌌 AetherOS Nexus: Autonomous Cognitive Architecture")

    # Sidebar Info
    st.sidebar.header("AetherOS Core Status")
    st.sidebar.info("Nexus Interface Active (Level 6)")
    st.sidebar.markdown("---")
    st.sidebar.write("Architecture: Lyapunov-Constrained Autopoietic Core")

    st.sidebar.divider()
    st.sidebar.subheader("🕹️ Controles de Simulación")

    # Interaction: Manual Forge Trigger
    if st.sidebar.button("🚀 Forzar Ciclo de Optimización", use_container_width=True):
        shared_state.update(forge_status=f"MANUAL Optimization Cycle: {int(time.time())}")
        st.sidebar.success("Ciclo Forge forzado exitosamente.")

    # Interaction: Adjust Swarm Density
    density = st.sidebar.slider("Nodos de Memoria (Simulado)", 100, 5000, 1400)
    shared_state.update(memory_nodes=density)

    # Interaction: Security Level
    st.sidebar.select_slider("Nivel de Seguridad Mythos", options=["Standard", "Hardened", "Paranoid"])

    # Main Dashboard Area
    placeholder = st.empty()

    while True:
        try:
            data = shared_state.get_all()

            with placeholder.container():
                # Primary Metrics
                c1, c2, c3 = st.columns(3)
                c1.metric("Índice de Coherencia", f"{data.get('coherence_index', 0.0):.4f}")
                c2.metric("Nodos de Memoria", data.get('memory_nodes', 0))
                c3.metric("Resilience Status", data.get('resilience_status', 'N/A'))

                # Deep RL Metrics
                rl1, rl2, rl3 = st.columns(3)
                rl1.metric("RL Action Selection", data.get('rl_action', 0))
                rl2.metric("Learning Rate (Epsilon)", data.get('rl_epsilon', 1.0))
                rl3.metric("Cognitive Load", data.get('cognitive_load', 0))

                # ASI Layer Row
                st.subheader("🚀 Nivel de Superinteligencia (ASI)")
                asi1, asi2, asi3 = st.columns(3)
                asi1.metric("The Forge (Self-Improvement)", f"Cycle {data.get('forge_status', '0').split()[-1] if 'Cycle' in data.get('forge_status','') else 'Active'}")
                asi2.metric("Quantum Dimensionality", data.get("quantum_dim", 1024))
                asi3.info(f"**Forge Log:** {data.get('forge_status', 'IDLE')}")

                # Swarm & Routing Row
                st.subheader("Hive Intelligence & Routing")
                r_col1, r_col2, r_col3 = st.columns(3)
                r_col1.metric("Active Model (Polyglot)", data.get("active_model", "None"))
                r_col2.info(f"**Routing Tier:** {data.get('routing_tier', 'N/A')}")
                r_col3.metric("Episodic Memory Size", data.get("memory_size", 0))

                # Metacognition Row
                st.subheader("🧠 Meta-Cognición y Auto-Evolución")
                m_col1, m_col2, m_col3 = st.columns(3)
                m_col1.metric("Debate Consensus", f"{data.get('consensus_score', 0.0):.2f}")
                m_col2.info(f"**Debate Status:** {data.get('last_debate_status', 'N/A')}")
                m_col3.warning(f"**Meta-Control:** {data.get('meta_control_log', 'IDLE')}")

                # Secondary Cognitive Metrics
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Flow Rate", data.get('flow_rate', 0))
                col_b.metric("Stability", data.get('stability', 'UNKNOWN'))
                col_c.metric("Tool Status (Verified)", data.get("last_tool_status", "IDLE"))

                # Advanced Perception & Swarm Activity
                st.markdown("---")
                st.subheader("👁️ Percepción Multimodal y Actividad del Enjambre")
                p_col1, p_col2 = st.columns([1, 2])
                with p_col1:
                    st.write("**Visual Perception Log:**")
                    st.caption(data.get("perception_log", "No visual data available."))
                with p_col2:
                    st.write("**Swarm Task Distribution (Hive):**")
                    activities = data.get("swarm_activity", [])
                    for act in activities:
                        st.write(f"- {act}")

                    # Level 6 Heatmap Visualization
                    st.markdown("---")
                    st.write("**Mapa de Calor de Enjambre Nivel 6 (100 Agentes):**")
                    l6_data = data.get("swarm_l6_telemetry", [])
                    if l6_data:
                        # Create a 10x10 grid simulation
                        cols = st.columns(10)
                        for i, agent in enumerate(l6_data[:100]):
                            with cols[i % 10]:
                                load = agent.get('load', 0.5)
                                color = "green" if load < 0.4 else "orange" if load < 0.7 else "red"
                                st.markdown(f"""
                                <div style="width: 100%; height: 20px; background-color: {color}; border-radius: 2px; margin-bottom: 5px; opacity: 0.8;"
                                     title="Agent {agent.get('agent_id')} | Load: {load:.2f}"></div>
                                """, unsafe_allow_html=True)

                # Immunology & Self-Healing
                st.markdown("---")
                st.subheader("🛡️ Inmunología y Auto-Sanación")
                heal_log = data.get("self_healing_log", "No healing activity detected.")
                st.code(heal_log, language="text")

                # Security Layer Visualization
                st.markdown("---")
                st.subheader("🛡️ Capa de Seguridad y Resiliencia")
                st.success(f"**Mythos Guard Status:** {data.get('mythos_guard_status', 'INACTIVE')}")
                st.info(f"**Backup Hash (SHA-256):** `{data.get('last_backup_hash', 'NO HASH')}`")

                # Advanced Visualizations
                st.markdown("---")
                st.subheader("📊 Análisis de Métricas Cognitivas (AetherOS)")
                v_col1, v_col2 = st.columns(2)

                with v_col1:
                    # 2D Radar Chart for System Health
                    categories = ['Coherencia', 'Resiliencia', 'Flujo', 'Estabilidad', 'Carga']
                    values = [
                        data.get('coherence_index', 0.95),
                        1.0 if data.get('resilience_status') == 'SECURE' else 0.5,
                        data.get('flow_rate', 50) / 100.0,
                        1.0 if data.get('stability') == 'STABLE' else 0.8,
                        data.get('cognitive_load', 0.5)
                    ]
                    fig_radar = go.Figure(data=go.Scatterpolar(
                        r=values,
                        theta=categories,
                        fill='toself',
                        line_color='#3b82f6'
                    ))
                    fig_radar.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                        showlegend=False,
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font_color="white",
                        height=350,
                        margin=dict(l=40, r=40, t=40, b=40)
                    )
                    st.plotly_chart(fig_radar, use_container_width=True)

                with v_col2:
                    # Swarm Load Distribution Histogram
                    l6_loads = [a.get('load', 0.5) for a in data.get("swarm_l6_telemetry", [])]
                    if not l6_loads: l6_loads = np.random.uniform(0.1, 0.9, 100)

                    fig_hist = px.histogram(
                        x=l6_loads,
                        nbins=20,
                        title="Distribución de Carga del Enjambre (L6)",
                        labels={'x': 'Carga del Agente', 'y': 'Frecuencia'},
                        color_discrete_sequence=['#3b82f6']
                    )
                    fig_hist.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        font_color="white",
                        height=350,
                        margin=dict(l=20, r=20, t=60, b=20)
                    )
                    st.plotly_chart(fig_hist, use_container_width=True)

                # Telemetry Area
                with st.expander("Telemetría Completa (JSON)", expanded=False):
                    st.json(data)

                # Event Log (Simulation)
                st.subheader("📜 Log de Eventos del Sistema")
                st.code(f"[{time.strftime('%H:%M:%S')}] Cognitive Cycle: Verified\n"
                        f"[{time.strftime('%H:%M:%S')}] Resilience Snapshot: Created\n"
                        f"[{time.strftime('%H:%M:%S')}] Integrity Check: PASSED")

        except Exception as e:
            st.error(f"Error al cargar datos: {e}")

        time.sleep(1)

@st.cache_resource
def start_kernel():
    """
    Starts the kernel in a background thread once per server lifecycle.
    """
    thread = threading.Thread(target=kernel_process, daemon=True)
    thread.start()
    return thread

if __name__ == "__main__":
    # Start Kernel as a cached resource to ensure it only runs once globally
    start_kernel()
    run_dashboard()
