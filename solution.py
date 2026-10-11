from datetime import datetime, timedelta
import requests


def cotar():
    cotacoes = []
    hoje = datetime.now()

    for i in range(365):
        data = datetime.strftime(hoje - timedelta(i), "%m-%d-%Y")
        url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
        res = requests.get(url).json()

        if res["value"]:
            cotacoes.append(res["value"][0]["cotacaoCompra"])
        else:
            cotacoes.append(None)

    return cotacoes

print(cotar())