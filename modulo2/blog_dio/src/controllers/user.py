from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus
from sqlalchemy import inspect
from src.controllers.post import _list_author_posters
from flask_jwt_extended import jwt_required
from src.utils import requires_role

app = Blueprint("user", __name__, url_prefix="/users")


def _create_user():
    data = request.json
    user = User(
        username=data["username"],
        email=data["email"],
        password=data["password"],
        role_id=data["role_id"],
    )

    db.session.add(user)
    db.session.commit()


def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": {
                "id": user.role.id,
                "name": user.role.name,
            },
        }
        for user in users
    ]


# CRAIR OU LISTAR USUARIO
@app.route("/", methods=["GET", "POST"])
@jwt_required()
@requires_role("admin")
def _list_create_user():

    if request.method == "POST":
        _create_user()
        return {"message": "User created"}, HTTPStatus.CREATED
    else:
        return {"users": _list_users()}


# BUSCAR USUARIO ID
@app.route("/<int:user_id>", methods=["GET"])
@jwt_required()
@requires_role("admin")
def get_user_id(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id,
        "username": user.username,
    }


# ATUALIZAR USUARIO
@app.route("/<int:user_id>", methods=["PATCH"])
@jwt_required()
def update_user_id(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json

    mapper = inspect(User)
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
    db.session.commit()

    return {
        "id": user.id,
        "username": user.username,
    }


# DELETAR USUARIO
@app.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user_id(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()

    return "", HTTPStatus.NO_CONTENT


# BUSCAR POST AUTHOR_ID
@app.route("/<int:user_id>/posts", methods=["GET"])
@jwt_required()
def get_post_author(user_id):

    user = db.get_or_404(User, user_id)
    resultado = _list_author_posters(user.id)
    return resultado
