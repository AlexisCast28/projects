def normalize_name(txt):
    """
        ESTA FUNCION NORMALIZA STRINGS LO QUE HACE
        ES QUITAR ESPACIOS EN BLANCO AL INICIO Y FIN DE MI STRING, 
        ESPACIOS EN BLANCO LOS ELIMINA Y EL NOMBRE EN TITULO.
        
        cARLos ANtOnIO -> Carlos Antonio

        :params (str): texto de entrada
        :return: texto formateado
    """
    return " ".join(txt.strip().title().split()) 
def to_mxn(valor, tasa: float = 1.0):
    """
    CONVIERTE UN VALOR NUMERICO EN MXN MULTIPLICADO POR LA TASA DE CAMBIO
    """"
    return float(valor) * float(tasa, 2)
