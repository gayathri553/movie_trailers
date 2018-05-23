import webbrowser
print("Content-type:text/html \n")


class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowswer.open(self.trailer_youtube_url)
