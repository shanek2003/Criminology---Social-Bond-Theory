# criminology unpaper
# the quiz will ask users a few questions than will tell them whether they are likely to engage in criminal behavior
# this explains social bond theory

from tkinter import *
import tkinter as tk
from tkinter.ttk import Radiobutton
from tkinter import messagebox
import sqlite3

# creating a window
window = Tk()
window.title('QUIZ: Your likelihood to engage in criminal behavior - Social Bond Theory')
window.geometry('400x400')
window.resizable(True, True)

frame = Frame(window)
frame.pack()

messagebox.showinfo("!!!WARNING!!!",
                    "For the best viewing experience, maximize the quiz popup window before starting the quiz. :-)")

# attachment questions
label_q1 = Label(frame, text = "The next questions relate to your ATTACHMENTS")
label_q1.grid(row = 0, column = 0, columnspan = 2)
#question 1
label_q1 = Label(frame, text="Do you consider yourself introverted?")
label_q1.grid(row=1, column=0, columnspan=2)
q1Var = IntVar()
q1Var.set(1)
radio_no = Radiobutton(frame, text="No - I'm extroverted!", variable=q1Var, value=1)
radio_no.grid(row=2, column=0)
radio_yes = Radiobutton(frame, text="Yes", variable=q1Var, value=2)
radio_yes.grid(row=2, column=1)

# Question 2
label_q2 = Label(frame, text="Are you single, or do you have a significant other?")
label_q2.grid(row=3, column=0, columnspan=2)
q2Var = IntVar()
q2Var.set(1)
radio_single = Radiobutton(frame, text = "I'm single", variable =q2Var, value = 1)
radio_single.grid(row = 4, column = 0)
radio_married = Radiobutton(frame, text = "I'm in a relationship", variable =q2Var, value = 2)
radio_married.grid(row = 4, column = 1)

# Question 3
label_slider = Label(frame, text="Are you close with friends/Family, on a scale of 1-10?")
label_slider.grid(row=5, column=0, columnspan=2)

# Slider (numeric scale)
slider = tk.Scale(frame, from_=0, to=10, orient="horizontal")
slider.grid(row=6, column=0, columnspan=2)

# Question 4
label_q4 = Label(frame, text="Have you or your family ever been involved in criminal activity")
label_q4.grid(row=7, column=0, columnspan=2)
q4Var = IntVar()
q4Var.set(1)
radio_yes1 = Radiobutton(frame, text = "Yes", variable =q4Var, value = 1)
radio_yes1.grid(row = 8, column = 0)
radio_maybe = Radiobutton(frame, text = "Cant confirm nor deny", variable =q4Var, value = 3) # the quiz will assume that the answer is 'YES' if this is checked
radio_maybe.grid(row = 8, column =1)
radio_no1 = Radiobutton(frame, text = "NO", variable =q4Var, value = 2)
radio_no1.grid(row = 8, column = 2)

# Commitment
label_q5 = Label(frame, text="This section relates to COMMITMENTS")
label_q5.grid(row = 9, column = 0, columnspan = 2)
#q5
label_q5 = Label(frame, text="Have you ever thought about committing a serious crime? This does not include minor speed violations, parking violations, or jaywalking? Instead, think murder, assault, burglary, robbery, etc.")
label_q5.grid(row=10, column=0, columnspan=2)
q5Var = IntVar()
q5Var.set(1)
radio_no2 = Radiobutton(frame, text="No", variable=q5Var, value=1)
radio_no2.grid(row=11, column=0)
radio_yes2 = Radiobutton(frame, text="Yes", variable=q5Var, value=2)
radio_yes2.grid(row=11, column=1)

#Q6
label_q6 = Label(frame, text = "Are you currently employed")
label_q6.grid(row = 12, column = 0, columnspan = 2)
q6var = IntVar()
q6var.set(1)
radio_no3 = Radiobutton(frame, text = "NO", variable = q6var, value = 1)
radio_no3.grid(row = 13, column = 0)
radio_yes3  = Radiobutton(frame, text = "Yes", variable = q6var, value = 2)
radio_yes3.grid(row = 13, column = 1)

