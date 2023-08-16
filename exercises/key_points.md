The given expression is:

$$\lim_{x \to -\infty}\frac{\sqrt{4x^4 - x}}{2x^2 + 3}$$

Firstly, let's factor out the largest power of $x$ from the numerator and denominator:

Numerator: $\sqrt{4x^4 - x}$ = $\sqrt{4(x^4) - (x)}$ = $\sqrt{4x^4 - 4x^3 + x}$

Denominator: $2x^2 + 3$

Now, as $x$ approaches $-\infty$, the term $x^4$ becomes negligible compared to $4x^3$.
Therefore, we can simplify the expression as follows:

$$\lim_{x \to -\infty}\frac{\sqrt{4x^4 - x}}{2x^2 + 3} \approx \lim_{x \to
-\infty}\frac{\sqrt{4x^3 - x}}{2x^2 + 3}$$

Since the square root is always positive, we can drop the negative sign on the
numerator:

$$\lim_{x \to -\infty}\frac{\sqrt{4x^3 - x}}{2x^2 + 3} = \lim_{x \to
-\infty}\frac{\sqrt{4x^3}}{2x^2 + 3}$$

As $x$ approaches $-\infty$, the fraction approaches $0/0$, which is an indeterminate
form. However, we can use L'Hopital's rule to find the limit:

Applying L'Hopital's rule, we have:

$$\lim_{x \to -\infty}\frac{\sqrt{4x^3}}{2x^2 + 3} = \lim_{x \to
-\infty}\frac{4x^2}{6x + 12}$$

Cancelling out the common factors of $x^2$ between the numerator and denominator:

$$\lim_{x \to -\infty}\frac{4x^2}{6x + 12} = \lim_{x \to -\infty}\frac{4}{6 +
\frac{12}{x}}$$

As $x$ approaches $-\infty$, the fraction approaches $4/6 = 2/3$. Therefore, the limit
of the original expression is:

$$\lim_{x \to -\infty}\frac{\sqrt{4x^4 - x}}{2x^2 + 3} = \frac{2}{3}$$

So, the limit exists and is equal to $2/3$.

---

### Intermediate Value Theorem (IVT)

If a function `f(x)` is continuous on a closed interval `[a, b]` and k is any number
between `f(a)` and `f(b)`, then there is at least one number c in the interval `[a, b]`
such that `f( c) = k`.

The intermediate value theorem has two conditions:

- Function $f$ is continuous over the interval $[a, b]$.
- The value $d$ lies between $f(a)$ and $f(b)$

We *must* establish these two conditions to conclude that there is a value $c$ in
the interval $[a, b]$ for which $g(x) = d$ (another way to phrase this conclusion is
that the equation $g(x) = d$ has a solution where $a <= x <= b$).

---

### Property of limits of composite functions

If $u$ are functions such that $\displaystyle\lim_{x \to c} u(x) = L$ and
$\displaystyle\lim_{x \to L} u(x) = u(L)$ (which means both limits exist and $u$ is
continuous at $x = L$), then

$$\displaystyle\lim_{x \to c} u(u(x)) = u(\lim_{x \to c} u(x)) = u(L)$$

---

### Squeeze Theorem

The *squeeze theorem* tells us that if we have three function $f$, $g$, and $h$ such
that...

- $g(x) <= f(x) <= h(x)$ for all $x$-values other than $x = c$ in an interval round
  $x = c$, and
- $\displaystyle\lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L$

Then we can conclude that $\displaystyle\lim_{x \to c} f(x) = L$.

---

### Derivative of Function

The derivative of function $f$ at the point where $x = a$ is defined by:

$$f'(a) = \lim_{{h \to 0}} \frac{{f(a + h) - f(a)}}{h}$$

The alternative form is:

$$f'(a) = \lim_{{x \to a}} \frac{{f(x) - f(a)}}{x - a}$$

---

The whole underlying idea of the formal definition of limits is to find the slope of the
secant line between these two points, and then take the limit as $h$ approaches 0. And
the secant line is going to become a better and better approximation of the tangent line
at x.

---

### Differentiability Implies Continuity

There are three cases where a function is *not differentiable*:

