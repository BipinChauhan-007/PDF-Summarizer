
# 📚 PDF Summarizer – GenAI Smart Assistant

A GenAI-powered document-aware assistant that reads PDF or TXT documents and performs contextual summarization, deep comprehension, and logic-based questioning.

---

## 🚀 Features

✅ Upload and analyze PDF/TXT documents  
✅ Generate a <150-word summary instantly  
✅ Ask free-form, context-grounded questions  
✅ "Challenge Me" mode: test your understanding with AI-generated logic questions  
✅ Justified answers with document-backed references  
✅ Clean, responsive Streamlit interface

---

## 🎯 Objective

This project was developed as part of a GenAI internship task to demonstrate the ability to build intelligent assistants that go beyond keyword search and can reason contextually with documents.

---

## 🧠 Modes of Interaction

### 1. 📥 Document Upload  
Upload a `.pdf` or `.txt` file. The assistant auto-generates a brief summary (≤ 150 words).

### 2. ❓ Ask Anything  
Ask any question related to the uploaded document. The assistant will respond with document-supported, inference-based answers.

### 3. 🧩 Challenge Me  
Generates 3 logical/comprehension questions from the document. You respond, and the assistant evaluates and justifies each response.

---

## 🧱 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **LLM API**: OpenAI GPT (via `openai` Python SDK)  
- **Document Parsing**: PyPDF2 / pdfminer / langchain loaders  
- **Vector Store**: FAISS  
- **Embeddings**: OpenAI

---

## 🏗️ Architecture

```text
User Uploads PDF/TXT
        ↓
    Text Extractor
        ↓
  ➤ Auto Summary (<150 words)
  ➤ Vector Embedding via OpenAI
        ↓
   Document Indexing (FAISS)
        ↓
➤ Ask Anything        ➤ Challenge Me
     ↓                      ↓
Query to LLM         Generate & Grade Logic Qs
     ↓                      ↓
Answer + Justification  Feedback + Scoring
```

---

## ⚙️ Setup Instructions

### 🖥️ Local Development

1. **Clone this repo**:
   ```bash
   git clone https://github.com/BipinChauhan-007/PDF-Summarizer.git
   cd PDF-Summarizer
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key**  
   Create a `.env` file with:
   ```
   OPENAI_API_KEY=your-key-here
   ```

5. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Streamlit Deployment

Deployed on **Streamlit Community Cloud**  
🔗 [Live App URL](https://pdf-summarizer-001.streamlit.app/)

---

## ✨ Bonus Features (Optional Goals)

- [x] Snippet-based justifications
- [x] Multi-mode interaction
- [ ] Memory / context retention (future enhancement)
- [ ] Answer highlighting in document (planned)

---

## 📁 Folder Structure

```text
PDF-Summarizer/
│
├── app.py                  # Main Streamlit app
├── utils.py                # Helper functions
├── qa_logic.py             # Ask Anything logic
├── challenge_mode.py       # Logic question generator
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ✅ Evaluation Criteria Alignment

| Criteria                             | Implemented |
|--------------------------------------|-------------|
| Response Quality + Justification     | ✅ Yes      |
| Reasoning + Evaluation Mode          | ✅ Yes      |
| UI/UX Experience                     | ✅ Yes      |
| Code Structure & Documentation       | ✅ Yes      |
| Creativity / Bonus Features          | ⚠️ Partial  |
| Minimal Hallucination & Context Use  | ✅ Yes      |

---

## 🧑‍💻 Author

**Bipin Bihari Chauhan**  
📧 bipinbiharichauhan67@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/bipinchauhan-007)  
🔗 [GitHub](https://github.com/BipinChauhan-007)

---

## 📃 License

MIT License — use freely with attribution.
