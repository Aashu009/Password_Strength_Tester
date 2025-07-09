import re
import pyttsx3
import streamlit as st

def speak(text):  
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def strength_checker(password):
    strength = 0
    feedback=[]
    
    
    pattern ={
        'lower':re.search(r'[a-z]', password),
        'upper':re.search(r'[A-Z]',password),
        'digit':re.search(r'[0-9]',password),
        'symbol':re.search(r'[!@#$%^&*(),.?":{}|<>]',password)
    }
    if(len(password)) >= 8:
        strength +=1
    else:
        feedback.append("Password should be atleast 8 characters long")

    if pattern['lower']:
        strength+=1
    else:
        feedback.append("Password must contain atleast 1 Lower case letter")
    
    if pattern['upper']:
        strength +=1
    else:
        feedback.append("Password must contain atleast 1 Upper case letter")

    if pattern['digit']:
        strength+=1
    else:
        feedback.append("Password must contain atleast 1 Digit")
    
    if pattern['symbol']:
        strength+=1
    else:
        feedback.append("Password must contain atleast 1 Symbol")
    
    if strength == 5:
        res = " Strong Password"
    elif strength>=3:
        res = " Moderate Password"
    else:
        res = "Weak Password"
    
    return res,feedback

# Front-end
st.set_page_config(page_title="Password Strength Checker")
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your Password : ", type='password')
enable_voice = st.checkbox("Enable Voice Feedback")

if st.button("Check"):
    if password:
        result, tips = strength_checker(password)
        
        st.subheader("Result : ")
        if "Strong" in result:
            st.success(result)
        elif "Moderate" in result:
            st.warning(result)
        else:
            st.error(result)

        if tips:
            st.subheader("Suggestions to Improve : ")
            for tip in tips:
                st.write('-> ', tip)
    
        if enable_voice:
            speak(result)
    
    else:
        st.warning("Please Enter a Password")
    