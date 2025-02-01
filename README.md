# A/B Testing de Modelos de Recomendação

Este projeto implementa uma estratégia de A/B testing para comparar o desempenho de dois modelos de recomendação utilizando um conjunto de dados de filmes.

## Estrutura do Projeto

- **data/**: Contém o conjunto de dados de filmes.
  - `movies_dataset.csv`: Conjunto de dados utilizado para treinar e avaliar os modelos.

- **models/**: Armazena os modelos treinados.
  - `model_a.pkl`: Modelo A treinado.
  - `model_b.pkl`: Modelo B treinado.

- **notebooks/**: Contém notebooks Jupyter para análise.
  - `analysis.ipynb`: Análise dos resultados e comparação de desempenho dos modelos.

- **src/**: Contém os scripts principais do projeto.
  - `data_preprocessing.py`: Funções para pré-processar os dados.
  - `model_training.py`: Funções para treinar os modelos de recomendação.
  - `model_evaluation.py`: Funções para avaliar o desempenho dos modelos.
  - `ab_testing.py`: Implementação da estratégia de A/B testing.

- **requirements.txt**: Lista as dependências necessárias para o projeto.

- **Dockerfile**: Instruções para construir uma imagem Docker do projeto.

- **.gitignore**: Especifica arquivos e diretórios a serem ignorados pelo Git.

## Como Configurar o Ambiente

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd ab-testing-repo
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute os scripts conforme necessário para treinar, avaliar e testar os modelos.

## Como Executar o Código

- Utilize os scripts na pasta `src/` para realizar as etapas de pré-processamento, treinamento e avaliação dos modelos.
- O notebook `analysis.ipynb` pode ser utilizado para visualizar e analisar os resultados dos modelos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.