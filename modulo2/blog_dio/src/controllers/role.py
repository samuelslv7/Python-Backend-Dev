from flask import Blueprint, request
from src.app import Role, db
from http import HTTPStatus
from sqlalchemy import inspect
from src.controllers.post import _list_author_posters
from flask_jwt_extended import jwt_required

app = Blueprint("role", __name__, url_prefix="/roles")


# CRAIR OU LISTAR USUARIO
@app.route("/", methods=["POST"])
def create_role():
    data = request.json
    role = Role(name=data["name"])
    db.session.add(role)
    db.session.commit()
    return {"message": "Role created"}, HTTPStatus.CREATED
