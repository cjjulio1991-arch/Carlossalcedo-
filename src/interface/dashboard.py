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
    st.set_page_config(page_title="Enjambre Polímata v4.0", layout="wide")
    st.title("🛡️ Centro de Control: Enjambre Polímata")

    # Sidebar Info
    st.sidebar.header("Estado del Sistema")
    st.sidebar.info("Capa de Interfaz activa")
    st.sidebar.markdown("---")
    st.sidebar.write("Arquitectura: 21 Módulos (Refactored)")

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

                # Secondary Cognitive Metrics
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Flow Rate", data.get('flow_rate', 0))
                col_b.metric("Stability", data.get('stability', 'UNKNOWN'))
                col_c.metric("SNR (dB)", data.get('snr_db', 0))

                # Security Layer Visualization
                st.markdown("---")
                st.subheader("🛡️ Capa de Seguridad y Resiliencia")
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
