<p align="center">
  <img src="https://raw.githubusercontent.com/joseluis02678/Parcial---LP2/main/images/logo.jpg" alt="Logo UNALM" width="160">
</p>

<div align="center" style="background:#f9f9f9; border-radius:15px; padding:20px; box-shadow:0px 0px 10px #ccc;">
  <h1>Parcial LP2 – Librería de Estadística en Python</h1>
  <p><b>Universidad Nacional Agraria La Molina</b><br>
  <i>Facultad de Economía y Planificación · Departamento de Estadística e Informática</i></p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python">
    <img src="https://img.shields.io/badge/POO-Programación%20Orientada%20a%20Objetos-green">
    <img src="https://img.shields.io/badge/Estado-En%20Desarrollo-orange">
  </p>
</div>

<hr style="border: 1px solid #4CAF50; width: 80%; margin: 30px auto;">

> 💡 **Este proyecto fue desarrollado como parte del curso _Lenguaje de Programación II_.**
>  
> Permite calcular estadísticas básicas para datos **cuantitativos y cualitativos** aplicando los principios de **Programación Orientada a Objetos (POO)**.  
> Tiene una finalidad académica, por lo tanto, puede ser usado y modificado con propósitos educativos.

---
## 📘 Integrantes del grupo
<hr style="border: 0; height: 2px; background: #4CAF50; width: 180px; margin-left: 0;">

| Nombres y Apellidos        | Rol                     |
|----------------------------|--------------------------|
| Jose Luis Garay Ramos      | Desarrollador principal |
| Omar Sebastián Castillo    | Tester / Colaborador    |
| Ayrton Sánchez Gómez       | Documentación y soporte |

---

## 🎯 Objetivo del proyecto
<hr style="border: 0; height: 2px; background: #4CAF50; width: 180px; margin-left: 0;">

El objetivo principal es **aplicar los conceptos de clases, herencia y polimorfismo** para crear un paquete que permita realizar análisis estadísticos simples, organizados en módulos fáciles de usar y mantener.

---

## 🧩 Estructura del proyecto
<hr style="border: 0; height: 2px; background: #4CAF50; width: 180px; margin-left: 0;">

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


