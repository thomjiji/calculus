<details>
<summary>Calculating the Limit of a Complex Rational Fraction</summary>
<br>

The given paragraph demonstrates the step-by-step process to assess the limit of a
complex rational function, specified as:

$$\lim_{x \to -\infty}\frac{\sqrt{4x^4 - x}}{2x^2 + 3}$$

The steps involve factoring out dominant terms, simplification using limits rules,
handling of the indeterminate form of type '0/0' and finally the application of
L'Hopital's rule, which aids in the determination of limits which reach the
indeterminate state.

After following these methodologies and taking advantage of limit properties centred
around indeterminate forms and infinite behavior, it is deduced that the limit of the
original expression is `2/3`. Thus, through the process of simplifying the expression,
the paragraph showcases how to handle complex limits and use L'Hopital’s rule to
evaluate the limit.

**Details**:

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

</details>
<details>
<summary>Proof of "Differentiability implies continuity"</summary>
<br>

(1)

$$
\lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} = f'(c)
$$

(2)

$$
\lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} \cdot \lim_{{x \to c}} (x - c) =
f'(c) \cdot \lim_{{x \to c}} (x - c)
$$

(3)

$$
\lim_{{x \to c}} (x - c) = 0
$$

We have the following from expressions (2) and (3)

(4)

$$
\lim_{{x \to c}} \frac{{f(x) - f(c)}}{{x - c}} \cdot \lim_{{x \to c}} (x - c) =
f'(c) \cdot 0
$$

From expression (4) and the rule about limit multiplication we have

(5)

$$
\lim_{{x \to c}} \left(\frac{{f(x) - f(c)}}{{x - c}} \cdot (x - c)\right) = 0
$$

(6)

$$
\lim_{{x \to c}} (f(x) - f(c)) = 0
$$

(7)

$$
\lim_{{x \to c}} f(x) - \lim_{{x \to c}} f(c) = 0
$$

(8)

$$
\lim_{{x \to c}} f(x) - f(c) = 0
$$

(9)

$$
\lim_{{x \to c}} f(x) = f(c)
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

   By definition, a function $f$ is continuous at $c$ if:

   $$ \lim_{{x \to c}} f(x) = f(c) $$

Therefore, $f$ is continuous at $c$.

</details>

Here is another example that makes me think about the meaning of implicit
differentiation and what it can bring to us:

"A 10-meter ladder is sliding down a vertical wall, so the distance between the top of
the ladder and the ground is decreasing at 3 meters per minute. At a certain instant,
the bottom of the ladder is 6 meters from the wall. What's the rate of change of the
area formed by the ladder at that instant (in square meters per minute)?"

In this question, I set the distance between the top of the ladder and the ground as y,
the bottom of the ladder from the wall is x, the certain point (that instant) as t_0,
the ares formed is A. Then we have these know information:

1. y’(t) = -3 meters/minute;
2. x(t_0) = 6 m;
3. The length of the ladder is 10 m;
4. y(t_0) = sqrt(10^2 - 6^2) = 8 m.

What we seek for is A’(t_0). For that, we have to figure out A’(t). Here is the key
point: we know A(t) = (x(t) * y(t)) / 2, it’s the relationship between right triangle’s
sides. We take derivative on both sides on equation, then we can get the relationship of
their derivatives. One of the derivatives is exactly what we're seeking for, A’(t).