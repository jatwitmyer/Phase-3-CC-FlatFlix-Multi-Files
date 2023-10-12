class Viewer:
    def __init__(self, username):
        self.username = username

        self._reviews = []
        self._movies = []
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("username must be a string between 6 and 16 characters")

    def reviews(self):
        return self._reviews

    def reviewed_movies(self):
        return list(set(self._movies))

    def has_reviewed_movie(self, movie):
        if movie in self._movies:
            return True
        else:
            return False

    def add_review(self, movie, rating):
        from classes.Review import Review
        new_review = Review(self, movie, rating)
        return new_review