#Q7
label_q7 = Label(frame, text = "THIS NEXT SECTION PERTAINS TO INVOLVEMENT")
label_q7.grid(row = 14, column = 0, columnspan = 2)
label_q7 = Label(frame, text = "Are you employed full time or part time?")
label_q7.grid(row = 15, column = 0)
q7Var = IntVar()
q7Var.set(1)
radio_part = Radiobutton(frame, text = "Part-time", variable = q7Var, value = 1)
radio_part.grid(row = 16, column = 0)
radio_full = Radiobutton(frame, text = "Full-time", variable = q7Var, value = 2)
radio_full.grid(row = 16, column = 1)

#q8
label_slider1 = Label(frame, text="How much free time do you have per day (in hours)?")
label_slider1.grid(row=17, column=0, columnspan=2)
slider1 = tk.Scale(frame, from_=0, to=5, orient="horizontal")
slider1.grid(row=18, column=0, columnspan=2)


#q9
label_q8 = Label(frame, text = "Do you play sports?")
label_q8.grid(row = 19, column = 0, columnspan = 2)
q8Var = IntVar()
q8Var.set(1)
radio_part = Radiobutton(frame, text = "Yes", variable = q8Var, value = 1)
radio_part.grid(row = 20, column = 0)
radio_full = Radiobutton(frame, text = "No", variable = q8Var, value = 2)
radio_full.grid(row = 20, column = 1)

#BELIEF
label_qten = Label(frame, text = "THIS NEXT SECTION PERTAINS TO BELIEF. This is the final section.")
label_qten.grid(row = 21, column = 0, columnspan = 2)
label_qten = Label(frame, text = "Would you say that you are a rule-follower?")
label_qten.grid(row = 22, column = 0, columnspan = 2)
qtenVar = IntVar()
qtenVar.set(1)
radio_yes4 = Radiobutton(frame, text = "Yes", variable = qtenVar, value = 1)
radio_yes4.grid(row = 23, column = 0)
radio_no4 = Radiobutton(frame, text = "No", variable = qtenVar, value = 2)
radio_no4.grid(row = 23, column = 1)

result = Label(frame, text="")
result.grid(row=26, column=0)
# Save all results to a database
# Answers will form an output of likely a form an answer of ~70% likelihood, ~35% likelihood, ~20% likelihood, <20= = highly UNLIKELY
def submit():
    criminal = 0
    if q1Var.get() == 1:  # Yes selected
        criminal += 5
    if q2Var.get() == 1: #single
        criminal += 5
    if slider.get() <=4:
        criminal += 15
    if q4Var.get() == 1 or 3:
        criminal += 15
    if q5Var.get() == 2:
        criminal += 10
    if q6var.get() == 1:
        criminal += 15
    if q7Var.get() == 1:
        criminal += 5
    if slider1.get() >= 4:
        criminal += 15
    if q8Var.get() == 2:
        criminal += 5
    if qtenVar.get() == 2:
        criminal += 10
    if criminal > 100:
        criminal = 100
     #using an f string - use expressions in print statement

    result.config(text=f"Your likelihood of engaging in criminal/deviant activity is: {criminal}%")

    #SUBMIT THIS DATA TO A SQL DATABASE
    conn = sqlite3.connect('results.db')  # CREATE and/or open a DATABASE ; CRIMINOLOGY QUIZ RESULTS
    cursor = conn.cursor()
    # Creating a table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        q1 INTEGER,
        q2 INTEGER,
        closeness INTEGER,
        q4 INTEGER,
        q5 INTEGER, 
        q6 INTEGER,
        q7 INTEGER, 
        freetime INTEGER,
        q8 INTEGER,
        qten INTEGER,
        criminal INTEGER
    )
    """)

    insert_command = f"""
    INSERT INTO results (q1,
                         q2,
                         closeness,
                         q4,
                         q5,
                         q6,
                         q7,
                         freetime,
                         q8,
                         qten,
                         criminal)
    VALUES ({q1Var.get()}, {q2Var.get()}, {slider.get()}, {q4Var.get()}, {q5Var.get()},
                {q6var.get()}, {q7Var.get()}, {slider1.get()}, {q8Var.get()}, {qtenVar.get()}, {criminal})
    """
    cursor.execute(insert_command)
    conn.commit()
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
submit_btn = Button(frame, text="Submit", command=submit)
submit_btn.grid(row=25, column=0, columnspan=2)
window.mainloop()