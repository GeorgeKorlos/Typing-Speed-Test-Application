import tkinter as tk
import time

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.start_time = 0
        
        self.label = tk.Label(root, text="Sample Text:")
        self.label.pack()

        self.sample_label = tk.Label(root, text=self.sample_text, wraplength=400, justify="center")
        self.sample_label.pack()

        self.typing_area = tk.Text(root, height=5, width=50)
        self.typing_area.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.calculate_wpm)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def start_test(self):
        """ Start the typing test and track time """
        self.typing_area.delete(1.0, tk.END) 
        self.start_time = time.time()  
        self.result_label.config(text="") 
        self.typing_area.focus_set()  
    def calculate_wpm(self):
        """ Calculate words per minute based on typing speed """
        end_time = time.time()
        typed_text = self.typing_area.get(1.0, tk.END).strip()  

        time_taken = end_time - self.start_time
        minutes_taken = time_taken / 60  

        words_typed = len(typed_text.split())
        
        if minutes_taken > 0:
            wpm = words_typed / minutes_taken
        else:
            wpm = 0

        self.result_label.config(text=f"Words Per Minute: {int(wpm)}")

root = tk.Tk()
app = TypingSpeedApp(root)
root.mainloop()
