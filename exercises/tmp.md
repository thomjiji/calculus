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

$$\lim_{x \to -\infty}\frac{4x^2}{6x + 12} = \lim_{x \to -\infty}\frac{4}{6 + 12/x}$$

As $x$ approaches $-\infty$, the fraction approaches $4/6 = 2/3$. Therefore, the limit
of the original expression is:

$$\lim_{x \to -\infty}\frac{\sqrt{4x^4 - x}}{2x^2 + 3} = \frac{2}{3}$$

So, the limit exists and is equal to $2/3$.