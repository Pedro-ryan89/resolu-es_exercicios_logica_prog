import json

with open("cursos.json", encoding="utf-8") as arq:
    dados = json.loads(arq.read())

for curso in dados:
    print(curso["nome"])