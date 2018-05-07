import fresh_tomatoes
from media import Movie


def main():
    """
    Hard coded a list of favourite movies and send to fresh_tomatoes.open_movies_page().
    A webpage is automatically popped up at the end of this function.
    :return: no return
    """
    mission_impossible_vi = Movie(title="Mission Impossible VI",
                                  poster_image_url="images/Mission-Impossible-Poster.jpg",
                                  trailer_youtube_url="https://www.youtube.com/watch?v=hR-0po0hzDQ")
    transformer_iii = Movie(title="Transformer III",
                            poster_image_url="images/TransformersIII-Poster.jpg",
                            trailer_youtube_url="https://www.youtube.com/watch?v=kHRf01Gjosk")
    independence_day = Movie(title="Independence Day",
                             poster_image_url="images/Independence-Day-Poster.jpg",
                             trailer_youtube_url="https://www.youtube.com/watch?v=NZZvtQtdbzM")
    manchester_by_the_sea = Movie(title="Manchester by the Sea",
                                  poster_image_url="images/Manchester-By-The-Sea-Poster.jpg",
                                  trailer_youtube_url="https://www.youtube.com/watch?v=gsVoD0pTge0")
    movies = [mission_impossible_vi, transformer_iii, independence_day, manchester_by_the_sea]
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    main()


