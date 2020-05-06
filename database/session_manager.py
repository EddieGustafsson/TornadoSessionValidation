from uuid import UUID

import asyncpg as asyncpg

from database.database_manager import DatabaseManager
from exceptions.session_exceptions import InvalidSession
from models.session_model import SessionModel


class SessionManager:
    @staticmethod
    async def create_session(session: SessionModel):
        conn = await DatabaseManager.get_connection()
        sql = '''INSERT INTO session_list(id, user_name, created_at, expires_at) VALUES ($1, $2, $3, $4)'''

        await conn.execute(sql, session.get_id(), session.get_user_name(), session.get_created_at(), session.get_expires_at())
        await conn.close()

    @staticmethod
    async def remove_session_by_id(session_id: UUID):
        conn = await DatabaseManager.get_connection()
        sql = '''DELETE FROM session_list WHERE id=$1'''

        await conn.execute(sql, session_id)
        await conn.close()

    @staticmethod
    async def remove_session_by_username(username: str):
        conn = await DatabaseManager.get_connection()
        sql = '''DELETE FROM session_list WHERE user_name=$1'''

        await conn.execute(sql, username)
        await conn.close()

    @staticmethod
    async def get_session_by_id(session_id: UUID) -> SessionModel:
        conn = await DatabaseManager.get_connection()
        sql = '''SELECT * FROM session_list WHERE id=$1'''

        result = await conn.fetchrow(sql, session_id)
        await conn.close()

        if result is None:
            raise InvalidSession

        session = SessionModel(result["id"], result["user_name"], result["created_at"], result["expires_at"])
        return session
