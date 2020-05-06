import tornado

from exceptions.session_exceptions import InvalidSession
from handlers.BaseHandler import BaseHandler
from handlers.SessionHandler import SessionHandler


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    async def get(self):
        try:

            remote_ip = self.request.remote_ip
            user_agent = self.request.headers.get('User-Agent')

            # Retrieves the current session-id and gets the session model.
            session_id = self.get_current_user().decode("utf-8")
            session = await SessionHandler.get_session(session_id, remote_ip, user_agent)

            self.render('index.html', session=session)

        except InvalidSession:
            self.redirect(self.reverse_url("logout"))
