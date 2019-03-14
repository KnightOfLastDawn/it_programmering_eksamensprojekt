x_n=4
x_resul=4
print('Bestemmelse af kvadratroden af 2')
print('f(x)=x**2-2')
print('f/(x)=2*x')
print('')
print('x 0=',x_n)
for n in range(1,10):
    x_n=x_resul
    x_n_1=n
    x_resul=x_n-((x_n**2)-2)/(2*x_n)
    print('x',x_n_1,'=',x_resul)
    if x_n - x_resul <0.000000000001 and x_n - x_resul > -0.000000000001:
        print('endeligt resultat:', x_resul)
        break
