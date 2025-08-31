import json, os

ARQ = "tarefas.json"

def carregar():
    if not os.path.exists(ARQ): return []
    with open(ARQ, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar(tarefas):
    with open(ARQ, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def listar(tarefas):
    if not tarefas:
        print("Sem tarefas!")
        return
    for i, t in enumerate(tarefas, 1):
        status = "✅" if t["done"] else "⏳"
        print(f"{i}. {status} {t['title']}")

def main():
    tarefas = carregar()
    while True:
        print("\n1) Adicionar  2) Concluir  3) Listar  0) Sair")
        op = input("Escolha: ").strip()
        if op == "0":
            salvar(tarefas); break
        elif op == "1":
            titulo = input("Título: ").strip()
            if titulo:
                tarefas.append({"title": titulo, "done": False})
        elif op == "2":
            listar(tarefas)
            try:
                idx = int(input("Número da tarefa: ")) - 1
                tarefas[idx]["done"] = True
            except Exception:
                print("Índice inválido.")
        elif op == "3":
            listar(tarefas)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
