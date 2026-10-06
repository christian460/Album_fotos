import streamlit as st
import pandas as pd
from utils.image_helper import image_to_base64

def render_places(data: dict):
    """
    Renderiza la sección 'Los Lugares que Vivimos'.
    Presenta tarjetas de destinos y está preparada para coordenadas y mapas.
    """
    places_data = data.get("capitulo_lugares", {})
    title = places_data.get("titulo", "Los Lugares que Vivimos")
    subtitle = places_data.get("subtitulo", "Rincones que ahora guardan un pedazo de nuestra historia")
    destinos = places_data.get("destinos", [])
    
    header_html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center;">05 · GEOGRAFÍA DE RECUERDOS</div>
<h2 class="story-title" style="margin-top: 0.5rem;">{title}</h2>
<div class="story-subtitle">{subtitle}</div>
<div style="margin-top: 2rem;">"""
    
    cards_html = ""
    map_points = []
    
    for destino in destinos:
        nombre = destino.get("nombre", "")
        fecha = destino.get("fecha", "")
        historia = destino.get("historia", "")
        foto_path = destino.get("foto", "")
        coords = destino.get("coordenadas", None)
        
        # Verificar si hay coordenadas para futuro mapa interactivo
        if coords and isinstance(coords, dict) and "lat" in coords and "lon" in coords:
            map_points.append({"lat": coords["lat"], "lon": coords["lon"]})
            
        foto_html = ""
        if foto_path:
            b64 = image_to_base64(foto_path)
            if b64:
                foto_html = f"""<div class="place-photo"><img src="{b64}" alt="{nombre}" /></div>"""
                
        cards_html += f"""<div class="place-card">
<div class="place-badge">📍 {fecha}</div>
<div class="place-name">{nombre}</div>
<div class="place-story">{historia}</div>
{foto_html}
</div>"""
        
    footer_html = """</div></div>"""
    
    full_html = header_html + cards_html + footer_html
    st.html(full_html)
    
    # Si existen coordenadas reales configuradas por el usuario, mostrar mapa interactivo
    if map_points:
        st.html("""<div class="story-card animate-fade-in" style="margin-top: 1rem;">
<div class="story-badge" style="text-align: center; margin-bottom: 1rem;">MAPA DE NUESTRA HISTORIA</div>
</div>""")
        df = pd.DataFrame(map_points)
        st.map(df, zoom=4)
