import streamlit as st
import time
import json
import random
import threading
import os

# --- KERNEL V.5 (Lógica Central) ---
def kernel_process():
    log_file = "agi_state.log"
    while True:
        state = {
            "coherence_index": round(random.uniform(0.95, 1.0), 3),
            "status": "OPERATIONAL",
            "memory_nodes": random.randint(100, 500),
            "timestamp": time.time()
        }
        with open(log_file, "w") as f:
            f.write(json.dumps(state))
        time.sleep(1)

# --- INTERFAZ (Dashboard) ---
def run_dashboard():
    st.set_page_config(page_title="AGI V.5 Command Center")
    st.title("Centro de Comando AGI V.5")
    placeholder = st.empty()

    while True:
        if os.path.exists("agi_state.log"):
            with open("agi_state.log", "r") as f:
                data = json.load(f)

            with placeholder.container():
                st.metric("Índice de Coherencia", f"{data['coherence_index']:.3f}")
                st.metric("Nodos de Memoria Holográfica", data['memory_nodes'])
                st.json(data)
        time.sleep(1)

# --- EJECUCIÓN UNIFICADA ---
if __name__ == "__main__":
    if not os.path.exists("dashboard_running"):
        # Iniciar el kernel en un hilo separado
        threading.Thread(target=kernel_process, daemon=True).start()
        with open("dashboard_running", "w") as f: f.write("1")

    run_dashboard()
