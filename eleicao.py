import requests
import json
import pandas as pd

URL = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
jsonURL = json.loads(URL.content)

candidato = []
partido = []
votos = []
porcentagem = []

for info in jsonURL['cand']:
    candidato.append(info['nm'])
    votos.append(info['vap'])
    porcentagem.append(info['pvap'])

eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
    'Candidato', 'Nº de Votos', 'Porcentagem'])

print(eleicao)
