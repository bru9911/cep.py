import requests

cep = input("Digite o CEP desejado: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Endereço: {data['logradouro']}, {data['bairro']}, {data['localidade']} - {data['uf']}")
else:
    print("Não foi possível encontrar informações para este CEP.")
