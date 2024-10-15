import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    X = data.drop('target', axis=1)
    y = data['target']
    
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def main():
    data = pd.read_csv('path/to/data.csv')
    model = train_model(data)
    print("Model training complete.")

if __name__ == "__main__":
    main()