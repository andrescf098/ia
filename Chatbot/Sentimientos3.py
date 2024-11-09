import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Datos de ejemplo (reemplaza con tus propios datos)
data = {'review': ['Este producto es excelente', 'El servicio al cliente fue pésimo', 'Estoy muy contento con la compra', 'No recomiendo este lugar'], 'sentiment': [1, 0, 1, 0]}
df = pd.DataFrame(data)

# Separar las características (reviews) y la etiqueta (sentimiento)
X = df['review']
y = df['sentiment']

# Vectorizar las reviews (convertir texto en números)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,  random_state=42)

# Crear y entrenar el modelo (Naive Bayes)   

model = MultinomialNB()
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo (accuracy) 
 
accuracy  = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)