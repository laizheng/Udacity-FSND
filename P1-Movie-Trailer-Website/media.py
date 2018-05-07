class Movie:
    """
    A class to store proper movie properties for fresh_tomatoes.create_movie_tiles_content() to
    populate page content.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url

