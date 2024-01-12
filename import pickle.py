import pickle
import streamlit as st

filename='model.pkl'
model= pickle.load(open(filename,'rb'))
print(model)


st.title('IPL WIN PREDICTION..')