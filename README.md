<p align="center">
  <img src="https://raw.githubusercontent.com/joseluis02678/Parcial---LP2/main/images/logo.jpg" alt="Logo UNALM" width="180">
</p>

<h1 align="center">Parcial LP2 – Librería de Estadística en Python</h1>

<p align="center">
  <b>Universidad Nacional Agraria La Molina</b><br>
  <i>Facultad de Economía y Planificación · Departamento de Estadística e Informática</i><br><br>
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python badge">
  <img src="https://img.shields.io/badge/POO-Programación%20Orientada%20a%20Objetos-green" alt="POO badge">
  <img src="https://img.shields.io/badge/Estado-En%20Desarrollo-orange" alt="Estado badge">
</p>

---

## Integrantes del grupo
### Nombres y apellidos:
- Jose Luis Garay Ramos	
- Omar Sebastian Castillo	
- Ayrton Sanchez Gómez	


## Objetivo del proyecto

El objetivo principal es aplicar los conceptos de clases, herencia y polimorfismo para crear un paquete que permita realizar análisis estadísticos simples, organizados en módulos fáciles de usar y mantener.

---

## Estructura del proyecto

```text
Parcial---LP2/
│
├── estadística_lib/
│   ├── estadistica/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── cuantitativos.py
│   │   ├── cualitativos.py
│   │
│   ├── otros/
│   │   └── matriz.py
│   │
│   └── tests/
│       ├── test_cuantitativos.py
│       └── test_cualitativos.py
│
├── notebooks/
│   ├── demo_cuantitativos.ipynb
│   ├── demo_cualitativos.ipynb
|   |── demo_inferencia.ipynb
|   |── demo_matrices.ipynb
│
├── images/
│   └── logo.jpg
│
├── README.md
└── requirements.txt

## Instalación y uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/joseluis02678/Parcial---LP2.git
Entrar a la carpeta del proyecto:

bash
Copiar código
cd Parcial---LP2
Instalar las dependencias (si es necesario):

bash
Copiar código
pip install -r requirements.txt
Ejecutar los ejemplos desde los notebooks:

bash
Copiar código
notebooks/demo_cuantitativos.ipynb
notebooks/demo_cualitativos.ipynb

Pruebas
Las pruebas se encuentran en la carpeta tests y se pueden ejecutar con el siguiente comando:
pytest estadística_lib/tests/


