# Entregaporparejas

### Ejercicio c. Puzle
    
    Código:
    
    ```
        class A: 
        def z(self): 
            return self 
    
        def y(self, t): 
            return len(t) 
    
        a = A 
        y = a.z 
        print(y(a)) 
        aa = a() 
        print(aa is a()) 
        z = aa.y 
        print(z(())) 
        print(a().y((a,))) 
        print(A.y(aa, (a,z))) 
        print(aa.y((z,1,'z'))) 
    ```
Explicación:

print(y(a)) = esta devolviendo el valor a, que es un elemento de la clase A

print(aa is a()) = retorna falso, porque son dos clases de A pero podrían pedir distintos atributos

print(z(())) = es un elemento de una clase, por lo que su longitud f sera 0

print(a().y((a,))) = la longitud es 1

print(A.y(aa, (a,z))) = la longitud es 2

print(aa.y((z,1,'z'))) = la longitud es 3