import streamlit as st

def render_small_moments(data: dict):
    """
    Renderiza la sección 'Pequeños Momentos'.
    Enfocada en el diseño tipográfico, la poesía y los detalles cotidianos.
    """
    moments_data = data.get("capitulo_pequenos_momentos", {})
    title = moments_data.get("titulo", "Pequeños Momentos")
    frase_1 = moments_data.get("frase_1", "No todos nuestros recuerdos fueron grandes momentos.")
    frase_2 = moments_data.get("frase_2", "Algunos fueron simplemente días normales que se volvieron especiales porque estábamos juntos.")
    pensamientos = moments_data.get("pensamientos", [])
    
    header_html = f"""<div class="story-card animate-fade-in">
<div class="story-badge" style="text-align: center;">04 · LO COTIDIANO</div>
<h2 class="story-title" style="margin-top: 0.5rem;">{title}</h2>
<div class="quote-highlight" style="margin-top: 1.5rem; margin-bottom: 1.5rem;">“{frase_1}”</div>
<p style="font-family: var(--font-quote); font-size: 1.35rem; font-style: italic; text-align: center; color: var(--text-muted); max-width: 620px; margin: 0 auto 2.5rem auto; line-height: 1.6;">{frase_2}</p>
<div class="ornament-divider">
<span class="ornament-line"></span>
<span class="ornament-symbol">✧</span>
<span class="ornament-line"></span>
</div>
<div style="margin-top: 2rem;">"""
    
    items_html = ""
    icons = ["💬", "🍽️", "😂", "🌷", "❤️"]
    for idx, pensamiento in enumerate(pensamientos):
        icon = icons[idx % len(icons)]
        items_html += f"""<div class="thought-card">
<div class="thought-icon">{icon}</div>
<div class="thought-text">{pensamiento}</div>
</div>"""
        
    footer_html = """</div></div>"""
    
    full_html = header_html + items_html + footer_html
    st.html(full_html)
