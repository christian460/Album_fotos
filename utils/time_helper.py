from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from typing import Dict, Any

def parse_start_date(date_str: str) -> date:
    """
    Parsea de forma segura la fecha de inicio en formato YYYY-MM-DD.
    Si falla, usa 2026-06-15 por defecto.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except Exception:
        return date(2026, 6, 15)

def calculate_time_together(start_date_str: str) -> Dict[str, Any]:
    """
    Calcula el tiempo transcurrido desde la fecha de inicio.
    Maneja el caso donde la fecha es futura.
    """
    start_date = parse_start_date(start_date_str)
    today = date.today()
    
    # Caso fecha futura (aún no llega el 15 de junio de 2026)
    if today < start_date:
        days_until = (start_date - today).days
        rd = relativedelta(start_date, today)
        return {
            "has_started": False,
            "days_until": days_until,
            "months_until": rd.months,
            "days_left": rd.days,
            "message": f"Faltan {days_until} días para comenzar esta gran historia",
            "start_formatted": start_date.strftime("%d de junio de %Y")
        }
    
    # Caso historia en curso
    total_days = (today - start_date).days
    rd = relativedelta(today, start_date)
    
    years = rd.years
    months = rd.months
    days = rd.days
    
    # Formateo secundario
    if years > 0:
        secondary_text = f"{years} {'año' if years == 1 else 'años'} · {months} {'mes' if months == 1 else 'meses'} · {days} {'día' if days == 1 else 'días'}"
    else:
        secondary_text = f"{months} {'mes' if months == 1 else 'meses'} · {days} {'día' if days == 1 else 'días'}"
    
    return {
        "has_started": True,
        "total_days": total_days,
        "years": years,
        "months": months,
        "days": days,
        "primary_text": f"{total_days} días juntos",
        "secondary_text": secondary_text,
        "start_formatted": start_date.strftime("%d de junio de %Y")
    }
