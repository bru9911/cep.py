import requests
import json

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = json.loads(resposta.content)
        return dados
    else:
        return None

cep = input("Digite o CEP que deseja consultar: ")
endereco = consulta_cep(cep)

if endereco is not None:
    print("Endereço encontrado:")
    print(f"Logradouro: {endereco['logradouro']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade: {endereco['localidade']}")
    print(f"Estado: {endereco['uf']}")
else:
    print("CEP não encontrado.")
