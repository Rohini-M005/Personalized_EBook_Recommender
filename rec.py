import streamlit as st
from langchain_groq import ChatGroq # Ensure you replace this with the actual library for ChatGroq

def get_book_recommendations(prompt):
    """Generate e-book recommendations using the ChatGroq model."""
    llm = ChatGroq(
        temperature=0.7,  # Adjust as needed
        groq_api_key='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',
        model_name="llama-3.1-8b-instant"
    )
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("Personalized E-Book Recommender")
    st.write("Discover e-books tailored to your preferences! Just specify your favorite genre or author.")

    # Input fields for user preferences
    preference_type = st.radio("Would you like to provide a favorite author or genre?", ("Author", "Genre"))
    if preference_type == "Author":
        favorite_author = st.text_input("Who is your favorite author?")
        favorite_genre = ""
    else:
        favorite_genre = st.text_input("What is your favorite genre?")
        favorite_author = ""

    # Generate recommendations button
    if st.button("Get Recommendations"):
        if favorite_author or favorite_genre:
            st.info("Fetching recommendations...")

            # Create the recommendation prompt
            prompt = (f"I enjoy reading books by {favorite_author} {('and in the ' + favorite_genre + ' genre') if favorite_genre else ''}. "
                      "Recommend 5 e-books that match these preferences, and provide a brief description "
                      "of each book, including its main theme and why it aligns with my interests.")

            # Get recommendations
            recommendations = get_book_recommendations(prompt)

            st.header("Your Personalized Recommendations")
            st.write(recommendations)
        else:
            st.error("Please provide a favorite author or genre to get recommendations.")

if __name__ == "__main__":
    main()
