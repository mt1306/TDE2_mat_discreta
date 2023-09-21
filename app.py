##Usando a biblioteca Sympy
from sympy import *

#a funcao lambda entende o parametro como uma funcao (nesse caso com x sendo a variavel dependente)
def compose(f, g):
    return lambda x: f(g(x))

# Função f(x)
f_expr = '3*x-1'
print(f"f(x) eh {f_expr}")
f = lambdify(Symbol('x'), sympify(f_expr))

# Função g(x)
g_expr = 'x+2'
print(f"f(x) eh {g_expr}")
g = lambdify(Symbol('x'), sympify(g_expr))

valor_de_x = 4
print(f"o valor de x eh {valor_de_x}")


g_de_f = compose(g, f)
g_de_g = compose(g, g)
f_de_f = compose(f, f)
f_de_g = compose(f, g)

x = Symbol('x')
print(f"g ° f(x) = {g_de_f(x)}")
print(f"substituindo x na funcao acima temos = {g_de_f(x).subs(x,valor_de_x)}")
print(f"g ° g(x) = {g_de_g(x)}")
print(f"substituindo x na funcao acima temos = {g_de_g(x).subs(x,valor_de_x)}")
print(f"f ° f(x) = {f_de_f(x)}")
print(f"substituindo x na funcao acima temos = {f_de_f(x).subs(x,valor_de_x)}")
print(f"f ° g(x) = {f_de_g(x)}")
print(f"substituindo x na funcao acima temos = {f_de_g(x).subs(x,valor_de_x)}" + "\n")