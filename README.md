# Nexus Framework Core V4

[![DOI](https://img.shields.io/badge/DOI-pending-blue.svg)](https://zenodo.org/)
[![License: Custom](https://img.shields.io/badge/License-Proprietary/Academic-red.svg)](#licencia)

**Motor de Dinámica de Fases y Criticalidad Informacional**  
Desarrollado por **Erick Fernando Rojas R. (Efeseis-F6)**  
*NexusLab Atacama SPA — Chile (2026)*

---

## Descripción General

Nexus Framework Core V4 es un framework computacional experimental diseñado para el estudio de sistemas complejos y dinámicas emergentes. El sistema utiliza una arquitectura de redes ternarias discretas para explorar cómo reglas de interacción local producen orden estructural global.

### Áreas de Estudio:
*   **Sincronización emergente:** Formación de dominios coherentes.
*   **Dinámica de fases:** Transiciones entre estados de orden y desorden.
*   **Curvatura informacional:** Mecanismos de penalización geométrica local.
*   **Criticalidad autoorganizada:** Evolución hacia estados metaestables.
*   **Correlación espacial:** Medición de la coherencia tensorial del sistema.

## El Modelo Ternario

El framework opera sobre una grilla bidimensional donde cada celda posee un estado informacional discreto:

$$\phi \in \{-1, 0, 1\}$$

La evolución del sistema integra acoplamiento no lineal, perturbación térmica y reversibilidad parcial, permitiendo una exploración profunda de la estabilidad informacional.

## Estructura del Repositorio

*   `/nexus_framework_core_v4.py`: Motor principal del framework (Axiomatic Validator).
*   `/paper/`: Documentación científica detallada y fundamentación matemática (PDF).
*   `/plots/`: Visualizaciones de métricas (Coherencia, Entropía, Susceptibilidad).
*   `/snapshots/`: Capturas de la evolución espacial del sistema.
*   `/nexus_v4_metrics.csv`: Datos experimentales exportados para análisis externo.
*   `/LICENSE.txt`: Términos legales de uso y atribución.

## Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/efeseis/nexus-framework-core-v4.git
cd nexus-framework-core-v4

2. Instalar dependencias
pip install -r requirements.txt

3. Ejecutar simulación
python nexus_framework_core_v4.py

Reproducibilidad Científica

Este proyecto utiliza una semilla aleatoria fija (seed(42)) para garantizar que todos los resultados, métricas y snapshots presentados en el paper puedan ser replicados exactamente por investigadores externos, asegurando la trazabilidad total del experimento.

Citación

Si utilizas este framework en tu investigación, por favor cítalo de la siguiente manera:
Rojas, E. F. (2026). Nexus Framework Core V4: Motor de Dinámica de Fases y Criticalidad Informacional. NexusLab Atacama SPA. Zenodo DOI: [PENDIENTE].

Licencia

Este framework se publica bajo una licencia de Atribución Académica y Uso Científico No Comercial.

Se permite el uso, estudio y reproducción con fines de investigación académica, siempre que se mantenga la autoría de Erick Fernando Rojas R. y NexusLab Atacama SPA. Queda estrictamente prohibido el uso comercial, la redistribución como software propietario y la creación de derivados cerrados o arquitecturas privadas basadas en este core sin autorización escrita explícita.

La publicación de este código no implica cesión de propiedad intelectual sobre los motores avanzados, sistemas de optimización o tecnologías internas de NexusLab Atacama SPA.

Para más detalles, consulte el archivo LICENSE.txt.