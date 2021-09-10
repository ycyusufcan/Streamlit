import streamlit as st

# for titles
st.title("Web App")

# for headers
st.header("This is a header")

# for subheaders
st.subheader("This is a subheader")

# for texts
st.text("Hello Streamlit. This is a text")

# for markdowns
st.markdown("This is a normal markdown")

st.markdown("# This is a bold markdown")

st.markdown("## This is a thin-bold Markdown")

st.markdown("* This is markdown with point")

st.markdown("** This is a small bold markdown**")

# for colorful text
st.success("Successfull")
st.markdown("'This is a markdown'")
st.info("This is an information")
st.warning("This is a warning")

# for boxes
st.selectbox("Graduation", ["High School", "College Degree", "Master Degree"])

st.multiselect("Where do you live?", ("Paris", "Roma", "Istanbul"))

# for buttons
st.button("Simple Button")

# for sliders
st.slider("What is your level?",0 , 100, step=10) 

# for good design we can do nicer web apps
html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Demo Web App </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.title('This is for a good design')

st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)