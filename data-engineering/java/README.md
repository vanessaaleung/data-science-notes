
![image](https://user-images.githubusercontent.com/24954551/163208415-bc145071-8dcc-4aa5-924c-87d337237c97.png)

- **main**: tell the compiler it's the starting point of the program
- **public**: access specifier, can be invoked from outside of the class
- **void**: return type, doesn't return anything, does not make sense for the main method to return anything
- **static**: keyword, can be invoked without instantiating the class
- **String[] args**: stores Java command-line arguments


### Java new Keyword
```java 
NewExample obj=new NewExample();
```
- It is used to create the object.
- It allocates the memory at runtime.
- It invokes the object constructor.

<img src="https://user-images.githubusercontent.com/24954551/163467845-0ab2853a-96b6-45b5-9833-c9cd4b76c630.png" height="300px" />


### Capture User Input
- `.next()` is used to get the user input
```java 
Scanner in = new Scanner(System.in);
String name = in.next();
```
