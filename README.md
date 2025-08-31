
#  Python — Primeiros Passos

Repositório com **mini‑projetos iniciais em Python** para praticar lógica, entrada/saída, condicionais, laços, funções, arquivos e consumo de API.  
Cada projeto é independente, com **objetivo**, **como executar** e **o que você vai aprender**.

> **Como executar (geral):**
> 1) Instale o Python 3.10+  
> 2) (Opcional) Crie um ambiente virtual:  
>    ```bash
>    python -m venv .venv && source .venv/bin/activate  # macOS/Linux
>    .venv\Scripts\activate                           # Windows
>    ```
> 3) (Opcional) Instale dependências extras:  
>    ```bash
>    pip install -r requirements.txt
>    ```
> 4) Rode o script desejado: `python caminho/do/script.py`

---

##  Estrutura
```
python-primeiros-passos/
├─ 01_hello_world.py
├─ 02_calculadora_imc.py
├─ 03_conversor_temperatura.py
├─ 04_jogo_adivinhacao.py
├─ 05_lista_tarefas_cli.py
├─ 06_analisador_texto.py
├─ 07_gerador_senhas.py
├─ 08_consulta_cep.py
├─ requirements.txt
└─ README.md
```

---

##  Projetos

### 1) `01_hello_world.py` — Entrada/Saída e f-strings
**Objetivo:** Imprimir mensagens, ler nome do usuário e cumprimentar.  
**Aprendizados:** `print`, `input`, variáveis, f-strings.

**Executar:** `python 01_hello_world.py`

---

### 2) `02_calculadora_imc.py` — Condicionais
**Objetivo:** Calcular IMC a partir de peso e altura e classificar o resultado.  
**Aprendizados:** `float`, operadores aritméticos, `if/elif/else`, formatação.

**Executar:** `python 02_calculadora_imc.py`

---

### 3) `03_conversor_temperatura.py` — Funções
**Objetivo:** Converter Celsius ↔ Fahrenheit em um menu simples.  
**Aprendizados:** definição de **funções**, retorno, conversão de tipos.

**Executar:** `python 03_conversor_temperatura.py`

---

### 4) `04_jogo_adivinhacao.py` — Laços e aleatoriedade
**Objetivo:** Usuário tenta adivinhar um número secreto.  
**Aprendizados:** `while`, tratamento de erro com `try/except`, `random`.

**Executar:** `python 04_jogo_adivinhacao.py`

---

### 5) `05_lista_tarefas_cli.py` — Persistência simples (JSON)
**Objetivo:** Criar, listar e concluir tarefas no terminal, salvando em arquivo `tarefas.json`.  
**Aprendizados:** listas, dicionários, leitura/escrita de arquivos, **JSON**.

**Executar:** `python 05_lista_tarefas_cli.py`

---

### 6) `06_analisador_texto.py` — Strings e coleções
**Objetivo:** Ler um texto e mostrar contagem de caracteres, palavras e top 5 palavras.  
**Aprendizados:** `split`, `Counter`, normalização, ordenação.

**Executar:** `python 06_analisador_texto.py`

---

### 7) `07_gerador_senhas.py` — Aleatoriedade e opções do usuário
**Objetivo:** Gerar senhas seguras com tamanho e conjuntos de caracteres configuráveis.  
**Aprendizados:** `random`, `string`, validação de entradas.

**Executar:** `python 07_gerador_senhas.py`

---

### 8) `08_consulta_cep.py` — Consumo de API (ViaCEP)
**Objetivo:** Consultar endereço pelo CEP usando a API pública ViaCEP.  
**Aprendizados:** requisições HTTP com `requests`, tratamento de resposta JSON, erros.

**Executar:**  
1) `pip install -r requirements.txt`  
2) `python 08_consulta_cep.py`

