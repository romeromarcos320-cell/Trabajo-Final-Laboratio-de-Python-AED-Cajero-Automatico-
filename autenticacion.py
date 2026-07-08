# Marcos Ariel Romero
# Valida el usuario y la contraseña ingresados por el usuario
# Niega el acesso despues de 3 intentos fallidos

from datos import cuentas_prueba, MAX_INTENTOS

def iniciar_sesion():
    print ("\n" + "=" * 40)
    print ("          SIMULADOR DE CAJERO AUTOMATICO")
    print ("=" * 40)
    
    usuario = input("Ingrese su nombre de usuario: ").strip().lower()
    contraseña = input("Ingrese su contraseña: ").strip()
    
    return usuario, contraseña

def validar_usuario(usuario, contraseña):
    
    if usuario not in cuentas_prueba:
        print("\n✗ Usuario no encontrado.")
        return False
    
    if cuentas_prueba[usuario]["bloqueado"]:
        print("\n✗ Usuario bloqueado. Contacte con el banco.")
        return False
    
    if cuentas_prueba[usuario]["contraseña"] != contraseña:
        print("\n✗ Contraseña incorrecta.")
        return False
    
    return True

def login():
    
    intentos = 0
    
    while intentos < MAX_INTENTOS:
        usuario, contraseña = iniciar_sesion()
        if validar_usuario(usuario, contraseña):
            print("\n✓ Ha iniciado seción correctamente.")
            return usuario
        
        intentos += 1
        intentos_restantes = MAX_INTENTOS - intentos
        
        if intentos_restantes > 0:
            print(f"\nQuedan {intentos_restantes} intentos.")
        else:
            if usuario in cuentas_prueba:
                print("\n✗ Ha superado el numero maximo de intentos. Se ha bloquedo su cuenta.")
                cuentas_prueba[usuario]["bloqueado"] = True
            else:
                print("\n✗ Acesso denegado. Usuario no encontrado.")
    
    return None        
            
