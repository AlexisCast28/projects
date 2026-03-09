from UTILIS import normalize_name, to mxn

raw = [
    {"nombre": " ana ", "activo": True, 'monto': '120.50' },
    {"nombre": " LUIS ", "activo": False, 'monto': '10' },
    {"nombre": " mara ", "activo": True, '99.99' }, 
]

def clean(reg):
    return {
        "nombre": normalize_name(reg['nombre']),
        "activo": bool(reg['activo']),
        "monto": to_mxn(reg['monto'], tasa=1.0)
    }