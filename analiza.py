from transformers import pipeline

emotion_model = pipeline("text-classification", model="arpanghoshal/EmoRoBERTa", top_k=3)

def analizuj_emocje(tekst):
    wyniki = emotion_model(tekst)
    return wyniki
