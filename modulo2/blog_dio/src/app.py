import os
import click
import sqlalchemy as sa
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
jwt = JWTManager()


class Role(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    user: Mapped[list["User"]] = relationship(back_populates="role")

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True)
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(default=True)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey("role.id"))
    role: Mapped["Role"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r}, active={self.active!r})"


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime] = mapped_column(
        nullable=False, server_default=sa.func.now()
    )
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), nullable=False)

    def __repr__(self) -> str:
        return (
            f"Post(id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"
        )


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    with current_app.app_context():
        db.create_all()
    click.echo("Banco de dados inicializado.")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///blog.sqlite",
        jwt_secret_key="super-secret",
        # app.config["JWT_SECRET_KEY"] = "super-secret"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    app.cli.add_command(init_db_command)

    # inicializar extensoes
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # registrar blueprints
    from src.controllers import user
    from src.controllers import post
    from src.controllers import auth
    from src.controllers import role

    app.register_blueprint(user.app)
    app.register_blueprint(post.app)
    app.register_blueprint(auth.app)
    app.register_blueprint(role.app)

    return app
