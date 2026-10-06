import streamlit as st
from utils.image_helper import render_image_or_placeholder
from components.counter import render_counter

def render_hero_cover(data: dict, on_start_callback=None):
    """
    Renderiza la portada visualmente impactante.
    """
    cover_data = data.get("capitulo_portada", {})
    start_date = data.get("fecha_inicio", "2026-06-15")
    
    title = cover_data.get("titulo", "NUESTRA HISTORIA")
    subtitle = cover_data.get("subtitulo", "Una historia que comenzó el 15 de junio de 2026.")
    photo = cover_data.get("foto", "")
    button_text = cover_data.get("frase_boton", "Comenzar nuestra historia ❤️")
    
    # Imagen de portada o placeholder
    image_html = render_image_or_placeholder(
        image_path=photo,
        alt_text=title,
        placeholder_quote="Cada gran amor tiene su propio universo de recuerdos.",
        placeholder_icon="🌹",
        max_height="360px"
    )
    
    # Hero Container completo
    header_html = f"""<div class="hero-container animate-fade-in">
<div class="hero-tagline">Capítulo Inicial</div>
<h1 class="hero-main-title">{title}</h1>
<div class="hero-date-highlight">{subtitle}</div>
{image_html}
</div>"""
    st.html(header_html)
    
    # Contador de tiempo
    render_counter(start_date)
    
    # Botón centrado
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.html('<div class="hero-start-btn" style="text-align: center; margin: 1.5rem 0;"></div>')
        if st.button(button_text, key="btn_hero_start", use_container_width=True):
            if on_start_callback:
                on_start_callback()

def render_chapter_beginning(data: dict):
    """
    Renderiza el capítulo 'El Comienzo'.
    """
    chapter_data = data.get("capitulo_inicio", {})
    
    title = chapter_data.get("titulo", "El Comienzo")
    date_str = chapter_data.get("fecha", "15 de Junio de 2026")
    quote = chapter_data.get("frase", "Todas las historias importantes tienen un comienzo. Esta es la nuestra.")
    text = chapter_data.get("texto", "")
    additional_quote = chapter_data.get("cita_adicional", "")
    photo = chapter_data.get("foto", "")
    
    img_html = ""
    if photo:
        img_html = render_image_or_placeholder(
            image_path=photo,
            alt_text=title,
            placeholder_quote=additional_quote or "El día en que todo cambió para bien.",
            placeholder_icon="🕊️",
            max_height="320px"
        )
    
    extra_quote_html = ""
    if additional_quote:
        extra_quote_html = f"""<div style="text-align: center; margin-top: 2rem; font-family: var(--font-quote); font-size: 1.3rem; font-style: italic; color: var(--accent-wine);">— {additional_quote}</div>"""
    
    html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center;">01 · EL ORIGEN</div>
<h2 class="story-title" style="margin-top: 0.5rem;">{title}</h2>
<div class="story-subtitle">{date_str}</div>
<div class="quote-highlight">“{quote}”</div>
<div class="ornament-divider">
<span class="ornament-line"></span>
<span class="ornament-symbol">❦</span>
<span class="ornament-line"></span>
</div>
<p style="font-size: 1.15rem; line-height: 1.8; color: var(--text-main); text-align: justify; margin: 1.5rem 0;">{text}</p>
{img_html}
{extra_quote_html}
</div>"""
    st.html(html)
