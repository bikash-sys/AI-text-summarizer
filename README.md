# AI-text-summarizer


## 🧠 AI Text Summarizer

A lightweight and efficient tool that uses AI to generate concise summaries of large text passages. Ideal for quickly understanding long articles, reports, or any body of text.

---

### 🚀 Features

- 📝 Summarizes long paragraphs into a few lines
- 🎯 Extractive and/or abstractive summarization
- 💬 Option for voice-based output (with `pyttsx3`)
- 📄 Supports plain text or clipboard input
- 🧠 Powered by HuggingFace Transformers or GPT-based models (optional)
- 🧪 Easy to integrate into JARVIS-style assistants

---

### 🔧 Requirements

Make sure Python 3.8+ is installed.

Install the required packages:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```txt
transformers
torch
pyttsx3
speechrecognition
pyaudio
```

---

### 🛠️ Usage

#### 1. 📄 Summarize a paragraph

```python
from transformers import pipeline

summarizer = pipeline("summarization")

text = """
The field of Artificial Intelligence has made tremendous progress in the last decade...
""" 

summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
print(summary[0]['summary_text'])
```

#### 2. 🔊 Add text-to-speech

```python
import pyttsx3

engine = pyttsx3.init()
engine.say(summary[0]['summary_text'])
engine.runAndWait()
```

---

### 🎙️ Voice Control (Optional)

Integrate with `speech_recognition` and `pyttsx3` to allow voice-controlled summarization.

---

### 📦 Example Integration (JARVIS)

In your assistant’s command handling:

```python
elif 'summarize' in self.query:
    speak("Please paste or speak the text you want summarized.")
    # Use summarizer pipeline here
    # Then read back the summary using speak()
```

---

### 💡 To-Do

- [ ] Add GUI using PyQt5 or Tkinter
- [ ] Summarize from PDF or DOCX files
- [ ] Add language selection

---

### 🧑‍💻 Author

Developed with ❤️ by bikash-sys

