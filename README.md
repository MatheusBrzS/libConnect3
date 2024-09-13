# LibConnect

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/libconnect.git
   cd libconnect
   ```

2. **Crie e ative um ambiente virtual (recomendado):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux / MacOS
   # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências do projeto:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuração do arquivo `.env`

Para rodar o projeto localmente, é necessário criar um arquivo `.env` na raiz do projeto para armazenar variáveis sensíveis, como a `SECRET_KEY` e o `DEBUG`.

1. **Crie o arquivo `.env` na raiz do projeto:**

   ```bash
   touch .env
   ```

2. **Adicione as variáveis abaixo ao arquivo `.env`:**

   ```bash
   SECRET_KEY=sua_secret_key_aqui
   DEBUG=True  # Para o ambiente de desenvolvimento
   ```

   - Para gerar uma `SECRET_KEY`, você pode usar a ferramenta online [Djecrety](https://djecrety.ir/) e copiar a chave gerada para o campo `SECRET_KEY`.

## Executando as migrações

1. **Gere as migrações necessárias:**

   ```bash
   python manage.py makemigrations
   ```

2. **Aplique as migrações ao banco de dados:**

   ```bash
   python manage.py migrate
   ```

## Executando o servidor de desenvolvimento

Para rodar o servidor de desenvolvimento localmente, execute o seguinte comando:

```bash
python manage.py runserver
```

O projeto estará acessível em `http://127.0.0.1:8000/`.

---

### Outras Informações

- **Administração Django**: Crie um superusuário para acessar a interface administrativa do Django com:

  ```bash
  python manage.py createsuperuser
  ```
