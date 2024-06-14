# Book Recommendation System

This is a Book Recommendation System built using a content-based filtering approach. The system recommends books based on the features of the books the user has rated highly.

![2022-book-recommendations-teg-4](https://github.com/RanaweeraHK/Book-Recommender-System/assets/129282753/e4b11076-8c5e-417f-8583-a794a4d9487c)


## Features

- Recommend books based on a selected book title.
- Display book details including Title, Author, and ISBN.
- Provide clickable links to book images that open in a new tab.

## Technologies Used

- Python
- Streamlit
- scikit-learn
- NumPy
- Pandas

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Git (to clone the repository)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/RanaweeraHK/book-recommender-system.git
    cd book-recommender-system
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - **Windows:**

        ```bash
        .\venv\Scripts\Activate
        ```

    - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```


## Usage

1. **Run the Streamlit Application**

    ```bash
    streamlit run app.py
    ```

2. **Open the Application in Your Browser**

    The application will be available at `http://localhost:8501` by default.

3. **Interact with the Application**

    - Select a book from the dropdown menu.
    - Click on "Recommend" to get book recommendations.
    - Click on the book images to open more details about the books in a new tab.

## File Structure

- `app.py`: The main application script for the Streamlit app.
- `artifacts/`: Directory containing the pickled model and data files.


## Acknowledgements

- Thanks to the open-source community for providing useful libraries and tools.
