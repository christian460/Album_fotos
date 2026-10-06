import streamlit as st
from utils.image_helper import render_image_or_placeholder

def render_final_letter(data: dict):
    """
    Renderiza la carta final 'Para ti ❤️' y la visión hacia el futuro.
    """
    letter_data = data.get("capitulo_carta", {})
    title = letter_data.get("titulo", "Para ti ❤️")
    subtitle = letter_data.get("subtitulo", "Una carta desde el corazón")
    cuerpo = letter_data.get("cuerpo", "")
    frase_futuro = letter_data.get("frase_futuro", "Todavía quedan fotografías que no hemos tomado, lugares que no hemos conocido y recuerdos que todavía no hemos creado.")
    cierre = letter_data.get("cierre", "Esta historia continúa...")
    foto = letter_data.get("foto", "")
    
    # Foto destacada si existe
    if foto:
        foto_html = render_image_or_placeholder(
            image_path=foto,
            alt_text="Nuestro Futuro",
            placeholder_quote="Por todos los momentos que aún esperan por nosotros.",
            placeholder_icon="🕊️",
            max_height="320px"
        )
        st.html(foto_html)
        
    html = f"""<div class="letter-container animate-fade-in">
<h2 class="letter-title">{title}</h2>
<div class="letter-subtitle">{subtitle}</div>
<div class="ornament-divider" style="margin-bottom: 2rem;">
<span class="ornament-line"></span>
<span class="ornament-symbol">💌</span>
<span class="ornament-line"></span>
</div>
<div class="letter-body">{cuerpo}</div>
<div class="letter-future-quote">“{frase_futuro}”</div>
<div class="letter-continuation">{cierre}</div>
</div>"""
    st.html(html)
