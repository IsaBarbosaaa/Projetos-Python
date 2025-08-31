def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9

while True:
    print("\n1) Celsius → Fahrenheit\n2) Fahrenheit → Celsius\n0) Sair")
    opc = input("Escolha: ").strip()
    if opc == "0": break
    try:
        if opc == "1":
            c = float(input("Celsius: "))
            print(f"Fahrenheit: {c_to_f(c):.2f}")
        elif opc == "2":
            f = float(input("Fahrenheit: "))
            print(f"Celsius: {f_to_c(f):.2f}")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite um número válido.")
