from db.user_dao import UserDao


class UserService:
    __user_dao = UserDao()

    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    def search_role(self, username):
        role = self.__user_dao.search_role(username)
        return role

    def add_user(self, username, password, email, role_id):
        self.__user_dao.add_user(username, password, email,role_id)
