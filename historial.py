# Registro basico de las operaciones realizadas por el usuario (Fecha, hora, tipo de operacion, monto, saldo final)

from datetime import datetime

_historial = []

def registrar_operacion(usuario, tipo, monto):
    
    operacion = {
        "usuario": usuario,
        "tipo": tipo,
        "monto": monto,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }
    _historial.append(operacion)
