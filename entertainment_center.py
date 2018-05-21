print("Content-type:text/html \n")
import media
import fresh_tomatoes

viram = media.Movie("Vinnavayya Ramayya","http://igmedia.blob.core.windows.net/igmedia/telugu/gallery/movies/vinavayyaramayya/main.jpg",
                    "aKijba1mkQU")
hel = media.Movie("Hello","https://i0.wp.com/southreel.com/wp-content/uploads/2017/12/"
                  "Akhil-Akkinenichiranjeevihello-event-in-hyderbadKalyani-Priyadarshantelugu-trailers"
                  "Anup-RubensHELLO-USA-tourupcoming-telugu-movieslatest-telugu-movieslatest-telugu-trailersteaser-trailer-1.jpg?ssl=1",
                  "6WgnE6J07e8")
char = media.Movie("Charuseela","https://encrypted-tbn0.gstatic.com/images?"
                   "q=tbn:ANd9GcTLH-mul-xxDqbwqrKCDl7J359ELLrdTfdrmM9si4E7fP9NpoEe",
                   "fRk86VZyJsU")
prema = media.Movie("Prema Kavali","https://tse1.mm.bing.net/th?id=OIP.lIO5XdWY2CBqbvoUJ_uuvQAAAA&pid=15.1&P=0&w=300&h=300",
                   "RnzQ1QC2VAg")

movies = [viram,hel,char,prema]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
