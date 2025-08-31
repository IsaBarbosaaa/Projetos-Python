def classifica_imc(imc: float) -> str:
    if imc < 18.5: return "Abaixo do peso"
    if imc < 25:   return "Peso normal"
    if imc < 30:   return "Sobrepeso"
    if imc < 35:   return "Obesidade grau I"
    if imc < 40:   return "Obesidade grau II"
    return "Obesidade grau III"

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f} — {classifica_imc(imc)}")
