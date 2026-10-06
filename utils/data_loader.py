import json
import os
from pathlib import Path

DEFAULT_DATA = {
    "nombre_historia": "Nuestra Historia",
    "pareja": {
        "persona_1": "Ella",
        "persona_2": "Él"
    },
    "fecha_inicio": "2026-06-15",
    "frase_principal": "No se trata solamente del tiempo que llevamos juntos, sino de todos los recuerdos que vamos construyendo durante ese tiempo.",
    "musica": {
        "archivo": "assets/musica/nuestra_cancion.mp3",
        "titulo": "Nuestra Canción Especial"
    },
    "capitulo_portada": {
        "titulo": "NUESTRA HISTORIA",
        "subtitulo": "Una historia que comenzó el 15 de junio de 2026.",
        "frase_boton": "Comenzar nuestra historia ❤️",
        "foto": "assets/portada/portada.jpg"
    },
    "capitulo_inicio": {
        "titulo": "El Comienzo",
        "fecha": "15 de Junio de 2026",
        "frase": "Todas las historias importantes tienen un comienzo. Esta es la nuestra.",
        "texto": "Aquel 15 de junio de 2026 comenzó a escribirse este camino compartido. Cada mirada, cada sonrisa y cada conversación sellaron el inicio de algo auténtico, sincero y profundamente especial.",
        "cita_adicional": "Hay momentos que dividen la vida en un antes y un después.",
        "foto": "assets/inicio/primer_dia.jpg"
    },
    "capitulo_timeline": {
        "titulo": "Nuestra Línea de Tiempo",
        "subtitulo": "Los momentos clave que han marcado nuestro camino",
        "eventos": [
            {
                "fecha": "15 JUN 2026",
                "titulo": "El Comienzo",
                "descripcion": "El momento exacto donde dos caminos decidieron empezar a caminar juntos.",
                "icono": "✨",
                "foto": ""
            },
            {
                "fecha": "Julio 2026",
                "titulo": "Primer recuerdo especial",
                "descripcion": "Esa tarde en la que el tiempo pareció detenerse y supimos que esto era diferente.",
                "icono": "☕",
                "foto": ""
            },
            {
                "fecha": "HOY",
                "titulo": "Nuestro presente",
                "descripcion": "Siguiendo juntos, celebrando cada detalle y eligiéndonos cada día.",
                "icono": "❤️",
                "foto": ""
            }
        ]
    },
    "capitulo_galeria": {
        "titulo": "Momentos que Guardamos",
        "subtitulo": "Menos fotografías, más significado. Instantes que quedaron grabados en el alma.",
        "items": []
    },
    "capitulo_pequenos_momentos": {
        "titulo": "Pequeños Momentos",
        "frase_1": "No todos nuestros recuerdos fueron grandes momentos.",
        "frase_2": "Algunos fueron simplemente días normales que se volvieron especiales porque estábamos juntos.",
        "pensamientos": [
            "Un mensaje a mitad de la tarde que cambió por completo el día.",
            "Cocinar juntos y reírnos de los pequeños desastres.",
            "Caminar sin prisa y hablar de todo y de nada a la vez.",
            "Esa mirada cómplice en medio de una multitud que solo nosotros entendemos."
        ]
    },
    "capitulo_lugares": {
        "titulo": "Los Lugares que Vivimos",
        "subtitulo": "Rincones que ahora guardan un pedazo de nuestra historia",
        "destinos": []
    },
    "capitulo_construyendo": {
        "titulo": "Todo lo que Estamos Construyendo",
        "frase_central": "El tiempo no solamente pasó. Se convirtió en recuerdos.",
        "reflexion": "Cada día compartido es una pieza más en este hogar que construimos con paciencia, empatía y mucho cariño.",
        "pilares": [
            {
                "titulo": "Cariño Sincero",
                "descripcion": "Un amor que cuida los detalles y celebra la autenticidad del otro."
            },
            {
                "titulo": "Complicidad Única",
                "descripcion": "Un idioma propio de risas, gestos y miradas."
            },
            {
                "titulo": "Sueños Compartidos",
                "descripcion": "Proyectos que nacen de una conversación y crecen con ilusión."
            }
        ]
    },
    "capitulo_carta": {
        "titulo": "Para ti ❤️",
        "subtitulo": "Una carta desde el corazón",
        "cuerpo": "Gracias por cada sonrisa compartida, por la calma en los días difíciles y por hacer que lo cotidiano se vuelva extraordinario.\n\nEstar a tu lado es el recordatorio constante de que las cosas más hermosas de la vida no se fuerzan: se sienten, se cuidan y se eligen con el corazón cada mañana.\n\nGracias por ser mi lugar seguro, mi inspiración y mi felicidad más honesta.",
        "frase_futuro": "Todavía quedan fotografías que no hemos tomado, lugares que no hemos conocido y recuerdos que todavía no hemos creado.",
        "cierre": "Esta historia continúa...",
        "foto": "assets/final/final.jpg"
    }
}

def load_story_config(config_path: str = "config/historia.json") -> dict:
    """
    Carga de forma segura la configuración de la historia.
    Si el archivo no existe o contiene errores, devuelve valores por defecto seguros.
    """
    path = Path(config_path)
    if not path.exists():
        return DEFAULT_DATA
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Combinar con valores por defecto para asegurar todas las claves requeridas
            merged = DEFAULT_DATA.copy()
            merged.update(data)
            return merged
    except Exception as e:
        print(f"Error al leer {config_path}: {e}. Usando datos por defecto.")
        return DEFAULT_DATA
