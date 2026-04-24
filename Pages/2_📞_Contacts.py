import streamlit as st

st.title("📞 Contact Me")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
    else:
        st.error("Please fill all fields.")

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
            
st.markdown("""
<div class="card">
<p>Email: jamelyngolingan831@email.com</p>
<p>Phone: 09854155218</p>
<p>GitHub: https://github.com/jamelyngolingan831-creator/GolinganJamelyn_MultiPageApp_Act2</p>
</div>
""", unsafe_allow_html=True)