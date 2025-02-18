while True:
    print('\n1. Porta',
          '\n2. Parede',
          '\n3. Teto',
          '\n4. Chão'
          )
    
    tipo_superficie = int(input('Escolha a superfície: '))
    
    print('\n1. Quarto',
      '\n2. Banheiro',
      '\n3. Sala',
      '\n4. Cozinha',
      )
    
    comodo = int(input('De qual cômodo desejas adicionar?: '))
    area = float(input('Digite a área da superfície do cômodo desejado em metros: '))
