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
