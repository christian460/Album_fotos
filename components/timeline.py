import streamlit as st
from utils.image_helper import image_to_base64

def render_timeline(data: dict):
    """
    Renderiza la línea de tiempo vertical con eventos y recuerdos.
    """
    timeline_data = data.get("capitulo_timeline", {})
    title = timeline_data.get("titulo", "Nuestra Línea de Tiempo")
    subtitle = timeline_data.get("subtitulo", "Los momentos clave que han marcado nuestro camino")
    eventos = timeline_data.get("eventos", [])
    
    header_html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center;">02 · EL RECORRIDO</div>
<h2 class="story-title" style="margin-top: 0.5rem;">{title}</h2>
<div class="story-subtitle">{subtitle}</div>
<div class="timeline-container">
<div class="timeline-line"></div>"""
    
    nodes_html = ""
    for idx, evento in enumerate(eventos):
        fecha = evento.get("fecha", "")
        e_title = evento.get("titulo", "")
        desc = evento.get("descripcion", "")
        icono = evento.get("icono", "●")
        foto_path = evento.get("foto", "")
        
        foto_html = ""
        if foto_path:
            b64 = image_to_base64(foto_path)
            if b64:
                foto_html = f"""<div class="timeline-photo"><img src="{b64}" alt="{e_title}" /></div>"""
        
        nodes_html += f"""<div class="timeline-item">
<div class="timeline-node">{icono}</div>
<div class="timeline-content">
<div class="timeline-date">{fecha}</div>
<div class="timeline-title">{e_title}</div>
<p class="timeline-desc">{desc}</p>
{foto_html}
</div>
</div>"""
        
    footer_html = """</div></div>"""
    
    full_html = header_html + nodes_html + footer_html
    st.html(full_html)
