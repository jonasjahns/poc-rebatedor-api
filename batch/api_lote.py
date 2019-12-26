import json
import requests
import pandas as pd

"""
    Versão 1.0 do batch
    Esse batch lê um arquivo de texto contendo os CNPJs
    Realiza a chamada da API da Fiserv
    Salva a agência em um arquivo de saída, quando sucesso
    Quando falha, salva "-" no lugar do número da agência
"""


def retorna_agencia(cnpj):
    try:
        r = requests.get("https://adquirencia-processadora-api.prd.rs-1.paas.sicredi.net" +
                         "/establishment/searchestablishment/00000004/" + cnpj,
                         verify=False, timeout=2)
    except:
        return "-"
    try:
        data = json.loads(r.content)
    except:
        print(r)
        return "-"
    return data['estabelecimentos'][0]['domiciliosBancario'][0]['numAgencia']


df = pd.read_excel("input2.xlsx", "1")
filename = "saida.csv"
myfile = open(filename, "w")

for cnpj in df.iterrows():
    agencia = retorna_agencia(str(cnpj[1]['cnpj']))
    print("AGENCIA: ------" + agencia + "------")
    print(str(cnpj[0]) + "de 5032")
    myfile.write(str(cnpj[1]['cnpj']) + ";" + agencia + "\n")
