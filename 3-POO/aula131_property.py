# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor, tamanho):
        self.cor_tinta = cor
        self.expressura = tamanho

    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def tamanho(self):
        return self.expressura
    
    @property
    def cor_tampa(self):
        return 'Cor tampa'


caneta = Caneta('Blue', 2)
print(caneta.cor, caneta.tamanho, caneta.cor_tampa)
print(caneta.cor, caneta.tamanho, caneta.cor_tampa)
print(caneta.cor, caneta.tamanho, caneta.cor_tampa)
print(caneta.cor, caneta.tamanho, caneta.cor_tampa)