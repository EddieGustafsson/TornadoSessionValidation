import asyncpg


class DatabaseManager:
    @staticmethod
    async def get_connection():
        conn = await asyncpg.connect('postgresql://localhost:5433/tornado_session?user=postgres&password=postgres')
        return conn
