import streamlit as st
from utils.time_helper import calculate_time_together

def render_counter(start_date_str: str, custom_title: str = "Tiempo de Nuestra Historia"):
    """
    Renderiza el contador dinámico de tiempo.
    """
    time_data = calculate_time_together(start_date_str)
    
    if time_data["has_started"]:
        html = f"""<div class="counter-box animate-fade-in">
<div class="counter-primary">{time_data["primary_text"]}</div>
<div class="counter-secondary">{time_data["secondary_text"]}</div>
<div class="counter-units">
<div class="unit-item">
<div class="unit-number">{time_data["total_days"]}</div>
<div class="unit-label">Días</div>
</div>
<div class="unit-item">
<div class="unit-number">{time_data["months"]}</div>
<div class="unit-label">Meses</div>
</div>
<div class="unit-item">
<div class="unit-number">{time_data["days"]}</div>
<div class="unit-label">Días</div>
</div>
</div>
</div>"""
    else:
        html = f"""<div class="counter-box animate-fade-in">
<div class="counter-primary">El comienzo está cerca</div>
<div class="counter-secondary">{time_data["message"]}</div>
<div class="counter-units">
<div class="unit-item">
<div class="unit-number">{time_data["days_until"]}</div>
<div class="unit-label">Días restantes</div>
</div>
<div class="unit-item">
<div class="unit-number">{time_data["months_until"]}</div>
<div class="unit-label">Meses</div>
</div>
</div>
</div>"""
    
    st.html(html)
