kvadratrod=int(input('indtast det tal der skal findes kvadratrod af:'))
print('Bestemmelse af kvadratroden af',kvadratrod)
print('')

x_resul=int(input('indtast x_0:'))
print('x_0=',x_resul)
for n in range(1,100):
    x_n=x_resul
    x_n_1=n
    x_resul=x_n-((x_n**2)-kvadratrod)/(2*x_n)
    print('x',x_n_1,'=',x_resul)
