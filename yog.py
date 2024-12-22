import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Quiz 2024")
        self.root.geometry("900x700")
        
        # Configure style with modern dark theme
        self.root.configure(bg='#1e293b')
        self.style = ttk.Style()
        self.style.configure('Quiz.TFrame', background='#1e293b')
        self.style.configure('Question.TLabel', 
                           background='#1e293b',
                           foreground='white',
                           font=('Arial', 12, 'bold'),
                           wraplength=800)

        # All 34 questions
        self.questions = [
            {
                "question": "1. In Linux, all programs are executed as:",
                "options": ["process", "data", "information", "all of these"],
                "correct": 0
            },
            {
                "question": "2. Each process when started has a unique number associated with it known as:",
                "options": ["memory id", "process id (PID)", "hard disk id", "all of these"],
                "correct": 1
            },
            {
                "question": "3. Which command is used to see the processes associated with the current shell without any parameters?",
                "options": ["ps", "ls", "id", "sp"],
                "correct": 0
            },
            {
                "question": "4. Which command is used to view the process of all the users?",
                "options": ["ps -ef", "ps -lf", "ps -er", "ps -er"],
                "correct": 0
            },
            {
                "question": "5. Which column name shows name or number of the user who owns the process?",
                "options": ["UID", "PID", "PPID", "STIME"],
                "correct": 0
            },
            {
                "question": "6. Which column name identifies the parent process id?",
                "options": ["UID", "PID", "PPID", "STIME"],
                "correct": 2
            },
            {
                "question": "7. Which column name identifies the terminal that controls the current process?",
                "options": ["TTY", "TIME", "CMD", "STIME"],
                "correct": 0
            },
            {
                "question": "8. Which column name identifies command used to invoke the process?",
                "options": ["TTY", "TIME", "CMD", "STIME"],
                "correct": 2
            },
            {
                "question": "9. To remove the process from memory we use the command:",
                "options": ["kill", "remove", "delete", "all of these"],
                "correct": 0
            },
            {
                "question": "10. In Linux, arguments from $1 to $9 are known as:",
                "options": ["command line command", "command line variable", "command line parameter", "command line arguments"],
                "correct": 3
            },
            {
                "question": "11. Which construct in shell scripts allows to perform decision making?",
                "options": ["loop", "if-then-fi", "while", "for"],
                "correct": 1
            },
            {
                "question": "12. What indicates whether the command was successfully executed or not?",
                "options": ["Exit status", "Entry status", "Both (a) and (b)", "None"],
                "correct": 0
            },
            {
                "question": "13. The exit status of command is _____ if it has been executed successfully:",
                "options": ["1", "0", "3", "4"],
                "correct": 1
            },
            {
                "question": "14. In if statement which bracket is used for opening and closing statement?",
                "options": ["* *", "[ ]", "( )", "{}"],
                "correct": 1
            },
            {
                "question": "15. Which decision making instructions does Linux offer?",
                "options": ["if-then-fi", "if-then-else-fi", "if-then-elif-else-fi & case-esac", "All of these"],
                "correct": 3
            },
            {
                "question": "16. Which command will be used to compare two files passed to it as argument?",
                "options": ["com", "cmp", "cam", "comp"],
                "correct": 1
            },
            {
                "question": "17. Linux provides which command that can be used in place of square brackets?",
                "options": ["if", "test", "then", "else"],
                "correct": 1
            },
            {
                "question": "18. Which operator can be used for numerical test for greater than?",
                "options": ["-gt", "-lt", "-ge", "-le"],
                "correct": 0
            },
            {
                "question": "19. Which operator can be used for numerical test 'less than or equal to'?",
                "options": ["-la", "-lq", "-el", "-le"],
                "correct": 3
            },
            {
                "question": "20. Which operator can be used for numerical test 'equal to'?",
                "options": ["-e", "-eq", "-ea", "-et"],
                "correct": 1
            },
            {
                "question": "21. How many relational operators are used to compare two numeric operands?",
                "options": ["4", "6", "3", "4"],
                "correct": 1
            },
            {
                "question": "22. To combine conditions, we make use of which operators?",
                "options": ["relational", "file", "logical", "all of these"],
                "correct": 2
            },
            {
                "question": "23. Shell script allows usage of how many logical operators while testing a condition?",
                "options": ["two", "three", "four", "five"],
                "correct": 1
            },
            {
                "question": "24. Which logical operator allows in shell script for testing a condition?",
                "options": ["-a (AND)", "-o (OR)", "! (NOT)", "All of these"],
                "correct": 3
            },
            {
                "question": "25. Which operator allows two or more conditions to be combined in a test?",
                "options": ["-a", "-o", "Both (a) and (b)", "none of these"],
                "correct": 2
            },
            {
                "question": "26. Which logical operator is used to convert true result to false and vice versa?",
                "options": ["AND", "NOT", "OR", "None of these"],
                "correct": 1
            },
            {
                "question": "27. Which operator is used to check the status of a file?",
                "options": ["relational", "file", "logical", "all of these"],
                "correct": 1
            },
            {
                "question": "28. Which condition returns True if a file exists and is not a directory?",
                "options": ["-s name", "-f name", "-d name", "-r name"],
                "correct": 1
            },
            {
                "question": "29. Which condition returns True if a file exists and has write permission?",
                "options": ["-w name", "-x name", "-d name", "-r name"],
                "correct": 0
            },
            {
                "question": "30. The alternate option for checking if-then-elif-then-else-fi conditions is to use:",
                "options": ["for", "case", "while", "None"],
                "correct": 1
            },
            {
                "question": "31. Which keyword is used to specify the end of case statement?",
                "options": ["esac", "easc", "case", "None"],
                "correct": 0
            },
            {
                "question": "32. Cleaning of disk space is a normal operation that the ___ needs to perform:",
                "options": ["user", "group", "administrator", "All"],
                "correct": 2
            },
            {
                "question": "33. Which of the following are used to perform repetitive action?",
                "options": ["for statements", "while statements", "until statements", "All of these"],
                "correct": 3
            },
            {
                "question": "34. Which of the following allows us to specify a list of values in its statement?",
                "options": ["for loop", "while loop", "until loop", "do while loop"],
                "correct": 0
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        # Create main container
        self.main_container = ttk.Frame(root, padding="20", style='Quiz.TFrame')
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            self.main_container,
            variable=self.progress_var,
            maximum=len(self.questions),
            length=800,
            mode='determinate'
        )
        self.progress_bar.pack(pady=(0, 20))
        
        # Score and question counter
        self.info_frame = ttk.Frame(self.main_container, style='Quiz.TFrame')
        self.info_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.score_label = ttk.Label(
            self.info_frame,
            text=f"Score: {self.score}/{len(self.questions)}",
            foreground='#4ade80',
            background='#1e293b',
            font=('Arial', 12, 'bold')
        )
        self.score_label.pack(side=tk.LEFT)
        
        self.question_num_label = ttk.Label(
            self.info_frame,
            text=f"Question {self.current_question + 1}/{len(self.questions)}",
            foreground='#60a5fa',
            background='#1e293b',
            font=('Arial', 12, 'bold')
        )
        self.question_num_label.pack(side=tk.RIGHT)
        
        # Question text
        self.question_label = ttk.Label(
            self.main_container,
            text="",
            style='Question.TLabel',
            wraplength=800
        )
        self.question_label.pack(pady=20)
        
        # Options
        self.options_frame = ttk.Frame(self.main_container, style='Quiz.TFrame')
        self.options_frame.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.options_frame,
                text="",
                width=60,
                height=2,
                font=('Arial', 11),
                bg='#334155',
                fg='white',
                activebackground='#1e40af',
                activeforeground='white',
                bd=0,
                cursor='hand2'
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        # Next button
        self.next_button = tk.Button(
            self.main_container,
            text="Next Question →",
            command=self.next_question,
            bg='#059669',
            fg='white',
            font=('Arial', 12, 'bold'),
            bd=0,
            pady=10,
            padx=20,
            cursor='hand2'
        )
        self.next_button.pack(pady=20)
        
        # Timer
        self.time_left = 30
        self.timer_label = ttk.Label(
            self.main_container,
            text=f"Time Left: {self.time_left}s",
            foreground='#94a3b8',
            background='#1e293b',
            font=('Arial', 10)
        )
        self.timer_label.pack()
        
        # Start quiz
        self.load_question()
        self.update_timer()
    
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.next_question()
    
    def load_question(self):
        self.time_left = 30
        self.progress_var.set(self.current_question)
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])
        
        self.question_num_label.config(
            text=f"Question {self.current_question + 1}/{len(self.questions)}"
        )
        
        for i, option in enumerate(question["options"]):
            self.option_buttons[i].config(
                text=option,
                command=lambda x=i: self.check_answer(x),
                state=tk.NORMAL,
                bg='#334155'
            )
    
    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct"]
        
        for i, btn in enumerate(self.option_buttons):
            if i == correct_answer:
                btn.config(bg='#059669')
            elif i == selected_option and i != correct_answer:
                btn.config(bg='#dc2626')
        
        if selected_option == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")
        
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)
    
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_results()
    
    def show_results(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()
        
        percentage = (self.score / len(self.questions)) * 100
        
        result_label = ttk.Label(
            self.main_container,
            text="Quiz Complete!",
            font=('Arial', 24, 'bold'),
            foreground='#4ade80',
            background='#1e293b'
        )
        result_label.pack(pady=30)
        
        score_label = ttk.Label(
            self.main_container,
            text=f"Final Score: {self.score}/{len(self.questions)}",
            font=('Arial', 18, 'bold'),
            foreground='white',
            background='#1e293b'
        )
        score_label.pack(pady=10)
        
        percentage_label = ttk.Label(
            self.main_container,
            text=f"Percentage: {percentage:.1f}%",
            font=('Arial', 18),
            foreground='white',
            background='#1e293b'
        )
        percentage_label.pack(pady=10)
        
        grade = self.get_grade(percentage)
        grade_label = ttk.Label(
            self.main_container,
            text=f"Grade: {grade}",
            font=('Arial', 18, 'bold'),
            foreground=self.get_grade_color(grade),
            background='#1e293b'
        )
        grade_label.pack(pady=20)
        
        restart_button = tk.Button(
            self.main_container,
            text="Restart Quiz",
            command=self.restart_quiz,
            bg='#059669',
            fg='white',
            font=('Arial', 12, 'bold'),
            bd=0,
            pady=10,
            padx=20,
            cursor='hand2'
        )
        restart_button.pack(pady=30)
    
    def get_grade(self, percentage):
        if percentage >= 90: return 'A+'
        elif percentage >= 80: return 'A'
        elif percentage >= 70: return 'B'
        elif percentage >= 60: return 'C'
        elif percentage >= 50: return 'D'
        else: return 'F'
    
    def get_grade_color(self, grade):
        colors = {
            'A+': '#059669',
            'A': '#10b981',
            'B': '#60a5fa',
            'C': '#f59e0b',
            'D': '#f97316',
            'F': '#dc2626'
        }
        return colors.get(grade, '#ffffff')
    
    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        for widget in self.main_container.winfo_children():
            widget.destroy()
        self.__init__(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
