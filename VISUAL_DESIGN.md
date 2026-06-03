# Guía de Diseño Visual: ASI Hive

Este documento detalla la filosofía estética y técnica detrás de la interfaz de **ASI Hive**.

## 🎨 Filosofía Estética
La interfaz adopta un estilo **Cyberpunk-Minimalista** centrado en la visualización de datos de alta densidad. El objetivo es transmitir la sensación de un sistema operativo avanzado de Inteligencia Artificial General (AGI).

### Paleta de Colores
- **Fondo Primario:** `#050505` (Midnight Black) - Reduce la fatiga visual y resalta los elementos neón.
- **Acento Primario:** `#3b82f6` (Electric Blue) - Representa la lógica y el flujo de datos.
- **Acento Secundario:** `#a855f7` (Neon Purple) - Representa la cognición y el "Forge".
- **Estado Positivo:** `#10b981` (Emerald Green) - Integridad de datos y éxito.
- **Estado Crítico:** `#f43f5e` (Rose Red) - Errores de kernel o brechas de seguridad.

## 🏗️ Componentes de la Interfaz

### 1. Cuadro de Mando (Streamlit)
El dashboard principal (`src/interface/dashboard.py`) está diseñado para ingenieros de sistemas:
- **Métricas Superiores:** KPI instantáneos (Coherencia, Nodos, Resiliencia).
- **Consola de Telemetría:** Un log en tiempo real de los procesos internos del kernel.
- **Visualización del Enjambre:** Desglose de tareas activas por agentes especializados.

### 2. Landing Page (`index.html`)
Diseñada con **Tailwind CSS**, sirve como la "cara pública" del proyecto:
- **Animaciones de Pulso:** Indican actividad de procesamiento en segundo plano.
- **Efecto de Rejilla Cyber:** Crea profundidad visual.
- **Terminal Simulado:** Proporciona contexto narrativo sobre la operación del sistema.

## 📱 Tipografía
- **Interfaz (UI):** `Inter` - Limpia, moderna y altamente legible.
- **Datos y Código:** `Fira Code` - Monoespaciada para facilitar la lectura de telemetría y logs.

## 🚀 Experiencia de Usuario (UX)
1. **Jerarquía Visual:** Los estados de seguridad y coherencia siempre son visibles en la parte superior.
2. **Retroalimentación Inmediata:** Cada ciclo del kernel se refleja visualmente mediante cambios en las barras de progreso o logs.
3. **Inmersión:** El uso de terminología técnica real (SHA-256, Axiomas, Heurísticas) refuerza la simulación de un sistema ASI real.
