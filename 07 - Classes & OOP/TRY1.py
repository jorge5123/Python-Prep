from herramientas import Herramientas

h = Herramientas([1,0,2,5,8,8,9,11,15,16,16,16,18,20])
h.conversion_grados('celsius','farenheit')
h.verifica_primo()
moda, repe = h.valor_modal(False)
print('El valor modal es', moda, 'y se reptie', repe, 'veces')
h.factorial()