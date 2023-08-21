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

If a function $f(x)$ is continuous on a closed interval $[a, b]$ and $k$ is any number
between $f(a)$ and $f(b)$, then there is at least one number $c$ in the interval
$[a, b]$ such that $f( c) = k$.

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

   $$
   \lim_{{x \to c}} (x - c) = 0
   $$

   Hence, the right-side of the equation above becomes $f'(c) * 0 = 0$.

4. Multiplication law of limits

   Using the multiplication law of limits, which states that the limit of a product of
   two functions is the product of their limits (provided they exist), we can write:

   $$ \lim_{{x \to c}} \left[ \frac{{f(x) - f(c)}}{{x - c}} \cdot (x - c) \right] = 0 $$

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

### Differentiation Rules

| Rules                  | Expression                                                                                                                      |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Constant rule          | $\frac{d}{dx}(k) = 0$                                                                                                           |
| Constant multiple rule | $\frac{d}{dx}[k \cdot f(x)] = k \cdot f'(x)$                                                                                    |
| Sum rule               | $\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)$                                                                                     |
| Difference rule        | $\frac{d}{dx}[f(x) - g(x)] = f'(x) - g'(x)$                                                                                     |
| Power Rule             | $\frac{d}{dx} (x^n) = n x^{n-1}$                                                                                                |
| Product Rule           | $\frac{d}{dx} [f(x) \cdot g(x)] = \frac{d}{dx}[f(x)] \cdot g(x) + f(x) \cdot \frac{d}{dx}[g(x)]$                                |
| Quotient Rule          | $\frac{d}{dx} \left[\frac{f(x)}{g(x)}\right] = \frac{\frac{d}{dx} [f(x)] \cdot g(x) -f(x) \cdot \frac{d}{dx}[g(x)]} {[g(x)]^2}$ |

---

### Chain Rule

If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then the composite
function $F = f \circ g$ defined by $F(x) = f(g(x))$ is differentiable at $x$ and
$F\prime$ is given by the product

$$
F\prime[f(g(x))] = f\prime(g(x)) \cdot g\prime(x)
$$

if $y = f(u)$ and $u = g(x)$ are both differentiable functions, then

$$
\frac{dy}{dx} = \frac{dv}{du} \cdot \frac{du}{dx}
$$

### Derivatives of the Trigonometric Functions

$$ \frac{d}{dx} [\sin (x)] = \cos(x) $$
$$ \frac{d}{dx} [\cos (x)] = -\sin(x) $$

$$
\frac{d}{dx} [\tan (x)] = \frac{d}{dx} \left [\frac{\sin(x)}{\cos(x)} \right] = \frac
{\cos(x) \cdot \cos(x) - \sin(x) \cdot (-\sin(x))}{\cos^2(x)} = \frac{1}{\cos^2(x)} =
\sec^2(x)
$$

$$
\frac{d}{dx} [\cot (x)] = \frac{d}{dx} \left[\frac{\cos(x)}{\sin(x)}\right] =
\frac{-\sin(x) \cdot \sin(x) - \cos(x) \cdot (\cos(x))}{\sin^2(x)} = -\frac{1}
{\sin^2(x)} = -\csc^2(x)
$$

$$ \frac{d}{dx} [\csc (x)] = -\frac{\cos(x)}{\sin^2(x)} = -\csc(x) \cdot \cot(x) $$
$$ \frac{d}{dx} [\sec (x)] = \frac{\sin(x)}{\cos^2(x)} = \sec(x) \cdot \tan(x) $$

#### Two Special Trigonometric Limits

$$
\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1 \\
\lim_{\theta \to 0} \frac{\cos \theta - 1}{\theta} = 0 \\
$$

### Derivative of $e$

$$ \frac{d}{dx} e^x = e^x $$

### Derivative of $\ln(x)$

$$ \frac{d}{dx} [\ln(x)] = \frac{1}{x} $$

### Composite and combined functions

A composite function is where we make the output from one function, such as $u$, the
input for another function, such as $w$.

We can also combine functions using arithmetic operations, but such a combination is not
considered a composite function.

Our two functions appear to be $x-8$ and $e^x$, but neither of them _takes the other
as its input_.

### Derivatives of General Exponential Functions

If $b$ is a constant, then

$$ \frac{d}{dx} (b^x) = \ln(b) \cdot b^x $$

### Derivatives of General Logarithmic Functions

If $a$ is a constant, $a \neq 1$, then

$$ \frac{d}{dx} \left[\log_a(x)\right] = \frac{1}{\ln(a) \cdot x} $$

---

$$ \frac{d}{dx} \left[\ln(u(x)) \right] = \frac{u\prime(x)}{u(x)} $$

### Derivative of Inverse Function

Let's say $f(x)$ and $g(x)$ are inverse function (and both are differentiable), so by
definition, we have this equation:

$$ f(g(x)) = x $$

We take derivative of both sides:

$$ \frac{d}{dx} f(g(x)) = \frac{d}{dx} (x)$$

Use chain rule to the left-hand side, right-hand side equals to 1. Finally, we get:

$$ f'(x) = \frac{1}{g'(f(x))} $$

### Derivative of Inverse Sine, Cosine, Tangent

$$\frac{d}{dx} \left[\sin^{-1}(x)\right] = \frac{1}{\sqrt{1 - x^2}} $$

$$\frac{d}{dx} \left[\cos^{-1}(x)\right] = -\frac{1}{\sqrt{1 - x^2}} $$

$$\frac{d}{dx} \left[\tan^{-1}(x)\right] = \frac{1}{1 + x^2} $$

---

### Interpret motion graph

The direction of movement is indicated by the velocity's sign:

- If the velocity is positive, the object is moving forward.
- If the velocity is negative, the object is moving backward.
- If the velocity is zero, the object is not moving.

The direction of the position graph indicates the direction of movement:

- If the graph is increasing, the object is moving forward.
- If the graph is decreasing, the object is moving backward.
- If the graph is nether increasing not decreasing, the object is not moving. This
  happens at extremum points of the graph.

Velocity as a function of time is the derivative of position:

$$ v(t) = x'(t) $$

Acceleration as a function of time is the derivative of velocity, which is the second
derivative of position:

$$ a(t) = v'(t) = x''(t) $$

#### Velocity and Acceleration

Velocity: The rate of change of _displacement_ (位移) with respect to time.

Acceleration: The instantaneous rate of change of _velocity_ with respect to time.

| Velocity | Acceleration | Speed      |
|----------|--------------|------------|
| Positive | Positive     | Increasing |
| Negative | Negative     | Increasing |
| Positive | Negative     | Decreasing |
| Negative | Positive     | Decreasing |

If the acceleration is positive, and velocity is positive, that means the magnitude
of velocity is increasing, so that means the speed is increasing.

If the acceleration is negative, and the velocity is also negative, that also means the
speed is increasing.

But the velocity and acceleration have different signs, that mean the speed is
decreasing.