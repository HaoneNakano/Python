# procurar cep
def procurar_cep(cep):
    import requests
    import json
    url = 'https://viacep.com.br/ws/' + cep + '/json/'
    response = requests.get(url)
    if response.status_code == 200:
        dados = json.loads(response.text)
        print('Cidade: {}'.format(dados['localidade']))
        print('Estado: {}'.format(dados['uf']))
        print('Bairro: {}'.format(dados['bairro']))
        print('Rua: {}'.format(dados['logradouro']))
        print('Complemento: {}'.format(dados['complemento']))
        print('CEP: {}'.format(dados['cep']))
    else:
        print('CEP não encontrado')


procurar_cep('01001000')
