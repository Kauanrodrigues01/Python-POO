from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bedida
from modelos.cardapio.prato import Prato

# Definindo bebidas e sucos pra colocar no cardapio dos restaurantes    
bebida_suco = Bedida('Suco de melancia', 5, 'Grande')
prato_paozinho = Prato('Paozinho', 2, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto(70)

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()