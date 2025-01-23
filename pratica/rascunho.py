import os
import random

os.system('cls')
# Lista de estados do Brasil
estados_capitais = {
    "Acre": "Rio Branco", 
    "Alagoas": "Maceió", 
    "Amapá": "Macapá", 
    "Amazonas": "Manaus", 
    "Bahia": "Salvador", 
    "Ceará": "Fortaleza", 
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia", 
    "Maranhão": "São Luís", 
    "Mato Grosso": "Cuiabá", 
    "Mato Grosso do Sul": "Campo Grande", 
    "Minas Gerais": "Belo Horizonte", 
    "Pará": "Belém", 
    "Paraíba": "João Pessoa", 
    "Paraná": "Curitiba", 
    "Pernambuco": "Recife", 
    "Piauí": "Teresina", 
    "Rio de Janeiro": "Rio de Janeiro", 
    "Rio Grande do Norte": "Natal", 
    "Rio Grande do Sul": "Porto Alegre", 
    "Rondônia": "Porto Velho", 
    "Roraima": "Boa Vista", 
    "Santa Catarina": "Florianópolis", 
    "São Paulo": "São Paulo", 
    "Sergipe": "Aracaju", 
    "Tocantins": "Palmas"
}



itens = list(estados_capitais.items())
random.shuffle(itens)
estado_capital = dict(itens)