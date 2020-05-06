from datetime import datetime, timedelta
from uuid import uuid4, UUID
from database.session_manager import SessionManager
from exceptions.session_exceptions import InvalidSession
from models.session_model import SessionModel


class SessionHandler:
    @staticmethod
    async def generate_session(user_name: str, remote_ip: str, user_agent: str):

        await SessionHandler.invalidate_session(None, user_name)

        # Creates a session model and inserts it into the database.
        # When finished it returns the session id encoded as bytes.
        session = SessionModel(uuid4(), user_name, datetime.now(), datetime.now() + timedelta(days=1), remote_ip, user_agent)
        session_id = str(session.get_id())
        await SessionManager.create_session(session)

        return bytes(session_id, 'utf-8')

    @staticmethod
    async def validate_session(session_id: UUID, remote_ip: str, user_agent: str):
        valid = await SessionManager.validate_session(session_id, remote_ip, user_agent)
        return valid

    @staticmethod
    async def invalidate_session(session_id: UUID, user_name: str):
        if session_id is not None:
            await SessionManager.remove_session_by_id(session_id)
        else:
            await SessionManager.remove_session_by_username(user_name)

    @staticmethod
    async def get_session(session_id: UUID, remote_ip: str, user_agent: str) -> SessionModel:
        valid = await SessionHandler.validate_session(session_id, remote_ip, user_agent)

        if valid:
            session = await SessionManager.get_session_by_id(session_id)
            return session
        else:
            raise InvalidSession
