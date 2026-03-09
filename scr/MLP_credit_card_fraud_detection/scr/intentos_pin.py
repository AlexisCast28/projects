"""
    ESTE PROGRAMA VA A PEDIR AL USUARIO SU PIN DE ACCESO-

    1) SI EL PIN ES CORRECTO, EL PRORAMA ENTONCES DEBE DECIRLE
    AUTENTIFACION EXITOSA, ACCESO CONCEDIDO

    2) SI EL PIN ES INCORRECTO, ENTONCES EL PROGRAMA DEBE DE DECIRLE PIN INCORRECTO
    Y WL NUMWEI SW INTENTOS QUE LE QUEDAN.

    3) SI EL USUARIO SUPERA EL NUMERO DE INTEWNTOS PERMITIDOS ENTONCES EL PROGRAMA LE DIRA
    NUMERO DE INTENTOS SUPERADO Y CUENTA BLOQUEADA.
"""
PIN_CORRECTO = '1234'
INTENTOS_MAX = 3
intento = 0

while intento < INTENTOS_MAX:
    entrada = input('ingresa tu pin (4 digitos)')
    if entrada  == PIN_CORRECTO:
        print('Autenticacion exitosa')
        print('acceso concedido')
        break
    else:
        intento += 1
        restantes = INTENTOS_MAX - intento 
        if restantes > 0:
            print(f'pin incorrecto. Te quedan {restantes} intentos')
        else:
            print('PIN INCORRECTO. CUENTA BLOQUEADA')