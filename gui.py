import streamlit as st
import math_solver.matrix as matrix
import math_solver.vectors as vectors

st.title("🧮 Math Solver of Python")

option = st.selectbox("Choose a topic:", ["Matrix", "Vectors"])

if option == "Matrix":
  