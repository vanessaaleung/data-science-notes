# Testing
```sbt
 libraryDependencies += "org.scalatest" %% "scalatest" % "3.0.8" % Test
```

```scala
import org.scalatest.FunSuite

class CubeCalculatorTest extends FunSuite {
   test("CubeCalculator.cube") {
     assert(CubeCalculator.cube(3) === 27)
   }
 }
```

- `"CubeCalculator.cube"`: name for the test. Convention is “ClassName.methodName”

# Definitions and Evaluation
## VAL VS DEF
- `def` is evaluaated on each use
- `val` is evaluated at the point of the definition
```scala
val x = 2
val y = square(x)
```
- `y` refers to `4` not `square(2)`

## Call-by-value AND Call-by-name
- Call-by-value: evaluates every function argument only once. Normally used by Scala
- Call-by-name: a function argument is not evaluated if the corresponding parameter is unused in the evaluation of the function body

# CONDITIONAL EXPRESSIONS
```scala
def factorial(n: Int): Int =
  if (n == 1) 1
  else factorial(n - 1) * n
```

# BLOCKS AND VISIBILITY
- The definitions inside a block are only visible from within the block
```scala
val x = 0
def f(y: Int) = y + 1
val result = {
  val x = f(3)
  x * x
} + x
```
- result should be 16

# SEMICOLONS
- Semicolons are optional
- Can have more than one statements on a line
```scala
val y = x + 1; y * y
```
- write multi-line expression in parentheses
```scala
(someLongExpression
  + someOtherExpression)
```
- or write the operator on the first line
```scala
someLongExpression +
  someOtherExpression
```

# TOP-LEVEL DEFINITIONS
- `def` and `val` definitions must be writen within a top-level object definition
```scala
object MyExecutableProgram {
  val myVal = …
  def myMethod = …
}
```

# PACKAGES AND IMPORTS
- Definitions located in a package are visible from other definitions located in the same package
```scala
// file foo/Bar.scala
package foo
object Bar { … }
```
```scala
// file foo/Baz.scala
package foo
object Baz {
  // Bar is visible because it is in the `foo` package too
  Bar.someMethod
}
```
- Definitions located in other packages are not directly visible, must use fully qualified names to refer to them:
```scala
// file quux/Quux.scala
package quux
object Quux {
  foo.Bar.someMethod
}
```
- Or import names to avoid repeating their fully qualified form:
```scala
// file quux/Quux.scala
package quux
import foo.Bar
object Quux {
  // Bar refers to the imported `foo.Bar`
  Bar.someMethod
}
```
