from flask import Flask


app = Flask(__name__)


@app.route("/")
def projeto():
    return {"Serviço": "OpsTrack", "status": "ONLINE"}


@app.route("/help")
def help():
    return "Página destinada a ajuda do user"


@app.route("/users")
def users():
    return [
        {"email": "email.com", "nome": "tavi"},
        {"email": "email.com", "nome": "ana"},
    ]


@app.route("/sobre")
def sobre():
    return "Projeto de exemplo, aula entrega contínua"


@app.route("/equipe")
def equipe():
    return [
        {"emailProfissional": "@indis...sp.gov.br", "nome": "Paulo"},
        {"emailProfissional": "...", "nome": "Ana"},
    ]


if __name__ == "__main__":
    app.run(debug=True)
