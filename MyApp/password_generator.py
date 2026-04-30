import streamlit as st
import random
import string

st.set_page_config(page_title="🔐 Memory Password Generator", page_icon="🔐")
st.title("🔐 Memory Password Generator")

st.write("Create a memorable password using things you know and love!")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["📝 Answer Questions", "🎲 Random Generator"])

with tab1:
    st.subheader("💡 Answer these questions")
    
    # Questions about things you know
    st.write("### 📚 Things You Know")
    favorite_color = st.text_input("What's your favorite color?", placeholder="e.g., blue")
    favorite_food = st.text_input("What's your favorite food?", placeholder="e.g., pizza")
    favorite_movie = st.text_input("What's your favorite movie?", placeholder="e.g., Inception")
    
    # Questions about things you love
    st.write("### ❤️ Things You Love")
    pet_name = st.text_input("Name of a pet (current or dream)?", placeholder="e.g., Luna")
    best_friend = st.text_input("Best friend's name?", placeholder="e.g., Sarah")
    hometown = st.text_input("Your hometown?", placeholder="e.g., Boston")
    
    # Numbers
    st.write("### 🔢 Important Numbers")
    birth_year = st.text_input("Birth year?", placeholder="e.g., 1995")
    lucky_number = st.text_input("Lucky number?", placeholder="e.g., 7")
    favorite_number = st.text_input("Favorite number (any)?", placeholder="e.g., 42")
    
    # Password options
    st.subheader("⚙️ Password Options")
    
    col1, col2 = st.columns(2)
    with col1:
        password_length = st.slider("Password Length", min_value=8, max_value=32, value=16)
    with col2:
        use_special_chars = st.checkbox("Add special characters (!@#$%)", value=True)
    
    separator = st.selectbox("Separator between words:", ["", ".", "_", "-", "#", "!"])
    
    # Generate from memory
    if st.button("🔐 Generate from Memory", type="primary"):
        answers = [favorite_color, favorite_food, favorite_movie, 
                   pet_name, best_friend, hometown, 
                   birth_year, lucky_number, favorite_number]
        
        # Filter out empty answers
        valid_answers = [a for a in answers if a.strip()]
        
        if not valid_answers:
            st.error("Please answer at least one question!")
        else:
            # Generate password from answers
            password_parts = []
            for answer in valid_answers:
                if answer:
                    # Take first 2 characters of each answer
                    cleaned = answer.strip().replace(" ", "")
                    if len(cleaned) >= 2:
                        password_parts.append(cleaned[:2].capitalize())
                    else:
                        password_parts.append(cleaned.capitalize())
            
            # Shuffle and combine
            random.shuffle(password_parts)
            password = separator.join(password_parts)
            
            # Pad or trim to desired length
            if len(password) < password_length:
                # Add random characters
                extra = password_length - len(password)
                extras = string.ascii_lowercase + string.digits
                password += separator + "".join(random.choices(extras, k=min(extra, 4)))
            elif len(password) > password_length:
                password = password[:password_length]
            
            # Add special chars if selected
            if use_special_chars and separator == "":
                special = "!@#$%^&*"
                password = random.choice(special) + password + random.choice(special)
            
            st.success("🎉 Your Memory Password:")
            st.code(password, language=None)
            
            # Strength indicator
            st.subheader("📊 Why this password works:")
            st.write(f"• Based on {len(valid_answers)} personal answers only you know")
            st.write("• Easy to remember - just recall your answers")
            st.write("• Hard for others to guess")
            
            st.download_button(
                label="📥 Download Password",
                data=password,
                file_name="memory_password.txt",
                mime="text/plain"
            )

with tab2:
    st.subheader("🎲 Quick Random Password")
    
    length = st.slider("Length", min_value=8, max_value=32, value=16)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        upper = st.checkbox("A-Z", value=True)
    with col2:
        lower = st.checkbox("a-z", value=True)
    with col3:
        nums = st.checkbox("0-9", value=True)
    with col4:
        special = st.checkbox("!@#$", value=True)
    
    if st.button("🎲 Generate Random"):
        chars = ""
        if upper: chars += string.ascii_uppercase
        if lower: chars += string.ascii_lowercase
        if nums: chars += string.digits
        if special: chars += "!@#$%^&*"
        
        if chars:
            pwd = "".join(random.choice(chars) for _ in range(length))
            st.success("🎲 Your Random Password:")
            st.code(pwd, language=None)
        else:
            st.error("Select at least one character type!")