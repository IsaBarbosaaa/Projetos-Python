import re
from collections import Counter

texto = input("Cole/Digite um texto: ").lower()
palavras = re.findall(r"[\wáàâãéêíóôõúüç]+", texto)
contagem = Counter(palavras)

print(f"Caracteres: {len(texto)}")
print(f"Palavras: {len(palavras)}")
print("Top 5 palavras:")
for palavra, freq in contagem.most_common(5):
    print(f"- {palavra}: {freq}")