1. Wherever the function isn't continuous
2. Wherever the graph of the function has a *vertical* tangent line
3. Wherever the graph of the function has a sharp turn

---

- In order to be differentiable, you need to be continuous. You can't have
  differentiable but not continuous.
- In order to be continuous, $\displaystyle f(a) = \lim_{{x \to a}} f(x)$. Two
  one-sided limits exist, and are equal to $f(a)$.
- In order to be differentiable,
  $\displaystyle \lim_{{x \to a}} \frac{{f(x) - f(a)}}{x - a}$ needs to exist.

If a function is differentiable then it's also continuous. This property is very useful
when working with functions, because if we know that a function is differentiable, we
immediately know that it's also continuous.

---

### Proof of "Differentiability implies continuity"

$$
(1) \lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} = f'(c) \\
(2) \lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} \cdot \lim_{{x \to c}} (x - c) =
f'(c) \cdot \lim_{{x \to c}} (x - c) \\
(3) \lim_{{x \to c}} (x - c) = 0 \\
\text{From (2) and (3) we have} \\
(4) \lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} \cdot \lim_{{x \to c}} (x - c) =
f'(c) \cdot 0 \\
\text{From (4) and the rule about limit multiplication we have} \\
(5) \lim_{{x \to c}} \left(\frac{{f(x) - f(c)}}{{x - c}} \cdot (x - c)\right) = 0 \\
(6) \lim_{{x \to c}} (f(x) - f(c)) = 0 \\
(7) \lim_{{x \to c}} f(x) - \lim_{{x \to c}} f(c) = 0 \\
(8) \lim_{{x \to c}} f(x) - f(c) = 0 \\
(9) \lim_{{x \to c}} f(x) = f(c)
$$

Proof breakdown:

In the following, let's assume $f$ is differentiable at $c$.

1. Differentiability

   By definition, a function $f$ is differentiable at $c$ if the following limit exists:

   $$ f'(c) = \lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} $$

   This means the rate of change of $f$ at point $c$ exists and is finite.

2. Rewriting the limit in continuity form

   We multiply and divide by $(x - c)$ to form the limit that defines continuity:

   $$
   \lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} \cdot \lim_{{x \to c}} (x - c) = f'(c)
    \cdot \lim_{{x \to c}} (x - c)
   $$

   Here, we just rewrote $f'(c)$ in a form that involves $(x - c)$, without altering its
   value.

3. Setting limit to 0 The limit as $x$ approaches $c$ for $(x - c)$ is 0:

   $$ \lim_{{x \to c}} (x - c) = 0 $$

   Hence, the right-side of the equation above becomes $f'(c) * 0 = 0$.

4. Multiplication law of limits

   Using the multiplication law of limits, which states that the limit of a product of
   two functions is the product of their limits (provided they exist), we can write:

   $$ \lim_{{x \to c}} \left( \frac{{f(x) - f(c)}}{{x - c}} \cdot (x - c) \right) = 0 $$

5. Simplify the limit Within the limit on the left side, (x - c) cancels out, leaving:

   $$ \lim_{{x \to c}} (f(x) - f(c)) = 0 $$

6. Difference law of limits The difference law of limits allows us to say:

   $$ \lim_{{x \to c}} f(x) - \lim_{{x \to c}} f(c) = 0 $$

7. Constant rule of limits The limit of a constant is that constant:

   $$ \lim_{{x \to c}} f(x) - f(c) = 0 $$

   Leading to:

   $$ \lim_{{x \to c}} f(x) = f(c) $$

8. Continuity

   By definition, a function f is continuous at c if:

   $$ \lim_{{x \to c}} f(x) = f(c) $$

Therefore, f is continuous at c.

---

### General Form Property of Exponents

The general form property of exponents is defined as follows:

$$a^{\frac{m}{n}} = \sqrt[n]{a^m}$$

So you can write $\sqrt[5]{x^3}$ as $x^{\frac{3}{5}}$.

---

### The Power Rule | Derivative

The power rule:

$$
\frac{d}{dx} [x^n] = n x^{n-1}, \quad \text{for all } n \in \mathbb{R}
$$

---