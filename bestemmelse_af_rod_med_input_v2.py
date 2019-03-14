kvadratrod=int(input('indtast det tal der skal findes kvadratrod af:'))
print('Bestemmelse af kvadratroden af',kvadratrod)
print('se graf for valg af x_0. Når x_0 er valgt lukkes grafen')
#print('f(x)=x**2-',kvadratrod)
#print('f/(x)=2*x')
print('')

x_resul=int(input('indtast x_0:'))
print('x_0=',x_resul)
for n in range(1,10):
    x_n=x_resul
    x_n_1=n
    x_resul=x_n-((x_n**2)-kvadratrod)/(2*x_n)
    #print('x',x_n_1,'=',x_resul)
    if x_n - x_resul <0.0000000000001 and x_n - x_resul > -0.0000000000001:
        print('endeligt resultat:', x_resul)
        print('test af resultat')
        print(x_resul,'*',x_resul,'=',x_resul**2)
        if x_resul**2==kvadratrod:
            print('den funde kvadratrod er korrekt')
        else:
            print('den funde kvadratrod er tilmærmelsesvis korrekt')
        break
