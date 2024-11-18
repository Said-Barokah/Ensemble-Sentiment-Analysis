import streamlit as st
from data import navbar
import pandas as pd
import time
navbar.navbar() 
st.markdown("""
        <style>
            [data-testid="stFileUploaderDropzone"] {
                margin-top: 10px !important;
            }
            [data-testid="stVerticalBlockBorderWrapper"] {
                margin-bottom: 100px !important;
            }
        </style>
        """, unsafe_allow_html=True)

data = st.file_uploader("upload data berformat excel (untuk mengubah data master)", type=['csv'])
# st.page_link(page="data")
if data is not None:

    data = pd.read_csv(data)
    data.to_json('data/data.json')
    with st.spinner('tunggu sebentar ...'):
        time.sleep(1)
    st.write(data)
    # st.caption("Masukkan banyak data test")
    # size_test = st.number_input('',min_value=0.1,max_value=0.9,value=0.2)
    # st.caption("Masukkan banyak k untuk klasifikasi KNN")
    # k_number = st.number_input("", min_value=2,value=5)
    text = data.columns[0]
    # label = data.columns[3]
    if st.button("Proses Data"):
        with st.spinner('Tunggu tahapan preprocessing selesai'):
            st.header("Preprocessing")
            expander_1 = st.expander("Hasil Preprocessing")
            data[text] = data[text].str.lower()
            expander_1.caption("Hasil Case Folding")
            expander_1.write(data[text])
            data[text] = data[text].str.replace('\d+', '', regex=True)
            data[text] = data[text].str.replace("\b[a-zA-Z]\b", "", regex=True)
            data[text] = data[text].str.replace('[^\w\s]+', '', regex=True)
            expander_1.caption("Hasil Filtering")
            expander_1.write(data[text])
            import nltk
            nltk.download('punkt')
            from nltk.tokenize import word_tokenize
            from nltk.corpus import stopwords
            nltk.download('stopwords')
            data[text] = data[text].apply(word_tokenize)
            expander_1.caption("Hasil Tokenizing")
            expander_1.write(data[text])
            data[text] =data[text].apply(lambda x: [token for token in x if token not in stopwords.words('indonesian')])
            expander_1.caption("Hasil Remove Stopword")
            expander_1.write(data[text])
            from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()
            data[text] = data[text].apply(lambda x: [stemmer.stem(y) for y in x])
            data[text] = data[text].str.join(" ")
            expander_1.caption("Hasil Stemming")
            expander_1.write(data[text])
        with st.spinner('Tunggu tahapan Feature Extraction'):
            st.header("Feature Extraction")
            expander_2 = st.expander("Hasil Preprocessing")
            from sklearn.feature_extraction.text import CountVectorizer
            vectorizer = CountVectorizer()
            TF_vector = vectorizer.fit_transform(data[text])
            df_TF_vector = pd.DataFrame(TF_vector.toarray(),columns=vectorizer.get_feature_names_out())
            expander_2.caption("Hasil Feature Extraction Term Frequency")
            expander_2.write(df_TF_vector)
            df_TF_vector.to_json('data/df_TF_vector.json')
        # with st.spinner("Tunggu Tahapan Data Split"):
        #     st.header("Data Split")
        #     from sklearn.model_selection import train_test_split
        #     X_train, X_test, y_train, y_test = train_test_split(df_TF_vector, data[label], test_size=size_test, random_state=1221)
        #     tab1, tab2 = st.tabs(["Data Train", "Data Test"])
        #     with tab1:
        #         result = pd.concat([y_train, X_train], axis=1)
        #         st.write(result)
        #     with tab2:
        #         result = pd.concat([y_test, X_test], axis=1)
        #         st.write(result)
   
            


        

            
