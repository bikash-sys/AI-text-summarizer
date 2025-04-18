import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Load the summarization model (once, to avoid delay on button click)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to summarize input text
def summarize_text():
    input_text = input_box.get("1.0", tk.END).strip()
    if input_text:
        try:
            summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, summary[0]['summary_text'])
        except Exception as e:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, f"Error: {str(e)}")

# GUI setup
window = tk.Tk()
window.title("AI Text Summarizer for Students")
window.geometry("800x600")

# Input label and text area
input_label = tk.Label(window, text="Paste your text here:", font=("Arial", 14))
input_label.pack(pady=10)

input_box = scrolledtext.ScrolledText(window, height=10, font=("Arial", 12))
input_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Summarize button
summarize_button = tk.Button(window, text="Summarize", font=("Arial", 14), command=summarize_text)
summarize_button.pack(pady=10)

# Output label and text area
output_label = tk.Label(window, text="Summary:", font=("Arial", 14))
output_label.pack(pady=10)

output_box = scrolledtext.ScrolledText(window, height=10, font=("Arial", 12))
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Run the application
window.mainloop()
