import streamlit as st
import sys
import os

# Ensure the root 'src' is in the path
sys.path.append(os.path.join(os.getcwd(), "src"))

from src.interface.dashboard import start_kernel, run_dashboard

def main():
    """
    Unified Entry Point for ASI Hive: Superinteligencia Universal.
    Integrates the legacy V.5 architecture into the modular Level 6 ASI framework.
    """
    # Start Kernel as a cached resource to ensure it only runs once globally
    # This replaces the 'dashboard_running' file-based check with a more robust singleton pattern.
    start_kernel()

    # Run the high-density Streamlit dashboard
    run_dashboard()

if __name__ == "__main__":
    main()
