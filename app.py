import os
from pathlib import Path
import streamlit as st

from utils.data_loader import load_story_config
from components.hero import render_hero_cover, render_chapter_beginning
from components.timeline import render_timeline
from components.gallery import render_gallery
from components.moments import render_small_moments
from components.places import render_places
from components.growth import render_growth
from components.letter import render_final_letter
from components.music_player import render_music_player

# Configuración de página
st.set_page_config(
    page_title="Nuestra Historia ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cargar estilos CSS
def load_css(css_path: str = "styles/romantic.css"):
    path = Path(css_path)
    if path.is_file():
        with open(path, "r", encoding="utf-8") as f:
            css_content = f.read()
            st.html(f"<style>{css_content}</style>")

# Inyectar estilos
load_css()

# Cargar datos de la historia
data = load_story_config()

# Definición de capítulos
CHAPTERS = [
    {"id": 0, "nombre": "Portada", "title": "Nuestra Historia"},
    {"id": 1, "nombre": "El Comienzo", "title": "01 · El Comienzo"},
    {"id": 2, "nombre": "Línea de Tiempo", "title": "02 · Los Primeros Recuerdos"},
    {"id": 3, "nombre": "Galería", "title": "03 · Momentos que Guardamos"},
    {"id": 4, "nombre": "Pequeños Momentos", "title": "04 · Lo Cotidiano"},
    {"id": 5, "nombre": "Lugares", "title": "05 · Los Lugares"},
    {"id": 6, "nombre": "Lo que Construimos", "title": "06 · Lo que Hemos Construido"},
    {"id": 7, "nombre": "Para ti", "title": "07 · Para ti & El Futuro"}
]

TOTAL_CHAPTERS = len(CHAPTERS) - 1 # 7 capítulos narrativos después de la portada

# Inicializar estado de navegación
if "current_chapter" not in st.session_state:
    st.session_state.current_chapter = 0

def go_to_chapter(index: int):
    st.session_state.current_chapter = max(0, min(index, len(CHAPTERS) - 1))
    st.rerun()

def next_chapter():
    go_to_chapter(st.session_state.current_chapter + 1)

def prev_chapter():
    go_to_chapter(st.session_state.current_chapter - 1)

def restart_story():
    go_to_chapter(0)

current_idx = st.session_state.current_chapter

# Reproductor de música (si existe el archivo)
render_music_player(data)

# Barra de navegación superior (visible en capítulos > 0)
if current_idx > 0:
    progress_percentage = int((current_idx / TOTAL_CHAPTERS) * 100)
    formatted_num = f"{current_idx:02d} / {TOTAL_CHAPTERS:02d}"
    
    st.html(f"""<div class="story-header-nav">
<div class="story-badge">NUESTRA HISTORIA</div>
<div class="chapter-indicator">{formatted_num}</div>
</div>
<div class="progress-track" style="margin-top: -1.2rem; margin-bottom: 2rem;">
<div class="progress-fill" style="width: {progress_percentage}%;"></div>
</div>""")

# Renderizar capítulo actual
if current_idx == 0:
    render_hero_cover(data, on_start_callback=next_chapter)

elif current_idx == 1:
    render_chapter_beginning(data)

elif current_idx == 2:
    render_timeline(data)

elif current_idx == 3:
    render_gallery(data)

elif current_idx == 4:
    render_small_moments(data)

elif current_idx == 5:
    render_places(data)

elif current_idx == 6:
    render_growth(data)

elif current_idx == 7:
    render_final_letter(data)

# Botones de navegación inferior (visibles a partir del capítulo 1)
if current_idx > 0:
    st.html("<div style='margin-top: 2rem;'></div>")
    col_prev, col_next = st.columns([1, 1])
    
    with col_prev:
        st.html('<div class="btn-secondary"></div>')
        if st.button("← Anterior", key="btn_nav_prev", use_container_width=True):
            prev_chapter()
        
    with col_next:
        if current_idx < len(CHAPTERS) - 1:
            if st.button("Continuar →", key="btn_nav_next", use_container_width=True):
                next_chapter()
        else:
            if st.button("Releer nuestra historia ↺", key="btn_nav_restart", use_container_width=True):
                restart_story()

