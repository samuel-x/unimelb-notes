Models of Computation COMP30026 Tutorial 5
==========================================

#### Predicate Basics
Domain 						-> Where X exists
Predicate: 	P, Q...			-> Outputs a true/false value
Function:  	f, g, h... 		-> Outputs a domain value
Constant:	a, b, c... 		-> i.e. function with arity 0

`Ex P(x) ∧ Q(x, f(x))`

Let's say
`D`: Z
`P`: is prime
`f`: x^2
`Q`: Less than (x is less than y)

Here we say `P` has an *arity* of 1, while `Q` has an *arity* of 2

With this, we can say that this predicate is *always true* as long as *x ̸= 1*

#### Converting Predicate to CNF

> `∀x(P(x) => ∃y(R(x, y) ∧ ∀z R(z, y)))`

First implication becomes ¬a ∨ b

> `∀x(¬P(x) ∨ ∃y(R(x, y) ∧ ∀z r(z, y)))`

We then want to remove `∃y` (i.e. all *existential* quantifiers). This can be converted to a *funcion*.

If we have a existential inside a universal, then it becomes a function of the previous quantifier.

e.g. `∃x∀y` -> y has no affect on x, but in `∀y∃x` -> y has a direct affect on x

> `∀x(¬P(x) ∨ R(x, f(x)) ∧ ∀z (R(z, f(x))))`

Now we want to remove `∀` (i.e. all *universal* quantifiers).

> `¬P(x) ∨ (R(x, f(x)) ∧ R(z, f(x)))`

Convert to CNF

> `(¬P(x) ∨ R(x, f(x))) ∧ (¬P(x) ∨ R(z, f(x)))`

Done!

--------------------------------------------

##### Converting a sentence to predicate
- "There is a monster living in my closet.":
	- `M(x)`: x is a monster
	- `L(x)`: x lives in my closet
	- `∃x M(x) ∧ L(x)`
- "There are no monsters living in my closet.":
	- `¬(∃x M(x) ∧ L(x))`
	- `∀x ¬M(x) ∨ ¬L(x)`
	- `∀x M(x) => ¬L(x)`
	- `∀x M(x) ∧ ¬L(x)` <- this does *not work* because we're only *applying to monsters*, otherwise if I live in the closet and I'm not a monster then it'll be false
- "No mouse likes a cat who likes mice.":
	- First try to do the high level part "a cat who likes mice"
		- `C(x)` cat
		- `M(x)` mouse
		- `L(x, y)` x likes y
	- "likes mice" implies "all mice"
		- `C(x) ∧ ∀yM(y) => L(x, y)`
	- Then join it up
	- "All mice not like all cats"
		- `[∀z M(z) ∧ ∀xC(x) ∧ ∀yM(y) => L(x, y)] => ¬L(z, x)