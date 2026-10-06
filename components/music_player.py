import streamlit as st
import os
from pathlib import Path

def render_music_player(data: dict):
    """
    Renderiza un reproductor de música discreto si existe el archivo de audio.
    """
    music_config = data.get("musica", {})
    audio_path = music_config.get("archivo", "assets/musica/nuestra_cancion.mp3")
    title = music_config.get("titulo", "Nuestra Canción Especial")
    
    path = Path(audio_path)
    
    if path.is_file():
        try:
            with open(path, "rb") as f:
                audio_bytes = f.read()
                
            st.html(f"""<div class="music-bar-container">
<div class="music-info">
<span class="music-icon">🎵</span>
<span>{title}</span>
</div>
</div>""")
            st.audio(audio_bytes, format="audio/mp3", loop=True)
        except Exception:
            pass
