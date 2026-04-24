import streamlit as st

st.title("👤 About Me")

st.markdown("""
<style>
/* Page background */
body {
    background-color: #0e1117;
}

/* Main app container */
.stApp {
    background: linear-gradient(135deg, #0e1117, #1c1f26);
    color: white;
}

/* Card design */
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 12px rgba(0, 212, 255, 0.2);
    margin-bottom: 20px;
}

/* Headings */
h1, h2, h3 {
    color: #00d4ff;
}

/* Text styling */
p, li {
    color: #e0e0e0;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.write("""
<div class="card">
            
<p>
I am <b>Jamelyn Golingan</b>, a dedicated student with a strong passion for technology and software development.
I am currently studying in the field of Information Technology, where I continuously explore programming, web development, and data visualization.
</p>

<p>
I enjoy building interactive applications using <b>Python</b> and <b>Streamlit</b> because they allow me to turn ideas into creative and useful web apps.
I am curious, hardworking, and always eager to learn new skills that can improve my abilities as a future developer.
</p>

<p>
This portfolio showcases my projects, skills, and learning journey as I grow in the world of programming.
Thank you for visiting my app!
</p>
</div>
""", unsafe_allow_html=True)

st.subheader("🎓 Education")
st.write("-BS Computer Science")
st.write("-Training WEB-DEV and learning Software Development")

st.subheader("♑ Goals")
st.write("Become a Full Stack Developer")
st.write("Build useful and creative web applications")