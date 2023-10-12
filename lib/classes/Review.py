class Review:

    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        Review.all.append(self)

        self.viewer._reviews.append(self)
        self.viewer._movies.append(self.movie)
        
        self.movie._reviews.append(self)
        self.movie._viewers.append(self.viewer)

    @property
    def viewer(self):
        return self._viewer
    @viewer.setter
    def viewer(self, viewer):
        from classes.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("viewer must be an instance of Viewer")
    
    @property
    def movie(self):
        return self._movie
    @movie.setter
    def movie(self, movie):
        from classes.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("movie must be an instance of Movie")
            
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else:
            raise Exception("rating must be an integer between 1 and 5 and cannot be changed")
    
    