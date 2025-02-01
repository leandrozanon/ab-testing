def train_model_a(data):
    # Função para treinar o modelo A
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    import joblib

    # Dividir os dados em conjunto de treinamento e teste
    X = data.drop('target', axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Definir e treinar o modelo
    model_a = RandomForestClassifier(n_estimators=100, random_state=42)
    model_a.fit(X_train, y_train)

    # Salvar o modelo treinado
    joblib.dump(model_a, 'models/model_a.pkl')

def train_model_b(data):
    # Função para treinar o modelo B
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    import joblib

    # Dividir os dados em conjunto de treinamento e teste
    X = data.drop('target', axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Definir e treinar o modelo
    model_b = LogisticRegression()
    model_b.fit(X_train, y_train)

    # Salvar o modelo treinado
    joblib.dump(model_b, 'models/model_b.pkl')

def main():
    import pandas as pd

    # Carregar o conjunto de dados
    data = pd.read_csv('data/movies_dataset.csv')

    # Treinar os modelos
    train_model_a(data)
    train_model_b(data)

if __name__ == "__main__":
    main()