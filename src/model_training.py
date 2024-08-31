# src/model_training.py

from sklearn import svm
import joblib
from src.config import load_config

config = load_config()

def train_model(X_train, Y_train):
    kernel = config['model']['kernel']
    classifier = svm.SVC(kernel=kernel)
    classifier.fit(X_train, Y_train)
    
    # Save the trained model
    joblib.dump(classifier, 'models/model.pkl')
    
    return classifier

def load_model(model_path='models/model.pkl'):
    return joblib.load(model_path)
