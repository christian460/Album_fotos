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
        
        # Verificar y procesar coordenadas (soporta lista [lat, lon] o dict {"lat": ..., "lon": ...})
        if coords:
            lat, lon = None, None
            if isinstance(coords, (list, tuple)) and len(coords) >= 2:
                try:
                    lat = float(coords[0])
                    lon = float(coords[1])
                except (ValueError, TypeError):
                    pass
            elif isinstance(coords, dict):
                lat = coords.get("lat") or coords.get("latitude")
                lon = coords.get("lon") or coords.get("lng") or coords.get("longitude")
                try:
                    lat = float(lat) if lat is not None else None
                    lon = float(lon) if lon is not None else None
                except (ValueError, TypeError):
                    lat, lon = None, None
            
            if lat is not None and lon is not None:
                map_points.append({"lat": lat, "lon": lon, "nombre": nombre})
            
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
    
    # Si existen coordenadas configuradas, mostrar mapa interactivo
    if map_points:
        st.html("""<div class="story-card animate-fade-in" style="margin-top: 1.5rem;">
<div class="story-badge" style="text-align: center; margin-bottom: 0.5rem;">🗺️ MAPA DE NUESTRA HISTORIA</div>
<div class="story-subtitle" style="text-align: center; margin-bottom: 1rem;">Los puntos exactos donde ocurrieron nuestros recuerdos</div>
</div>""")
        df = pd.DataFrame(map_points)
        # Si hay 1 solo punto, hacer zoom cercano (14); si hay varios, zoom automático o 12
        zoom_level = 14 if len(map_points) == 1 else 12
        st.map(df, latitude="lat", longitude="lon", zoom=zoom_level)

