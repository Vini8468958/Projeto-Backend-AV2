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

Importante ressaltar que a `Aplicação Flask` roda na `porta 5000`!

## API FastAPI

### PIPS !

Tive que atualizar o pip para conseguir instalar o fastapi, não sei se alguém mais teve esse problema, mas segue a linha de comando: 
```
python.exe -m pip install --upgrade pip
pip install flask
pip install fastapi
pip install uvicorn
```
Uma breve explicação da API e sua aplicação neste código.

O fluxo lógico começa com os imports, precisamos importar as ferramentas para que possamos utilizá-las no código, ferramentas como FastAPI, HTTPException, status, BaseModel do pydantic e o sqlite3, esses kits disponibilizam ótimas ferramentas para manipulação de dados, isto é, para conexão, troca de dados e validação destes.

Declaramos uma função de conexão com o banco de dados, onde colocamos seu endereço, essa função é importante para que possamos fazer nossas requisições HTTP e manipulação CRUD. Declaramos também um modelo base para que haja uma validação de dados, isso evitará conflitos e problemas lógicos e/ou hábitos ruins na hora de constituirmos e realizarmos atualizações e manipulações em nosso banco de dados. Essas duas declarações são cruciais para a lógica do código como um todo, pois aqui colocamos uma restrição e estabelecemos uma conexão para que:

* Método get(todo o banco) - Fazemos um endpoint aqui onde, uma vez conectado ao banco de dados, utilizamos o método get, por meio do "SELECT * FROM livros" e pegamos toda a lista, armazenando num dictionary

* Método get by id - Uma vez que temos a lista inteira, podemos aplicar, aqui, um filtro por ID, o que significa que agora podemos fazer uma pesquisa mais específica.

* Método post - Aqui o basemodel é utilizado para validação dos dados inseridos, já que estamos falando de um método de inserção de dados, que consiste, basicamente, em duas partes, uma na qual o usuário insere o livrro seguindo o modelo base e, uma vez que os dados são validados, ele atualiza o db e retorna o novo livro, mas desta vez com o id.

* Método put - Esse método atualiza os livros já existentes, não se tratando de uma inserção de dados mas uma mudança de dados, onde o processo envolve verificação de existencia, e caso haja o livro, uma troca dos dados, sendo título, autor, ano_publicacao e disponibilidade, sendo str, str, int e bool respectivamente, e logo após isso, uma confirmação, uma busca pelo livro atualizado e busca por erros.

* Método delete - Esse método remove do banco o registro correspondente ao Id, havendo também uma verificação de existencia para que prossiga em sua ação.

Vale ressaltar que, nos métodos, temos também linhas que estabelecem uma comunicação diante dos erros, isto é, quando um método tem problemas de conexão, é retornado um código referente ao seu erro, e que a `Fast API` roda na `porta 8000`!

## Colaboradores

Projeto desenvolvido por: 

* [Alex Campos Ferreira Chaves](https://github.com/AlexCampos265) - 01690931
* [Aquiles de Melo Albuquerque](https://github.com/Aquiles-adm) - 01725424
* [Lucas Rafael Santana Santos de Holanda](https://github.com/LucasHolanda23) - 01734128
* [Matheus Heraclio Monteiro dos Santos](https://github.com/Matheus-Heraclio) - 01687149
* [Maria Carolina Bezerra Melo](https://github.com/Carol-Melo22) - 01837312
* [Raphael Guedes Corrêa](https://github.com/raphaelgc2004) - 01746290
* [Vinícius Barbosa de Figueirêdo](https://github.com/Vini8468958) - 01726804




