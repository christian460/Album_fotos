# ❤️ Nuestra Historia

Una experiencia interactiva y romántica de **storytelling** desarrollada con **Streamlit (Python)**, diseñada para revivir momentos especiales, celebrar el paso del tiempo y mirar con ilusión hacia el futuro.

---

## 🌹 Características Principales

* **Storytelling por Capítulos:** Navegación inmersiva con indicador `01 / 07` y barra de progreso.
* **Contador Dinámico:** Calcula automáticamente los días y meses juntos desde el **15 de junio de 2026** (o cualquier fecha que elijas).
* **Diseño para Pocas Fotografías:** Concepto *"menos fotografías, más significado"*. Si tienes entre 3 y 8 fotografías (o incluso si faltan algunas), la interfaz se presenta completa y artística con tipografía sofisticada, citas y degradados.
* **Línea de Tiempo Vertical:** Hitos y recuerdos con nodos luminosos y detalles narrativos.
* **Galería Polaroid:** Presentación asimétrica tipo álbum de fotos.
* **Música Opcional:** Soporte para reproducir tu canción favorita de fondo.
* **Carta Final:** Sección emotiva "Para ti ❤️" orientada al futuro.
* **100% Personalizable:** Todo el contenido se edita cómodamente desde un único archivo `config/historia.json`.

---

## 📁 Estructura del Proyecto

```text
Nuestra-Historia/
│
├── app.py                     # Punto de entrada de la aplicación
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Manual de uso y personalización
│
├── config/
│   └── historia.json          # Textos, fechas, capítulos y configuración
│
├── assets/                    # Carpeta para tus fotos y música
│   ├── portada/               # Imagen de portada principal (ej. portada.jpg)
│   ├── inicio/                # Foto del primer día (ej. primer_dia.jpg)
│   ├── momentos/              # Fotos de momentos especiales (recuerdo_1.jpg, momento_1.jpg...)
│   ├── viajes/                # Fotos de lugares y salidas (lugar_1.jpg, lugar_2.jpg...)
│   ├── final/                 # Foto para la carta final (final.jpg)
│   └── musica/                # Tu canción favorita (nuestra_cancion.mp3)
│
├── components/                # Componentes modulares de interfaz
│   ├── hero.py                # Portada y capítulo inicial
│   ├── counter.py             # Contador de tiempo transcurrido
│   ├── timeline.py            # Línea de tiempo vertical
│   ├── gallery.py             # Galería polaroid/álbum
│   ├── moments.py             # Sección de pequeños momentos cotidianos
│   ├── places.py              # Sección de lugares visitados y soporte de mapa
│   ├── growth.py              # Sección de crecimiento y pilares de la relación
│   ├── letter.py              # Carta final y visión hacia el futuro
│   └── music_player.py        # Reproductor de audio discreto
│
├── styles/
│   └── romantic.css           # Hoja de estilos con paleta romántica, tipografías y animaciones
│
└── utils/                     # Utilidades de carga de datos, cálculo de fechas e imágenes
    ├── data_loader.py
    ├── image_helper.py
    └── time_helper.py
```

---

## 🚀 1. Instalación y Ejecución

### Requisitos previos
* Python 3.9 o superior instalado.

### Paso 1: Instalar dependencias
Abre una terminal o PowerShell en la carpeta del proyecto y ejecuta:
```bash
pip install -r requirements.txt
```

### Paso 2: Ejecutar la aplicación
```bash
streamlit run app.py
```
La aplicación se abrirá automáticamente en tu navegador web en `http://localhost:8501`.

---

## 📸 2. Dónde colocar tus Fotografías

Coloca tus fotos dentro de las carpetas de `assets/`:

1. **Foto de Portada:** Guárdala en `assets/portada/portada.jpg`.
2. **Foto de El Comienzo:** Guárdala en `assets/inicio/primer_dia.jpg`.
3. **Fotos de Recuerdos:** Guárdalas en `assets/momentos/` (ejemplo: `momento_1.jpg`, `momento_2.jpg`, etc.).
4. **Fotos de Lugares:** Guárdalas en `assets/viajes/` (ejemplo: `lugar_1.jpg`, `lugar_2.jpg`...).
5. **Foto de la Carta Final:** Guárdala en `assets/final/final.jpg`.

> **Nota:** Puedes usar formatos `.jpg`, `.jpeg`, `.png` o `.webp`. Si no tienes una foto para alguna sección, la aplicación se adaptará de forma elegante sin mostrar errores ni espacios vacíos.

---

## 📅 3. Cómo modificar la Fecha de Inicio

Abre el archivo `config/historia.json` y edita el campo `"fecha_inicio"` con el formato `YYYY-MM-DD`:

```json
{
  "fecha_inicio": "2026-06-15"
}
```

El contador calculará automáticamente los días y meses juntos en tiempo real.

---

## ✍️ 4. Cómo personalizar Textos, Nombres y Frases

Todo el texto de la historia se edita dentro de `config/historia.json`:

* **Nombres:** Modifica `"pareja"` con vuestros nombres.
* **Citas y Frases:** Modifica `"frase_principal"` o las frases de cada capítulo.
* **Carta Final:** Modifica el texto en `"capitulo_carta"` dentro de `"cuerpo"`, `"frase_futuro"` y `"cierre"`.

---

## 🗺️ 5. Agregar nuevos Eventos o Lugares

Dentro de `config/historia.json`:

### Para la Línea de Tiempo:
Agrega un nuevo elemento a la lista `"eventos"`:
```json
{
  "fecha": "Septiembre 2026",
  "titulo": "Nuestro viaje sorpresa",
  "descripcion": "Una escapada de fin de semana que nunca olvidaremos.",
  "icono": "✈️",
  "foto": "assets/viajes/viaje_sorpresa.jpg"
}
```

### Para Lugares y Mapa:
Agrega un nuevo destino en `"destinos"`:
```json
{
  "nombre": "Playa Escondida",
  "fecha": "Octubre 2026",
  "historia": "Ver el atardecer frente al mar.",
  "foto": "assets/viajes/playa.jpg",
  "coordenadas": {
    "lat": -12.0464,
    "lon": -77.0428
  }
}
```
*(Si incluyes coordenadas `lat` y `lon`, se generará automáticamente un mapa interactivo de vuestros viajes).*

---

## 🎶 6. Cómo agregar Música

1. Selecciona tu archivo de música favorito en formato MP3.
2. Cópialo en `assets/musica/nuestra_cancion.mp3`.
3. Al iniciar la aplicación, aparecerá el reproductor en la parte superior para escuchar la canción mientras recorren la historia.

---

## 💖 Diseñado con Amor y Elegancia
Creado para celebrar lo que verdaderamente importa: los momentos compartidos y el camino que sigue construyéndose día a día.
