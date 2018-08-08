Graphics and Interaction COMP30019 Tutorial 2 
=============================================

### Transformation

Set object position to x=1, y=0, z=0...

`this.transform.localPosition = new Vector3(1.0f, 0.0f, 0.0f);`

Translate object one unit in the x-axis...

`this.transform.localPosition += new Vector(1.0f, 0.0f, 0.0f);`
Note: Overloaded `+=` operator for Vectors

### Rotation

Set object rotation to be 90 degrees around the y-axis...

`this.transform.localRotation = Quaternion.AngleAxis(90.0f, Vector3.up);`

Rotate Object 90 degrees around the y-axis

`this.transform.localRotation *= Quarternion.AngleAxis(90.0f, Vector3.up);`

### Scale

Set object to be double its original size in all axes

`this.transform.localScale = new Vector3(2.0f, 2.0f, 2.0f);`

Double the current scale of the object

`this.transform.localScale *= 2.0f;`

### User Input

Often we want to have *user input* when moving objects

Keyboard Input is done via:
```C#
// Get Key tests if a key is currently being held
Input.GetKey(KeyCode.UpArrow)

// Only happens if the key is pressed for the first time up->down
Input.GetKeyDown(KeyCode.UpArrow)

// Only happens when the key is let go down->up
Input.GetKeyUp(KeyCode.UpArrow)
```

### Mouse Input

```C#
Input.GetMouseButton(0)
Input.GetMouseButtonDown(0)
Input.GetMouseButtonUp(0)
```

### Creating a new script
- When we make a new script, we are usually given two methods to override: Start() and Update()
	- Start() is to do with *initialisation*
		- e.g.
		```C#
			void Start() {
				this.transform.localRotation *= Quarternion.AngleAxis(45.0f, Vector3.right);
				// Note: Vector3.right is equivalent to new Vector3(1, 0, 0);
			}
		```
	- Update() is *called every frame* 
		- e.g. 
		- ```C#
			void Update() {
				this.transform.localRotation *= Quarternion.AngleAxis(Time.deltaTime * 20.0f, Vector3.right);
				// Note: Time.deltaTime gives you the time from the last frame in case there's lag
			}
		```