from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=300,
                                                     text="some question text", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="score: ", bg=THEME_COLOR, fg="White")
        self.score_label.grid(row=0, column=1)

        x_img = PhotoImage(file="images/false.png")
        y_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=x_img, highlightthickness=0, command=self.check_if_true)
        self.right_button.grid(row=2, column=0)
        self.false_button = Button(image=y_img, highlightthickness=0, command=self.check_if_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.score_label.config(text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_if_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_if_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
