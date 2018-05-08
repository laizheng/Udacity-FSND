class Movie:
    """
    A class to store proper movie properties for fresh_tomatoes.create_movie_tiles_content() to
    populate page content.
    """
    """A class to store proper movie properties

    Attributes:
            trailer_youtube_url (str): url to the trailer stored on Youtube.
            trailer_youtube_url (str): Name of the movie.
            poster_image_url (str): url to the poster image.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Constructor of Movie class.

        Args:
            trailer_youtube_url (str): url to the trailer stored on Youtube.
            trailer_youtube_url (str): Name of the movie.
            poster_image_url (str): url to the poster image.
        """
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url

