Models of Computation Tutorial 8
================================

f : A → B
g : B → A

∀yeB f(g(y)) = y

Assume g not injective : 
g(x) = g(y) x̸=y
f(g(x)) = f(g(y))
x = y

Subjectivity
Where everything maps to something in the other set
f : A → B
∀yeB : x = g(y) → f(x) = f(g(y)) = y
see if you can always find an element of the domain


### Well-founded is when something *terminates*:
- e.g. (N, <) → 0 < 1 < 2 < 4
	- Since when you reach 0, you reach the end of the sequence
- e.g. (R, <) is *not well founded* as the sequence never terminates

## Lexographical Ordering
- Ordering by its components (usually left->right)
- Kind of like in song playlists, when you have numbers that start at 01 as opposed to 1
```python
def for_fun():
	i = 100
	while (i > 1):
		i -= 1
```
This is equivalent to saying
({0,1...100}, <)

### Hercules vs Hydra
- Every Time you cut off a head, two more heads at a lower level sprout
- Represent it in a tuple with numbers at each level e.g. (1, 2, 2, 1)
	- (1, 2, 2, 1)
	- (0, 4, 2, 1)
	- (0, 3, 4, 1)
	- (0, 0, 0, X)
	- (0, 0, 0, 0)
- Eventually this will end
- Represented as a State Machine
	- State: (a, b, c, d)
	If (0,0,0,0) halt
	elif (0,0,0,d) → (0,0,0,d-1)
	elif (0,0,c,d) → (0,0,c-1,d+2)
	elif (0,b,c,d) → (0,b-1,c+2,d)
	elif (a,b,c,d) → (a-1,b+2,c,d)
- Note: If you have something that *decreases in lexigraphical order*, then *it will halt*

## State Machine
- **DFA**
	- Basically an input only results in two states
	- e.g.
		- {w | w has an even # of a's} ∑ = {a, b}
		- ![](wk8/wk81.png)
