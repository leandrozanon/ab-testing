def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }

def main():
    import pandas as pd
    from sklearn.model_selection import train_test_split

    # Carregar o conjunto de dados
    data = pd.read_csv('../data/movies_dataset.csv')
    
    # Supondo que a coluna 'target' é a variável alvo
    X = data.drop('target', axis=1)
    y = data['target']

    # Dividir os dados em conjunto de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Carregar os modelos
    model_a = load_model('../models/model_a.pkl')
    model_b = load_model('../models/model_b.pkl')

    # Avaliar os modelos
    results_a = evaluate_model(model_a, X_test, y_test)
    results_b = evaluate_model(model_b, X_test, y_test)

    print("Resultados do Modelo A:", results_a)
    print("Resultados do Modelo B:", results_b)

if __name__ == "__main__":
    main()