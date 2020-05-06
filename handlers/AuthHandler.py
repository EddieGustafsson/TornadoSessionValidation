from handlers.BaseHandler import BaseHandler
from handlers.SessionHandler import SessionHandler


class LoginHandler(BaseHandler):
    async def get(self):
        if self.current_user:
            self.redirect("/")
            return

        self.render('login.html')

    async def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        if "eddie" == username and "ärcool" == password:
            session_id = await SessionHandler.generate_session(username)

            self.set_secure_cookie("session", session_id)
            self.redirect(self.reverse_url("main"))
        else:
            self.redirect(self.reverse_url("login") + "?failed=credentials")


class LogoutHandler(BaseHandler):
    async def get(self):

        session_id = self.get_current_user().decode("utf-8")
        await SessionHandler.invalidate_session(session_id, None)

        self.clear_cookie("session")
        self.redirect(self.get_argument("next", self.reverse_url("main")))
