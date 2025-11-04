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

>  **Este proyecto fue desarrollado como parte del curso _Lenguaje de Programación II_.**
>  
> Permite calcular estadísticas básicas para datos **cuantitativos y cualitativos** aplicando los principios de **Programación Orientada a Objetos (POO)**.  
> Tiene una finalidad académica, por lo tanto, puede ser usado y modificado con propósitos educativos.

---
##  Integrantes del grupo
<hr style="border: 0; height: 2px; background: #4CAF50; width: 180px; margin-left: 0;">

|      Nombres y Apellidos       | Nombre de usuario   |
|--------------------------------|---------------------|
| Jose Luis Garay Ramos          |   joseluis02678     |
| Omar Sebastián Castillo Torres |   Sebas20050700     |
| Ayrton Sánchez Gómez           |   ayrtonsg752294    |

---

##  Objetivo del proyecto
<hr style="border: 0; height: 2px; background: #4CAF50; width: 180px; margin-left: 0;">

El objetivo principal es **aplicar los conceptos de clases, herencia y polimorfismo** para crear un paquete que permita realizar análisis estadísticos simples, organizados en módulos fáciles de usar y mantener.

---

## Estructura del proyecto

<p align="center">
  <img src="https://raw.githubusercontent.com/joseluis02678/Parcial---LP2/main/images/Arquitectura%20del%20proyecto.jpg" alt="Arquitectura del proyecto" width="600">
</p>

<hr style="border: 0; height: 2px; background: #4CAF50; width: 180px; margin-left: 0;">

```text
estadística_lib/
│
├── estadistica/
│   ├── .ipynb_checkpoints/
│   ├── __init__.py
│   ├── base.py
│   ├── cualitativos.py
│   ├── cuantitativos.py
│   ├── inferencia.py
│   │
│   ├── otros/
│   │   ├── docs_matriz.md
│   │   ├── op_matriz.py
│   │
│   └── tests/
│       ├── test_cualitativos.md
│       ├── test_cuantitativos.md
│       ├── test_inferencia.md
│       ├── test_matrices.md
│
├── images/
│   ├── Salida 1 - Base_files.jpg
│   ├── Salida 2 - Base_files.jpg
│   ├── Salida 1 - inferencia.jpg
│   ├── Salida 2 - inferencia.jpg
│   ├── Salida 3 - inferencia.jpg
│   ├── Salida 4 - inferencia.jpg
│   ├── Salida 5 - inferencia.jpg
│   ├── Salida 6 - inferencia.jpg
│   ├── Salida 7 - Inferencia.jpg
│   ├── barras_pie_contract.png
│   ├── barras_pie_paymentmethod.png
│   ├── cualitativos_test.png
│   ├── deter1.png
│   ├── deter2.png
│   ├── deter3.png
│   ├── logo.jpg
│   ├── multi_escalar_matriz.png
│   ├── multi_matriz.png
│   ├── resta_matriz.png
│   ├── suma_matriz.png
│   ├── test_cuanti1.jpg
│   ├── test_cuanti2.jpg
│   └── test_cuanti3.jpg
│
├── requirements.txt
├── README.md
└── .gitignore

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

Pruebas
Las pruebas se encuentran en la carpeta tests y se pueden ejecutar con el siguiente comando:
pytest estadística_lib/estadistica/tests/


