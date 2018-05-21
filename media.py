print("Content-type:text/html \n")
import webbrowser


class Movie():
    VALID_RATINGS=["Excellent","Good","Average","Ok"]
    def __init__(i,movie_title,poster_image,trailer_youtube):
        i.title=movie_title
        i.poster_image_url=poster_image
        i.trailer_youtube_url=trailer_youtube
    def show_trailer(i):
        webbrowswer.open(i.trailer_youtube_url)
