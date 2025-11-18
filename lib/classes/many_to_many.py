class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
     
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            return
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._name = value
 

    def articles(self):
        return [article for article in Article.all if article.author == self]


    def magazines(self):
        return list({article.magazine for article in self.articles()})


    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        topics = {mag.category for mag in self.magazines()}
        return list(topics) if topics else None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

     @property
    def name(self):
        return self._name


    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass