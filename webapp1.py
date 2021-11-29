
import streamlit as st 
import joblib
model=joblib.load('model_joblib_lr')
st.title("Medical Insurence cost")
fn=st.text_input("Enter your name")
f1=st.selectbox("which city you want to choose for Medical Insurence Check-up ",('Pune','Nagpur','Kolhapur','Mumbai'))
p1=st.slider('Enter your age',65,100)
s1=st.selectbox('select your gender',('Male','Female'))
if s1=="Male":
    p2=1
else:
    p2=0
p3=st.number_input("Enter Your BMI value")
p4=st.slider("Enter no of children",0,4) 
s2=st.selectbox(' Do you smoke ?',("Yes","No"))
if s2=="Yes":
    p5=1
else:
    p5=0
p6=st.slider("Choose the city Pune':1, 'Nagpur':2, 'Kolhapur':3, 'Mumbai':4",1,4) 
if st.button('Predict'):
    pred=model.predict([[p1,p2,p3,p4,p5,p6]])   
    st.success("hello"+ "  "+fn+"  " +" you choose the city "+f1+ "  your Medical Insurence cost will be {}".format(pred[0]))