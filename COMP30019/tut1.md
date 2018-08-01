Graphics and Interaction COMP30019 Lab 1
========================================
- Fun and useful subject
- Using Unity
- Game dev-centric subject
- 1st half of course technical graphics centric
- 2nd half is evaluating comptuer interaction perspective

- Study in your own time
- OOP is important
	- Apparently it takes 5 years before a prereq is added into a unimelb subject system
- Use the same version of Unity
- Game dev programming isn't that hard
- Shaders are a bit weird

## Unity
- 3D games and simuluation engine
- Very easily build 3d applications - not limited to PC
	- Can build for any sort of device
	- Pokemon Go was written in Unity
- Cross platform
- Scripting in C# in Cg/HLSL
- Rapid development
- WebGL
- Component based architecture

### Component Based Architecture
- Arguably the most flexible engine architecture type for games
- Use *composition* instead of *inheritence* during development
- A *scene* made of game objects
- All game objects have a "Transform" component, describing their position, rotation and scale in the game world.
- A game object can have 0 or more additional optional components attached to it
- Some example entities/game objects:
	- `<Transform>`
	- `<Transform, Mesh Filter, Mesh Renderer>`
	- `<Transform, Camera>`
		- e.g. what the user looks through
	- `<Transform, Spot Light>`
	- `<Transform, Mesh Filter, Mesh Renderer, Health Script>`
		- e.g. things that have health
			- When the health script reaches zero the object disappears
- Attach these things yourself to make things

### 3D Objects
- How do we represent 3D objects in a scene?
	- *Perspective*/*Orthographic Projection*?
		- Way of looking at the world - way of *projection*
	- *Vertecies*
		- Points in 3D space
	- *Polygons*
		- Fancy version of a triangle
		- Break up an object into triangles via *tesselation*
		- *Triangles have nice mathematical properties that make it easy to calculate*
- How do we make things more detailed?
	- More edges/Triangles
	- The way it's *shaded*
		- e.g. Each triangle may be flat shaded (one colour) instead of blending things
		- Shading is more powerful

### Triangles
- Simply defined by 3 vectors

### Coordinate Systems
- In order for sets of verticies to be meaningful, we need to define some axes
- In 3D we have a z-axis
	- Having "inward and outward" complicates things
	- Left handed vs Right handed coords
		- Imagine making a gun shape with your hand - 3rd finger will go "inward" or "outward" of the screen
		- *Unity is a **Left-Handed Coordinate System***
		- Impossible to convert between these
		- Historical reason
			- DirectX rendered differently to OpenGL
			- Different systems were adopted

### Front Back Faces
- 3 Vertices define a triangle
- What defines which side is the "front" of the triangle?
- Can calculuate this with the **Vertex Winding Order**
	- Clock-Wise vs Counter Clock-Wise
	- Can figure out the front/back
	- The front is the "winding order" where the vertexes are clock-wise winding order
- Might want to render a particluar "side" of the triangle in a way
	- We don't need to render the back faces of triangles in objects that are closed
		- e.g. we don't need to render the inside of a box
		- Dot product between the viewer and the normal of the surface
	- *This is called **culling***




