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
        # Chama a requisição da API
        r = requests.get("https://adquirencia-processadora-api.prd.rs-1.paas.sicredi.net" +
                         "/establishment/searchestablishment/00000004/" + cnpj,
                         verify=False, timeout=2)
    except:
        # Retorna - se timeout
        return "-"
    try:
        data = json.loads(r.content)
    except:
        # Retorna se problema de parse no json outros erros
        return "+"
    return data['estabelecimentos'][0]['domiciliosBancario'][0]['numAgencia']


# Lê o arquivo input.xlsx e carrega em um dataframe
df = pd.read_excel("input2.xlsx", "1")
# Abre o arquivo de saída
filename = "saida.csv"
myfile = open(filename, "w")

# Para cada CNPJ lido no excel, busca a agência na api da Fiserv
for cnpj in df.iterrows():
    agencia = retorna_agencia(str(cnpj[1]['cnpj']))
    # Printa a agência encontrada e a quantidade de chamadas até o momento
    print("AGENCIA: ------" + agencia + "------")
    print(str(cnpj[0]) + "de 5032")
    # Salva a agência, se encontrada, ou "-" se timeout
    myfile.write(str(cnpj[1]['cnpj']) + ";" + agencia + "\n")
