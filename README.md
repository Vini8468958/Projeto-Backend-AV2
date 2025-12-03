# Sistema simples de cadastro de livros para uma biblioteca universitária

Uma aplicação backend completa utilizando Flask e FastAPI, aplicando os conceitos de HTTP, CRUD, 
e conexão com banco de dados relacional, simulando um ambiente real de desenvolvimento de 
um sistema simples de cadastro de livros para uma biblioteca universitária.


## Visão Geral

O projeto utiliza um banco de dados SQLite chamado biblioteca.db, responsável por armazenar as informações dos livros cadastrados no sistema.
Todo o CRUD do projeto (Flask ou FastAPI) utiliza este banco como fonte de dados.

## Local do Banco
O arquivo do banco está em:
`src/data/biblioteca.db`

### Estrutura da Tabela
O banco possui uma única tabela chamada livros, com os seguintes campos:

 Campo          | Tipo    | Descrição                        |
| -------------- | ------- | -------------------------------- |
| id             | INTEGER | Chave primária, autoincremento   |
| titulo         | TEXT    | Título do livro                  |
| autor          | TEXT    | Autor do livro                   |
| ano_publicacao | INTEGER | Ano de publicação (opcional)     |
| disponivel     | INTEGER | 1 = disponível, 0 = indisponível |

### Criação e Reset do Banco

Se for necessário recriar o banco, use o script:
`python src/scripts/create_db.py`


### Esse script:
Cria o arquivo biblioteca.db

Cria a tabela livros
adiciona 3 registros iniciais para testes

Testar o Banco (listar livros)

Para verificar os dados do banco, execute:
```
python src/scripts/check_db.py
```
## Aplicação Flask com Jinja2

O arquivo `app_flask.py` está em: `src/scripts/app_flask.py`

### Como instalar

Para instalar Flask com Jinja2, basta instalar o Flask — o Jinja2 já vem incluído automaticamente como dependência.

### Instalar o Flask

Abra o CMD/Bash e execute:
```
pip install flask
```
Isso já instala:

* Flask
* Jinja2 (motor de templates)
* Werkzeug
* Outras dependências necessárias

### Criar e ativar o ambiente virtual (venv) (Opcional)

Windows (CMD, PowerShell ou Bash):
```
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:
```
python3 -m venv venv
source venv/bin/activate
```

Quando o venv estiver ativo, você verá algo como:
```
(venv) C:\seu_projeto>
```

### Instalar Flask e Jinja2 no ambiente virtual

Com o venv ativado, execute:
```
pip install flask jinja2
```

O Flask já inclui o Jinja2 por padrão, mas instalar explicitamente não faz mal.

### Verificar a instalação

Opcional:
```
pip show flask
pip show jinja2
```
### Abrir o projeto e Rodar

Digite o seguinte código no seu terminal bash para rodar o projeto:
```
python src/scripts/app_flask.py
```

Abra no seu navegador:
```
http://127.0.0.1:5000/
```

## Colaboradores

Projeto desenvolvido por: 

* [Alex Campos Ferreira Chaves](https://github.com/AlexCampos265) - 01690931
* [Aquiles de Melo Albuquerque](https://github.com/Aquiles-adm) - 01725424
* [Lucas Rafael Santana Santos de Holanda](https://github.com/LucasHolanda23) - 01734128
* [Matheus Heralio Monteiro dos Santos](https://github.com/Matheus-Heraclio) - 01687149
* [Maria Carolina Bezerra Melo](https://github.com/Carol-Melo22) - 01837312
* [Raphael Guedes Corrêa](https://github.com/raphaelgc2004) - 01746290
* [Vinícius Barbosa de Figueirêdo](https://github.com/Vini8468958) - 01726804

