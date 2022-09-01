'''
@autores:
    Euller Francisco Alvarado Vargas
        ealvarado@unal.edu.co
    Ruben Dario Ariza Noriega
        rariza@unal.edu.co
    Albeiro Junior Díaz Oquendo
        adiazoq@unal.edu.co
'''
#TALLER 3
#Ejercicios 5

# Punto 1
print("Hello World!")

# Punto 2
x = 5
y = 7
c= (x+y)/2
print(c)

# Punto 3
import numpy as np
a = np.array([1,2,3,4,5])
print(a)

# Punto 4
from statistics import mean
b = np.array([6,7,8,9])
print("El promedio del vector b es:", float(mean(b)))

# Punto 5
import numpy as np
c = np.array([12, 7, 6, 11, 2, 9, 15, 5, 14])
np.amin(c) #Valor minimo
np.amax(c) #Valor maximo

# Punto 6
def maximo_minimo(numeros):
    if len (numeros)>0:
        mayor = numeros[0]
        menor = numeros[0]
        
        for n in numeros:
            if n > mayor:
                mayor = n
            
            if n < menor:
                menor = n
        
        return mayor, menor
    else:
        return None
    
vec_1 = np.array([10,5,3,2,8,6])

print(maximo_minimo(vec_1))

# Punto 7
import numpy as np
a = np.random.normal(0,1,100)
print(a)

# Punto 8
import numpy as np
a = np.random.normal(0,1,100)
a_abs = np.abs(a)
a_b = a[a_abs>1]
print(a_b)

# Punto 9
import numpy as np
a = np.random.normal(0, 1, 100)
vp = a.copy()
vp[np.arange(0,100,10)] = np.nan
print(vp)

# Punto 10
a = np.random.normal(0, 1, 100)
vp = a.copy()
vp[np.arange(0,100,10)] = np.nan
pm = vp[np.logical_not(np.isnan(vp))]
m = mean(pm)
vp[np.arange(0,100,10)] = m
print(vp)
print(m)

#_______________________________________________________
#-------------------------------------------------------
           
#TALLER 3
#Ejercicios 6

# Punto 1
import matplotlib.pyplot as plt 
a1 = np.random.normal(-5,1,5000 )
a2 = np.random.normal(3, 0.5, 5000 )
a1a2 = np.concatenate((a1,a2), axis=0)
print(len(a1a2))
plt.hist(a1a2)
plt.show()

# Punto 2
vec1 = np.array([[1],[2],[3],[4],[5]])
vec2 = np.array([[6],[7],[8],[9],[10]])
vec3 = np.array([[11],[12],[13],[14],[15]])
vec4 = np.array([[16],[17],[18],[19],[20]])
vec5 = np.array([[21],[22],[23],[24],[25]])
vg = np.hstack((vec1,vec2,vec3,vec4,vec5))
print(vg)
print(f"Numero de filas: {len(vg)}, "
      f"Numero de columnas: {len(vg[0])}")

# Punto 3
import numpy as np

vec_1 = np.array([1,2,3,4,5])
vec_2 = np.array([6,7,8,9,10])
vec_3 = np.array([11,12,13,14,15])
vec_4 = np.array([16,17,18,19,20])
vec_5 = np.array([21,22,23,24,25])
vec_6 = np.array([26,27,28,29,30])
vec_7 = np.array([31,32,33,34,35])
vec_8 = np.array([36,37,38,39,40])
vec_9 = np.array([41,42,43,44,45])
vec_10 = np.array([46,47,48,49,50])

vg2 = np.vstack((vec_1,vec_2,vec_3,vec_4,vec_5,vec_6,vec_7,vec_8,vec_9,vec_10))
print(vg2)
print(f"Numero de filas: {len(vg2)}, "
      f"Numero de columnas: {len(vg2[0])}")

# Punto 4
import numpy as np
A = np.random.randint(20, size = (10,10))
B = np.random.randint(20, size =(10,2) )
print(A)
print(B)
print(np.dot(A,B))

# Punto 5
import numpy as np
A = np.random.randint(20, size = (10,10))
inver = np.linalg.inv(A)
Inv = np.dot(A,inver)
print(np.round(Inv))

# Punto 6
import pandas as pd

mi_df = pd.DataFrame(data={"entero": range(1,5),
                           "factor": ["a", "b", "c", "d"],
                           "cadena": ["a", "b", "c", "d"]
})

nueva_columna = mi_df.assign( numero = [1.3,3.4,4.5,5.6])

print(mi_df)
print((nueva_columna))

# Punto 7
df = pd.DataFrame([[4, 9]] * 3,
                  columns = ["A", "B"])
print(df)
print(df.apply(np.sqrt)) #Sucede que nos muestra la raíz cuadrada de los valores

# Punto 8
x = np.random.normal(-10,2,500)
y = np.random.normal(10,2,500)
z = np.concatenate((x,y))

q = {'normal_1' : np.random.normal(-10,2,1000),
     'normal_2' : np.random.normal(10,2,1000),
     'bimodal' : z }

mi_df = pd.DataFrame(data = q)

print(mi_df)
print(len(mi_df))











