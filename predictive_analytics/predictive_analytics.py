from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_yield_model(data_frame):
    X = data_frame.drop('yield', axis=1)
    y = data_frame['yield']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    return model
