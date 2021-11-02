def dependencies():
    return ["direcao", "velocidade"]

def willUpdate(value):
    direcao = deps["direcao"]
    velocidade = deps["velocidade"]

    if direcao == "DIR" or direcao == "FRT":
        return velocidade

    return 0
