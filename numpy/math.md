# markdown测试

# title1

## tiltle2

### title3

#### 数学输入模式
* 位于$$之间时，开启数学输入模式
* 空格，白字符不起作用。除非使用特殊符号\quad
* 每个公式只有一行
---

reference
https://en.wikibooks.org/wiki/LaTeX/Mathematics

---

> 内联公式
$f(x)=a+b$

---


>独立公式

$$
f(x) = \int_{-\infty}^\infty \hat f(\xi)\,e^{2 \pi \xi x} \,d\xi
$$

$$
\left(\frac{x^2}{y^3}\right)
$$

不支持：\middle |
$$
P \left(A=2 | \frac{A^2}{B}>4\right)
$$

$$
\left\{\frac{x^2}{y^3}\right\}
$$

---
括号

$$
( a ), [ b ], \{ c \}, | d |, \| e \|,
\langle f \rangle, \lfloor g \rfloor,
\lceil h \rceil, \ulcorner i \urcorner,
/ j \backslash
$$

---

上标 
$x^4$ 
$10^{10}$
$\vec x$
$\vec {xyz}$

下标 $x_2$

---
$$ k_{n+1} = n^2 + k_n^2 - k_{n-1}$$

$$f(n) = n^5 + 4n^3 + 2|_{n=17}$$

---

$$\binom{n}{k} = \frac{n!}{k!(nk)!}$$

$$\frac{\displaystyle \frac{1}{x} + \frac{1}{y}}{y-z}$$

$$^3/_7$$

$$x^\frac{1}{2}$$

$$
x = \frac
$$
---


除法 $\frac{x+y}{y+z}$

字体控制 $\displaystyle \frac{x+y}{y+z}$

---

$$
\frac{1}{\displaystyle x+\frac{1}{y}}
$$

---
括号
$\langle \rangle$
$\displaystyle ({\frac{x}{y}})$

---
$$ 
\sqrt[a]{b}
$$

$$
\sqrt{\frac{x}{y}}
$$

$$
\sqrt[n]{1+x^2+x^3+...+x^n}
$$

---
下划线 $\underline{x+y}$

---
$ a mod b$

$a \pmod b$

$$x \equiv a \pmod {b}$$


---
求和

$$
\sum_{i=0}^Na_i
$$


$$
\prod_{i=1}^n a_i
$$
---

积分
$$
\int_a^bg(t)dt
$$

$$
\int_0^{\infty}{fxdx}
$$

$$
\int_0^{\infty} \mathrm{e}^{-x} \mathrm{d}x
$$


---
$$\lim_{x \to 0}$$

$$\lim_{x \to \infty}\exp(-x) = 0$$

---


---
$$
\alpha \beta \gamma \delta

\epsilon \zeta \theta \lambda

\sigma \omega
$$

$$
\ Alpha
$$


---

$\forall x \in X, \quad \exists y \leq \epsilon$

---
$$
cos(2\theta) = cos^2(\theta) - sin^2(\theta)
$$

---

占位符

一个空格 $x \quad y$

两个空格 $x \qquad y$

---
matrix:
$$
\begin{matrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots  & \vdots  & \ddots & \vdots \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n} \\
\end{matrix}
$$

$$
A_{m,n} = 
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
 \end{pmatrix}
$$

$$
M = \begin{bmatrix}
       \frac{5}{6} & \frac{1}{6} & 0           \\
       \frac{5}{6} & 0           & \frac{1}{6} \\
       0           & \frac{5}{6} & \frac{1}{6}
     \end{bmatrix}

$$

$$
 \dot{a} 
 \ddot{a} 
 \bar{a} 
 \grave{a} 
 \acute{a} 
 a' a'' a''' a'''' 
 \hat{a}
 $$

$$
\check{a}
\vec{a}
\tilde{a}
\overline{a}
\underline{a}
$$

$$
\pm \mp
$$

$$
f(n) =
  \begin{cases}
    n/2       & \quad \text{if n is even}\\
    -(n+1)/2  & \quad \text{if n is odd}
  \end{cases}
$$

$$
f(n) =
  \begin{cases}
    n/2       & \quad \text{if } n \text{ is even}\\
    -(n+1)/2  & \quad \text{if } n \text{ is odd}
  \end{cases}
$$

$$
\left(
    \begin{array}{c}
      n \\
      r
    \end{array}
  \right) = \frac{n!}{r!(n-r)!}
$$

$$
\left(
    \begin{array}{c}
      n \\
      r
    \end{array}
  \right) = \frac{n!}{r!(n-r)!}
$$
