EchoEvaluator
=============

Evaluates the python code and replaces it with the echoed result just like `<?php echo "text"?>`.

**Installation :**

- **_Recommended_** - Using [Sublime Package Control](http://wbond.net/sublime_packages/package_control "Sublime Package Control")
    - `ctrl+shft+p` then select `Package Control: Install Package`
    - install `EchoEvaluator`
- Alternatively, download the package from [GitHub](https://github.com/Monnoroch/EchoEvaluator "EchoEvaluator") into your `Packages` folder

**Usage :**

Select a piece of python code and press `ctrl+shift+e`, the code will be replaced with echoed result. You can use multiple selections, than all code pieces will be evaluated esparatly.
The plugin can evaluate native ST python: 2.x for ST2, 3.x for ST3.
If an exception occured during evaluation, it will be printed into a ST console.

**Examples :**

Evaluating

```
for x in [1, 3, 5]:
    echo(x)
```
    
will replace it with "135".


Evaluating

```
for x in [1, 3, 5]:
    echo("result[%d] = 2*%d\n" % (x, x + 1))
```
    
will replace it with:

```
result[1] = 2*2
result[3] = 2*4
result[5] = 2*6
```
