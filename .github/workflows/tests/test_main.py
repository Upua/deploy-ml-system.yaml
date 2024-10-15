import pytest
import pandas as pd
from src.main import train_model

def test_train_model():
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4],
        'feature2': [10, 20, 30, 40],
        'target': [0, 1, 0, 1]
    })
    model = train_model(data)
    assert model is not None
    assert hasattr(model, 'predict')