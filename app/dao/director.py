from app.dao.model.movies import Movie
from app.dao.model.genres import Genre
from app.dao.model.directors import Director



class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()
