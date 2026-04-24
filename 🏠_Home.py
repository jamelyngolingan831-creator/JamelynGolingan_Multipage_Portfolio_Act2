import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="centered")

st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: center;
    gap: 25px;
    background-color: #1c1f26;
    padding: 12px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,212,255,0.2);
    flex-wrap: wrap;
}

.stButton>button {
    background-color: transparent;
    color: black;
    border: none;
    font-size: 16px;
    font-weight: bold;
}

.stButton>button:hover {
    color: #00d4ff;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0e1117, #1c1f26);
    color: white;
}

/* Glass card */
.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0,212,255,0.2);
    backdrop-filter: blur(10px);
}

/* Center text */
.center {
    text-align: center;
}

/* Profile image */
img {
    border-radius: 50%;
    border: 3px solid black;
}

/* Buttons */
.stButton>button {
    background-color: gray;
    color: black;
    border-radius: 10px;
    padding: 8px 20px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #00aacc;
    color: white;
}

/* Progress bar labels */
.progress-label {
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("jam.jpeg", width=300)

st.markdown("<h2 class='center'>Hi, I'm Jamelyn 👋</h2>", unsafe_allow_html=True)

st.markdown("""
<p class='center'>
<b>Aspiring IT Developer | Learning | Building & Growing</b>
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<p class='center'>
I am a Computing and Information Technology student passionate about building interactive web applications using Python and Streamlit.
I enjoy learning new technologies and creating simple, useful projects that improve my skills as a developer.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🚀 Explore")

col1, col2 = st.columns(2)

with col1:
    if st.button("👤 About Me", use_container_width=True):
        st.switch_page("Pages/1_🧩_About.py")

    if st.button("🎮 Projects", use_container_width=True):
        st.switch_page("Pages/3_🎮_Projects.py")

with col2:
    if st.button("🧠 Skills", use_container_width=True):
        st.switch_page("Pages/4_⚙️_Skills.py")

    if st.button("📞 Contacts", use_container_width=True):
        st.switch_page("Pages/2_📞_Contacts.py")
