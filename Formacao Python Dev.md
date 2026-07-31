# Formação Python Backend Developer - DIO
A Formação Python Backend Developer prepara você para construir aplicações robustas e eficientes com Python. A formação cobre desde boas práticas e gerenciamento de pacotes até desenvolvimento avançado de APIs e aplicações full stack.
Você começará com fundamentos essenciais, como boas práticas em Python e interação com bancos de dados relacionais. Em seguida, aprenderá a desenvolver APIs RESTful com Flask, abordando manipulação de dados, autenticação, testes e deploy. A formação também inclui desenvolvimento full stack com Django, explorando modelos, views, templates, formulários, e deploy de aplicações completas. Por fim, você estudará APIs assíncronas com FastAPI, culminando em um projeto prático de criação de uma API bancária assíncrona.

## Módulo 1 - Boas práticas em Python: Pacotes, Banco de Dados e Desenvolvimento WEB

### Curso 1.1 - Gerenciamento de pacotes, convenções e boas práticas

#### O que são pacotes?
Pacotes em Python são diretórios/pastas organizadas contendo um ou mais módulos (arquivos `.py`) e um arquivo especial chamado `__init__.py` (obrigatório até o Python 3.2, mas mantido como boa prática). Eles permitem modularizar o código, reusar funcionalidades e distribuir soluções de forma estruturada, dividindo grandes sistemas em partes menores e gerenciáveis.

