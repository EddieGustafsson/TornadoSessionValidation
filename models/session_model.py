from datetime import datetime
from uuid import UUID


class SessionModel:
    def __init__(self, _id: UUID, user_name: str, created_at: datetime, expires_at: datetime, remote_ip: str, user_agent: str):
        self._id = _id
        self._user_name = user_name
        self._created_at = created_at
        self._expires_at = expires_at
        self._remote_ip = remote_ip
        self._user_agent = user_agent

    def get_id(self):
        return self._id

    def set_age(self, _id: UUID):
        self._id = _id

    def get_user_name(self):
        return self._user_name

    def set_user_name(self, user_name: str):
        self._user_name = user_name

    def get_created_at(self):
        return self._created_at

    def set_created_at(self, created_at: datetime):
        self._created_at = created_at

    def get_expires_at(self):
        return self._expires_at

    def set_expires_at(self, expires_at: datetime):
        self._expires_at = expires_at

    def get_remote_ip(self):
        return self._remote_ip

    def set_remote_ip(self, remote_ip: str):
        self._remote_ip = remote_ip

    def get_user_agent(self):
        return self._user_agent

    def set_user_agent(self, user_agent: str):
        self._user_agent = user_agent
