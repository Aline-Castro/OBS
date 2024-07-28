import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Função para verificar e criar o diretório
def verificar_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

# Função para extrair dados de presença de um dia específico
def extrair_dados_dia(ano, mes, dia):
    url = f"https://app-sipws-prd.azurewebsites.net/Servico/ConsultaSIP.asmx/JsonPresencaAnoMesDia?ano={ano}&mes={mes}&dia={dia}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        data = json.loads(soup.text)
        return data
    except requests.RequestException:
        pass  # Suprimir mensagens de erro de requisição
    except json.JSONDecodeError:
        pass  # Suprimir mensagens de erro de decodificação de JSON
    return None

# Função para extrair dados de presença do mês
def extrair_dados_mes(ano, mes):
    with ThreadPoolExecutor() as executor:
        dias = range(1, 32)  # Considerando até o 31º dia
        resultados = list(executor.map(lambda dia: extrair_dados_dia(ano, mes, dia), dias))
    return [resultado for resultado in resultados if resultado is not None]

# Função para criar planilhas com os dados de presença dos parlamentares
def criar_planilhas(ano, mes, diretorio="C:/Voluntario/PRESENCA-2023"):
    # Adicionando o subdiretório com o ano e mês
    diretorio_mes = os.path.join(diretorio, f"{ano}-{mes:02d}")
    verificar_diretorio(diretorio_mes)
    
    parlamentares = {}
    dados_mes = extrair_dados_mes(ano, mes)
    
    for data in dados_mes:
        data_sessao = datetime.strptime(data['Dia'][:10], "%Y-%m-%d").strftime("%d/%m/%Y")
        for item in data['Presencas']:
            for presenca in item['Presencas']:
                parlamentar = [
                    item['Nome'], 
                    data_sessao, 
                    presenca.get('Numero', ''), 
                    presenca.get('Tipo', ''), 
                    presenca.get('Presenca', 'Sem registro de presença').strip() or 'Sem registro de presença'
                ]
                if item['Nome'] not in parlamentares:
                    parlamentares[item['Nome']] = []
                parlamentares[item['Nome']].append(parlamentar)

    colunas = ['nome_parlamentar', 'data_sessao', 'numero_sessao', 'tipo_sessao', 'presenca_sessao']

    for nome, dados in parlamentares.items():
        df = pd.DataFrame(dados, columns=colunas)
        df.to_excel(os.path.join(diretorio_mes, f"{nome}.xlsx"), index=False)

    print("Planilhas criadas com sucesso!")

# Solicitar mês e ano ao usuário
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))

# Chamada da função para criar as planilhas com os valores fornecidos pelo usuário
criar_planilhas(ano, mes)
