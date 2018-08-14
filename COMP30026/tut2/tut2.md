Models of Computation COMP30026 Tutorial 2
=========================================

8. Check these for equivalence

(a) ¬P ⇒ Q and P ⇒ ¬Q
- Nope

(b) ¬P ⇒ Q and Q ⇒ ¬P
- 

(c) ¬P ⇒ Q and ¬Q ⇒ P
(d) (P ⇒ Q) ⇒ P and P
(e) P ⇒ (Q ⇒ R) and Q ⇒ (P ⇒ R)
- No

(f) P ⇒ (Q ⇒ R) and (P ⇒ Q) ⇒ R
(g) (P ∧ Q) ⇒ R and P ⇒ (Q ⇒ R)
- Yes

(h) P ∨ Q ⇒ R and (P ⇒ R) ∧ (Q ⇒ R)
- Yes


9.  Find a formula that is equivalent to (P ∧ Q) ∨ P but simpler, that is, using fewer symbols.
- Simplify to `P ∧ (P ∨ Q)`
- Must be P from removing tautologies

10.  Recall that ⊕ is the “exclusive or” connective. Show that (P ⊕ Q) ⊕ Q is equivalent to P.



11.  Show that P ⇔ (Q ⇔ R) ≡ (P ⇔ Q) ⇔ R. This tells us that we could instead write
P ⇔ Q ⇔ R (1)
without introducing any ambiguity. Mind you, that may not be such a good idea, because
many people (incorrectly) tend to read “P ⇔ Q ⇔ R” as
P, Q, and R all have the same truth value (2)
Show that (1) and (2) are incomparable, that is, neither is a logical consequence of the other.
- 