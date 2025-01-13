from datetime import datetime

def dias_restantes():
    today = datetime.now()
    end_year = datetime(today.year, 12, 31)
    return (end_year - today).days

def puntaje():
    hoy = datetime.now()
    resultado = 152 - (10 * hoy.month + hoy.day)
    return resultado

if __name__ == "__main__":
    print(f"Días restantes para el fin de año: {dias_restantes()}")
    print(f"Puntaje del año: {puntaje()}")