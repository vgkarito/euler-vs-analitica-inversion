# euler-vs-analitica-inversion
Comparación entre la solución analítica usando separación de variables y la aproximación numérica con el método de Euler, para el crecimiento de una inversión con interés continuo, dy/dt = k·y.

## Problema

Se modela el crecimiento de una inversión de $1000 con una tasa de interés continuo k = 0.5, mediante la ecuación diferencial:

dy/dt = k·y, con y(0) = 1000

## Solución analítica

Separando variables e integrando:

dy/y = k dt → ln(y) = kt + C → y(t) = 1000·e^(0.5t)

## Solución numérica (método de Euler)

Se aproxima la solución en el intervalo t ∈ [0,1] con paso h = 0.2, usando la fórmula:

y_(n+1) = y_n + h·f(t_n, y_n)

## Código

Ver `euler_vs_analitica.py`
