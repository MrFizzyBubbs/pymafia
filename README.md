# pymafia

pymafia is a Python package and bridge for reflecting KoLmafia's Java environment. It aims to provide an easy-to-use environment for scripting [Kingdom of Loathing](https://www.kingdomofloathing.com/) (KoL) in Python by reflecting and wrapping the community-developed [KoLmafia](https://github.com/kolmafia/kolmafia) desktop tool. While [other languages](https://loathing-associates-scripting-society.github.io/KoL-Scripting-Resources/) for scripting KoL exist, they simply aren't Python.

## Installation

You can install pymafia from the [Python Package Index (PyPI)](https://pypi.org/project/pymafia/) using the following command:

```
pip install pymafia
```

pymafia uses [JPype](https://github.com/kivy/pyjnius) to reflect KoLmafia's Java environment, so you will need to install a Java Development Kit (JDK) on your operating system — KoLmafia's developers recommend [Adoptium v17](https://adoptium.net/index.html). For information on troubleshooting your Java installation, see [JPype's troubleshooting guide](https://jpype.readthedocs.io/en/latest/install.html#if-it-fails).

## Usage

### Configuration

You can choose the revision of KoLmafia to use or location to run it from by setting these properties in the `config` module prior to starting the Java Virtual Machine (JVM). The revision defaults to the last known working revision at the time of release and the location defaults to a folder named "kolmafia" in the current working directory.

```python
>>> from pymafia import config

>>> config.set_revision(27469)

>>> config.set_location('C:\\Users\\Documents\\kolmafia\\')
```

### Starting the JVM

To start KoLmafia, call the `start_kolmafia()` method from the `kolmafia` sub-package. Doing so will download a KoLmafia jar file (if it is not present in the configured location) and start a JVM with the jar file included in the JVM's classpath. This process can take over a minute depending on your internet connection.

```python
>>> from pymafia.kolmafia import start_kolmafia

>>> start_kolmafia()
```

Once you have configured and started pymafia, you will most likely want to launch the KoLmafia GUI and login to your character. Both of these actions can be performed using the `utils` module.

```python
>>> from pymafia.utils import launch_gui, login

>>> launch_gui()

>>> login('devster6')
```

Note that almost all `pymafia` objects are available at the top level, although this is subject to change.

```python
>>> from pymafia import launch_gui
```

### Accessing Java Classes

The reflected KoLmafia jar file can be accessed through a `KoLmafia` wrapper class instance called `km`. Most, if not all, of KoLmafia's Java classes are available as attributes through `km`.

```python
>>> from pymafia.kolmafia import km

>>> km.AdventureResult
<java class 'net.sourceforge.kolmafia.AdventureResult'>
```

These classes behave similar to how they do in Java with the exception of returning Python objects when possible. For more information on type conversion, see [JPype's type matching guide](https://jpype.readthedocs.io/en/latest/userguide.html#type-matching).

```python
>>> km.AdventureResult.tallyItem("big rock")
<java object 'net.sourceforge.kolmafia.AdventureResult'>

>>> km.AdventureResult.tallyItem('big rock').isBountyItem()
False
```

### ASH and Special Datatypes

KoLmafia's runtime library functions are available through the `ash` sub-package, which will automatically handle conversion of the inputs and output for the underlying Java function.

```python
>>> from pymafia import ash

>>> ash.gameday_to_string()
'Dougtember 3'
```

This conversion means that the functions accept and return Python objects, including KoLmafia's [special datatypes](https://wiki.kolmafia.us/index.php/Data_Types#Special_Datatypes), which have been implemented in the `datatypes` sub-package.

```python
>>> from pymafia.datatypes import Location

>>> ash.to_item('big rock')
Item('big rock')

>>> ash.appearance_rates(Location("Noob Cave"))
{Monster('none'): 0.0, Monster('crate'): 100.0}
```

As demonstrated above, the datatypes can be instantiated directly from their name, id, or string representation where applicable. Each datatype has a set of properties that match those available from their [KoLmafia proxy record](https://wiki.kolmafia.us/index.php/Proxy_Records) equivalent.

```python
>>> from pymafia.datatypes import Familiar, Item

>>> Item('big rock').tradeable
True

>>> Familiar('God Lobster').hatchling
Item('God Lobster Egg')
```

Datatypes also have an `all()` class method that returns every non-none instance of that type.

```python
>>> from pymafia.datatypes import Stat

>>> Stat.all()
[Stat('Muscle'), Stat('Mysticality'), Stat('Moxie')]
```

Several datatypes define class instances as class variables for convenient reference. Notably, all datatypes define a `NONE` class variable.

```python
>>> Coinmaster.NONE
Coinmaster('none')

>>> Slot.HAT
Slot('hat')
```

### Non-Documented Functionality

There are modules and subpackages available within pymafia that have not been described here; I hope to provide comprehensive documentation in the future.

## Contributing

To contribute to pymafia, you will need to set up a development environment using the following steps:

1. Install [uv](https://docs.astral.sh/uv/) (and [GnuWin32 Make](https://gnuwin32.sourceforge.net/packages/make.htm) if on Windows)
2. Clone this repository
3. Run `make install` inside the cloned repository

## Acknowledgements

This project was inspired by Samuel Gaus's [frattlesnake](https://github.com/gausie/frattlesnake) and tadpoleloop's [pymafia](https://github.com/tadpoleloop/pymafia) repositories.
