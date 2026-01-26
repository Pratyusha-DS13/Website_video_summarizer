

---

# 🦜 LangChain Summarizer (YouTube & Website)

This project is a **Streamlit app** that summarizes content from **YouTube videos** or **websites** using **LangChain** and **Groq LLMs**.

---

## 🚀 Features

* Summarize **YouTube videos** (using transcripts).
* Summarize **webpage content** from any URL.
* Uses **Groq’s LLaMA-4 Maverick model** for fast, high-quality summaries.
* Generates concise summaries (~300 words).
* Simple **Streamlit UI**.

---

## 📂 Project Structure

```
.
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies (see below)
└── README.md           # Project documentation
```

---

## 🛠️ Installation

1. Clone this repo or download the code:

   ```bash
   git clone https://github.com/yourusername/langchain-summarizer.git
   cd langchain-summarizer
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Dependencies

Add these to `requirements.txt`:

```txt
streamlit
validators
langchain
langchain-community
langchain-groq
pytubefix
langdetect
unstructured
```

---

## 🔑 Configuration

* You’ll need a **Groq API Key**.
  Get it from: [Groq Console](https://console.groq.com/)

In the app, enter your API key in the **sidebar input box**.

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Steps:

1. Enter your **Groq API key** in the sidebar.
2. Paste a **YouTube video URL** or a **website URL**.
3. Click **Summarize**.
4. Wait for the AI-generated summary 🎉

---

## ⚠️ Notes

* If a YouTube video has no transcript, a message will be shown.
* Some websites may block scraping; in that case, try another URL.
* Summaries are limited to around **300 words**.

---

## 📌 Example

**Input:**
👉 URL: [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

**Output:**
✔ A 300-word AI-generated summary of the video’s transcript.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

APACHE License. 

---

