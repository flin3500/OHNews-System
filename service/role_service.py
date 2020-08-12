from db.role_dao import RoleDao


class RoleService:
    __role_dao = RoleDao()

    def search_list(self):
        result = self.__role_dao.search_list()
        return result
