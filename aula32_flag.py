"""

Flag (Bandeira) - Marcar um valor
Nome = não valor
is e is not = é ou nao é (tipo, valor, identidade)
id = identidade
"""


condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
  print('Não faça algo')

if passou_no_if is None:
   print('Não passou no if')
else:
   print('Passou no if')