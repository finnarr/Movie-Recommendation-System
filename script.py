from movie_data import *

sample_data = movie_data[:5]
print(sample_data)

# Recommend movies based on a specific genre
def recommend_by_genre(genre):
    recommended_movies = [movie for movie in movie_data if movie[0].lower()==genre.lower()]

    return recommended_movies

# Recommend movies based on a specific director
def recommend_by_director(director):
    recommended_movies = [movie for movie in movie_data if movie[2].lower()==director.lower()]

    return recommended_movies

# Recommend movies based on minimum rating
def recommend_by_rating(min_rating):
    recommended_movies = [movie for movie in movie_data if float(movie[4]) >= min_rating]

    return recommended_movies

# Command-Line Interface for the Recommendation System

def movie_recommendation_cli():
    print("Welcome to the Movie Recommendation System")
    print("Please choose your recommendation type:")
    print("1. By Genre")
    print("2. By Director")
    print("3. BY Rating")

    choice = input("Enter your choice (1, 2, 3 or 4): ")

    if choice == '1':
        print("\nAvailble Genres:")
        print(", ".join(genres))
        selected_genre = input("Enter the genre for movie recommendations: ")
        recommendations = recommend_by_genre(selected_genre)
    elif choice == '2':
        selected_director = input("Enter the director's name for movie recommendations: ")
        recommendations = recommend_by_director(selected_director)
    elif choice == '3':
        selected_rating = float(input("Enter the minimum rating (1.0 to 5.0) for movie recommendations: "))
        recommendations = recommend_by_rating(selected_rating)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    if recommendations:
        print("\nRecommended Movies: ")
        for movie in recommendations[:10]:
            print(f"{movie[1]} ({movie[3]}) - Genre: {movie[0]}, Director: {movie[2]}, Rating: {movie[4]}")
    else:
        print("No movies found for your selection.")

movie_recommendation_cli()
