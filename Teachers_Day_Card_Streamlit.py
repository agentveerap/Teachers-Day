import streamlit as st
from streamlit_extras.let_it_rain import rain

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Happy Teachers’ Day", page_icon="🌸", layout="centered")

# -------------------- ANIMATION --------------------
rain(
    emoji="🌸",
    font_size=30,
    falling_speed=5,
    animation_length="infinite"
)

# -------------------- MAIN TITLE --------------------
st.markdown(
    """
    <h1 style="text-align: center; color: #e75480; font-family: 'Comic Sans MS', cursive;">
        🌹 Happy Teachers’ Day 🌹
    </h1>
    """,
    unsafe_allow_html=True
)

# -------------------- SUBTITLE --------------------
st.markdown(
    """
    <h2 style="text-align: center; color: #444;">
        Dedicated to <span style="color:#e75480;">Mrinalini Ma'am</span>
    </h2>
    """,
    unsafe_allow_html=True
)

# -------------------- ICON BUTTONS --------------------
st.write("")
st.markdown("### Click on an icon to see your note:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💌 Thank You"):
        st.success(
            "Dear Ma'am,\n\n"
            "Thank you for your guidance, patience, and inspiration. 🌟 "
            "Am lucky to have you as our teacher. 💖\n\n"
            "Happy Teachers’ Day! 🎉"
        )

with col2:
    if st.button("😔 Sorry"):
        st.warning(
            "Dear Ma'am,\n\n"
            "If I have ever been careless or inattentive, we sincerely apologize. 🙏\n"
            "I truly appreciate all that you do for us. 🌸"
        )

with col3:
    if st.button("🌟 Appreciation"):
        st.info(
            "Dear Ma'am,\n\n"
            "Your dedication and passion for teaching inspire us every day. ✨\n"
            "Thank you for making learning fun and meaningful! 💐"
        )

# -------------------- FOOTER --------------------
st.markdown(
    """
    <p style="text-align:center; color:gray; font-size:14px;">
       (Aur bhi accha bana sakta tha lekin exams aane waale hai and already python ka code 300 line tak pahuch gya tha)
       Coded by Arnav Pratyaksh (Prem se)
    </p>
    """,
    unsafe_allow_html=True
)