#### O que é PIP?
O **PIP** (*Pip Installs Packages*) é o gerenciador de pacotes oficial e padrão da linguagem Python. Ele se conecta ao [PyPI (Python Package Index)](https://pypi.org/), que é o repositório central da comunidade, permitindo baixar, instalar, atualizar e remover bibliotecas de terceiros diretamente pelo terminal.

#### Comandos do PIP
* `pip install <pacote>`: Instala a versão mais recente de um pacote.
* `pip install <pacote>==<versao>`: Instala uma versão específica do pacote.
* `pip uninstall <pacote>`: Remove/desinstala um pacote.
* `pip list`: Exibe a lista de todos os pacotes instalados no ambiente atual.
* `pip freeze > requirements.txt`: Exporta a lista e as versões exatas de todas as dependências instaladas para um arquivo de texto.
* `pip install -r requirements.txt`: Instala todas as dependências listadas no arquivo `requirements.txt`.

#### O que são ambientes virtuais?
Um ambiente virtual (*virtual environment* ou `venv`) é um ambiente isolado do sistema operacional. Ele permite instalar bibliotecas e dependências de forma independente para cada projeto, evitando conflitos de versão entre bibliotecas que diferentes projetos possam exigir (ex.: Projeto A exige Django 3.2 e Projeto B exige Django 5.0).

#### O que é Pipenv?
O **Pipenv** é uma ferramenta de gerenciamento de dependências que combina o `pip` e o `virtualenv` em uma única CLI. Ele automatiza a criação e gerenciamento de ambientes virtuais, utilizando os arquivos `Pipfile` (substituto do `requirements.txt`) e `Pipfile.lock` (que garante a reprodução exata das versões das dependências em qualquer ambiente/máquina).

#### Comandos Pipenv
* `pipenv install`: Cria o ambiente virtual e instala as dependências listadas no `Pipfile`.
* `pipenv install <pacote>`: Instala o pacote e o adiciona automaticamente ao `Pipfile`.
* `pipenv shell`: Ativa o ambiente virtual no terminal atual.
* `pipenv run python <script.py>`: Executa um script Python diretamente no ambiente virtual sem precisar ativá-lo manualmente.
* `pipenv check`: Verifica vulnerabilidades conhecidas de segurança nas dependências instaladas.
* `pipenv lock`: Gera ou atualiza o arquivo `Pipfile.lock`.

#### O que é Poetry?
O **Poetry** é uma ferramenta moderna para gerenciamento de dependências e empacotamento de projetos Python. Ele unifica o gerenciamento de ambientes virtuais, resolução de dependências complexas e a publicação de pacotes usando o padrão moderno `pyproject.toml` (conforme as PEPs 517 e 518).

#### Comandos Poetry
* `poetry new <nome_projeto>`: Cria uma nova estrutura de diretórios e arquivos pronta para uso.
* `poetry init`: Configura interativamente um arquivo `pyproject.toml` em um projeto existente.
* `poetry env use python`: Especifica e cria o ambiente virtual com a versão do Python escolhida.
* `poetry add <pacote>`: Adiciona e instala uma nova dependência no projeto.
* `poetry add --group dev <pacote>`: Adiciona uma dependência exclusiva para o ambiente de desenvolvimento.
* `poetry install`: Instala todas as dependências listadas no arquivo `pyproject.toml`.
* `poetry run python <script.py>`: Executa um comando ou script dentro do contexto do ambiente virtual.
* `poetry shell`: Ativa o ambiente virtual do projeto no terminal.

#### Boas práticas em Python

- **PEP 8:**
  O guia de estilo oficial do código Python. Define convenções de formatação para manter o código legível e consistente. Entre suas regras principais estão: uso de 4 espaços para indentação (sem tabulações), nomes de variáveis e funções em `snake_case`, nomes de classes em `PascalCase`, e limite de linhas (recomendado até 79 caracteres).

- **flake8:**
  Um *linter* (analisador estático de código) que verifica o seu código-fonte em busca de erros de sintaxe, possíveis bugs e desvios das convenções estéticas definidas na PEP 8.

- **Black:**
  Um formatador de código automático e opinionativo ("*uncompromising code formatter*"). Ele reescreve todo o código ajustando a formatação automaticamente de acordo com regras estritas, garantindo conformidade com a PEP 8 e padronização total entre membros de uma equipe.

- **isort:**
  Uma ferramenta para organizar e ordenar automaticamente as declarações de importação (`import` e `from ... import ...`) no topo dos arquivos Python. Ele separa as importações por categoria (biblioteca padrão, bibliotecas de terceiros e arquivos locais) e as coloca em ordem alfabética.

### Curso 1.2 - Banco de Dados Relacionais com DB API

#### O que é Banco de Dados?
Um **Banco de Dados** (ou *Database*) é um sistema organizado para armazenar, gerenciar e recuperar dados de forma estruturada, eficiente e segura. Em vez de salvar informações em arquivos soltos (como `.txt` ou `.csv`), o banco de dados garante integridade, controle de acesso e alta performance mesmo ao lidar com grandes volumes de dados.

#### Tipos de Banco de Dados
Os bancos de dados são divididos em duas grandes famílias:

*   **Relacionais (SQL):** Armazenam dados em tabelas compostas por linhas e colunas com esquemas pré-definidos. Exemplos: PostgreSQL, MySQL, SQLite, Oracle, SQL Server.
*   **Não Relacionais (NoSQL):** Modelos flexíveis sem esquema fixo, otimizados para grandes volumes de dados não estruturados ou semi-estruturados. Podem ser baseados em documentos (MongoDB), chave-valor (Redis), colunas (Cassandra) ou grafos (Neo4j).

#### Aspectos de Banco de Dados Relacional
Os bancos de dados relacionais organizam os dados baseando-se no modelo relacional de Codd:

*   **Tabelas (Relações):** Estruturas que representam entidades (ex: `Usuarios`, `Produtos`).
*   **Colunas (Atributos):** Definem os tipos de dados armazenados (ex: `nome: TEXT`, `idade: INT`).
*   **Linhas (Tuplas/Registros):** Cada entrada individual de dados na tabela.
*   **Chave Primária (Primary Key - PK):** Identificador único de cada registro na tabela (ex: `id`).
*   **Chave Estrangeira (Foreign Key - FK):** Campo que cria um vínculo entre o registro de uma tabela e a chave primária de outra tabela.

#### A.C.I.D
ACID é um conjunto de quatro propriedades essenciais que garantem a confiabilidade e segurança de transações em um Banco de Dados Relacional:

*   **A - Atomicidade (Atomicity):** A transação é tratada como uma unidade única. Ou "tudo é executado com sucesso" ou "nada é aplicado" (*rollback*).
*   **C - Consistência (Consistency):** Os dados devem respeitar todas as regras de integridade e restrições do banco antes e depois da transação.
*   **I - Isolamento (Isolation):** Transações concorrentes não interferem umas nas outras enquanto estão sendo executadas.
*   **D - Durabilidade (Durability):** Uma vez confirmada a transação (*commit*), os dados são salvos permanentemente, mesmo em caso de falha de energia ou sistema.

#### Tipos de Relacionamentos
*   **Um para Um (1:1):** Um registro na Tabela A está associado a no máximo um registro na Tabela B (ex: `Usuario` e `Perfil`).
*   **Um para Muitos (1:N):** Um registro na Tabela A pode se relacionar com múltiplos registros na Tabela B, mas o da Tabela B pertence a apenas um da Tabela A (ex: `Cliente` e `Pedidos`).
*   **Muitos para Muitos (N:N):** Múltiplos registros na Tabela A se relacionam com múltiplos na Tabela B. Requer uma **tabela intermediária** (ou tabela de junção) com duas chaves estrangeiras (ex: `Estudantes` e `Cursos`).

#### O que é SQL
**SQL** (*Structured Query Language* ou Linguagem de Consulta Estruturada) é a linguagem padrão utilizada para interagir, criar, manipular e consultar dados em Bancos de Dados Relacionais.

#### Comandos SQL
Os comandos SQL são categorizados conforme sua finalidade:

1.  **DDL (Data Definition Language) - Define a estrutura:**
    *   `CREATE DATABASE`: Cria o banco de dados.
    *   `CREATE TABLE`: Cria uma nova tabela.
    *   `ALTER TABLE`: Modifica a estrutura de uma tabela.
    *   `DROP TABLE`: Deleta uma tabela e seus dados.
2.  **DML (Data Manipulation Language) - Manipula os dados:**
    *   `INSERT INTO`: Insere novos registros.
    *   `UPDATE`: Atualiza registros existentes.
    *   `DELETE`: Remove registros.
3.  **DQL (Data Query Language) - Consulta dados:**
    *   `SELECT`: Recupera informações do banco.
    *   `WHERE`: Filtra os resultados por condições.
    *   `JOIN` (`INNER`, `LEFT`, `RIGHT`): Combina dados de duas ou mais tabelas relacionáveis.
4.  **TCL (Transaction Control Language) - Controle de transações:**
    *   `COMMIT`: Salva permanentemente as alterações.
    *   `ROLLBACK`: Desfaz as alterações da transação atual.

#### Boas Práticas com SQL
*   **Evite o `SELECT *`:** Sempre especifique as colunas necessárias (`SELECT id, nome FROM ...`) para otimizar o uso da memória e tráfego de rede.
*   **Atenção ao `UPDATE` e `DELETE` sem `WHERE`:** Executar estes comandos sem um filtro aplicará as alterações a **todos** os registros da tabela acidentalmente.
*   **Uso de Índices (`INDEX`):** Crie índices em colunas frequentemente pesquisadas (como chaves estrangeiras e IDs) para acelerar a busca.
*   **Nomenclatura Clara:** Padronize nomes de tabelas e colunas em minúsculo, no plural ou singular, utilizando `snake_case` (ex: `data_criacao`, `pedidos`).
*   **Uso de Transações:** Para operações em lote ou dependentes, utilize transações (`BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`).

#### DB API
A **Python DB-API (PEP 249)** é a especificação padrão do Python para conexão com bancos de dados relacionais. Ela estabelece uma interface consistente que qualquer biblioteca/driver Python (como `sqlite3`, `psycopg2` para PostgreSQL ou `mysql-connector`) deve seguir, garantindo reuso de conhecimento.

Os componentes fundamentais da DB API são:

1.  **Conexão (`connect()`):** Estabelece o vínculo com o banco de dados.
2.  **Cursor (`cursor()`):** Objeto responsável por executar os comandos SQL e percorrer os resultados retornados.
3.  **Execução (`execute()` / `executemany()`):** Envia e executa o comando SQL no banco.
4.  **Prevenção contra SQL Injection (Placeholders):** O uso de placeholders (como `?` no SQLite ou `%s` no PostgreSQL) garante que parâmetros passados via código sejam devidamente higienizados e escapados.
    *   *Errado (Vulnerável):* `cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")`
    *   *Correto (Seguro):* `cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))`
5.  **Coleta de Dados (`fetchone()` / `fetchall()`):** Métodos do cursor para extrair um ou todos os resultados da consulta.
6.  **Encerramento (`commit()` e `close()`):** Confirmação das alterações e fechamento da conexão com o banco para liberar recursos.


### Curso 1.3 - Introdução a aplicações REST

#### O que é Desenvolvimento WEB?
O **Desenvolvimento Web** é o processo de criação e manutenção de aplicações, sites e softwares que são executados pela internet através de navegadores (como Chrome, Firefox, Safari) ou consumidos por outros sistemas via requisições de rede.

A arquitetura do desenvolvimento web é dividida principalmente em dois lados:

*   **Front-end (Client-side):** A interface visual e a camada de interação com o usuário final (desenvolvido tradicionalmente com HTML, CSS e JavaScript).
*   **Back-end (Server-side):** A lógica de negócios, processamento de dados, comunicação com bancos de dados, autenticação e gerenciamento de APIs (onde linguagens como Python se destacam através de frameworks como FastAPI, Flask e Django).

#### O que é API e características das APIs (RESTful, SOAP, GraphQL)
Uma **API** (*Application Programming Interface* ou Interface de Programação de Aplicações) é um conjunto de rotinas, protocolos e padrões que permite que diferentes softwares se comuniquem entre si sem precisar conhecer a implementação interna um do outro. 

Os três principais paradigmas e arquiteturas de APIs são:

1.  **RESTful (Representational State Transfer):**
    *   **Características:** O padrão mais utilizado na web moderna. Baseado nos princípios do protocolo HTTP, é *stateless* (cada requisição é independente e contém todas as informações necessárias), utiliza URLs para identificar recursos e formatos leves para transferência de dados (como JSON).
    *   **Pontos Fortes:** Leve, escalável, fácil de aprender e de consumir.

2.  **SOAP (Simple Object Access Protocol):**
    *   **Características:** Protocolo de comunicação estrito, fortemente tipado e baseado em XML. Possui um contrato rigoroso chamado WSDL (*Web Services Description Language*) e padrões avançados de segurança nativos (WS-Security).
    *   **Pontos Fortes:** Muito utilizado em sistemas legados, corporativos, bancários e ambientes que exigem conformidade estrita e contratos de dados rígidos.

3.  **GraphQL:**
    *   **Características:** Linguagem de consulta criada pelo Meta (Facebook) para APIs. Em vez de múltiplos endpoints fixos, disponibiliza **um único endpoint** onde o cliente especifica exatamente quais dados precisa na requisição.
    *   **Pontos Fortes:** Elimina os problemas de *over-fetching* (receber mais dados do que o necessário) e *under-fetching* (fazer múltiplas chamadas para obter dados relacionados).

#### Verbos HTTP e Convenções RESTful
Em arquiteturas RESTful, o protocolo **HTTP** fornece um conjunto de métodos (chamados de "verbos") que indicam a ação que se deseja realizar sobre um recurso específico da API.

##### Principais Verbos HTTP:
*   **GET:** Solicita a leitura/recuperação de dados de um recurso. Não deve alterar o estado do servidor (é uma operação segura e idempotente).
*   **POST:** Cria um novo recurso no servidor com os dados enviados no corpo (*body*) da requisição.
*   **PUT:** Atualiza um recurso existente **por completo**. Se o recurso não existir, pode ser criado dependendo da implementação.
*   **PATCH:** Atualiza **parcialmente** um recurso existente (modifica apenas os campos enviados no corpo da requisição).
*   **DELETE:** Remove um recurso especificado no servidor.

##### Convenções RESTful Importantes:
*   **Substantivos no Plural para URIs:** Os caminhos (endpoints) devem ser substantivos que representam recursos, nunca ações/verbos.
    *   *Correto:* `GET /usuarios`, `POST /pedidos`
    *   *Incorreto:* `GET /buscarUsuarios`, `POST /criarNovoPedido`
*   **Identificação de Recursos Específicos:** Utilize IDs diretamente no caminho da URL para referenciar um item único.
    *   *Exemplo:* `GET /usuarios/42` (Busca o usuário de ID 42) ou `DELETE /produtos/10` (Remove o produto 10).
*   **Códigos de Status HTTP apropriados:** A API deve sempre responder com o código de status HTTP correto para o resultado da operação:
    *   `200 OK`: Requisição executada com sucesso.
    *   `201 Created`: Novo recurso criado com sucesso (comum após um `POST`).
    *   `204 No Content`: Requisição bem-sucedida, mas sem corpo na resposta (comum após um `DELETE`).
    *   `400 Bad Request`: Dados ou parâmetros enviados pelo cliente são inválidos.
    *   `401 Unauthorized`: Requer autenticação.
    *   `403 Forbidden`: O cliente está autenticado, mas não tem permissão para acessar o recurso.
    *   `404 Not Found`: O recurso solicitado não foi encontrado no servidor.
    *   `500 Internal Server Error`: Erro inesperado no processamento do lado do servidor.


## Modulo 2 - Desenvolivmento de API com Flask

### Curso 2.1 - Introdução ao Flask para APIs RESTful

#### O que é o Flask
O **Flask** é um micro-framework em Python voltado para o desenvolvimento web e criação de APIs RESTful. Ele é categorizado como um "micro-framework" porque fornece apenas os recursos essenciais para colocar um serviço web no ar — como o sistema de roteamento de URLs e a manipulação de requisições HTTP — sem impor uma arquitetura de arquivos rígida ou ferramentas pré-determinadas para banco de dados, validação ou autenticação. Essa simplicidade garante total liberdade ao desenvolvedor para escolher as bibliotecas e padrões de projeto mais adequados para a sua aplicação.

---

### Curso 2.2 - Primeiros Passos

#### Como ativar debug
O modo **Debug** é uma funcionalidade voltada exclusivamente para o ambiente de desenvolvimento. Quando ativado, ele oferece dois recursos principais:

* **Recarregamento Automático (*Auto-reload*):** O servidor detecta alterações salvas nos arquivos do projeto e se reinicia automaticamente, dispensando a necessidade de parar e subir a aplicação manualmente a cada alteração no código.
* **Depurador Interativo (*Interactive Debugger*):** Caso ocorra uma exceção ou erro não tratado durante a execução da aplicação, o Flask exibe um rastreamento detalhado do erro (*stack trace*) diretamente no terminal ou navegador, facilitando a identificação do problema.

#### O que são rotas e endpoints
Embora frequentemente usados como sinônimos, no contexto de arquiteturas RESTful e do Flask esses termos possuem responsabilidades distintas:

* **Rotas (*Routes*):** Correspondem ao caminho textual ou padrão da URL declarado na aplicação (ex: `/`, `/usuarios`, `/produtos/42`). A rota define o endereço em que o recurso está localizado na estrutura do servidor.
* **Endpoints:** Representam o ponto final da comunicação entre o cliente e o servidor. É a combinação de uma **Rota** com um **Método HTTP específico** (`GET`, `POST`, `PUT`, `DELETE`) associada à lógica da aplicação que irá processar a requisição e retornar uma resposta formatada (como um JSON e seu respectivo código de status HTTP).

Aqui está o conteúdo estruturado e objetivo para completar a sua documentação do curso:

---

### Curso 2.3 - Manipulação de dados

#### O que é ORM

**ORM** (*Object-Relational Mapping* ou Mapeamento Objeto-Relacional) é uma técnica de programação que permite interagir com um banco de dados relacional utilizando orientação a objetos.

* **Como funciona:** Em vez de escrever consultas SQL puras em formato de string, você define **classes Python** que representam tabelas e **instâncias de objetos** que representam linhas do banco.
* **Vantagens:** Abstração de código, facilidade na manutenção, prevenção contra SQL Injection e independência de SGBD (é fácil trocar de SQLite para PostgreSQL, por exemplo).

---

#### O que é SQLAlchemy

O **SQLAlchemy** é o toolkit SQL e ORM mais popular e poderoso do ecossistema Python. Ele fornece uma suíte completa de ferramentas para persistência de dados.

* **Flask-SQLAlchemy:** É uma extensão que simplifica a integração do SQLAlchemy ao Flask, gerenciando sessões, conexões e a inicialização da aplicação (`db = SQLAlchemy(app)`).

---

#### Comandos do SQL para SQLAlchemy

Abaixo está a correspondência entre os comandos SQL tradicionais e a sintaxe do SQLAlchemy (utilizando a sintaxe moderna 2.0+):

| Operação SQL | SQL Tradicional | SQLAlchemy (2.0+) |
| --- | --- | --- |
| **SELECT All** | `SELECT * FROM users;` | `db.session.scalars(select(User)).all()` |
| **SELECT Filter** | `SELECT * FROM users WHERE age = 18;` | `db.session.scalars(select(User).where(User.age == 18)).all()` |
| **SELECT ID** | `SELECT * FROM users WHERE id = 1;` | `db.session.get(User, 1)` |
| **INSERT** | `INSERT INTO users (name) VALUES ('Ana');` | `user = User(name='Ana')` <br> `db.session.add(user)` <br> `db.session.commit()` |
| **UPDATE** | `UPDATE users SET name='Ana' WHERE id=1;` | `user = db.session.get(User, 1)`<br>`user.name = 'Ana'`<br>`db.session.commit()` |
| **DELETE** | `DELETE FROM users WHERE id = 1;` | `user = db.session.get(User, 1)`<br> `db.session.delete(user)`<br> `db.session.commit()` |

---

#### O que é Flask-Migrate

O **Flask-Migrate** é uma extensão que lida com as **migrações de banco de dados** para aplicações Flask que utilizam o SQLAlchemy. Ela adapta as alterações feitas nos seus modelos Python (como adicionar uma nova coluna ou criar uma nova tabela) diretamente no banco de dados sem que você precise apagar e recriar o banco.

---

#### Comandos Flask-Migrate

Os comandos são executados via CLI na raiz do projeto (onde o aplicativo Flask está configurado):

1. **flask db init:**
Inicializa o repositório de migrações no projeto (cria a pasta `migrations/`). Executado apenas uma vez no início do projeto.


2. **flask db migrate -m 'mensagem':**
Compara os seus modelos Python com a estrutura atual do banco de dados e gera um script de migração automático com as alterações detectadas.


3. **flask db upgrade:**
Aplica as migrações pendentes ao banco de dados (executa as alterações de fato).


4. **flask db downgrade:**
Reverte a última migração aplicada ao banco de dados (útil em caso de erro na alteração).


---

#### O que é o Alembic

O **Alembic** é a ferramenta nativa de migração de banco de dados criada pelo próprio autor do SQLAlchemy.

* O **Flask-Migrate** é na verdade um *wrapper* (uma camada de adaptação) que envolve o Alembic para integrá-lo ao ecossistema e à linha de comando do Flask.

---

#### Comandos Alembic

Caso esteja trabalhando em um projeto Python puro usando o Alembic sem o Flask, os comandos diretos do Alembic são:

* **`alembic init <pasta>`**: Inicializa o ambiente de migrações do Alembic (cria o arquivo `alembic.ini` e a pasta de scripts).
* **`alembic revision --autogenerate -m "mensagem"`**: Analisa os modelos SQLAlchemy e cria um novo script de migração na pasta `versions/`.
* **`alembic upgrade head`**: Aplica todas as migrações pendentes até a versão mais recente (*head*).
* **`alembic downgrade -1`**: Reverte a aplicação para a versão imediatamente anterior.


### Curso 2.4 - Autenticação e autorização

#### O que é Autenticação e autorização

Embora sejam termos frequentemente usados juntos, eles representam etapas distintas da segurança de uma aplicação:

* **Autenticação (Quem é você?):** É o processo de verificação da identidade do usuário. Ocorre quando o usuário fornece credenciais (como e-mail/usuário e senha) para provar que ele é quem afirma ser.
* *Exemplo:* Fazer login no sistema bancário digitando a senha correta.


* **Autorização (O que você pode fazer?):** É o processo de checar quais permissões um usuário autenticado possui dentro do sistema.
* *Exemplo:* Um usuário comum pode visualizar seu próprio extrato bancário, mas apenas um usuário admin pode deletar contas ou alterar permissões de terceiros.



---

#### O que é JWT

**JWT (JSON Web Token)** é um padrão aberto (RFC 7519) compacto e autocontido para transmitir informações com segurança entre partes como um objeto JSON. Ele é amplamente utilizado em arquiteturas RESTful por ser **stateless** (o servidor não precisa manter sessões gravadas em memória ou banco de dados para validar o acesso).

Estrutura de um JWT (dividida por três pontos `.`):

1. **Header (Cabeçalho):** Contém o tipo do token (`JWT`) e o algoritmo de hash utilizado (ex: `HS256`).
2. **Payload (Carga útil):** Contém os *claims* (declarações/dados do usuário e do token), como `sub` (identidade/Subject), `exp` (data de expiração) e `iat` (data de criação).
3. **Signature (Assinatura):** Garante a integridade do token. É gerada combinando o Header codificado, o Payload codificado e uma **chave secreta** mantida apenas no servidor.

```text
[Header Base64].[Payload Base64].[Signature]

```

---

#### Cuidados com JWT

Apesar de ser extremamente prático, o uso incorreto do JWT pode gerar graves vulnerabilidades de segurança:

1. **Dados Sensíveis no Payload:** O Payload é apenas codificado em **Base64**, não criptografado. Qualquer pessoa que interceptar o token pode ler os dados contidos nele. **Nunca inclua senhas, números de cartão ou dados pessoais sensíveis no Payload.**
2. **Armazenamento no Frontend:**
* Guardar em `localStorage` ou `sessionStorage` expõe o token a ataques de **XSS (Cross-Site Scripting)**.
* A abordagem mais segura é armazenar o token em um **Cookie HttpOnly com flag Secure**, impedindo o acesso via JavaScript malicioso.


3. **Expiração Apropriada (`exp`):** Configure sempre um tempo de vida curto para os Access Tokens (ex: 15 a 60 minutos) e utilize *Refresh Tokens* para renovação sem exigir re-login constante do usuário.
4. **Validação da Chave Secreta:** Mantenha a chave usada para assinar os tokens (`JWT_SECRET_KEY`) em variáveis de ambiente extremamente seguras. Se a chave vazar, terceiros poderão forjar tokens válidos.
5. **Tipagem da Identidade (`sub`):** Nas versões recentes do `flask-jwt-extended` (v4+), o `identity` (claim `sub`) deve **obrigatoriamente ser passado como string** (ex: `str(user.id)`), evitando falhas de parsing e garantindo aderência ao padrão da RFC.

---

#### O que é um decorator e como fazer

##### O que é um Decorator?

Um **Decorator** em Python é uma função que recebe outra função como argumento, estende ou altera o seu comportamento sem modificar seu código fonte diretamente, e retorna uma nova função. Em frameworks web como o Flask, eles são amplamente utilizados para aplicar lógicas repetitivas (como checagem de autenticação, validação de rotas ou logging).

A sintaxe utiliza o símbolo `@` logo acima da definição da função.

##### Como criar um Decorator personalizado?

Para criar decorators com suporte a repasse de argumentos de forma limpa, utiliza-se a biblioteca padrão `functools.wraps`.

**Exemplo básico de Decorator:**

```python
from functools import wraps

def log_execucao(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"[LOG] A função '{f.__name__}' está sendo executada.")
        resultado = f(*args, **kwargs)
        print(f"[LOG] A função '{f.__name__}' foi concluída.")
        return resultado
    return wrapper

# Aplicando o decorator
@log_execucao
def minha_rota():
    return "Processando requisição..."

```

##### Decorator no contexto do Flask e JWT

No `flask-jwt-extended`, o decorator `@jwt_required()` intercepta a requisição HTTP, extrai o token do cabeçalho `Authorization: Bearer <token>`, valida a assinatura e a expiração, e bloqueia o acesso (retornando erro 401) se o token for inválido:

```python
from flask import Flask, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# Gerando o token (lembrando de converter o ID para string no v4)
@app.route("/login", methods=["POST"])
def login():
    user_id = 1  # Exemplo de ID vindo do banco
    access_token = create_access_token(identity=str(user_id))
    return jsonify(access_token=access_token)

# Protegendo a rota com o decorator
@app.route("/perfil", methods=["GET"])
@jwt_required()
def perfil():
    current_user_id = get_jwt_identity()  # Retorna a string "1"
    return jsonify(logged_in_as=current_user_id)

```




















































### Curso 2.5 - Teste









### Curso 2.6 - Deploy
### Curso 2.7 - Boas praticas

## Modulo 3 - Desenvolivmento Fullstack com Django
## Modulo 4 - API's assincronas com FastAPI