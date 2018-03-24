# Origin
Origin is a simple python library with no dependencies that was coded by me. It is in very heavy Alpha so don't expect it to be perfect
# Usage
Simple Example:
```python
from origin import Origin

MyCLI = Origin.create("MyCLI","$ ","1.0")
MyCLI.add_command("hello",lambda name: print("Hello {name}!".format(name=name)))
MyCLI.add_help("hello","Say Hello to Somebody!")
MyCLI.loop()
```
Output:
```
MyCLI V0.1
$ hello George
Hello George!
$ exit 0
Process finished with code 0
```
