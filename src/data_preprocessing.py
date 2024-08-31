# src/data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from src.config import load_config

config = load_config()

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    X = df.drop(columns='Outcome', axis=1)
    Y = df['Outcome']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, Y

def split_data(X, Y):
    test_size = config['data']['test_size']
    random_state = config['data']['random_state']
    print(test_size)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, stratify=Y, random_state=random_state)
    return X_train, X_test, Y_train, Y_test
