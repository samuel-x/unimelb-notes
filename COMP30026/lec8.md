Models of Computation COMP30026 Lecture 8
=========================================

# Predicate Logic: Clausal Form
- This section covers the problem of how to show validity and unsatisfiability via computation.

## Resolution for Predicate Logic
- We can resolve a predicate when it assumes **clausal form** (formula in *conjunctive normal form (CNF)* without *any quantifiers*)
- Works similarly to the way done in prepositional logic
- Existential quantifiers can be eliminated in a process called **Skolemization**

### Eliminating Existential Quantifiers
- Consider the formula `F = ∃x∀y P(x, y)` under some interpretation I
	- `F` is satisfiable iff some valuation `σ` makes `∀y P(x, y)` true, where `σ(x) = d`
		- Let's say we add the *fresh constant `a`*, and the formula `∀y P(a, y)`
		- The formula is *satisfiable* if `F` is; because we can map `a` to `d`
	- If `∀y P(x, y)` is unsatisfiable, there is no valuation that'll make it true, hence no interpretation will make `∀y P(a, y)`
- We *call this new constant a* a **skolem constant**

## Skolem Constants and Functions
- Now consider the formula `G = ∀y∃x P(x, y)`
- We cannot conclude that `∀y P(a,y)` is satisfiable iff G is
- Since ∃x is within the scope of ∀y, the value of x for which P(x, y) holds may differ, given different values of y.
- The value of *x is a function of the value of y*
	- We can generate a formula `∀y P(f(y), y)`, choosing a new function symbol f
	- The same satisfiability properties apply to the above example
- We *call this new formula f* a **skolem function**
- Arbitrary arity
- To eliminate `∃y` in `∀x1, x2, x3 ∃y[...]` we replace each occurence of `y` in its scope by `f(x1, x2, x3)`
- Each introduced Skolem constant or function must be 'fresh'

### Converting from Predicate Formulas to Clausal Form
1. Replace occurrences of ⇒, ⇔, and ⊕
2. Drive negation in
3. Standardise bound variables apart
4. Eliminate existential quantifiers (Skolemize)
5. Eliminate universal quantifiers (just remove them)
6. Bring to CNF (using normal distributive laws)

### Skolemization and Logical Equivalence
- Skolomization of a formula **does not** produce a logically equivalent formula.
- Skolomization produces an *equsatisfiable formula* - one that is *satisfiable iff the original was*

## Resolution for Predicate Logic
- Simple cases seem simple enough
- `¬B(x) ∨ M(x) and ¬M(c)`
- Note that all variables in this are universally quantified
- We then *instantiate*
	- `¬B(x) ∨ M(x)` to `¬B(c) ∨ M(c)`
	- Resolving the two clauses on M(c) and its negation results in `¬B(c)`
- Repeat until there are no clauses left