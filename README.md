
# Projeto hackathon

Repositório voltado para a criação de uma plataforma de solicitação de artigos de T.I para a UFC (Universidade Federal do Ceará).

_Por motivos de segurança, este repositório foi transferido antes do término do projeto para os domínios da UFC, mas você pode ver o resultado em: https://pedidostic.ufc.br/_

## Funcionalidades

- Cadastrar produtos
- Sistema de E-commerce completo (carrinho, finalização de pedido, etc...)
- Envio de Emails de aviso com prazos 
- Sistema de acompanhamento do pedido

## Instalação

Rode esses comandos no terminal da raiz do projeto:

```bash
.\NomeDoSeuAmbienteVirtual\Scripts\Activate.ps1
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
    
## Bibliotecas

Com o ambiente virtual ativado, instale as seguintes dependências antes de rodar os comandos migrate:

```bash
asgiref==3.7.2
Django==4.2.4
django-filter==23.2
djangorestframework==3.14.0
Markdown==3.4.4
psycopg2==2.9.7
pytz==2023.3
sqlparse==0.4.4
tzdata==2023.3
```
## Usado por

Esse projeto é usado pela UFC.

