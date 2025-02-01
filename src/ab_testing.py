# Conteúdo do arquivo /ab-testing-repo/ab-testing-repo/src/ab_testing.py

import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def load_models(model_a_path, model_b_path):
    model_a = joblib.load(model_a_path)
    model_b = joblib.load(model_b_path)
    return model_a, model_b

def load_data(data_path):
    data = pd.read_csv(data_path)
    return data

def run_ab_test(data, model_a, model_b):
    # Supondo que a coluna 'features' contém as características para previsão
    features = data['features']
    true_labels = data['true_labels']
    
    predictions_a = model_a.predict(features)
    predictions_b = model_b.predict(features)
    
    accuracy_a = accuracy_score(true_labels, predictions_a)
    accuracy_b = accuracy_score(true_labels, predictions_b)
    
    return accuracy_a, accuracy_b

def main():
    model_a_path = '../models/model_a.pkl'
    model_b_path = '../models/model_b.pkl'
    data_path = '../data/movies_dataset.csv'
    
    model_a, model_b = load_models(model_a_path, model_b_path)
    data = load_data(data_path)
    
    accuracy_a, accuracy_b = run_ab_test(data, model_a, model_b)
    
    print(f'Accuracy Model A: {accuracy_a}')
    print(f'Accuracy Model B: {accuracy_b}')
    
if __name__ == "__main__":
    main()