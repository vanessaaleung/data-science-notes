# The Computer and the Human

## Graphics, Drawing, and Photorealism
1. [2-D Graphics](#2-d-graphics)
2. [SVG example]()
3. [2-D Drawing]()
4. [3-D Graphics]()
5. [Photorealism]()
6. [Non-Photorealism]()

### 2-D Graphics

#### Vector v. Raster Graphics
- Vector Graphics
  - Describes shapes with verticles, strokes, and fills
  - Used for drawing
- Raster Graphics
  - Describes shapes with a table of pixels
  - used for TV, phones
  - Vector graphics are converted to raster graphics for display
  - rectilinear array of pixels and pixels are assigned colors
- Rasterization: 
  - <img src="images/rasterization.png" height="300px">
  - Primitives: a vector graphics format that consists of verticles, strokes, fills
  - Converts the primitives into an array of pixels so that  they can be displayed
  - Aliasing: get stairstep artifacts when rasterizing a smooth straight line
  
#### Canvas Coordinates
- Can redefine corners of canvas coordinates to whatever is convenient
- Can use coordinates for domain and range
- Hierarchical Coordinate Systems: canvas in canvas
  - <img src="images/hierarchical-coordinate.png" height="300px">

#### Screen Coordianates
_For raster graphics, display of information_
- Per-pixel integer coordinates
- <img src="images/screen-coordinates.png" height="300px">

#### Canvas -> Screen Transformation
_2D graphics plotting on canvas can be automatically resized and repositioned anywhere on the screen_

- Can use same coordinates for both canvas and screen coordinates, results in non-scalable resolution dependent output, not recommended

## Humans and Visualization
