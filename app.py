import streamlit as st
import sqlite3
# using streamlit to make the quiz be available online, rather than tkinter window via IDE
# creating a window
st.title("Criminology Quiz: Social Bond Theory")

st.info("For the best viewing experience, maximize the quiz popup window before starting the quiz. :-)")

# attachment questions
st.write("This section pertains to your ATTACHMENTS.")
label_q1 = st.radio("Do you consider yourself introverted?",
                    ["No - I'm extroverted", "Yes"])
# Question 2
label_q2 = st.radio("Are you single, or do you have a significant other?",
                    ["I'm single", "I'm in a relationship"])
# Question 3
label_slider = st.slider("Are you close with friends/Family, on a scale of 1-10?",
                         min_value=0, max_value=10, value=5)
# Question 4
label_q4 = st.radio ("Have you or your family ever been involved in criminal activity",
                    ["Yes", "Cant confirm nor deny", "NO"])
# Commitment
label_q5 = st.write("This section relates to COMMITMENTS")
label_q5 = st.radio("Have you ever thought about committing a serious crime? This does not include minor speed violations, parking violations, or jaywalking? Instead, think murder, assault, burglary, robbery, etc.",
                    ["NO", "Yes"])
#Q6
label_q6 = st.radio("Are you currently employed",
                    ["No", "Yes"])
#Q7
st.write("THIS NEXT SECTION PERTAINS TO INVOLVEMENT")
label_q7 = st.radio("Are you employed full time or part time?",
                    ["Full-time", "Part-time"])
#q8
label_slider1 = st.slider("How much free time do you have per day (in hours)?",
                          min_value=0, max_value=5, value=2)
#q9
label_q8 = st.radio("Do you play sports?",
                    ["Yes", "NO"])
#BELIEF
label_qten = st.write("THIS NEXT SECTION PERTAINS TO BELIEF. This is the final section.")
label_qten = st.radio("Would you say that you are a rule-follower?",
                      ["Yes", "No"])

# Save all results to a database
# Answers will form an output of likely a form an answer of ~70% likelihood, ~35% likelihood, ~20% likelihood, <20= = highly UNLIKELY
if st.button("Submit"):
    criminal = 0
    if label_q1 == "No - I'm extroverted!": criminal += 5
    if label_q2 == "I'm single": criminal += 5
    if label_slider <= 4: criminal += 15
    if label_q4 in ["Yes", "Can't confirm nor deny"]: criminal += 15
    if label_q5 == "Yes": criminal += 10
    if label_q6 == "No": criminal += 15
    if label_q7 == "Part-time": criminal += 5
    if label_slider1 >= 4: criminal += 15
    if label_q8 == "No": criminal += 5
    if label_qten == "No": criminal += 10
    if criminal > 100: criminal = 100

     #using an f string - use expressions in print statement

    st.info(f"Your likelihood of engaging in criminal/deviant activity is: {criminal}%")

    def escape_quotes(value):
        if isinstance(value, str):
            return value.replace("'", "''")
        return value

    q1_safe = escape_quotes(label_q1)
    q2_safe = escape_quotes(label_q2)
    q4_safe = escape_quotes(label_q4)
    q5_safe = escape_quotes(label_q5)
    q6_safe = escape_quotes(label_q6)
    q7_safe = escape_quotes(label_q7)
    q8_safe = escape_quotes(label_q8)
    qten_safe = escape_quotes(label_qten)



    #SUBMIT THIS DATA TO A SQL DATABASE
    conn = sqlite3.connect('results.db')  # CREATE and/or open a DATABASE ; CRIMINOLOGY QUIZ RESULTS
    cursor = conn.cursor()
    # Creating a table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        q1 TEXT,
        q2 TEXT,
        slider INTEGER,
        q4 TEXT,
        q5 TEXT, 
        q6 TEXT,
        q7 TEXT, 
        slider1 INTEGER,
        q8 TEXT,
        qten TEXT,
        criminal INTEGER
    )
    """)

    insert_command = f"""
    INSERT INTO results (q1,
                         q2,
                         slider,
                         q4,
                         q5,
                         q6,
                         q7,
                         slider1,
                         q8,
                         qten,
                         criminal)
    VALUES ('{label_q1}', '{label_q2}', '{label_slider}', '{label_q4}', '{label_q5}',
                '{label_q6}', '{label_q7}', '{label_slider1}', '{label_q8}', '{label_qten}', '{criminal}')
    """
    cursor.execute(insert_command)
    conn.commit()

    conn.close()
