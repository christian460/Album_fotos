import base64
import os
from pathlib import Path
from typing import Optional

def image_to_base64(image_path: str) -> Optional[str]:
    """
    Convierte una imagen local a cadena base64 para embebido HTML seguro en Streamlit.
    Retorna None si la imagen no existe o no se puede leer.
    """
    if not image_path:
        return None
    
    path = Path(image_path)
    if not path.is_file():
        return None
    
    suffix = path.suffix.lower().replace(".", "")
    if suffix in ["jpg", "jpeg"]:
        mime = "image/jpeg"
    elif suffix == "png":
        mime = "image/png"
    elif suffix == "webp":
        mime = "image/webp"
    elif suffix == "gif":
        mime = "image/gif"
    else:
        mime = "image/jpeg"
        
    try:
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:{mime};base64,{encoded}"
    except Exception:
        return None

def render_image_or_placeholder(
    image_path: Optional[str],
    alt_text: str = "",
    placeholder_quote: str = "Un recuerdo que vive en nuestra memoria.",
    placeholder_icon: str = "✨",
    custom_class: str = "",
    max_height: str = "350px"
) -> str:
    """
    Genera el HTML para mostrar la imagen si existe, o un elegante contenedor
    con tipografía y degradado si no hay imagen disponible.
    """
    b64 = image_to_base64(image_path) if image_path else None
    
    if b64:
        return f"""
        <div class="hero-image-frame {custom_class}">
            <img src="{b64}" alt="{alt_text}" style="max-height: {max_height};" />
        </div>
        """
    else:
        return f"""
        <div class="elegant-placeholder-frame {custom_class}">
            <div class="elegant-placeholder-icon">{placeholder_icon}</div>
            <div class="elegant-placeholder-text">“{placeholder_quote}”</div>
        </div>
        """
