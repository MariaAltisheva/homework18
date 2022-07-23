
from app.dao.model.movies import Movie
from app.dao.model.directors import Director
from app.dao.model.genres import Genre

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()
