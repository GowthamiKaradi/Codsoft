import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("350x350")
        
        self.questions = [
            
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
                'correct_answer': 'Mars'
            },
            {
                'question': 'What is the largest mammal?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
                'correct_answer': 'Blue Whale'
            },
            {
                'question': 'Which is the tallest building on the earth?',
                'options': ['Burj Khalifa', 'Shanghai Tower', 'Merdeka ', 'Lottery world tower'],
                'correct_answer': 'Burj Khalifa'
            },
            {
                'question': 'Which is the largest country by area ?',
                'options': ['Canada', 'Russia', 'China', ' India'],
                'correct_answer': 'Russia'
            },
            {
                'question': 'Who invented the Light bulb ?',
                'options': ['Michael Faraday ', 'Charles Babbage ', 'Thomas Alva Edison', ' Galileo'],
                'correct_answer': 'Thomas Alva Edison'
            },
            {
                'question': 'Who discovered zero ?',
                'options': ['Aryabhatta', 'Vedavyas', 'Maharishi panini', ' None of these'],
                'correct_answer': 'Aryabhatta'
            },
            {
                'question': 'Which is the largest living animal in the world ?',
                'options': ['Elephant ', 'Giraffe ', 'Blue whale', ' Rhinoceros'],
                'correct_answer': 'Blue whale'
            },
            {
                'question': 'Who is called the iron man of India?',
                'options': ['Dr.Rajendra prasad', 'Sardar vallabhai Patel', ' Mahatma Gandhi', ' Pandit Jawaharlal Nehru'],
                'correct_answer': 'Sardar vallabhai Patel'
            },
            {
                'question': 'Who is known as father of mathematics?',
                'options': [' Aryabhatta', 'Archimedes', 'Ramanujan', ' Baudhayana'],
                'correct_answer': 'Archimedes'
            },
             {
                'question': 'Which year did india celebrate its first Republic day?',
                'options': ['1947', '1949', '1950', ' 1948'],
                'correct_answer': '1950'
            },
            {
                'question': 'What is the largest organ in human body?',
                'options': [' Stomach ', 'Brain', 'Brain', 'Skin'],
                'correct_answer': 'Skin'
            },

        ]
        
        self.score = 0
        self.current_question = 0
        
        self.question_label = tk.Label(root, text="", padx=10, pady=10)
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", padx=10, pady=5, command=lambda i=i: self.select_option(i))
            button.pack()
            self.option_buttons.append(button)
        
        self.next_button = tk.Button(root, text="Next Question", padx=10, pady=5, command=self.next_question)
        self.next_button.pack()
        
        self.score_label = tk.Label(root, text="", padx=10, pady=10)
        self.score_label.pack()
        
        self.display_question()
    
    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data['question'])
            options = question_data['options']
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            self.next_button.config(state=tk.DISABLED)
        else:
            self.question_label.config(text="Quiz completed!")
            self.next_button.config(state=tk.DISABLED)
            self.score_label.config(text="Total Score: {}/{}".format(self.score, len(self.questions)))
    
    def select_option(self, option_index):
        question_data = self.questions[self.current_question]
        selected_option = question_data['options'][option_index]
        correct_option = question_data['correct_answer']
        
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        
        if selected_option == correct_option:
            self.score += 1
            self.option_buttons[option_index].config(bg='light green')
        else:
            self.option_buttons[option_index].config(bg='red')
            correct_index = question_data['options'].index(correct_option)
            self.option_buttons[correct_index].config(bg='light green')
        
        self.next_button.config(state=tk.NORMAL)
        
    def next_question(self):
        self.current_question += 1
        self.display_question()
        for button in self.option_buttons:
            button.config(state=tk.NORMAL, bg='SystemButtonFace')

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
