import requests

def consulta_cep(cep: str) -> dict:
    cep = "".join(filter(str.isdigit, cep))
    if len(cep) != 8:
        raise ValueError("CEP deve ter 8 dígitos.")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    dados = resp.json()
    if dados.get("erro"):
        raise ValueError("CEP não encontrado.")
    return dados

if __name__ == "__main__":
    try:
        cep = input("Digite o CEP (somente números): ")
        dados = consulta_cep(cep)
        print(f"{dados['logradouro']}, {dados['bairro']} — {dados['localidade']}/{dados['uf']} (IBGE: {dados['ibge']})")
    except Exception as e:
        print("Erro:", e)
