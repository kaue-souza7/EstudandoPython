# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅]

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, menssagem):
        self.mensagem = menssagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotifiçãoEmail(Notificacao):

    def enviar(self) -> bool:
        print('E-mail, enviado - ', self.mensagem)
        return True


class NotifiçãoSMS(Notificacao):

    def enviar(self) -> bool:
        print('SMS, enviado - ', self.mensagem)
        return True

def notificar(notificacao: Notificacao):
    notificacao_eviada = notificacao.enviar()

    if notificacao_eviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificar(NotifiçãoEmail('TESTANDO EMAIL'))
notificar(NotifiçãoSMS('TESTANDO SMS'))
