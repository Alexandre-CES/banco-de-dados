# Projeto Desenvolve - ze code challenge

## Introdução
Fiz esse desafio como trabalho para o Projeto Desenvolve BD
link: https://github.com/ab-inbev-ze-company/ze-code-challenges/blob/master/backend.md

# Instruções de instalação

1. clone o repositório:
    ```bash
    git clone https://github.com/Alexandre-CES/banco-de-dados.git
2. Vá para a pasta do desafio:
    ```bash
    cd desafio
3. Crie um ambiente virtual:
    ```bash
    python3 -m venv .venv
4. Ative o ambiente:
    * Linux:
        ```bash
        source ./venv/bin/activate
    * Windows:
        ```bash
        .venv/Scripts/activate
5. Instale as dependências:
    ```bash
    pip install requirements.txt
6. Vá para o arquivo .env e coloque os dados de sua base de dados mysql:
    USERNAME=(usuário)
    PASSWORD=(senha)
    HOST=(geralmente localhost)
    PORT=(porta)
    DATABASE=(nome da base de dados que será usada)
7. Rode o projeto:
    ```bash
    flask --app main.py run
