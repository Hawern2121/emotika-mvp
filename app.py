import streamlit as st
from transkrypcja import transkrybuj_audio
from analiza import analizuj_emocje

st.set_page_config(page_title="Emotika MVP", layout="wide")

st.title("🎙️ Emotika - Analiza Emocji z Głosu")

uploaded_file = st.file_uploader("Prześlij plik audio (MP3/WAV)", type=["mp3", "wav"])

if uploaded_file is not None:
    with st.spinner("Transkrybuję audio..."):
        tekst = transkrybuj_audio(uploaded_file)
    st.success("✅ Transkrypcja zakończona!")

    st.markdown("### ✍️ Transkrypcja:")
    st.write(tekst)

    with st.spinner("Analizuję emocje..."):
        emocje = analizuj_emocje(tekst)
    st.success("✅ Analiza emocji zakończona!")

    st.markdown("### 💬 Emocje:")
    st.json(emocje)
