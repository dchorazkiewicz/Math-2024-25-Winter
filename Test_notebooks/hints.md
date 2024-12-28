# Intelligent use of ChatGPT

- ChatGPT is **NOT TO AVOID WORK**! Instead, it is to **help you** understand problems better and improve your work.

- Don't reduce yourself to the protein proxy mindlessly copy-pasting between one window and another.

- Engage with the material, ask for explanations, and use ChatGPT to enhance your understanding and general presentation. Read what ChatGPT gives you! Master this tool! Soon it will be required everywhere. Be ahead of the curve.

## Guidelines for Effective Use

- Generate notes/solutions in Markdown Code! Use ChatGPT to create markdown code for notes that can be easily pasted into platforms like Google Colab (*.ipynb) or markdown files (*.md).

- Often ChatGPT will give you markdown code that is not perfect. For example rendering of math formulas in markdown require extra command added to your prompts.

```markdown
"In markdown code, use single and double dollars $...$ and $$...$$ for math formulas!"
```

## Ask first for useful formulas, definitions and not for the solutions!

```markdown
I have a list of problems below:

---
 
## 19. Limits of Sequences
 
1. Calculate:
   - $\displaystyle \lim_{n \to \infty} \frac{n^2 + 3n}{2 n^2 - 2n}$
 
   - $\displaystyle \lim_{n \to \infty} \frac{(2n+3)^3}{n^3-1}$
 
2. Prove using the squeeze theorem:
   - $\displaystyle\lim_{n \to \infty} \frac{\sin(n)}{n}$
 
4. Find the limit of the sequence:
   - $a_n = (1+\frac{1}{n})^n$
 
## 20. Limits of Real Functions
 
1. Compute:
   - $\displaystyle\lim_{x \to \infty} \frac{x^3 + 2x^2}{x^4 - 3x^3}$
 
2. Find:
   - $\displaystyle \lim_{x \to 0} \frac{\sin(3x)}{2x+1}$.
 
4. Find the asymptotes of the function:
   - $f(x) = \frac{x^2 - 1}{x^2 + 1}$
   - $g(x) = \frac{\sin(x)}{x^2+1}$

---
Give me markdown code for notes having useful formulas and definitions assigned to each problem that will help me to solve these problems. 

Use single and double dollars $...$ and $$...$$ for math formulas!
```

## Request step-by-step explanations

 - Once you have the formulas, ask for concise and clear explanations.

```markdown
I have a list of problems below:

---
Yadi Yadi Yada 
---
Give me (short/concise/clear) step-by-step explanation for each problem. Write me note in markdown code using single and double dollars $...$ and $$...$$ for math formulas!
```

## Request explanations in your native language

```markdown
Please explain in my native (Turkish/Spanish/...) language the definition of the Derivative.
```

- Aftewards ask for the short note in English in markdown code that you could use for the class.

## Simplify Concepts for Better Understanding

- Ask for explanations as if you were a beginner.

```markdown
Please explain to me as if I were a 10-year-old the definition of the Integral.
```

## Enhance Your Notes
   - If your notes are messy or incomplete, ask ChatGPT to improve them.

```markdown
I have my very sketchy and messy notes below:

---
Lalala
---

Please, make them more readable, understandable, and beautifully formatted.
Use nice markdown code with single and double dollars $...$ and $$...$$ for
math formulas!
```

## Convert handwritten notes to markdown

```markdown
I have photo of my handwritten notes. Convert them to markdown code with single and double dollars $...$ and $$...$$ for math formulas! Check and correct the formulas if needed.

[INCLUDE PHOTO OF YOUR HANDWRITTEN NOTES]
```

## Get solutions with visualizations

```markdown
I need markdown notes with solutions and visualizations in GeoGebra. Provide step-by-step instructions for GeoGebra visualization.

Find the intersection points of the hyperbola $x^2 - y^2 = 1$ with the ellipse's line $x^2 + 4y^2 = 6$.
```

## Tables make information more structured and easier to reference.

```markdown
Give me a table with columns: the commands in markdown, descriptions, and examples.

Give me other table with columns: the math code in latex/markdown showing fractions, powers, integrals, derivatives, (and other basic math examples), descriptions, and examples.
``` 
