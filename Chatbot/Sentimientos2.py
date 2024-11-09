import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar los recursos necesarios de NLTK
nltk.download('vader_lexicon')

# Crear un analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Texto de ejemplo
texto = "Este producto es increíble. Me encanta cómo funciona. Sin embargo, el precio es demasiado alto."

# Obtener el puntaje de sentimiento
sentiment_score = sia.polarity_scores(texto)

# Imprimir los resultados
print("Negativo:", sentiment_score['neg'])
print("Neutral:", sentiment_score['neu'])
print("Positivo:", sentiment_score['pos'])
print("Compuesto:", sentiment_score['compound'])

# Interpretación del sentimiento compuesto
if sentiment_score['compound'] >= 0.05:
    print("Sentimiento positivo")
elif sentiment_score['compound'] <= -0.05:
    print("Sentimiento negativo")
else:
    print("Sentimiento neutral")