import fresh_tomatoes
import media
#

#
# # print(how_train_dragon.storyline)
#
homeland = media.Movie("Homeland",
                       "A bipolar CIA",
                       "https://images-na.ssl-images-amazon.com/images/I/71hbjCBeNML._SY450_.jpg",
                       "https://www.youtube.com/watch?v=KyFmS3wRPCQ")

# # print(homeland.storyline)
# # homeland.show_trailer()
#
punisher = media.Movie("Punisher",
                       "After the murder",
                       "https://images-na.ssl-images-amazon.com/images/I/71rWFEPLPZL._SY679_.jpg",
                       "https://www.youtube.com/watch?v=lIY6zFL95hE")


# punisher.show_trailer()


# a single movie object
# toyStory = media.Movie("Toy story", "a good movie", "http://aforismi.meglio.it/img/film/Toy_story.jpg",
#                        "https://www.youtube.com/watch?v=7FQ68Rw25gM")
how_train_dragon = media.Movie("How to Train Your Dragon",
                               "A hapless young",
                               "https://images-na.ssl-images-amazon.com/images/I/51uJGH71GsL.jpg",
                               "https://www.youtube.com/watch?v=fVr3J3Ddz70")
#
batman = media.Movie("Batman the Dark Knight",
                     "a great experience for comic fans",
                     "http://geekretreatimages.s3.amazonaws.com/wp-content/uploads/2016/03/The-Dark-Knight.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")
equilibrium = media.Movie("Equilibrium",
                          "a great action movie, with a deep message",
                          "http://www.gstatic.com/tv/thumb/movieposters/30590/p30590_p_v8_aa.jpg",
                          "https://www.youtube.com/watch?v=raleKODYeg0")

avengers = media.Movie("Avengers",
                       "Earth's mightiest heroes",
                       "https://ae01.alicdn.com/kf/HTB1iJ.ni9tYBeNjSspaq6yOOFXaE/Custom-Canvas-Wall-Decor-Avengers-Infinity-War-Poster-Marvel-Infinity-War-Wallpaper-Hulk-Thanos-Wall-Sticker.jpg_640x640.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

doctor_strange = media.Movie("Doctor Strange",
                             "a brilliant neurosurgeon",
                             "https://images-na.ssl-images-amazon.com/images/I/71gyLVWIfIL._SY606_.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

captain_marvel = media.Movie("Captain Marvel",
                             "Carol Danvers",
                             "https://m.media-amazon.com/images/M/MV5BMTE0YWFmOTMtYTU2ZS00ZTIxLWE3OTEtYTNiYzBkZjViZThiXkEyXkFqcGdeQXVyODMzMzQ4OTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=Z1BCujX3pw8")
# the list of movie objects to be displayed in the webpage
movies = [homeland, punisher, how_train_dragon, avengers, doctor_strange, captain_marvel]
# movies = [how_train_dragon, homeland, punisher, batman, avengers, doctor_strange]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__module__)
