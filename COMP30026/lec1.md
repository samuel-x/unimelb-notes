Models of Computation COMP30026 Lecture 1
=========================================

This subject is all about *what does it mean to compute stuff*?

The subject will be assessed within [grok](https://groklearning.com/course/unimelb-comp30026-2018-s2/?ignore_lc=true). Yay!

Consultation hour on Thursdays from 12:00 (Doug McDonell 8.16).
Prefer to use the discussion forum.

### Why study Logic and Discrete Maths?
Logic and discrete mathematics probide the _theoretical foundations_ for computer science.
- **Prepositional logic** has applications in hardware and software verification, planning, testing and fault finding...
- **Predicate logic** is essential to artificial intelligence, computational linguistics, automatic theorm proving, logic programming
- **Algebra** underpins theories of databases, programming languages, program analysis, data mining...
- **Integers and rational numbers**:
	- Planners/constraint solvers, operations research
- **Modular arithmetic, number theory**:
	- Verification, encryption and decryption
- **Graphs and trees**:
	- Efficient data structures and their algorithms; information retrieval - covered in earlier subjects
- **Finite state automata**:
	- Controllers/counters, pattern matching, computational linguistics
- **Formal languages, grammars**:
	- Parsing, semantics, language based security

### Discrete vs Continuous Mathematics
Traditionally strong emphasis on *continuous mathematics (calculus/analysis)* in science and engineering education.

However, the world has *gone digital* so *discrete mathematics has become more important for "computational thinking"*

### Automata and Formal Languages
- Useful because of the applications
- `A e s t h e t i c` dimension
	- Different languages may be more/less similar to regular algebra
- Perfect stepping stone on the way to computability theory

### Why study this?
- Need to have a good understanding of *what can be computed*
- Hard to grasp the *limitations of algorithmic problem solving*
- There are simple functions which are hard to compute, but hard functions that are simple to compute

#### Let's play a game:
Consider the three symbols I, M, U with the following rules:
```
1:	Mx 		-> Mxx
2:	xI 		-> xIU
3:	xIIIy 	-> xUy
4: 	xUUy	-> xy
```

Starting from _MI_ generate _MU_

- The logic behind this is finding the *correct multiples of 'I' and 'U'*
	- You can then quantify each I in an equation, e.g. `(3n + 1) I's for operation 1`
- Generally when we try this on paper we're doing a random (bad) search
- We can instead try to *program our way out of this*.