import requests
import json
import pandas as pd

URL = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

json_URL = json.loads(URL.content)

candidato = []
partido = []
votos = []
porcentagem = []

for info in json_URL['cand']:

    if info['seq'] == '1' or info['seq'] == '2' or info['seq'] == '3' or info['seq'] == '4':
        candidato.append(info['nm'])
        votos.append(info['vap'])
        porcentagem.append(info['pvap'])

df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
    'Candidato', 'Nº de Votos', 'Porcentagem'
])

print(df_eleicao)