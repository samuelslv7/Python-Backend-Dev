from flask import Blueprint, request
from src.app import Post, db
from http import HTTPStatus
from sqlalchemy import inspect, select

app = Blueprint("post", __name__, url_prefix="/posts")


def _create_post():
    data = request.json

    post = Post(title=data["title"], body=data["body"], author_id=data["author_id"])

    db.session.add(post)
    db.session.commit()


def _list_posters():
    query = db.select(Post)
    posters = db.session.execute(query).scalars()
    return [
        {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "author_id": post.author_id,
        }
        for post in posters
    ]


def _list_author_posters(user_id):
    # Cria a instrução SELECT filtrando pelo ID do usuário
    stmt = select(Post).where(Post.author_id == user_id)
    # Executa e obtém todos os resultados como lista
    user_posts = db.session.scalars(stmt).all()

    return [
        {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "author_id": post.author_id,
        }
        for post in user_posts
    ]


# CRAIR OU LISTAR POST
@app.route("/", methods=["GET", "POST"])
def handle_post():
    if request.method == "POST":
        _create_post()
        return {"message": "poster creado"}, HTTPStatus.CREATED
    else:
        return {"posts": _list_posters()}


# BUSCAR POST ID
@app.route("/<int:post_id>", methods=["GET"])
def get_post_id(post_id):
    post = db.get_or_404(Post, post_id)
    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
    }


# ATUALIZAR POST
@app.route("/<int:post_id>", methods=["PATCH"])
def update_post_id(post_id):
    post = db.get_or_404(Post, post_id)
    data = request.json

    mapper = inspect(Post)
    for column in mapper.attrs:
        if column.key in data:
            setattr(post, column.key, data[column.key])
    db.session.commit()

    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
    }


# DELETAR POST
@app.route("/<int:post_id>", methods=["DELETE"])
def delete_user_id(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()

    return "", HTTPStatus.NO_CONTENT
