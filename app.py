import streamlit as st
from data import navbar
navbar.navbar()
st.markdown("""
        <style>
            #text_area_1 {
                margin-top: 10px !important;
            }
            [data-testid="stVerticalBlockBorderWrapper"] {
                margin-bottom: 100px !important;
            }
        </style>
        """, unsafe_allow_html=True)
st.header("Klasifikasi Sentiment Metode KNN")
import streamlit as st
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Input text area
text_test = st.text_area('Masukkan teks berita yang ingin dilabelkan', height=100)

# Button to trigger prediction
if st.button('Mulai prediksi') and len(text_test) != 0:
    # Text preprocessing
    text_test = text_test.lower()
    text_test = re.sub(r'\d+', '', text_test)
    text_test = re.sub(r'\b[a-zA-Z]\b', '', text_test)
    text_test = re.sub(r'[^\w\s]+', '', text_test)
    # st.write(f'Teks setelah preprocessing: {text_test}')

    # Tokenization and stopword removal
    nltk.download('punkt')
    nltk.download('stopwords')
    tokens = word_tokenize(text_test)
    tokens = [token for token in tokens if token not in stopwords.words('indonesian')]
    # st.write(tokens)
    
    # Stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Join tokens back into a single string
    processed_text = ' '.join(stemmed_tokens)
    # st.write(f'Teks setelah tokenisasi dan stemming: {processed_text}')

    




