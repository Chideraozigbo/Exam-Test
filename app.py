import streamlit as st
import random
from streamlit_lottie import st_lottie
import requests

# Set page config
st.set_page_config(page_title="SS3 Advanced Practice Quiz", layout="wide")

# Quiz questions
math_questions = [
    {
        "question": "If log₂(x) = 3 and log₂(y) = 4, what is the value of log₂(xy)?",
        "options": ["7", "12", "5", "Cannot be determined"],
        "correct": "7"
    },
    {
        "question": "In an arithmetic sequence, a₁ = 5 and d = 3. What is the sum of the first 20 terms?",
        "options": ["590", "600", "610", "620"],
        "correct": "610"
    },
    {
        "question": "Solve the equation: 2sin²x - 3sinx + 1 = 0 for 0° ≤ x ≤ 360°",
        "options": ["30° and 90°", "30° and 150°", "45° and 135°", "60° and 120°"],
        "correct": "30° and 90°"
    },
    {
        "question": "What is the probability of getting a sum of 8 when rolling two fair dice?",
        "options": ["5/36", "1/8", "1/6", "7/36"],
        "correct": "5/36"
    },
    {
        "question": "If f(x) = x² - 4x + 4 and g(x) = 2x - 2, find f(g(3)).",
        "options": ["16", "4", "8", "12"],
        "correct": "16"
    },
    {
        "question": "What is the area between the curves y = x² and y = 4 - x² in the first quadrant?",
        "options": ["16/3 square units", "8/3 square units", "4 square units", "32/3 square units"],
        "correct": "16/3 square units"
    },
    {
        "question": "If the sum of the interior angles of a polygon is 1080°, how many sides does it have?",
        "options": ["6", "8", "10", "12"],
        "correct": "8"
    },
    {
        "question": "What is the period of the function f(x) = 3sin(2x) + cos(2x)?",
        "options": ["π", "2π", "π/2", "π/4"],
        "correct": "π"
    },
    {
        "question": "In a geometric sequence, a₁ = 3 and r = 2. What is the sum of the first 6 terms?",
        "options": ["189", "192", "186", "183"],
        "correct": "189"
    },
    {
        "question": "Find the volume of a sphere inscribed in a cube of side length 6 units.",
        "options": ["36π units³", "24π units³", "72π units³", "18π units³"],
        "correct": "36π units³"
    }
]

english_questions = [
    {
        "question": "Which rhetorical device is exemplified in the phrase 'Ask not what your country can do for you – ask what you can do for your country'?",
        "options": ["Anaphora", "Chiasmus", "Epistrophe", "Anadiplosis"],
        "correct": "Chiasmus"
    },
    {
        "question": "In the sentence 'The painting, which was created in the 15th century, is a masterpiece of the Renaissance period,' what type of clause is 'which was created in the 15th century'?",
        "options": ["Relative non-defining clause", "Relative defining clause", "Noun clause", "Adverbial clause"],
        "correct": "Relative non-defining clause"
    },
    {
        "question": "What figure of speech is used in the phrase 'The pen is mightier than the sword'?",
        "options": ["Metaphor", "Simile", "Synecdoche", "Metonymy"],
        "correct": "Metonymy"
    },
    {
        "question": "Identify the mood in the sentence: 'If I were you, I would reconsider your decision.'",
        "options": ["Indicative", "Imperative", "Subjunctive", "Interrogative"],
        "correct": "Subjunctive"
    },
    {
        "question": "Which of these is an example of a portmanteau word?",
        "options": ["Oversee", "Brunch", "Undertake", "Understand"],
        "correct": "Brunch"
    },
    {
        "question": "In the sentence 'Despite the rain, they continued their journey,' what type of grammatical construction is 'Despite the rain'?",
        "options": ["Participial phrase", "Prepositional phrase", "Absolute phrase", "Infinitive phrase"],
        "correct": "Prepositional phrase"
    },
    {
        "question": "What literary term describes a seemingly contradictory statement that may nonetheless be true?",
        "options": ["Oxymoron", "Paradox", "Antithesis", "Hyperbole"],
        "correct": "Paradox"
    },
    {
        "question": "Which word formation process is illustrated in the term 'UNESCO'?",
        "options": ["Blending", "Clipping", "Acronym", "Back-formation"],
        "correct": "Acronym"
    },
    {
        "question": "In the phrase 'crystal clear water,' what type of adjective is 'crystal'?",
        "options": ["Proper adjective", "Compound adjective", "Attributive noun", "Participial adjective"],
        "correct": "Attributive noun"
    },
    {
        "question": "Which linguistic feature is demonstrated in the sentence 'The silence was deafening'?",
        "options": ["Hyperbole", "Litotes", "Oxymoron", "Euphemism"],
        "correct": "Oxymoron"
    }
]

# Load animation from URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    if 'start_quiz' not in st.session_state:
        st.session_state.start_quiz = False
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'math_answers' not in st.session_state:
        st.session_state.math_answers = {}
    if 'english_answers' not in st.session_state:
        st.session_state.english_answers = {}

    st.title("SS3 Advanced Practice Quiz")

    if not st.session_state.start_quiz:
        st.write("Welcome to the Advanced SS3 Quiz")
        st.write("Please enter your details to begin.")
        
        name = st.text_input("Enter your full name:")
        class_option = st.selectbox("Select your class:", ["", "SS3A", "SS3B", "SS3C"])
        
        if st.button("Start Quiz", disabled=not (name and class_option)):
            st.session_state.name = name
            st.session_state.class_option = class_option
            st.session_state.start_quiz = True
            st.experimental_rerun()

    elif not st.session_state.submitted:
        st.write(f"Welcome, {st.session_state.name} from {st.session_state.class_option}!")
        
        math_tab, english_tab = st.tabs(["Mathematics Section", "English Section"])

        with math_tab:
            st.header("Mathematics Section")
            for i, q in enumerate(math_questions):
                st.write(f"Question {i+1}: {q['question']}")
                st.session_state.math_answers[i] = st.radio(
                    f"Select your answer for Math Q{i+1}:",
                    [""] + q['options'],
                    key=f"math_{i}"
                )
                st.write("---")

        with english_tab:
            st.header("English Section")
            for i, q in enumerate(english_questions):
                st.write(f"Question {i+1}: {q['question']}")
                st.session_state.english_answers[i] = st.radio(
                    f"Select your answer for English Q{i+1}:",
                    [""] + q['options'],
                    key=f"eng_{i}"
                )
                st.write("---")

        if st.button("Submit Quiz"):
            st.session_state.submitted = True
            st.experimental_rerun()

    else:  # Results display
        math_score = sum([1 for i, q in enumerate(math_questions) 
                         if st.session_state.math_answers.get(i, "") == q['correct']])
        english_score = sum([1 for i, q in enumerate(english_questions) 
                            if st.session_state.english_answers.get(i, "") == q['correct']])
        total_score = math_score + english_score
        
        if total_score >= 15:
            lottie_url = "https://assets5.lottiefiles.com/packages/lf20_rc6CDU.json"
            lottie_celebration = load_lottie_url(lottie_url)
            st_lottie(lottie_celebration, height=200, key="celebration")
            st.balloons()
            st.write("🎉 Congratulations 🎉")
        elif total_score >= 10:
            st.write("😊 Well done. Keep practicing.")
        else:
            st.write("😐 You can do better. Keep studying and try again.")
        
        st.write(f"Your total score: {total_score}/20")
        st.write(f"Math score: {math_score}/10")
        st.write(f"English score: {english_score}/10")

        if st.button("Restart Quiz"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.experimental_rerun()

if __name__ == "__main__":
    main()
