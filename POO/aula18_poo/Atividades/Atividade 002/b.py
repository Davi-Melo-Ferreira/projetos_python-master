# dicionario = {}

porta = {}
parede = {}
teto = {}
chao = {}

while True:
    print('\n.Porta',
          '\n.Parede',
          '\n.Teto',
          '\n.Chão'
          )
    
    tipo_superficie = input('Escolha a superfície: ').lower()
    
    print('\n.Quarto',
      '\n.Banheiro',
      '\n.Sala',
      '\n.Cozinha',
      )
    
    comodo = input('De qual cômodo desejas adicionar?: ').lower()
    area = float(input('Digite a área da superfície do cômodo desejado em metros: '))
    
    if tipo_superficie == 'porta':
      porta[f'Porta - {comodo}'] = {'área' : area}
    if tipo_superficie == 'parede':
      parede[f'Parede - {comodo}'] = {'área' : area}
    if tipo_superficie == 'teto':
      teto[f'Teto - {comodo}'] = {'área' : area}
    if tipo_superficie == 'chão' or tipo_superficie == 'chao':
      chao[f'Chão - {comodo}'] = {'área' : area}
    
    opcao = input('Desejas continuar?(s/n): ').lower()
    
    if opcao == 's':
      continue
    elif opcao == 'n':
      break
    else:
      print('Inválido!!')

# print(porta)
# print(parede)
# print(teto)
# print(chao)

for i in porta, parede, teto, chao:
  print(i)