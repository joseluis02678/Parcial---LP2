<p align="center">
  <img src="https://github.com/joseluis02678/Parcial---LP2/blob/main/images/logo.jpg" alt="Logo UNALM" width="180">
</p>

<h1 align="center">📊 Parcial LP2 - Librería de Estadística en Python</h1>

Este proyecto fue desarrollado como parte del curso **Lenguaje de Programación II**.  
Consiste en una librería en Python que permite calcular estadísticas básicas para datos **cuantitativos y cualitativos** aplicando los principios de **programación orientada a objetos (POO)**.
Tiene una finalidad académica, por lo tanto, puede ser usado y modificado con propósitos educativos.

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


