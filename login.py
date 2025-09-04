import streamlit as st


if "users" not in st.session_state:
    st.session_state["users"] = {}

if "page" not in st.session_state:
    st.session_state["page"] = "Login"  


def login_page():
    st.title("🔑 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email in st.session_state["users"] and st.session_state["users"][email] == password:
            st.success("✅ Login successful!")
            st.session_state["logged_in"] = True
            st.session_state["email"] = email
        else:
            st.error("❌ Invalid email or password")

    st.markdown("👉 Don't have an account? [Sign Up](#)", unsafe_allow_html=True)
    if st.button("Go to Sign Up"):
        st.session_state["page"] = "Sign Up"
        st.rerun()


def signup_page():
    st.title("📝 Sign Up")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if email in st.session_state["users"]:
            st.error("❌ Email already exists!")
        elif password != confirm_password:
            st.error("❌ Passwords do not match!")
        elif len(password) < 6:
            st.warning("⚠️ Password must be at least 6 characters")
        else:
            st.session_state["users"][email] = password
            st.success("✅ Sign Up successful! Please login now.")
            st.session_state["page"] = "Login"
            st.rerun()

    st.markdown("👉 Already have an account? [Login](#)", unsafe_allow_html=True)
    if st.button("Go to Login"):
        st.session_state["page"] = "Login"
        st.rerun()


# Show the correct page
if st.session_state["page"] == "Login":
    login_page()
else:
    signup_page()
