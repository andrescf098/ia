import pandas as pd
import joblib

class Utils:
    def load_from_csv(self, path):
        return pd.read_csv(path)
    
    def features_target(self, df, drop_cols, y):
        X = df.drop(drop_cols, axis=1)
        y = df[y]
        return X, y
    
    def model_export(self, clf, score):
        joblib.dump(clf, "./models/best_model.pkl")