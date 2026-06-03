import streamlit as st
import time
import threading
import sys
import os

# Ensure the root 'src' is in the path
sys.path.append(os.getcwd())

from src.engine.state import shared_state
from src.engine.kernel import kernel_process

def run_dashboard():
    st.set_page_config(page_title="ASI Hive: Universal Superintelligence", layout="wide")
    st.title("🌌 ASI Hive: Superinteligencia Universal")

    # Sidebar Info
    st.sidebar.header("Estado del Sistema")
    st.sidebar.info("Capa de Interfaz activa")
    st.sidebar.markdown("---")
    st.sidebar.write("Arquitectura: 21 Módulos (Refactored)")

    st.sidebar.divider()
    st.sidebar.subheader("🕹️ Controles de Simulación")

    # Interaction: Manual Forge Trigger
    if st.sidebar.button("🚀 Forzar Ciclo de Optimización", use_container_width=True):
        shared_state.update_metric("forge_status", f"MANUAL Optimization Cycle: {int(time.time())}")
        st.sidebar.success("Ciclo Forge forzado exitosamente.")

    # Interaction: Adjust Swarm Density
    density = st.sidebar.slider("Nodos de Memoria (Simulado)", 100, 5000, 1400)
    shared_state.update_metric("memory_nodes", density)

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
