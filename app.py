import pickle
import streamlit as st  
import numpy as np
import sklearn

st.title("Book Recommendation System")

# Load the pickled model
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

# Create a function that takes the book title and returns the top 10 recommended books
selected_book_name = st.selectbox('Type or select a book', book_names)

def fetch_image_url_and_links(suggestion):
    image_url = []
    book_links = []
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            image_url.append(final_rating[final_rating['Title'] == j]['Image'].values[0])
            book_links.append(final_rating[final_rating['Title'] == j]['Image'].values[0])  # Assuming 'URL' column exists
    return image_url, book_links

def recommend_book(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1, -1), n_neighbors=6)
    
    image_url, book_links = fetch_image_url_and_links(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)

    return book_list, image_url, book_links

if st.button('Recommend'):
    recommendation_books, image_url, book_links = recommend_book(selected_book_name)
    
    for book, img, link in zip(recommendation_books[1:], image_url[1:], book_links[1:]):  # Skip the first item to avoid showing the selected book
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f'<a href="{link}" target="_blank"><img src="{img}" width="100"/></a>', unsafe_allow_html=True)
        
        with col2:
            book_details = final_rating[final_rating['Title'] == book].iloc[0]
            st.write("")
            st.write("")
            st.write(f"**Title**  : {book_details['Title']}")
            st.write(f"**Author**  : {book_details['Author']}")
            st.write(f"**ISBN**  : {book_details['ISBN']}")
