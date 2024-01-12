def main():
    import requests
    print('##########################')
    print('####### Consulta CEP #####')
    print('##########################')
    print()

    cep_input= input('Digite o CEP para a consulta: ')

    if len(cep_input) != 8:
        print('quantidade de digitos inválida!')
        exit()

    requests = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    adress_data = requests.json()

    if 'erro' not in adress_data:
        print('==> CEP ENCONTRADO <==')
        print('CEP: {}'.format(adress_data['cep']))
        print('LOGRADOURO: {}'.format(adress_data['logradouro']))
        print('COMPLEMENTO: {}'.format(adress_data['complemento']))
        print('BAIRRO: {}'.format(adress_data['bairro']))
        print('LOCALIDADE: {}'.format(adress_data['localidade']))
        print('UF: {}'.format(adress_data['uf']))
    else:
        print( '{}CEP Inválido.'.format(cep_input))

    option = int(input('Deseja realizar uma nova consulta ?: \n 1.SIM \n 2.NÃO \n R:'))
    if option == 1:
        main()
    else:
        exit()

if __name__ == "__main__":
    main()

