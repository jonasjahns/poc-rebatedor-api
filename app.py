import flask
from files import reader


app = flask.Flask(__name__)


@app.route("/")
def helloworld():
    return "Bem vindo ao Rebatedor de APIs! </br>" \
           "Temos 02 APIs mapeadas até o momento :D </br>" \
           "GLHF!"


@app.route("/acquirer-status/acquirerstatus/<cpfcnpj>")
@app.route("/acquirer-status/acquirerstatus/00000004/<cpfcnpj>")
def acquirer_status(cpfcnpj):
    """
    Versão 1.1 da API de statuso do estabelecimento
    Nessa versão não é necessário passar o número da instituição
    Retorna a massa de dados atribuída para o CNPJ/CPF escolhido
    """
    return reader.file_open("massa/acquirer_status/", cpfcnpj+".txt")


@app.route("/establishment/searchestablishment/<cpfcnpj>")
@app.route("/establishment/searchestablishment/00000004/<cpfcnpj>")
def establishment(cpfcnpj):
    """
    Versão 1.0 da API de status do estabelecimento
    Retorna a massa de dados atribuída para o CNPJ/CPF escolhido
    """
    return reader.file_open("massa/establishment/", cpfcnpj+".txt")


@app.route("/sale/consultsale/realizadas/<merchant>/<datainicio>/<datafim>")
@app.route("/sale/consultsale/00000004/realizadas/<merchant>/<datainicio>/<datafim>")
def sales(merchant, datainicio, datafim):
    """
        Versão 1.0 da API de vendas
        Retorna a massa de dados atribuída para o merchant escolhido
        Não realiza filtro por mês
    """
    return reader.file_open("massa/sales/", merchant+".txt")


@app.route("/terminal/consultterminal/<merchant>")
@app.route("/terminal/consultterminal/00000004/<merchant>")
def terminal(merchant):
    """
        Versão 1.0 da API de vendas
        Retorna a massa de dados atribuída para o merchant escolhido
    """
    return reader.file_open("massa/terminal/", merchant+".txt")


@app.route("/mdr-fees/getmdrfees/<merchant>")
@app.route("/mdr-fees/getmdrfees/00000004/<merchant>")
def mdr_fees(merchant):
    """
        Versão 1.0 da API de vendas
        Retorna a massa de dados atribuída para o merchant escolhido
    """
    return reader.file_open("massa/mdr_fees/", merchant+".txt")


@app.route("/service-order/consultaos/00000004/<merchant>")
def service_order(merchant):
    return reader.file_open("massa/service_order/", merchant + ".txt")


app.run()
