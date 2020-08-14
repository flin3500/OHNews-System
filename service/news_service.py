from db.news_dao import NewsDao
from db.redis_dao import RedisNewsDao
from db.mongo_dao import MongoNewsDao


class NewsService:
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    __mongo_news_dao = MongoNewsDao()


    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    def review_news(self, id):
        self.__news_dao.review_news(id)

    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

    def delete_news(self, id):
        self.__news_dao.delete_news(id)

    def add_news(self, title, editor_id, type_id, content, if_top):
        self.__mongo_news_dao.insert(title, content)
        content_id = self.__mongo_news_dao.search_id(title)
        self.__news_dao.add_news(title, editor_id, type_id, content_id, if_top)

    def search_cache(self, id):
        result = self.__news_dao.search_cache(id)
        return result

    def insert(self, id, title, username, type, content, if_top, create_time):
        self.__redis_news_dao.insert(id, title, username, type, content, if_top, create_time)

    def delete(self, id):
        self.__redis_news_dao.delete(id)

    def search_by_id(self, id):
        result = self.__news_dao.search_by_id(id)
        return result

    def edit_news(self, id, title, type_id, content_id, if_top):
        self.__news_dao.edit_news(id, title, type_id, content_id, if_top)
        self.delete(id)

