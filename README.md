
# Description
The goal of this project is to reproduce the results presented in _[Hussein, R., et al. (2018)](https://doi.org/10.1016/j.clinph.2018.10.010)_.
* `reading.py` contains functions to load the Ubonn Dataset which must be downloaded prior to running the project.
* `preprocessing.py` includes some functions to perform data augmentation. This is done in `extending.py`.


This project was done as part of what would be my thesis project, rest of the intructions is in spanish below because of that.

----

# Descripción
El propósito del proyecto es replicar los resultados presentados en _[Hussein, R., et al. (2018)](https://doi.org/10.1016/j.clinph.2018.10.010)_.

El script `reading.py` contiene funciones para cargar el [dataset](http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3) de EEG de la universidad de Ubonn en una estructura de datos conveniente para su análisis visual así como en un formato conveniente para entrenar una red LSTM.

El script `preprocessing.py` contiene funciones para añadir artefactos artificiales, un ejemplo de su uso se encuentra en `extending.py`. 

Ejecutar el anterior (`python extending.py`) añade los tres tipos de artefactos descritos por _Hussein, R., et al. (2018)_ a _todo_ el dataset, efectivamente extendiendolo de 500 a 2000 muestras. Solo debe ejecutarse **una** vez. Las funciones de `reading.py` son compatibles con el dataset extendido.

# Ejecutando el proyecto
- Como prerequisito se requiere una instalación de Python 3.6+

## Instalar dependencias
1. Ejecutar
```
pip install -r requirements.txt
```
- Es conveniente utilizar un entorno virtual (eg. `venv`).
## Dataset
1. Crear un directorio `data` en la raíz del proyecto. 
2. Descargar los cinco archivos comprimidos que componen el [dataset de Ubonn](http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3).
3. Descomprimir los archivos en una carpeta por comprimido, manteniendo el nombre de cada uno (Z, O, etc).

El resultado debe ser una estructura de carpetas tal como:
```
preprocessing.py
reading.py
...
data
├ F
  ├ F001.txt
  | ...
  | ...
  └ F100.txt
├ N
├ O
├ S
└ Z
```

# Referencias & Credito
- Hussein, R., et al. (2018) _Optimized deep neural network architecture for robust detection of epileptic seizures using EEG signals_  https://doi.org/10.1016/j.clinph.2018.10.010
- [Andrzejak RG, Lehnertz K, Rieke C, Mormann F, David P, Elger CE (2001) Indications of nonlinear deterministic and finite dimensional structures in time series of brain electrical activity: Dependence on recording region and brain state, Phys. Rev. E, 64, 061907](http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3)
- Some code taken from: https://github.com/ramyh/Epileptic-Seizure-Detection
