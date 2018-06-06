# SWEN30006 Software Modelling and Design

### What is Software Modelling for?
- **Analysis**: Investigation of the problem/requirements
- **Design**: Purposefully choosing the structure and behaviour of your software system
	- The behaviour is *all about how your systems responds to inputs* and events
	- "Alright let's write everything in main()"
- **Modelling**: Creation of tangible but abstract representations of a system so you can communicate ideas
	- "Alright look at my diagram I put everything in one function and now it's faster"
---------------------------------------

### Iterative UP (Unified Process)
- This is the main process of software development considered in this course
	- Requirements -> Design -> Implementation -> Test -> Integrate
	- *Feedback during testing helps the next iteration*
	- Like *rewriting a draft*
	- Iterations are *fixed in length*
![](summary/summary0.png)
- **Definitions**:
	- **SuD**: System Under Discussion
	- **Actor**: Something with behaviour such as a person computer system or organisation
		- **Primary Actor**: Has user goals fulfilled through using the SuD
		- **Supporting**: Provides a service to the SuD
		- **Offstage**: Has an interest in the behaviour of the use case, but is not primary or supporting
	- **Scenario (or use case instance)**: A specific set of actions and interactions between actors the SuD
	- **Use Case**: Text descriptions of an actor using the system to achieve a goal, fail or success.
		- Can be *brief*, *casual*, or *fully dressed*
		- **Boss Test**
			- *Boss*: "What have you been doing all day?"
			- *You*: `<doing use case>`
			- Is your boss happy?
				- No. he never is.
		- **Elementary Business Process Test (EBP Test)**
			- A task performed by one person in one place at one time in response to business event
		- **Size Test**
			- Very seldom a single step; typically many steps.
---------------------------------------

### Domain vs Design Models
- **Domain**:
	- Shows what you are using within a domain
	- Overview of the world
	- Most layman way to explain a problem 
	- Drawing it so that everyone can understand 
	- Has nothing to do with development
	- **No Privacy Modifiers**
	- **No Interfaces/Abstract Classes (i.e. software concepts)**
	- **No Methods**
	- **No Data Types**
- **Design**:
	- Software representation of the problem
	- Discusses objects
	- Not specific to language
	- For a software developer
	- Blueprint of program

### Domain Models
- **_Uses Conceptual Classes_**
	- An 'entity', 'thing' or object irl
	- Combination of a
	- Symbol: Words or images representing class
	- Intension: Definition of class
	- Extension: Set of instances represented by C
- **Create one by**:
	- Finding *Conceptual classes*
	- *Drawing* these in a *UML* class diagram
	- *Adding associations* and attributions
- **Find one by**:
	- *Reusing or modifying existing models* e.g.
		- Standardised/adopted domain model
		- Organisational domain model
	- Use a *category list*
		- Basically a list of definitions that looks like this: ![](summary/summary1.png)
	- Identify *noun phrases*
		- Make a list of candidate conceptual classes ![](summary/summary2.png)

### Attributes vs Classes
- We can differentiate between an *attribute* and a *class*
	- If the entity is not considered a number/text value irl, it's probably a conceptual class, not an attribute

### Description Class
- Contains info that describes something else
- *Groups of items share* the same *description*
- *Items need to be described even* when there are currently *no examples*
- *Reduces redundant or duplicated information* (design)
- *Deleting instances results in losing required info* (design)

### Associations
- An **association** respresents some meaningful and significant relationship between classes
- Significant in the domain
- Knowledge of the relaionship needs to be preserved
- Draw an arrow from one class to another
- This can **also be defined by a category list**
	- ![](summary/summary3.png)
- Associations have _**Multiplicity**_

### Multiplicity
- ![](summary/summary4.png)
- Defines *how many* of another class is associated with another
- Depends on the scope of our model
	- Do we care about items before/after the store
- Is this a constraint we want to maintain?

---------------------------------------------------------------------------------

### UML Interaction Diagrams
- **Sequence**:
	- Clearly shows times ordering of messages
	- Can more easily convey the detail of message protocols between objects
	- ![](summary/summary5.png)
- **Communications**:
	- More layout options
	- Clearly shows relationships between object instances
	- Combine to provide a more complete picture
	- ![](summary/summary6.png)
	
### Sequence Diagrams
- We have *lifelines* which show instances doing things down their "lines"
	- Named with a colon like `:Sale`
	- You can define an *instance of a class* with `s1 : Sale`
	- Interfaces/Abstract Classes can also be defined with `sale : List` where List is an interface/abstract class
	- Arrays/Other data structures are done with the following `sales: ArrayList<Sale>` or `sale[i] : Sale`
- Function calls/events and methods are shown *by solid arrows between lifelines* which are called from a *execution specification bar*
	- A *dotted arrow* shows a **return from a result**
	- Arrows can lead to *new lifelines being created*
	- If an object _is being deleted by a call, it is shown by an **"X"**_
	- A **conditional message** is shown by **`[ condition = true ]`**
- A **loop** can be shown by a **UML frame**

### UML Frames
- This is basically a way of *"encapsulating" operations* such as *loops or conditionds (alts)*
	- This is done by a small box in the top left corner of the frame followed by the condition e.g. `[i < lineitems.size]`
	- ![](summary/summary7.png)
- This can also be used to refer to "references"
- You can define *polymorphic* classes too by using `Payment {abstract}`

### Communication Diagrams
- Kind of like a node-graph sort of setup 
	- each *node is an instance*
	- every *arc is a function call*
- You can *create instances from a function call by using `create() or <<create>>`*
- *Conditionals* are done the same way, with `[ condition = true ]` brackets
	- Can be mutually exclusive messages if you have two conditions branching off of a instance
	- ![](summary/summary8.png)
- Static/Class Messages are done by having no colon: `<<metaclass>> Bicycle`
- Iteration is also done like conditions, with `* [i = 1..n]: num = nextInt`
	- Note the **\***
	- The square bracket condition is optional
	- You could do `: st = getSubtotal` for example

-------------------------------------

## GRASP
All about doing things *responsibly*
- General Responsibility Assignment Software Patterns (or Principles):
	- Creator Pattern
	- Information Expert
	- Low Coupling
	- Controller Pattern
	- High Cohesion
	- Polymorphism
	- Indirection
	- Pure Fabrication
	- Protected Variations

### Creator Pattern
- We learnt this in OOSD
- *Class B contains A* and is *responsible for initialising it*
- Gets kinda weird when you have to create different instances based on properties
```java
// Inside our creator class
private SomeObject objectName = null;

// Initialise when created
public Creator() {
	objectName = new SomeObject(property1, property2);
}
```

### Low Coupling
- Make sure classes depend on each other as little as possible
- Coupling is unavoidable but we want to couple where things are stable
- Means stuff is modular and easier to stand by themselves
```java
// If we were in a "player" class
private getSquare() {
	return this.square;
}
// vs. offloading to a different class
board.getSquare();
```

### Information Expert
- The general principle of assigning responsibilities to objects
- Assign things to objects which *"know"* the most about it
- Increases cohesion and reduces coupling
```java
// instead of
private Square s = new Square();

// We pass the responsibility of creating/getting squares to the board class
private Square s = board.getSquare(name)
```

### Controller
- Coordinates the system
- Delegates events and responses


### Patterns
*"A pattern is a recurring successful application of expertise in a particular domain."*
- Improve Understandability
- Simplify Documentation
- Facilitate generating modified applications
- Make it easier to reuse successful code
- Capture 'expertise' and make it accessible to non-experts in standard form

### Types of Patterns




徐聲恩