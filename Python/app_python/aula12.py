import requests
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = response.json()
    return dados_cep
def pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon
def retorna_response(url):
    response = requests.get(url)
    return response.text
if __name__ == '__main__':
    cep = 12031030
    #cep = int(input('Digite o cep somente com numeros'))
    cep = retorna_dados_cep(cep)
    print(cep['cep'])
    print(cep['logradouro'])
    print(cep['bairro'])
    print(cep['localidade'])
    print('--------------------------------')
    dados_pokemon = pokemon('pikachu')
    print(dados_pokemon['sprites']['front_shiny'])
    print('--------------------------------')
    response = retorna_response('https://web.digitalinnovation.one/home')
    print(response)
