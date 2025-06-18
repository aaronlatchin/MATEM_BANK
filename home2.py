import streamlit as st
 
def login_page() :
    st.title("login to bank")
    username = st.text_input("username")
    if st.button("login"):
        if username:
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("please enter a username")

def home_page():
    st.title(f"welcome, {st.session_state.username}!")
    st.write("your trusted partner for all your financial needs")

    col1, col2 = st.columns(2)
 
    with col1:
        st.image("https://via.placeholder.com/300", caption="secure banking")

    with col2:
        st.write("at Maten banking app, we prioritize your financial security and provide a range of services.")
        st.write("our mission is to create excellent customer services.")

    st.write(".....")
    st.write("thanks for banking with us.")

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        login_page()
    else:
        home_page()
if __name__== "__main__":
    main()
  





