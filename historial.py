# Juan Agustín Centurión
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
    
def mostrar_historial(usuario):
    operaciones_usuario = [op for op in _historial if op["usuario"] == usuario]
    
    if not operaciones_usuario:
        print("\nNo hay operaciones registradas para este usuario.")
        return
    
    print("\n" + "=" * 40)
    print("          HISTORIAL DE OPERACIONES")
    print("=" * 40)
    
    for op in operaciones_usuario:
        if op["monto"] == 0:
            print(f"{op['fecha']} | {op['tipo']}")
        else:
            print(f"{op['fecha']} | {op['tipo']} | Monto: ${op['monto']:,.2f}")
    
    print("=" * 40)
