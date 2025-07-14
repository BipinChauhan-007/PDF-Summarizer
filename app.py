import streamlit as st
from backend import utils, summarizer, qa_engine, challenge_engine

st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("📚 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    doc_text = utils.extract_text(uploaded_file)

    st.subheader("📌 Auto Summary")
    summary = summarizer.summarize_text(doc_text)
    st.success(summary)

    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    # ✅ Mode 1: Ask Anything
    if mode == "Ask Anything":
        question = st.text_input("💬 Ask your question:")
        if question:
            answer, ref = qa_engine.answer_question(doc_text, question)
            st.info(f"**Answer:** {answer}")
            st.caption(ref)

    # ✅ Mode 2: Challenge Me
    elif mode == "Challenge Me":
        raw_output = challenge_engine.generate_questions(doc_text)
        questions = challenge_engine.parse_questions(raw_output)

        st.subheader("🧠 Answer These Questions:")

        user_answers = {}
        score = 0

        for idx, q in enumerate(questions):
            st.markdown(f"**Q{idx+1}. {q['question']}**")

            # ✅ Show full options with text
            choice = st.radio(
                label="Choose your answer:",
                options=[
                    f"A) {q['options']['A']}",
                    f"B) {q['options']['B']}",
                    f"C) {q['options']['C']}",
                    f"D) {q['options']['D']}",
                ],
                key=f"question_{idx}"
            )

            selected_letter = choice[0]  # "A", "B", etc.
            user_answers[f"Q{idx+1}"] = {
                "chosen": selected_letter,
                "correct": q["answer"]
            }

            st.markdown("---")

        if st.button("✅ Submit Answers"):
            st.subheader("📊 Your Results:")
            for qid, result in user_answers.items():
                correct = result["correct"]
                chosen = result["chosen"]
                if chosen == correct:
                    st.success(f"{qid}: ✅ Correct (Answer: {correct})")
                    score += 1
                else:
                    st.error(f"{qid}: ❌ Incorrect (Your Answer: {chosen}, Correct: {correct})")

            st.markdown(f"### 🏁 Final Score: **{score} / {len(questions)}**")
