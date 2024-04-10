import strawberry
from typing import List
from models.index import users
from connection.db import conn


@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, info, id: int) -> User:
        return conn.execute(users.select().where(users.c.id == id)).fetchone()

    @strawberry.field
    def users(self, info) -> List[User]:
        return conn.execute(users.select()).fetchall()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name: str, email: str, password: str) -> bool:
        result = conn.execute(
            users.insert().values(name=name, email=email, password=password)
        )
        return result.inserted_primary_key[0]

    @strawberry.mutation
    def update_user(self, info, id: int, name: str, email: str, password: str) -> str:
        result = conn.execute(
            users.update()
            .where(users.c.id == id)
            .values(name=name, password=password, email=email)
        )
        return str(result.rowcount) + " row(s) affected"

    @strawberry.mutation
    def delete_user(self, info, id: int) -> bool:
        result = conn.execute(users.delete().where(users.c.id == id))
        return result.rowcount == 1
