import streamlit as st
from gramformer import Gramformer

# Load the Gramformer model
gf = Gramformer(models=1, use_gpu=False)

def correct_grammar(input_text):
    # Split the input text into sentences
    sentences = input_text.split(". ")
    corrected_paragraph = ""
    
    # Correct grammar for each sentence and join them back into a paragraph
    for sentence in sentences:
        corrected_sentences = gf.correct(sentence, max_candidates=1)
        corrected_paragraph += " ".join(corrected_sentences) + ". "
    
    return corrected_paragraph

def main():
    st.title("Grammar Correction App")
    st.write("Enter your text in the box below and click 'Correct Grammar' to see the corrected version.")
    
    # Text input area for user input
    input_text = st.text_area("Enter your text here:", height=200)
    
    # Button to trigger grammar correction
    if st.button("Correct Grammar"):
        if input_text:
            corrected_text = correct_grammar(input_text)
            st.subheader("Corrected Text:")
            st.write(corrected_text)
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()
