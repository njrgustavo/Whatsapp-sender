# Envio de WPP

Este projeto utiliza Docker para orquestrar uma API de mensagens, banco de dados PostgreSQL e Redis.

## Estrutura dos Serviços

- **API**: Serviço principal, container `evolution_api`, exposto na porta `5521` (mapeada para `5520` no container).
- **Postgres**: Banco de dados relacional, usuário e senha padrão `admin`, banco `evolution_db`.
- **Redis**: Cache em memória, exposto na porta `6380` (mapeada para `6379` no container).

## Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Como subir os containers

```sh
docker-compose up -d
```

## Configuração

As variáveis de ambiente estão definidas no arquivo `.env`.

## Testando a API

Exemplo de requisição via Python (`test.py`):

```python
import requests

url = "http://localhost:8081/message/sendText/Test1"
payload = {
    "number": "5513997537748",
    "text": "sdadasdas",
    "delay": 123,
    "linkPreview": True,
    "mentionsEveryOne": True,
    "mentioned": ["5513997537748"], 
    "quoted": {
        "key": {"id": "BC2285612233-4F70-9F01-13BA796ACEB9"},
        "message": {"conversation": "alo"}
    }
}
headers = {
    "apikey": "429683C4C977415CAAFAAGG0F7D57E11",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
```

## Volumes Persistentes

- Dados do Postgres: `pg_data`
- Instâncias da API: `evolution_instances`

## Rede

Todos os serviços estão conectados à rede Docker `evolution-net`.

## Observações

- Certifique-se de as portas `5521` e `6380` estejam livres em sua máquina.
- Para customizar variáveis, edite o arquivo `.env`.
