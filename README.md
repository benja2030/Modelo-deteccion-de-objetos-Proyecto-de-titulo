# Preparación de Dataset para YOLO: Detección de Bastones Blancos

Este repositorio incluye un script de automatización en Python diseñado para tomar un dataset crudo de Kaggle y formatearlo automáticamente bajo la estricta estructura de carpetas que requieren los modelos de la familia YOLO (YOLOv8, YOLOv9, YOLO26, etc.) para su entrenamiento.

## 1. Descarga dataset original

El dataset original de imágenes de bastones blancos se encuentra alojado en Kaggle.

* **Enlace del Dataset:** [Visually Impaired / White Cane Dataset](https://www.kaggle.com/datasets/jangbyeonghui/visually-impairedwhitecane)

Al descargarlo, obtendrás un archivo comprimido llamado `archive.zip`. Al descomprimirlo, verás que contiene dos carpetas en su interior: `images` y `labels`.


## 2. Preparación del Entorno

Para que el script funcione correctamente, debes organizar las carpetas extraídas. 

1. Crea una carpeta principal llamada `White_Cane_Dataset`.
2. Mueve las carpetas `images` y `labels` (extraídas del zip) dentro de esta nueva carpeta.
3. Asegúrate de que tu script de Python (ej. `split_dataset.py`) esté en el mismo directorio donde se encuentra la carpeta `White_Cane_Dataset`.

Tu estructura de archivos debería verse exactamente así antes de ejecutar el código:

```text
Tu_Proyecto
 ├── split_dataset.py      # El script de este repositorio
 └── White_Cane_Dataset    # Carpeta que acabas de crear
      ├── images           # Imágenes extraídas de Kaggle
      └── labels           # Etiquetas extraídas de Kaggle
```
## 3. Ejecución del Script

Abre el terminal, navega hasta la carpeta del proyecto y ejecuta el script:

```bash
python split_dataset.py
```

## 4. Resultado Final

Una vez que el script finalice, se habrá creado una nueva carpeta llamada White_Cane_YOLO_Ready.


# Como entrenar un modelo

```python
from ultralytics import YOLO

# Elegir un modelo base para entrenar, en este caso se esta utilizando el modelo yolo8m
model = YOLO('yolo8m.pt') 

# Apuntar al archivo autogenerado
yaml_path = 'White_Cane_YOLO_Ready/dataset.yaml'

# Iniciar entrenamiento
results = model.train(data=yaml_path, epochs=50, imgsz=640, batch=16, device=0)
```
# [Link a todos los modelos de YOLO](https://docs.ultralytics.com/models/)

# Modelos YOLO ya entrenados con dataset de Kaggle:

- YOLO8n
- YOLO9t
- YOLO10n
- YOLO11n
- YOLO26n
- YOLO26m

Recomiendo entrenar modelos S y M, ya que los N ya estan entrenados.

# Links para otros posibles dataset que se podrian utilizar para entrenar

[Crossroad Camera Dataset - Mobility Aid Users](https://repository.tugraz.at/records/2gat1-pev27)
[White-Cane Computer Vision Dataset](https://universe.roboflow.com/new-workspace-3cjjl/white-cane)


