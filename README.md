# pymafia

*pymafia* is a Python module and bridge for reflecting KoLmafia's Java environment. It aims to provide an easy-to-use environment for scripting [Kingdom of Loathing](https://www.kingdomofloathing.com/) (KoL) in Python by reflecting and wrapping the community-developed [KoLmafia](https://github.com/kolmafia/kolmafia) desktop tool. While [other languages](https://loathing-associates-scripting-society.github.io/KoL-Scripting-Resources/) for scripting KoL exist, they are arguably less approachable to non-developers. 

## Installation
*pymafia* is available at the [Python Package Index (PyPI)](https://pypi.org/project/pymafia/):

```
pip install pymafia
```

*pymafia* uses [JPype](https://github.com/kivy/pyjnius) to reflect KoLmafia's Java environment, so you will need to install a Java Development Kit (JDK) on your operating system — KoLmafia's developers recommend [Adoptium v17](https://adoptium.net/index.html). For information on troubleshooting your Java installation, see [JPype's troubleshooting guide](https://jpype.readthedocs.io/en/latest/install.html#if-it-fails).

## Usage
To get started, simply import *pymafia* or any of its components. Doing so will download a KoLmafia jar file (if it is not present in the configured location) and start a Java Virtual Machine (JVM) with the jar file included in the JVM's classpath. This process can take over a minute depending on your internet connection. 

You can choose the revision of KoLmafia to use or location to run it from by setting these properties in the `pymafia_config` module prior to importing *pymafia*. The revision defaults to the last known working revision at the time of release and the location defaults to a folder named "kolmafia" in the current working directory.

```python
>>> import pymafia_config

>>> pymafia_config.set_revision(27467)

>>> pymafia_config.set_location("C:\\Users\\Documents\\kolmafia\\")

>>> import pymafia # Start the JVM
```

Once you have configured *pymafia* and started, you will most likely want to launch the KoLmafia GUI and login to your character. Both of these actions can be performed using the `utils` module.

```python
>>> from pymafia.utils import launch_gui, login

>>> launch_gui()

>>> login("devster6")
```

Note that almost all *pymafia* objects are available at the top level, although this is subject to change.

```python
>>> from pymafia import launch_gui
```

### Accessing KoLmafia
The reflected KoLmafia jar file can be accessed through a `KoLmafia` wrapper class instance called `km`. Most, if not all, of KoLmafia's Java classes are available as attributes on `km`.

```python
>>> from pymafia.kolmafia import km

>>> km.AdventureResult
<java class 'net.sourceforge.kolmafia.AdventureResult'>
```

These classes behave similar to how they do in Java with the exception of returning Python objects when possible. For more information on type conversion, see [JPype's type matching guide](https://jpype.readthedocs.io/en/latest/userguide.html#type-matching).

```
>>> km.AdventureResult.tallyItem("big rock")
<java object 'net.sourceforge.kolmafia.AdventureResult'>

>>> km.AdventureResult.tallyItem("big rock").isBountyItem()
False
```

### ASH and Special Datatypes
All of KoLmafia's runtime library functions can be accessed through the `ash` submodule, which returns a `LibraryFunction` instance. 

```python
>>> from pymafia import ash

>>> ash.gameday_to_string
LibraryFunction("gameday_to_string")
```

The `LibraryFunction` is a thin wrapper around the desired Java method that will automatically convert the inputs and outputs of the wrapped method to and from Java objects, respectively. This conversion means that the functions accept and return Python objects, including KoLmafia's [special datatypes](https://wiki.kolmafia.us/index.php/Data_Types#Special_Datatypes), which have been implemented in the `datatypes` sub-package.

```python
>>> from pymafia.datatypes import Location

>>> ash.gameday_to_string()
"Dougtember 3"

>>> ash.to_item("big rock")
Item("big rock")

>>> ash.appearance_rates(Location("Noob Cave"))
{Monster("none"): 0.0, Monster("crate"): 100.0}
```

As demonstrated above, the datatypes can be instantiated directly from their name, id, or string representation where applicable. Each datatype has a set of properties that mirror those available from their [KoLmafia proxy record](https://wiki.kolmafia.us/index.php/Proxy_Records) equivalent.

```python
>>> from pymafia.datatypes import Familiar, Item

>>> Item("big rock").tradeable
True

>>> Familiar("God Lobster").hatchling
Item("God Lobster Egg")
```

Each datatype also has an `all()` class method that returns every non-none instance of that type.

```python
>>> from pymafia.datatypes import Stat

>>> Stat.all()
[Stat("Muscle"), Stat("Mysticality"), Stat("Moxie")]
```

Many datatypes contain predefined class instances as class variables for convenient reference. Notably, all datatypes define a `NONE` class variable.

```python
>>> Coinmaster.NONE
Coinmaster('none')

>>> Slot.HAT
Slot('hat')
```

### Non-Documented Functionality
There are  modules and subpackages and available within *pymafia* that have not been described here; I hope to provide comprehensive documentation in the future.

## Contributing
To contribute to *pymafia*, you will need to set up a development environment using the following steps:
1. Install [poetry](https://python-poetry.org/)
2. Clone this repository
3. Run `poetry install` inside the cloned repository


## Acknowledgements

This project was inspired by Samuel Gaus's [frattlesnake](https://github.com/gausie/frattlesnake) and tadpoleloop's [pymafia](https://github.com/tadpoleloop/pymafia) repositories.