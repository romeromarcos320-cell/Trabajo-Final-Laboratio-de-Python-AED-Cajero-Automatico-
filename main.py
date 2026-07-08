# Nicolas Arzuaga | Juan Agustín Centurión
# Menu de operaciones del usuario
# Inicio y cierre de sesion

from autenticacion import login
from historial import mostrar_historial 
from operaciones import consultar_saldo, extraer_dinero, depositar_dinero, transferir_dinero

def menu_principal(usuario):
    while True:
        print("\n" + "=" * 40)
        print(f"          BIENVENIDO, {usuario.upper()}")
        print("=" * 40)
        print("1. Consultar saldo")
        print("2. Extraer dinero")
        print("3. Depositar dinero")
        print("4. Transferir dinero")
        print("5. Ver historial de operaciones")
        print("6. Cerrar sesión")
        print("-" * 40)
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            consultar_saldo(usuario)
        elif opcion == "2":
            extraer_dinero(usuario)
        elif opcion == "3":
            depositar_dinero(usuario)
        elif opcion == "4":
            transferir_dinero(usuario)
        elif opcion == "5":
            mostrar_historial(usuario)
        elif opcion == "6":
            print("\nCerrando sesión...")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione una opción válida.")

def main():
    
    usuario = login()
    
    if usuario:
        menu_principal(usuario)
    else:
        print("\n✗ Aceso bloqueado. Saliendo del programa.")
        
if __name__ == "__main__":
     main()

main()       
