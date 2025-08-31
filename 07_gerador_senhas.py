import random, string

def gerar(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
    pool = ""
    if usar_maiusculas: pool += string.ascii_uppercase
    if usar_minusculas: pool += string.ascii_lowercase
    if usar_digitos:    pool += string.digits
    if usar_simbolos:   pool += "!@#$%&*?-_"
    if not pool:
        raise ValueError("Selecione pelo menos um conjunto de caracteres.")
    return "".join(random.choice(pool) for _ in range(tamanho))

try:
    t = int(input("Tamanho da senha (padrão 12): ") or "12")
    print("Use 1 para Sim e 0 para Não")
    sets = {
        "Maiúsculas": bool(int(input("Incluir maiúsculas? (1/0): ") or "1")),
        "Minúsculas": bool(int(input("Incluir minúsculas? (1/0): ") or "1")),
        "Dígitos":    bool(int(input("Incluir dígitos? (1/0): ") or "1")),
        "Símbolos":   bool(int(input("Incluir símbolos? (1/0): ") or "1")),
    }
    senha = gerar(t, sets["Maiúsculas"], sets["Minúsculas"], sets["Dígitos"], sets["Símbolos"])
    print("Senha gerada:", senha)
except Exception as e:
    print("Erro:", e)
