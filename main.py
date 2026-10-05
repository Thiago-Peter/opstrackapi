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
        {"email": "tpstoy1@gmail.com", "nome": "Thiago"},
        {"email": "gustavopatrocinio25@gmail.com", "nome": "Gustavo"},
    ]


@app.route("/sobre")
def sobre():
    return "Projeto de exemplo, aula entrega contínua"


@app.route("/equipe")
def equipe():
    return [
        {
            "emailProfissional": "tpstoy1@gmail.com",
            "nome": "Thiago",
        },
        {
            "emailProfissional": "gustavopatrocinio25@gmail.com",
            "nome": "Gustavo",
        },
    ]


if __name__ == "__main__":
    app.run(debug=True)
