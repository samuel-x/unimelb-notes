Models of Computation COMP30026 Lecture 9
=========================================

# Predicate Logic: Resolution and Unification
- This section covers basically the process of 'resolving' a predicate as you've done in tutorials

## Notation for Variables and Constants in Predicate Logic
- Letters from the *start of the alphabet* `(a, b, c, ...)` for *constants*
- Letters from the *end of the alphabet* `(u, v, x, y, ...)` for *variables*
- *Lower case letters from `f`* as *function symbols*
- *Upper case letters* as *predicate symbols*

### Functions vs Predicates
- In some contexts it may be important to distinguish between these (formulas, etc.)
- In *unification*, predicate symbols and function symbols are considered the same

## Substitution
- When you come across a variable in resolution, you can *substitute it* with a term (function or predicate) 
- Eventually you end up with a **substitution**: a finite set of replacements of variables by terms
	- It looks like this: `{x₁ ↦ t₁, x₂ ↦ t₂,...}`
	- Where `xi` are variables and `tᵢ` are terms
- **Example:**
	- if `F` is `P(f(x), y)` and set `θ = {x ↦ h(u), y ↦ a}` then `θF` is `P(f(h(u)), a)`
- This is similar to *valuation (mapping term to variable)* but this *maps a **variable to a term*** and therefore a ***term to a term***
- However, **you cannot map a term that contains the variable to the variable itself**
	- e.g. you can't map `{x ↦ f(x)}` as you end up with an infinite loop of `f(f(f(...)))`

## General Unifiers
- A unifier of two terms `s` and `t` is a substitution `θ` such that `θ(s) = θ(t)`
- Basically if you can *resolve two terms to the same thing* then they are **unifiable**
- A *most general unifier (mgu)* for `s` and `t` is a substitution `θ` where:
	- `θ` is a unifier for `s` and `t`
	- every other unifier of `s` and `t` can be *expressed as a result produced by unifying `s` and `t`*

### Unifier Examples
1. `P(x, a)` and `P(b, c)` are not unifiable (can't map constants to constants)
2. `P(f(x), y)` and `P(a, w)` are not unifiable (can't map term to a constant)
3. `P(x)` and `P(f(x))` are not unifiable (infinite loop)
4. `P(x, c)` and `P(a, y)` are unifiable using `{x ↦ a, y ↦ c}`
5. `P(f(x), c)` and `P(f(a), y)` also unifiable using `{x ↦ a, y ↦ c}`

### Most General Unifier Example
- Consider `P(f(x), g(y, a))` and `P(f(a), g(z, a))`
- You can have any of the following unifiers, but `{x ↦ a, y ↦ z}` is considered the best (i.e. the most general unifier)
	- `{x ↦ a, y ↦ z}`
	- `{x ↦ a, y ↦ a, z ↦ a}`
	- `{x ↦ a, y ↦ g(b, f(u)), z ↦ g(b, f(u))}`
	- `{x ↦ a, z ↦ y}` <-- this is also equivalent to the first one and is also a MGU
- This is because they avoid making unnecessary substitutions