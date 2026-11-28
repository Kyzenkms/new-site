# Programming for Problem Solving (C) — CAE-1 Study Notes (Units 1–5)

> **Units per official NEP Programming for Problem Solving syllabus.**

---

# Unit 1: Problem Solving Concepts

> Before writing any program, you must be able to solve the problem on paper. This unit is about the thinking, not the C syntax.

---

## 1. Types of Problems

| Type | Meaning | Example |
|---|---|---|
| **Computational** | Solved by calculation / well-defined steps | Factorial, sorting numbers |
| **Decision** | Answer is yes/no (true/false) | Is the number prime? |
| **Search** | Find an item in a collection | Find a name in a list |
| **Optimization** | Find the best option among many | Shortest route, cheapest cost |
| **Undecidable / ill-defined** | No clear algorithm or steps possible | "Write a beautiful poem" |

## 2. Problem Solving with Computers (the process)

1. **Understand the problem** — what are the inputs, outputs, constraints?
2. **Devise a plan** — design an algorithm (step-by-step solution).
3. **Represent the plan** — flowchart or pseudocode.
4. **Implement** — write the program in a language (C).
5. **Test and debug** — run with sample inputs; fix errors (syntax, logical, runtime).

Computers only execute **precise, unambiguous, finite** instructions — so the plan must leave nothing to guesswork.

## 3. Algorithms

**Definition:** a finite, ordered set of unambiguous steps that takes input(s) and produces the desired output in finite time.

**Qualities of a good algorithm:** correctness, finiteness (must terminate), definiteness (each step unambiguous), effectiveness (each step doable), efficiency (reasonable time/memory).

**Building blocks of algorithms** (everything is built from these three):
- **Sequence** — steps executed one after another in order.
- **Selection** — choose between paths based on a condition (if-else).
- **Iteration** — repeat a block while a condition holds (loops).

## 4. Flowcharts

A diagram of the algorithm using standard symbols:

| Symbol | Shape | Use |
|---|---|---|
| Oval | ⬭ | Start / Stop (terminator) |
| Parallelogram | ▱ | Input / Output |
| Rectangle | ▭ | Process (calculation, assignment) |
| Diamond | ◇ | Decision (yes/no branch) |
| Arrow | → | Flow direction |
| Small circle | ○ | Connector (continue elsewhere) |

**Example — largest of three numbers:**
```
START → input a, b, c → is a > b? ──yes──→ is a > c? ──yes──→ print a → STOP
                            │ no                 │ no
                            ↓                    ↓
                       is b > c? ──yes──→ print b ──no──→ print c → STOP
```

## 5. Pseudocode

An informal, English-like description of the algorithm — no strict syntax, but structured.

**Example — factorial:**
```
BEGIN
  READ n
  SET fact = 1, i = 1
  WHILE i <= n DO
      fact = fact * i
      i = i + 1
  END WHILE
  PRINT fact
END
```

Pseudocode is preferred over flowcharts for big/complex logic (flowcharts get messy).

---

## Likely CAE Questions (Unit 1) with short answers

**Q1. What are the building blocks of algorithms? Give an example of each.**
Sequence (steps in order, e.g., read a, read b, compute sum), selection (if-else choice, e.g., pick larger of two), iteration (repeat while a condition holds, e.g., loop to print 1 to n). Every algorithm is built from these three.

**Q2. Draw a flowchart to find the largest of three numbers.**
(See diagram in §4.) Key symbols: oval for START/STOP, parallelogram for input/print, diamond for comparisons, rectangle for assignments.

**Q3. Differentiate algorithm and flowchart.**
An algorithm is the step-by-step procedure in words/pseudocode; a flowchart is its pictorial (diagrammatic) representation using standard symbols. Both describe the same logic; pseudocode scales better for complex problems.

**Q4. Write pseudocode to check whether a number is prime.**
```
BEGIN
  READ n
  IF n < 2 THEN PRINT "not prime"; STOP
  FOR i = 2 TO n/2 DO
      IF n MOD i == 0 THEN PRINT "not prime"; STOP
  END FOR
  PRINT "prime"
END
```

---

# Unit 2: Introduction to Programming Language

---

## 1. History and Types of Programming Languages

- **Machine language (1GL):** binary 0/1 — fastest, but hard to write/read, machine-dependent.
- **Assembly language (2GL):** mnemonics (ADD, MOV) — needs an **assembler** to convert to machine code.
- **High-level languages (3GL):** English-like (C, Python, Java) — portable, need a **compiler/interpreter**.
- **Very high-level / 4GL:** e.g., SQL — closer to problem statements.

