# Bollywood Movie Recommendation System

This project is a Bollywood Movie Recommendation System built using Kaggle, Streamlit, Pandas, and the OMDb API. The system recommends movies similar to a selected movie and fetches their posters.
It utilizes a precomputed similarity matrix to suggest similar movies and fetches movie posters from the OMDb API for display. Users can interact with the app by selecting a movie from a dropdown menu to receive personalized recommendations with accompanying posters.

## Features

- Select a Bollywood movie from a dropdown menu
- Get top 5 movie recommendations similar to the selected movie
- Display movie titles and posters for recommended movies

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Mighty3Niket/bollywood-movie-recommendation-system.git
   cd bollywood-movie-recommendation-system
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
3. Ensure you have the necessary data files:

- `movie_dict.pkl`
- `similarity.pkl`

## Usage

1. Run the application:
   ```sh
   streamlit run app.py
2. In your web browser, select a Bollywood movie from the dropdown menu.
3. Click the `Recommend` button to get movie recommendations.

## Project Structure

- `BollywoodMovieDetail.csv` : CSV file containing all the data to be pre-processed
- `main.py` : Main application file
- `app.py` : Application deployment file
- `movie_dict.pkl` : Pickle file containing movie data
- `similarity.pkl` : Pickle file containing movie similarity matrix
- `requirements.txt` : Text file containing required libraries to be installed
- `README.md` : Project documentation

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- `Kaggle`
- `Streamlit`
- `Pandas`
- `OMDb API`
