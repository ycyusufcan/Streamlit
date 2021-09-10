import streamlit as st

#for images
from PIL import Image
im = Image.open("summer.jfif")
st.image(im, width = 700, caption="Summer")

# for graphs
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(0, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)