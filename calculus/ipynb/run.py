"""General block to calculate derivative."""

from sympy import (
    symbols,
    diff,
    latex,
    ln,
    solve,
    Eq,
    solveset,
    S,
    Rational,
    simplify,
    N,
    sqrt,
    root,
    expand,
    factor,
)

x = symbols("x")

f = x**4 + 4 * x**3 - 18 * x**2

f_prime = diff(f, x)

f_subs = f.subs(x, 5)

critical_points = solve(Eq(f, 0), x)

undefined_points = solveset(Eq(f_prime, S.NaN), x)

print(f"$$ {latex(diff(f_prime))} $$")
# print(N(ln(2) / 4))
print(factor(12 * x**2 + 24 * x - 36))
