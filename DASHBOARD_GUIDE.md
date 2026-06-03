# Guía del Dashboard Interactivo (Streamlit)

El Dashboard de **ASI Hive** es la consola central para monitorear y controlar la Superinteligencia. Se ejecuta mediante Streamlit y se comunica con el Kernel en tiempo real.

## 🕹️ Secciones Principales

### 1. Panel de Control de ASI
- **Índice de Coherencia:** Mide la estabilidad lógica de los pensamientos del sistema.
- **Nodos de Memoria:** Cantidad de conexiones activas en la memoria episódica.
- **Estado de Resiliencia:** Indica si la cadena de integridad SHA-256 es válida.

### 2. The Forge (La Forja)
Esta sección visualiza la **Auto-Mejora Recursiva**.
- **Ciclo Forge:** Muestra si el sistema está optimizando sus propios algoritmos.
- **Dimensionalidad Quantum:** Una métrica simulada de la complejidad del espacio latente.

### 3. Meta-Cognición y Debate
Visualiza el proceso de toma de decisiones del Enjambre (Swarm).
- **Debate Consensus:** El nivel de acuerdo entre los agentes (Socrates, Ada, Themis).
- **Estado del Debate:** Muestra si una acción ha sido `APROBADA` o `RECHAZADA` por el consenso.

### 4. Percepción Multimodal y Enjambre
- **Log de Percepción Visual:** Muestra el análisis de la interfaz y elementos visuales.
- **Distribución de Tareas:** Listado dinámico de lo que cada agente (Investigador, Programador, Validador) está haciendo en el ciclo actual.

### 5. Inmunología y Auto-Sanación
Muestra logs del sistema de auto-reparación cuando detecta inconsistencias en el estado compartido.

### 6. Capa de Seguridad (Mythos Guard)
- **Estado Guard:** `ACTIVE` indica que todas las herramientas están siendo verificadas formalmente antes de su ejecución.
- **Telemetría JSON:** Sección expandible para inspeccionar el estado crudo del sistema para depuración avanzada.

## 🛠️ Cómo Ejecutar
Para iniciar el dashboard, usa el siguiente comando desde la raíz del proyecto:
```bash
streamlit run src/interface/dashboard.py --server.port 3000
```
