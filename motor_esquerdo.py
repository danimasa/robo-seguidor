def dependencies():
    return ["direcao", "velocidade"]

def willUpdate(value):
    direcao = deps["direcao"]
    velocidade = deps["velocidade"]

    if direcao == "ESQ" or direcao == "FRT":
        return velocidade

    return 0
