import pandas as pd
import sklearn
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    path = "./data/heart.csv"
    df = pd.read_csv(path)
    df_features = df.drop(["target"], axis=1)
    df_target = df["target"]

    df_features = StandardScaler().fit_transform(df_features)
    
    X_train, X_test, y_train, y_test = train_test_split(df_features, df_target, test_size=0.3, random_state=42)

    pca = PCA(n_components=3)
    pca.fit(X_train)

    ipca = IncrementalPCA(n_components=3, batch_size=10)
    ipca.fit(X_train)

    logistic = LogisticRegression(solver="newton-cg")

    df_train = pca.transform(X_train)
    df_test = pca.transform(X_test)
    logistic.fit(df_train, y_train)
    print("Score PCA: ", logistic.score(df_test, y_test))

    df_train_ipca = ipca.transform(X_train)
    df_test_ipca = ipca.transform(X_test)
    logistic.fit(df_train_ipca, y_train)
    print("Score IPCA: ", logistic.score(df_test_ipca, y_test))