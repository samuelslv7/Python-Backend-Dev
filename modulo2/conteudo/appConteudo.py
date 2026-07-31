from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/olamundo", methods=["GET", "POST"])
def ola_mundo():
    if request.method == "GET":
        return {"message": "<p>Ola, GET!</p>"}
    else:
        return {"message": "<p>Ola, POST!</p>"}


@app.route("/bemvindo/<usuario>/<int:idade>")
def bem_vindo_user(usuario, idade):
    print(idade)
    print(f"valor do tipo idade = {type(idade)}")
    print(f"valor do tipo nome = {type(usuario)}")
    return {"usuario": usuario, "idade": idade}


# redirecionar URL
@app.route("/projects/")
def projects():
    return "The project page"


# url unico
@app.route("/about")
def about():
    return "The about page"


# URL building
@app.route("/")
def index():
    return "index"


with app.test_request_context():
    print(url_for("ola_mundo"))
    print(url_for("projects", next="/"))
    print(url_for("bem_vindo_user", usuario="Samuel", idade=28))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()
