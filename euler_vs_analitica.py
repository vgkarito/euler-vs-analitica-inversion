import math

# Problema: dy/dt = k*y, y(0) = 1000 (inversion con interes continuo)
k = 0.5
y0 = 1000
t0 = 0
t_final = 1
h = 0.2

def f(t, y):
    return k * y

def solucion_analitica(t):
    return y0 * math.exp(k * t)

def euler(t0, y0, t_final, h):
    t = t0
    y = y0
    resultados = [(t, y)]
    while t < t_final:
        y = y + h * f(t, y)
        t = t + h
        resultados.append((round(t, 2), round(y, 4)))
    return resultados

resultados_euler = euler(t0, y0, t_final, h)

print("t\tEuler\t\tAnalitica")
for t, y_euler in resultados_euler:
    y_exacta = round(solucion_analitica(t), 4)
    print(f"{t}\t{y_euler}\t\t{y_exacta}")
