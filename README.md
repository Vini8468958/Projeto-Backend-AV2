# Sistema simples de cadastro de livros para uma biblioteca universitária

Uma aplicação backend completa utilizando Flask e FastAPI, aplicando os conceitos de HTTP, CRUD, 
e conexão com banco de dados relacional, simulando um ambiente real de desenvolvimento de 
um sistema simples de cadastro de livros para uma biblioteca universitária.


## Visão Geral

O projeto utiliza um banco de dados SQLite chamado biblioteca.db, responsável por armazenar as informações dos livros cadastrados no sistema.
Todo o CRUD do projeto (Flask ou FastAPI) utiliza este banco como fonte de dados.

## Local do Banco
O arquivo do banco está em:
src/data/biblioteca.db

## Estrutura da Tabela
O banco possui uma única tabela chamada livros, com os seguintes campos:

 Campo          | Tipo    | Descrição                        |
| -------------- | ------- | -------------------------------- |
| id             | INTEGER | Chave primária, autoincremento   |
| titulo         | TEXT    | Título do livro                  |
| autor          | TEXT    | Autor do livro                   |
| ano_publicacao | INTEGER | Ano de publicação (opcional)     |
| disponivel     | INTEGER | 1 = disponível, 0 = indisponível |

## Criação e Reset do Banco

Se for necessário recriar o banco, use o script:
python src/scripts/create_db.py


## Esse script:
cria o arquivo biblioteca.db
cria a tabela livros
adiciona 3 registros iniciais para testes

Testar o Banco (listar livros)
Para verificar os dados do banco, execute:

python src/scripts/check_db.py


