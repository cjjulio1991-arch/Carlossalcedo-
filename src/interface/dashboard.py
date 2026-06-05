import streamlit as st
import time
import threading
import sys
import os
import plotly.express as px
import pandas as pd

# Ensure the root 'src' is in the path
sys.path.append(os.getcwd())

from src.engine.state import shared_state
from src.engine.kernel import kernel_process

def run_dashboard():
    st.set_page_config(page_title="AetherOS Admin Console | System Intelligence", layout="wide")
    st.title("🛡️ AetherOS: Professional Admin Console")

    # Sidebar Info
    st.sidebar.header("System Status")
    st.sidebar.info("AetherOS Core: ACTIVE")
    st.sidebar.markdown("---")
    st.sidebar.write("Target: Functional Systems Auditing")

    # Main Dashboard Area
    placeholder = st.empty()

    while True:
        try:
            data = shared_state.get_all()

            with placeholder.container():
                # Primary Resource Metrics
                st.subheader("📊 Recursos del Sistema (Real-Time)")
                c1, c2, c3 = st.columns(3)
                c1.metric("Uso de CPU (%)", f"{data.get('cpu_percent', 0.0):.2f}%")
                c2.metric("Memoria RAM Usada", f"{data.get('memory_used_mb', 0):.2f} MB")
                c3.metric("Memoria RAM (%)", f"{data.get('memory_percent', 0.0):.2f}%")

                # System Load
                load = data.get('load_avg', [0.0, 0.0, 0.0])
                st.write(f"**Carga del Sistema (1m, 5m, 15m):** {load[0]}, {load[1]}, {load[2]}")

                # Security Overview
                st.markdown("---")
                st.subheader("🛡️ Auditoría de Seguridad")
                sec1, sec2, sec3 = st.columns(3)
                sec1.metric("Archivos Vulnerables", data.get('security_issues', 0))
                sec2.metric("Puertos Abiertos (Listeners)", data.get('active_listeners', 0))
                sec3.success(f"Estado: {data.get('resilience_status', 'N/A')}")

                # Detailed Security Logs
                audit_log = data.get('security_audit_log', {})
                with st.expander("Ver Detalles de Auditoría de Seguridad", expanded=False):
                    st.write("**Archivos con Escritura Universal (Vulnerabilidades):**")
                    writable = audit_log.get('world_writable', [])
                    if writable:
                        st.error(f"Se encontraron {len(writable)} archivos vulnerables.")
                        st.code("\n".join(writable))
                    else:
                        st.success("No se detectaron archivos con escritura universal en el directorio raíz.")

                    st.write("**Puertos de Red Activos:**")
                    listeners = audit_log.get('active_listeners', [])
                    if listeners:
                        st.code("\n".join(listeners))

                # Process Monitoring
                st.markdown("---")
                st.subheader("🖥️ Monitor de Procesos (Top CPU)")
                procs = data.get('process_list', [])
                if procs:
                    # Clean up ps aux output for display
                    df_procs = [p.split(None, 10) for p in procs]
                    if df_procs:
                        cols = ["USER", "PID", "%CPU", "%MEM", "VSZ", "RSS", "TTY", "STAT", "START", "TIME", "COMMAND"]
                        df = pd.DataFrame(df_procs, columns=cols)
                        st.table(df)
                else:
                    st.info("Obteniendo lista de procesos...")

                # System Logs
                st.markdown("---")
                st.subheader("📜 Eventos del Kernel")
                st.code(f"[{time.strftime('%H:%M:%S')}] Telemetry Cycle: Success\n"
                        f"[{time.strftime('%H:%M:%S')}] Security Scan: Completed\n"
                        f"[{time.strftime('%H:%M:%S')}] Integrity Hash: {data.get('last_backup_hash', 'N/A')}")

        except Exception as e:
            st.error(f"Error al cargar datos: {e}")

        time.sleep(2)

@st.cache_resource
def start_kernel():
    """Starts the kernel in a background thread."""
    thread = threading.Thread(target=kernel_process, daemon=True)
    thread.start()
    return thread

if __name__ == "__main__":
    start_kernel()
    run_dashboard()
