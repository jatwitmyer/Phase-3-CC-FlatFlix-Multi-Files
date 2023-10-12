class Movie:
    def __init__(self, title):
        self.title = title

        self._reviews = []
        self._viewers = []

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("title must be a string of at least 1 character")

    def reviews(self):
        return self._reviews

    def reviewers(self):
        return list(set(self._viewers))

    def average_rating(self):
        if len(self._reviews) > 0:
            avg = sum([review.rating for review in self._reviews])/len(self._reviews)
            avg_rounded = round(avg, 1)
            return avg_rounded
        else:
            return None
