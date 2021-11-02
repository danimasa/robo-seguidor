def dependencies():
    return ["ligado", "sensor_direito", "sensor_esquerdo"]

def willUpdate(value):
    s_dir = deps["sensor_direito"]
    s_esq = deps["sensor_esquerdo"]
    ligado = deps["ligado"]

    if not ligado:
        return "PARADO"

    if s_dir and not s_esq:
        return "ESQ"

    if s_esq and not s_dir:
        return "DIR"

    return "FRT"
