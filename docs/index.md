# Dice Project
This project is used to simulate individual die or hands of dice.

You have the option to select the type and quality of dice that you want to work with.

The dice available include `D4`, `D6`, `D8`, `D10`, `D12`, `D20` and `custom die`. In addition we have a `coin` option that is considered a `D2` die.

## How to call the Dice project files

The first step is to import the files in the `dice` folder and select the classes that contain the type of die that you are trying to use. The following example shows how to call a standard `D6` die:

```python
from dice import D6
```
There is also the possibility of importing all of the classes in the project using the following call:

```python
from dice import *
```

We then will have to call the instance of the `die` before we could take any actions with the `die`. The process will look as follows:

```
d1 = D6()
```

After the instance of the die assigned we can then take actions in the die such as **rolling** a die. The roll die will give as an output the **face** or final value of the die. The following example shows how to roll the die:

```python
result = d1.roll()
print(f"The die face after rolling is: {result}")
```

There are other operations that can be done in a die such as **shaking** the die, getting the **die face**, getting the **die type** or setting the **die face**. 

We can think of the operation of **shaking** the **die** as the process of scrambling the die before rolling it. It is important to notice that the shaking process does not output a value, just changes the face of the die internally. The following example shows how to shake a die.

```
d1.shake()
```

We can confirm that the face of the die has actually changed by making use of the **get_face** method. Here is an example on how to call the get_face method:

```python
result = d1.get_face()
print(f"The face value is:{result}")
```

Another useful method is the **get_type** method. it allows us to know which is the type of die that we are working with. The following example shows us how to use the get_type method:

```python
result = d1.get_type()
print(f"The die is of type: {result}")
```

We also have the ability to set the face of a die using the **set_face** method. The following example shows us how to use the set_face method:

```python
d1.set_face(3)
```