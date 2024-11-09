#pip install nltk

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar los recursos necesarios de NLTK si es la primera vez
nltk.download('vader_lexicon')

# Crear un analizador de sentimientos
sia = SentimentIntensityAnalyzer()

# Texto de ejemplo
""" texto = "Este producto es increíble. Me encanta su diseño y funciona a la perfección. Sin embargo, el precio es un poco elevado." """
texto = "This product is amazing. I love the design its  put it works perfectly. However, the price is a bit high."

""" texto = input("Escribe el texto para analizar ") """

# Realizar el análisis de sentimientos
sentiment = sia.polarity_scores(texto)

# Imprimir los resultados
print(sentiment)