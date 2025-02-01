def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Remover duplicatas
    data = data.drop_duplicates()
    
    # Tratar valores ausentes
    data = data.fillna(method='ffill')
    
    return data

def preprocess_data(file_path):
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    return cleaned_data

if __name__ == "__main__":
    file_path = '../data/movies_dataset.csv'
    processed_data = preprocess_data(file_path)
    print(processed_data.head())