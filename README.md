# API MBL LINKTREE

## Linguagem e Framework

- **Linguagem:** Python 3.11
- **Framework:** Flask

## Procedimentos para levantar aplicação localmente

0. **Clonar a instalação:**

```shell
git clone https://github.com/MBLivreDev/MBLinktree.git
```

e entrar na pasta clonada:

```shell
cd MBLinktree
```

1. **Criar ambiente virtual:**
   ```shell
   python -m venv venv
   ```
2. **Ativar o ambiente virtual (venv):**

   2.1. Windows:

   ```shell
     ./venv/Scripts/activate
   ```

   2.2. Linux/Mac:

   ```shell
   ./venv/bin/activate
   ```

3. **Atualizar os pacotes utilizados na aplicação através do arquivo requirements.txt:**

   ```shell
   pip install -r requirements.txt
   ```

   > OBS: Caso precise de um novo pacote, adicionar o pacote no arquivo requirements.txt. Ao executar o comando acima, irá atualizar e instalar tudo que o ambiente necessita.\

4. **Crie o arquivo .env:**
   Crie o arquivo .env no mesmo nível do arquivo config.py contendo as chaves:

```
FLASK_APP=app
FLASK_ENV=development
LOCAL_DATABASE_URI=postgresql://postgres:password@localhost:5432/postgres
SECRET_KEY=XXXX
DATABASE_URI=postgresql://postgres:password@localhost:5432/postgres
```

5. **Executar o comando para iniciar a aplicação**

```shell
 flask run --debug
```

> OBS: Executar esse comando dentro da pasta Flask_app.

## Procedimentos para levantar aplicação localmente

Dentro do projeto, existe um arquivo Dockerfile e docker-compose.yml. Toda alteração feita na aplicação precisa compilar a imagem e depois subir a mesma.

Para compilar a imagem executar o comando:

```shell
  docker-compose build
```

Para subir a imagem executar o comando:

```shell
  docker-compose up
```
