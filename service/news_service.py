from db.news_dao import NewsDao


class NewsService:
    __news_dao = NewsDao()

    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    def review_news(self, id):
        self.__news_dao.review_news(id)
