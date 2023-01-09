import streamlit as st
import pickle


st.title('Weather Preduction')
model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
precipitation=col1.number_input('Enter precipitation')
temp_max=col2.number_input('Enter temp_max')
temp_min=col1.number_input('Enter temp_min')
wind=col2.number_input('Enter Wind')


if st.button('Predict'):
    data=[[precipitation,temp_max,temp_min,wind]]
    result=model.predict(data)[0]
    st.success(result)