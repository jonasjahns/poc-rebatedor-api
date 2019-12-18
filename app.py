import flask
from files import reader


app = flask.Flask(__name__)


@app.route("/")
def helloworld():
    return "Bem vindo ao Rebatedor de APIs! </br>" \
           "Temos 02 APIs mapeadas até o momento :D </br>" \
           "GLHF!"


@app.route("/acquirer-status/acquirerstatus/<cpfcnpj>")
def acquirer_status(cpfcnpj):
    """
    Versão 1.1 da API de statuso do estabelecimento
    Nessa versão não é necessário passar o número da instituição
    Retorna a massa de dados atribuída para o CNPJ/CPF escolhido
    """
    return reader.file_open("massa/acquirer_status/", cpfcnpj+".txt")


@app.route("/establishment/searchestablishment/<cpfcnpj>")
def establishment(cpfcnpj):
    """
    Versão 1.0 da API de statuso do estabelecimento
    Retorna a massa de dados atribuída para o CNPJ/CPF escolhido
    """
    return reader.file_open("massa/establishment/", cpfcnpj+".txt")


app.run()
