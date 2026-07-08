# Retirar dinero del saldo del usuario 
# Control de saldo negativo
# Limite de retiro diario
# Ingreso de dinero al saldo del usuario
# Enviar dinero a otro usuario
# Control de saldo para  transferencias (minimo y maximo de dinero permitido)

from datos import cuentas_prueba, LIM_EXTRACCION
from historial import registrar_operacion

def consultar_saldo(usuario):
    saldo = cuentas_prueba[usuario]["saldo"]
    print(f"\nSaldo disponible: ${saldo:,.2f}")
    registrar_operacion(usuario, "Consulta de saldo", 0)
    return saldo

def extraer_dinero(usuario):
    saldo = cuentas_prueba[usuario]["saldo"]
    print(f"\nSaldo disponible: ${saldo:,.2f}")
    print(f"Límite de extracción diaria: ${LIM_EXTRACCION:,.2f}")
    
    try:
        monto = float(input("\nIngrese el monto a extraer: $"))
    except ValueError:
        print("\n✗ Monto inválido. Debe ingresar un número.")
        return
    
    if monto <= 0: # Si el monto es menor o igual a cero
        print("\n✗ Monto inválido. Debe ser mayor a cero.")
        return
    
    if monto > LIM_EXTRACCION: # Si el monto supera el límite de extracción
        print(f"\n✗ El monto supera el límite de extracción diaria de ${LIM_EXTRACCION:,.2f}.")
        return
    
    if monto > saldo: # Si el monto supera el saldo disponible
        print(f"\n✗ Saldo insuficiente para realizar la extracción. Su saldo es ${saldo:,.2f}")
        return

    cuentas_prueba[usuario]["saldo"] -= monto
    print(f"\n✓ Extracción exitosa.") 
    print(f"\nNuevo saldo: ${cuentas_prueba[usuario]['saldo']:,.2f}")
    registrar_operacion(usuario, "Extracción de dinero", monto)
    
def depositar_dinero(usuario):
    try:
        monto = float(input("\nIngrese el monto a depositar: $"))
    except ValueError:
        print("\n✗ Monto inválido. Debe ingresar un número.")
        return
    
    if monto <= 0: # Si el monto es menor o igual a cero
        print("\n✗ El monto debe ser mayor a cero.")
        return
    
    cuentas_prueba[usuario]["saldo"] += monto
    print(f"\n✓ Depósito exitoso.")
    print(f"\nNuevo saldo: ${cuentas_prueba[usuario]['saldo']:,.2f}")
    registrar_operacion(usuario, "Deposito", monto)
    
def transferir_dinero(usuario):
    saldo = cuentas_prueba[usuario]["saldo"]
    print(f"\nSaldo disponible: ${saldo:,.2f}")
    
    destinatario = input("\nIngrese el usuario del destinatario:").strip().lower()
    
    if destinatario == usuario:
        print("\n✗ No puede transferirse dinero a sí mismo.")
        return
    
    if destinatario not in cuentas_prueba:
        print(f"\n✗ Usuario '{destinatario}' no encontrado.")
        return
    
    try:
        monto = float(input("\nIngrese el monto a transferir: $"))
    except ValueError:
        print("\n✗ Monto inválido. Debe ingresar un número.")
        return
    
    if monto <= 0: # Si el monto es menor o igual a cero
        print("\n✗ El monto debe ser mayor a cero.")
        return
    
    if monto > saldo: # Si el monto supera el saldo disponible
        print(f"\n✗ Saldo insuficiente. Su saldo es ${saldo:,.2f}")
        return 
    
    cuentas_prueba[usuario]["saldo"] -= monto
    cuentas_prueba[destinatario]["saldo"] += monto
    
    print(f"\n✓ Transferencia exitosa de ${monto:,.2f} a {destinatario.capitalize()}.")
    print(f"\nNuevo saldo: ${cuentas_prueba[usuario]['saldo']:,.2f}")
    registrar_operacion(usuario, f"Transferencia a {destinatario}", monto)  
