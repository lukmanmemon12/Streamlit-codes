import streamlit as st

st.title("Mini Calculator")

n1 = st.number_input("Enter n1")
n2 = st.number_input("Enter n2")
col1, col2, col3, col4 = st.columns(4)
with col1:
    Sum = n1 + n2
with col2:
    sub = st.button("sub")
with col3:
    mul = st.button("mul")
with col4:
    div = st.button("div")
if sum:
    ans = n1 + n2
    st.text("Sum is {}".format(ans))
if sub:
    ans = n1 - n2 
    st.text("Subtration is {}".format(ans))
if mul :
    ans = n1 * n2
    st.text("Multiplication is {}".format(ans))
if div:
    ans = n1 / n2
    st.text("Division is {}".format(ans))               
