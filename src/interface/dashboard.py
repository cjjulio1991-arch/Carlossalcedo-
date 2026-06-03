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
    col1, col2 = st.columns(2)

    placeholder = st.empty()

    while True:
        try:
            data = shared_state.get_all()

            with placeholder.container():
                c1, c2, c3 = st.columns(3)
                c1.metric("Índice de Coherencia", f"{data['coherence_index']:.3f}")
                c2.metric("Nodos de Memoria", data['memory_nodes'])
                c3.metric("Status", data['status'])

                st.subheader("Telemetría en Tiempo Real (JSON)")
                st.json(data)

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
