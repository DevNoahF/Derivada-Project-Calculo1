import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Input do user
symbol_variable = sp.Symbol('x')
expr_input = input("Digite a função f(x): ")

# Correção para entradas como x3 → transforma em x*3
expr_input = expr_input.replace("x", "*x").replace("*xx", "x")
expr_input = expr_input.lstrip("*")

# Converte para expressão SymPy
try:   # TODO FIX: erro de transformação de x3 -> x**3 continua
    input_conversion = sp.sympify(expr_input)
except Exception:
    print("Função inválida. Use exemplo como: x**2 + 3*x - 1 ou sin(x).")
    exit()

# Calcula derivada
input_deriv = sp.diff(input_conversion, symbol_variable)
input_deriv_dervi = sp.diff(input_deriv, symbol_variable)

print(f"\nDerivada de f(x): {input_deriv}")
print(f"\nDerivada de f'(x): {input_deriv_dervi}")

# Pontos críticos
search_mark_points = sp.solve(sp.Eq(input_deriv, 0), symbol_variable)
print(f"\nPontos críticos: {search_mark_points}")

# Converte para função numérica
expression_convert = sp.lambdify(symbol_variable, input_conversion, 'numpy')
expression_convert_deriv = sp.lambdify(symbol_variable, input_deriv, 'numpy')

# Segundo derivada para gráfico
input_second_deriv = sp.diff(input_deriv, symbol_variable)
expression_convert_second = sp.lambdify(symbol_variable, input_second_deriv, 'numpy')

# Intervalo para gráfico
x_vals = np.linspace(-10, 10, 500)
y_vals = expression_convert(x_vals)
y_deriv_vals = expression_convert_deriv(x_vals)
y_second_vals = expression_convert_second(x_vals)

# Plotagem
plt.figure(figsize=(10,6))
plt.plot(x_vals, y_vals, label=f"$f(x) = {sp.latex(input_conversion)}$", color='blue')
plt.plot(x_vals, y_deriv_vals, label=f"$f'(x) = {sp.latex(input_deriv)}$", color='red', linestyle='--')
plt.plot(x_vals, y_second_vals, label=f"$f''(x) = {sp.latex(input_second_deriv)}$", color='green', linestyle='-.')

# Marca pontos críticos
for p in search_mark_points:
    p_val = float(p)
    plt.scatter(p_val, expression_convert(p_val), color='purple')
    plt.text(p_val, expression_convert(p_val), f" x={p_val:.2f}", color='purple')

plt.title("Visualizador de Funções e Derivadas")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
