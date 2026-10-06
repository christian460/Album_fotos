import json
import streamlit as st
import streamlit.components.v1 as components
from utils.image_helper import image_to_base64

def generate_leaflet_map_html(points: list) -> str:
    """
    Genera un mapa interactivo Leaflet con diseño romántico (Voyager CartoDB tiles)
    y marcadores personalizados para cada lugar con recuerdos.
    """
    points_json = json.dumps(points)
    
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background: transparent;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      padding: 4px;
    }}
    #map {{
      width: 100%;
      height: 390px;
      border-radius: 16px;
      box-shadow: 0 8px 24px rgba(74, 45, 52, 0.12);
      border: 1.5px solid rgba(132, 42, 59, 0.2);
    }}
    .custom-heart-pin {{
      background: #842A3B;
      color: #FFFFFF;
      border: 2px solid #FFFFFF;
      border-radius: 50%;
      width: 34px;
      height: 34px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      box-shadow: 0 4px 12px rgba(132, 42, 59, 0.45);
      cursor: pointer;
      transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .custom-heart-pin:hover {{
      transform: scale(1.25);
    }}
    .leaflet-popup-content-wrapper {{
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(44, 36, 38, 0.18);
      border: 1px solid rgba(132, 42, 59, 0.15);
      padding: 6px;
    }}
    .popup-title {{
      font-weight: 700;
      color: #842A3B;
      font-size: 14px;
      margin-bottom: 3px;
    }}
    .popup-date {{
      font-size: 12px;
      color: #6B5E60;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
  </style>
</head>
<body>
  <div id="map"></div>
  <script>
    const points = {points_json};
    if (points && points.length > 0) {{
      const map = L.map('map', {{
        scrollWheelZoom: true,
        zoomControl: true
      }});
      
      // Capa base estética y limpia (Voyager de CartoDB)
      L.tileLayer('https://{{s}}.basemaps.cartocdn.com/rastertiles/voyager/{{z}}/{{x}}/{{y}}{{r}}.png', {{
        attribution: '&copy; OpenStreetMap &copy; CARTO',
        maxZoom: 19
      }}).addTo(map);
      
      const bounds = [];
      
      points.forEach(pt => {{
        const pinIcon = L.divIcon({{
          className: '',
          html: '<div class="custom-heart-pin">❤️</div>',
          iconSize: [34, 34],
          iconAnchor: [17, 17],
          popupAnchor: [0, -18]
        }});
        
        const marker = L.marker([pt.lat, pt.lon], {{ icon: pinIcon }}).addTo(map);
        marker.bindPopup(`
          <div class="popup-title">${{pt.nombre}}</div>
          <div class="popup-date">📍 ${{pt.fecha}}</div>
        `);
        
        bounds.push([pt.lat, pt.lon]);
      }});
      
      if (bounds.length === 1) {{
        map.setView(bounds[0], 15);
      }} else {{
        map.fitBounds(bounds, {{ padding: [45, 45], maxZoom: 16 }});
      }}
    }}
  </script>
</body>
</html>"""

def render_places(data: dict):
    """
    Renderiza la sección 'Los Lugares que Vivimos'.
    Presenta las tarjetas de destinos y el mapa interactivo funcional al final.
    """
    places_data = data.get("capitulo_lugares", {})
    title = places_data.get("titulo", "Los Lugares que Vivimos")
    subtitle = places_data.get("subtitulo", "No necesitamos ir muy lejos para crear recuerdos")
    destinos = places_data.get("destinos", [])
    
    # 1. Cabecera del Capítulo
    header_html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center;">05 · GEOGRAFÍA DE RECUERDOS</div>
<h2 class="story-title" style="margin-top: 0.5rem;">{title}</h2>
<div class="story-subtitle">{subtitle}</div>
</div>"""
    st.html(header_html)
    
    map_points = []
    cards_html = ""
    
    # 2. Procesar destinos y extraer puntos con coordenadas
    for destino in destinos:
        nombre = destino.get("nombre", "")
        fecha = destino.get("fecha", "")
        historia = destino.get("historia", "")
        foto_path = destino.get("foto", "")
        coords = destino.get("coordenadas", None)
        
        lat, lon = None, None
        if coords:
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
                map_points.append({
                    "lat": lat,
                    "lon": lon,
                    "nombre": nombre,
                    "fecha": fecha
                })
        
        foto_html = ""
        if foto_path:
            b64 = image_to_base64(foto_path)
            if b64:
                foto_html = f"""<div class="place-photo"><img src="{b64}" alt="{nombre}" /></div>"""
        
        maps_link_html = ""
        if lat is not None and lon is not None:
            maps_link_html = f"""<div style="margin-top: 0.8rem;">
<a href="https://www.google.com/maps?q={lat},{lon}" target="_blank" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.85rem; color: var(--accent-wine); text-decoration: none; font-weight: 600; padding: 5px 12px; background: rgba(132, 42, 59, 0.08); border-radius: 99px; transition: background 0.2s ease;">
📍 Ver en Google Maps ↗
</a>
</div>"""
                
        cards_html += f"""<div class="place-card">
<div class="place-badge">📍 {fecha}</div>
<div class="place-name">{nombre}</div>
<div class="place-story">{historia}</div>
{maps_link_html}
{foto_html}
</div>"""

    # 3. Mostrar las tarjetas de cada lugar
    full_cards_html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center; margin-bottom: 1.5rem;">HISTORIAS Y RINCONES</div>
{cards_html}
</div>"""
    st.html(full_cards_html)

    # 4. Mapa Interactivo al final del capítulo (garantizado con Leaflet)
    if map_points:
        st.html("""<div class="story-card animate-fade-in" style="margin-top: 2rem; margin-bottom: 0.5rem;">
<div class="story-badge" style="text-align: center; margin-bottom: 0.4rem;">🗺️ MAPA INTERACTIVO DE NUESTRA HISTORIA</div>
<div class="story-subtitle" style="text-align: center; margin-bottom: 1rem; font-size: 1.05rem;">
Haz clic en los corazones ❤️ para ver el nombre de cada recuerdo
</div>
</div>""")
        map_html = generate_leaflet_map_html(map_points)
        components.html(map_html, height=410)