**Language processors:**
- **Compiler:** translates the **whole program** to machine code at once, then runs it (fast execution; errors reported after compilation). *C uses a compiler.*
- **Interpreter:** translates and executes **line by line** (slower, easier debugging). *Python uses an interpreter.*

## 2. Structure of a Programming Language

Every language needs: **character set** (allowed symbols), **syntax** (grammar rules), **semantics** (meaning of statements), **data types**, **operators**, **control structures**, and **functions/libraries** for reuse.

## 3. Tokens

**Token** = the smallest meaningful unit of a program. C has six kinds:

| Token | Examples |
|---|---|
| **Keywords** | `int`, `float`, `if`, `while`, `return` (reserved, 32 in C) |
| **Identifiers** | `sum`, `total_marks`, `_x1` (names you create; start with letter/underscore) |
| **Constants** | `10`, `3.14`, `'A'`, `"hello"` (values that don't change) |
| **Strings** | `"hello"` (characters in double quotes) |
| **Operators** | `+ - * / % = == &&` (act on operands) |
| **Special symbols** | `; , { } ( ) [ ] #` |

## 4. Data Types

- **Built-in (basic):** `int` (4B), `float` (4B), `double` (8B), `char` (1B), `void`.
- **User-defined:** `struct`, `union`, `enum`, `typedef` — you create these.
- **Derived:** `array`, `pointer`, `function` — built from basic types.

**C program structure:**
```c
#include <stdio.h>     // header: declarations of printf/scanf
int main() {           // execution starts here
    int a = 10;
    float b = 5.5;
    printf("Sum = %.2f\n", a + b);
    scanf("%d", &a);   // & is a must in scanf
    return 0;
}
```

## 5. Operators and Expressions

**Operators:** arithmetic `+ - * / %`, relational `< > <= >= == !=`, logical `&& || !`, assignment `= += -=`, increment/decrement `++ --`, conditional `?:`, `sizeof`, bitwise `& | ^ ~ << >>`.

**Precedence (high → low):** `()` → unary → `* / %` → `+ -` → relational → `== !=` → `&&` → `||` → `?:` → `=`.

**Expression** = operands + operators that evaluate to a value, e.g., `a + b * 2`. Watch **type conversion**: implicit (int→float automatic) vs explicit cast `(float)a/b`; and the classic trap — integer division: `5/9` = `0`.

**Format specifiers:** `%d %f %c %s %lf`; `%.2f` prints 2 decimals.

---

## Likely CAE Questions (Unit 2) with short answers

**Q1. Differentiate compiler and interpreter.**
A compiler translates the entire program to machine code before execution (fast run, whole-program error report — C). An interpreter translates and executes line by line (slower, easier debugging — Python).

**Q2. What are tokens? List the types of tokens in C.**
Tokens are the smallest meaningful units of a program: keywords, identifiers, constants, strings, operators, special symbols. (Examples in the table above.)

**Q3. Classify C data types with examples.**
Built-in: int, float, char, double, void. User-defined: struct, union, enum, typedef. Derived: array, pointer, function.

**Q4. What is an expression? Explain type conversion with an example.**
An expression combines operands and operators to produce a value (e.g., `a + b*2`). Implicit conversion happens automatically (int→float in `3 + 2.5`); explicit conversion uses a cast: `(float)5/9` gives 0.555…, while `5/9` gives 0 (integer division).

**Q5 practice programs (Units 1–2):** swap two numbers without a third variable; Celsius→Fahrenheit (mind the `9/5` trap); simple + compound interest; largest of three with nested `?:`; area/circumference printed with `%.2f`.

---

# Unit 3: Control Flow & Loop

---

## 1. Selection Statements

- **if / if-else / else-if ladder / nested if** — choose a path on a condition.
- **switch:** multi-way branch on an integer/char expression.

```c
switch (ch) {
    case 1: printf("One"); break;
    case 2: printf("Two"); break;
    default: printf("Other");   // runs if no case matches
}
```

**`break`** inside a case stops fall-through (without it, execution continues into the next case!). **`default`** is optional but good practice. `break` also exits loops.

## 2. Loops

| Loop | Behaviour | Use when |
|---|---|---|
| `for` | init → condition → update, all in one line | Number of iterations is known |
| `while` | Condition checked **first** | Iterations unknown; may run zero times |
| `do-while` | Body runs **first**, then condition | Must run **at least once** (menus!) |

- **Multiple loop variables:** `for (i = 0, j = n-1; i < j; i++, j--)` — legal and handy.
- **`break`** exits the loop entirely; **`continue`** skips the rest of the current iteration.
- **Nesting:** loops and ifs can be nested; inner loop completes fully for each outer iteration (basis of pattern programs).

## 3. Common traps

`= ` vs `==` in conditions • `;` right after `if (...)` kills the if • missing `&` in `scanf` • integer division `5/9 = 0` • forgetting `break` in switch cases • off-by-one in loop bounds.

---

## Likely CAE Questions (Unit 3) with short answers

**Q1. Differentiate `while` and `do-while` with examples.**
`while` tests the condition first — the body may run zero times. `do-while` runs the body first, then tests — it always runs at least once (good for menus: `do { show menu; read choice; } while (choice != 0);`).

**Q2. Explain `switch` with an example. Why is `break` necessary?**
switch branches on the value of an integer/char expression. Without `break`, execution "falls through" into the next case's statements — so `break` is needed to exit after the matching case.

**Q3. Write a program to check whether a number is prime.**
```c
int n, i, prime = 1;
scanf("%d", &n);
if (n < 2) prime = 0;
for (i = 2; i <= n/2 && prime; i++)
    if (n % i == 0) prime = 0;
printf(prime ? "prime" : "not prime");
```

**Q4. Print the Fibonacci series up to n terms; print a pyramid pattern.**
```c
// Fibonacci
int a = 0, b = 1, c, i, n;
for (i = 0; i < n; i++) { printf("%d ", a); c = a + b; a = b; b = c; }
// Pyramid (n rows)
for (i = 1; i <= n; i++) {
    for (j = 1; j <= n - i; j++) printf(" ");
    for (k = 1; k <= 2*i - 1; k++) printf("*");
    printf("\n");
}
```

**5 practice programs:** prime / Fibonacci / palindrome / Armstrong (153); menu-driven calculator with `switch` in a `do-while`; pyramid + reverse pyramid patterns (CAE favourites).

---

# Unit 4: Functions

---

## Key concepts

- **Function:** declaration (prototype) → definition → call. Lets you reuse code.
- **Call by value:** a *copy* of the argument is passed — the original can't change.
- **Call by reference:** the *address* is passed (using pointers — basics only) — the original can change.
- **Recursion:** a function calling itself; **must have a base case** or it recurses forever. Trace with a stack diagram.
- **Storage classes:** `auto` (default, local), `static` (retains value between calls), `extern` (global across files), `register` (hint to keep in CPU register).

```c
int fact(int n) {              // recursive factorial
    if (n <= 1) return 1;      // base case
    return n * fact(n - 1);
}
```

**Likely questions:** explain recursion with factorial; trace `fact(4)` by hand (returns 24); call by value vs call by reference with an example.

---

# Unit 5: Arrays & Pointers

---

## Key concepts

- **Arrays:** `int a[10];` — indexing starts at **0**; `int a[5] = {1,2,3,4,5};`; loop `for (i = 0; i < 5; i++) scanf("%d", &a[i]);`
- **2D arrays:** `int m[3][3];` — nested loops for input/output; stored in row-major order.
- **Strings:** `char s[20];` — `scanf("%s", s)` (no `&` needed); `<string.h>` gives `strlen`, `strcpy`, `strcmp`.
- **Pointers (basics):** `int *p = &a;` — `p` holds the address of `a`; `*p` is the value at that address.

**Likely programs:** largest + smallest + second largest in an array; bubble sort (trace on {5, 2, 8, 1}); matrix addition and multiplication (3×3, check dimension rule: columns of A = rows of B); reverse an array in place; string palindrome check.

---

## Quick revision checklist

- [ ] Unit 1: algorithm definition + 3 building blocks (sequence/selection/iteration); flowchart symbols; one pseudocode from memory
- [ ] Unit 2: compiler vs interpreter; 6 token types; data-type categories; precedence order; cast vs implicit conversion
- [ ] C skeleton + format specifiers `%d %f %c %s` + `&` in scanf
- [ ] `=` vs `==`, stray `;` after if — traps
- [ ] switch with break + default
- [ ] for vs while vs do-while — when to use each; multiple loop variables
- [ ] Prime / Fibonacci / palindrome / Armstrong logic by heart
- [ ] One pattern program (pyramid) practised
- [ ] Recursion base case + hand trace of fact(4)
- [ ] Bubble sort steps on a 4-element array
- [ ] 2D array input/output nested loops
