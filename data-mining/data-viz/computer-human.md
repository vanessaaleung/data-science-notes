# The Computer and the Human

## Graphics, Drawing, and Photorealism
1. [2-D Graphics](#2-d-graphics)
2. [2-D Drawing](#2-d-drawing)
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

### 2-D Drawing
#### SVG (Scalable Vector Graphics)
_Format specification for describing 2-D graphics_
- Embedded in HTML with <svg> tag
  ```html
  <svg width=pw height=ph viewbox="x y w h"></svg>
  ```
  - viewbox: creates a drawing canvas x, y are the upper left corner
- Example:
  ```html
  <svg width=... height=... viewbox="0 0 1 1">
    <svg x="10%" y="10%" width="80%" height="80% viewbox="0 0 1 1">
  ```

  <img src="images/svg-coordinates.png" height="300px">

#### Path
- Example
   ```html
  <path d="M 0.2 0.1
           L 0.2 0.3
           L 0.4 0.3
           Z"
        fill = blue />
  ```
  - `M`: move to a new position without drawing a line
  - `L`: move to a new position while drawing a line
  - `Z`: close the path
  
## Humans and Visualization





