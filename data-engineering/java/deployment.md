# Deployment
- [Javadoc](#javadoc)
- [JAR files](#jar-files)

## Javadoc
<img src="https://s3.us-west-1.wasabisys.com/idbwmedia.com/images/api/classsummary.png" height="300px">

- Comments go above the class
```java
/** My Main class **/
public class Main {
  /**
  * @param type ...
  * @param size ...
  */
}
```
- Can use HTML markup in the comments
```java
/** <b>My Main class</b> **/
public class Main {
...
```


## JAR files
- A file in zip formats
- Contains 1+ java classes
- Pre-compiled into byte codes
- Application manifest: indicates how the application is supposed to be run
  ```mf
  Manifest-Version: 1.0
  Main-class: com.example.java.Main
  ```
- Cross platform (Windows/Mac OS, etc.)
