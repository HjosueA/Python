# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

lista1= [(1, 2, 3, 45.00), (1, 3, 3, 24.00)]
lista2 =[]
total = 0
for n in lista1:
    item1= n[1]
    total += n[3]
    
    dict={
        'item1':item1,
    }
    lista2.append(dict)

dict2={
    'suma_total':total
}
lista2.append(dict2)

    
print(lista2)
