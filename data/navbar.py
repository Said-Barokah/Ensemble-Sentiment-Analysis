def navbar():
    import streamlit as st
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {
            display:none;
            position:fixed
        }
                [data-testid="stHeader"]{
                display:none;
            position:fixed
                }
    .st-emotion-cache-gh2jqd{
            max-width: 100vw;
                }
        
        .st-emotion-cache-gh2jqd {
                padding: 0rem
                
            }
        </style>
    """, unsafe_allow_html=True)
    import streamlit as st

    # CSS untuk meniru navbar
    st.markdown("""
        <style>
        body {
            background-color:white
        }
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(to right, #8e4caf, #ec9c9c);  /* Gradasi warna hijau */
            padding: 20px 10px;
            border-right: 1px solid #d1d1d1;
            z-index: 9999;
            color: white;  /* Warna teks putih */
        }
        .navbar a {
            text-decoration: none;
            color: white;  /* Warna teks putih */
            padding: 8px 16px;
            transition: background-color 0.3s, color 0.3s;  /* Animasi transisi */
        }
        .navbar a:hover {
            background-color: rgba(255, 255, 255, 0.2);  /* Warna latar belakang semi-transparan saat di-hover */
            color: #ffeb3b;  /* Warna teks kuning saat di-hover */
            border-radius: 4px;
        }
        .st-emotion-cache-zt5igj {
            text-align: center;
        }
        .st-emotion-cache-wghjn0 {
            position: relative;
            width: 800px;
            margin: auto;
        }
        #selamat-datang-di-kamus-bahasa-madura {
            margin-top: 80px;
            color:#848484;
        }
        .st-emotion-cache-ue6h4q{
            display:none
        }
       
    """, unsafe_allow_html=True)
    import streamlit as st

    st.markdown("""
        <style>
            .st-emotion-cache-uf99v8 {
                padding-left: 8% !important;
                padding-right: 8% !important;
                background: white !important;
            }
        </style>
        """, unsafe_allow_html=True)



    # Membuat navbar
    st.markdown("""
        <div class="navbar">
            <div>
                <a href="/">Home</a>
                <a href="stacking">Klasifikasi Ensemble Stacking</a>
                <a href="#about">About</a>
            </div>
        </div>
    """, unsafe_allow_html=True)