import streamlit as st
from components.counter import render_counter

def render_growth(data: dict):
    """
    Renderiza la sección 'Todo lo que Estamos Construyendo'.
    Enfatiza el paso del tiempo y el significado de los recuerdos.
    """
    growth_data = data.get("capitulo_construyendo", {})
    start_date = data.get("fecha_inicio", "2026-06-15")
    title = growth_data.get("titulo", "Todo lo que Estamos Construyendo")
    frase_central = growth_data.get("frase_central", "El tiempo no solamente pasó. Se convirtió en recuerdos.")
    reflexion = growth_data.get("reflexion", "")
    pilares = growth_data.get("pilares", [])
    
    header_html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center;">06 · TIEMPO & RECUERDOS</div>
<h2 class="story-title" style="margin-top: 0.5rem;">{title}</h2>
<div class="quote-highlight" style="margin-top: 1.5rem; margin-bottom: 2rem;">“{frase_central}”</div>
<p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-muted); text-align: center; max-width: 660px; margin: 0 auto 2.5rem auto;">{reflexion}</p>
</div>"""
    st.html(header_html)
    
    # Integrar el contador dentro de la sección
    render_counter(start_date)
    
    # Pilares construidos
    pillars_html = """<div class="story-card animate-fade-in" style="margin-top: 1.5rem;">
<div class="story-subtitle" style="font-size: 1.15rem; margin-bottom: 1.2rem;">Lo que nos une cada día</div>"""
    
    for pilar in pilares:
        p_title = pilar.get("titulo", "")
        p_desc = pilar.get("descripcion", "")
        pillars_html += f"""<div class="pillar-card">
<div class="pillar-title">✦ {p_title}</div>
<p class="pillar-desc">{p_desc}</p>
</div>"""
        
    pillars_html += """</div>"""
    st.html(pillars_html)
