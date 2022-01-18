# Open file
user = input("movie ")
with open("movies.txt") as movie_file:
    for movie in movie_file:
        movie.split()
        parts = movie.split(",")
        title = parts[0].strip()
        year = parts[1].strip()
        rating = parts[2].strip()
        
        print(f"{title} Rated: {rating}")
        