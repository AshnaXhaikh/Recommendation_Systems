# Recommendation Systems - Book Recommender
This is a simple book recommender system that uses content-based filtering to recommend books based on user ratings.

## Features
- Content-based filtering using TF-IDF vectorization
- Cosine similarity to find similar books
- User interface for inputting book ratings and receiving recommendations
- Displays book details including title, author, and description
- Visualizations of book ratings
- Cover image scraping from Archive.org

## Requirements
- Python 3.12
- Flask
- scikit-learn
- pandas
- numpy
- nltk
- requests
- BeautifulSoup4
- tqdm
- matplotlib
- seaborn
- wordcloud
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Book_Recommender.git
   cd Book_Recommender
   ```  
2. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
3. Download the NLTK stopwords:

    ```python
    import nltk
    nltk.download('stopwords')
    ```
4. Run the Flask application:

    ```bash
    python app.py
    ```
5. Open your web browser and go to `http://localhost:5000`
## Usage
1. Input the title of a book you like in the search bar.
2. Click the "Recommend" button.
3. The system will display a list of recommended books based on the input book.
4. You can also view the details of each recommended book by clicking on the book title.
## Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions, whether it's fixing bugs, improving documentation, or adding new features, are welcome!
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
## Acknowledgments
This project was inspired by the need for a simple and effective book recommendation system. Special thanks to the contributors of the libraries used in this project, including Flask, scikit-learn, and NLTK.
## Contact
For any questions or suggestions, feel free to open an issue on the GitHub repository or contact me at [ashnaxhaikh@gmail.com](mailto:ashnaxhaikh@gmail.com) 