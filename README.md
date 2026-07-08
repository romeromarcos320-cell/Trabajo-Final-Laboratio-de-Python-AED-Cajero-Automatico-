# Cajero Automático – Simulador en Python

Trabajo Práctico Grupal Lab. de Python – Algoritmo y estructuras de datos 

Grupo B42 AED Comision K1.2

## Descripción

Este proyecto simula las operaciones básicas de un cajero automático (ATM)
desarrollado en Python. El sistema permite a un usuario autenticarse con su
usuario y contraseña, y luego realizar operaciones bancarias simples:
consulta de saldo, extracción de dinero, depósito y transferencia entre
cuentas.

El sistema contempla además controles de seguridad y de negocio:
validación de acceso con bloqueo por intentos fallidos, control de saldo
insuficiente, límite máximo y minimo de extracción por operación, y un registro
(historial) de las operaciones realizadas durante la sesión.

## Integrantes del grupo

- Romero Marcos Ariel
- Centurion Juan Agustin
- Arzuaga Nicolas

## Cómo ejecutar el programa

En caso de querer probar el programa por su cuenta, sigue los siguientes pasos:

1. Cloná o descargá este repositorio
2. Abrí una terminal en la carpeta del proyecto
3. Ejecutá:

```bash
python main.py
```
4. Ingresá con uno de los usuarios de prueba (ver tabla más abajo) cuando el
   programa lo solicite

> **Importante:** el programa requiere ingresar datos por teclado
> (`input()`). Si se ejecuta desde VSCode, debe usarse la **Terminal
> integrada** (no el panel "Output" de Code Runner), ya que ese panel no
> admite entrada interactiva del usuario.

## Video DEMO



## Usuarios de prueba

| Usuario   | Contraseña | Saldo   | Estado    |
|-----------|------------|---------|-----------|
| marcos    | 1234       | $50.000 | Activo    |
| ana       | 5678       | $120.000| Activo    |
| luis      | abcd       | $8.000  | Activo    |
| sofia     | 4321       | $35.000 | Activo    |
| pedro     | 9999       | $15.000 | Activo    |
| valentina | 1111       | $200.000| Activo    |
| nicolas   | 2222       | $5.000  | Activo    |
| camila    | 3333       | $75.000 | Activo    |
| julian    | 4444       | $9.500  | Activo    |
| luciana   | 5555       | $42.000 | Activo    |
| mateo     | 6666       | $18.000 | Activo    |
| florencia | 7777       | $63.000 | Activo    |
| diego     | 8888       | $11.000 | Activo    | 
| martina   | 9876       | $95.000 | Activo    |
| gabriel   | 1357       | $27.000 | Activo    |
| agustina  | 2468       | $33.000 | Activo    |
| rodrigo   | 1122       | $4.500  | Bloqueado |
| carolina  | 3344       | $88.000 | Bloqueado |
| facundo   | 5566       | $7.200  | Bloqueado |
| micaela   | 7788       | $51.000 | Bloqueado |
------------------------------------------------

## Funciones implementadas

### Autenticación `autenticacion.py`
- Validación de usuario y contraseña antes de permitir el acceso al sistema
- Hasta 3 intentos de inicio de sesión
- Bloqueo automático de la cuenta al superar el límite de intentos fallidos
- Distinción entre "usuario no encontrado" y "cuenta bloqueada", con
  mensajes específicos para cada caso

### Consulta de saldo `datos.py`
- Muestra el saldo actual de la cuenta del usuario autenticado

### Extracción `operaciones.py`
- Permite retirar dinero, descontándolo del saldo de la cuenta
- Controla que el monto solicitado no supere el saldo disponible
- Aplica un límite máximo de extracción por operación ($10.000)

### Depósito `operaciones.py`
- Permite ingresar dinero a la cuenta, sumándolo al saldo actual

### Transferencia `operaciones.py`
- Permite transferir dinero de la cuenta propia a otra cuenta del sistema
- Valida que la cuenta destino exista
- Valida que haya saldo suficiente antes de transferir

### Registro de operaciones `historial.py`
- Registra cada operación realizada (tipo, monto, fecha/hora)
- Permite consultar el historial de movimientos de la sesión

### Menú principal `main.py`
- Centraliza el acceso a todas las operaciones disponibles
- Permite cerrar sesión de forma controlada

## Estructura del proyecto

```
cajero/
│
├── main.py             # Punto de entrada del programa y menú principal
├── autenticacion.py     # Login, validación de usuario y contraseña
├── operaciones.py        # Extracción, depósito y transferencia
├── historial.py          # Registro de operaciones realizadas
├── datos.py              # Datos de prueba (usuarios, cuentas, constantes)
└── README.md
```

## Decisiones de diseño

- **Separación en módulos:** cada archivo tiene una responsabilidad
  específica (datos, autenticación, operaciones, historial), siguiendo el
  principio de que cada función/módulo debe encargarse de una sola cosa.
  Esto facilita el trabajo en grupo, ya que distintos integrantes pueden
  trabajar en módulos diferentes.
- **Datos en memoria:** las cuentas y el historial se almacenan en
  estructuras de datos de Python (diccionarios y listas) durante la
  ejecución del programa, sin persistencia en archivo o base de datos, ya
  que no fue un requisito del enunciado.
- **Bloqueo de cuenta:** se optó por bloquear la cuenta tras 3 intentos
  fallidos de inicio de sesión como medida de seguridad básica, en lugar de
  permitir intentos ilimitados.
- **Límite de extracción:** se fijó un monto máximo y minimo por operación de
  extracción, independiente del saldo disponible, simulando una política
  real de cajeros automáticos.

## Limitaciones conocidas

- Los datos no persisten entre ejecuciones: al cerrar el programa, los
  saldos y el historial vuelven a su estado inicial definido en `datos.py`.
- No se contempla la posibiladad que dos usuarios operen la misma cuenta al
  mismo tiempo.
- El sistema utiliza usuarios y contraseñas predefinidos; no existe una
  funcionalidad de alta de nuevos usuarios. Por ahora 

## Estado del proyecto

| Módulo             | Estado        |
|--------------------|---------------|
| `datos.py`         | Completo      |
| `autenticacion.py` | Completo      |
| `main.py`          | Completo      |
| `cuenta.py`        | Completo      |
| `operaciones.py`   | Completo      |
| `historial.py`     | Completo      |