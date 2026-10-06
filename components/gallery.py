import streamlit as st
from utils.image_helper import image_to_base64

def render_gallery(data: dict):
    """
    Renderiza la galería tipo Polaroid/Álbum romántico.
    Diseñada especialmente para pocas fotografías de alto valor sentimental.
    """
    gallery_data = data.get("capitulo_galeria", {})
    title = gallery_data.get("titulo", "Momentos que Guardamos")
    subtitle = gallery_data.get("subtitulo", "Menos fotografías, más significado. Instantes que quedaron grabados en el alma.")
    items = gallery_data.get("items", [])
    
    header_html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center;">03 · RECUERDOS</div>
<h2 class="story-title" style="margin-top: 0.5rem;">{title}</h2>
<div class="story-subtitle">{subtitle}</div>
<div class="polaroid-grid">"""
    
    cards_html = ""
    for idx, item in enumerate(items):
        item_title = item.get("titulo", "")
        item_date = item.get("fecha", "")
        item_desc = item.get("descripcion", "")
        foto_path = item.get("foto", "")
        
        rotate_class = "polaroid-rotate-left" if idx % 2 == 0 else "polaroid-rotate-right"
        b64 = image_to_base64(foto_path) if foto_path else None
        
        if b64:
            media_content = f"""<div class="polaroid-img-wrapper"><img src="{b64}" alt="{item_title}" /></div>"""
        else:
            media_content = """<div class="polaroid-img-wrapper" style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding: 2rem; text-align: center; background: linear-gradient(135deg, #F9F1EB 0%, #EFE3DA 100%);">
<span style="font-size: 2.4rem; color: var(--accent-wine); margin-bottom: 0.8rem;">📷</span>
<span style="font-family: var(--font-quote); font-size: 1.25rem; font-style: italic; color: var(--text-muted); line-height: 1.4;">“Un instante guardado en la memoria más que en el papel.”</span>
</div>"""
            
        cards_html += f"""<div class="polaroid-card {rotate_class}">
{media_content}
<div class="polaroid-caption">
<div class="polaroid-date">{item_date}</div>
<div class="polaroid-title">{item_title}</div>
<p class="polaroid-desc">“{item_desc}”</p>
</div>
</div>"""
        
    footer_html = """</div></div>"""
    
    full_html = header_html + cards_html + footer_html
    st.html(full_html)
