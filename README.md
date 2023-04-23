# pymafia

*pymafia* is a Python module and bridge for reflecting KoLmafia's Java environment. It aims to provide an easy-to-use environment for scripting [Kingdom of Loathing](https://www.kingdomofloathing.com/) (KoL) in Python by reflecting and wrapping the community-developed [KoLmafia](https://github.com/kolmafia/kolmafia) desktop tool. While [other languages](https://loathing-associates-scripting-society.github.io/KoL-Scripting-Resources/) for scripting KoL exist, they are arguably less approachable to non-developers. 

## Installation
*pymafia* is available at the [Python Package Index (PyPI)](https://pypi.org/project/pymafia/):
```
pip install pymafia
```
*pymafia* uses [JPype](https://github.com/kivy/pyjnius) to reflect KoLmafia's Java environment, so you will need to install a Java Development Kit (JDK) on your operating system — KoLmafia's developers recommend [Adoptium v17](https://adoptium.net/index.html). For more information on troubleshooting your Java installation, see [JPype's troubleshooting guide](https://jpype.readthedocs.io/en/latest/install.html#if-it-fails).

## Quickstart

```python
>>> from pymafia import *

>>> login("devster6")
>>> ash.my_name()
"devster6"

>>> Effect("Synthesis: Greed").quality
<EffectQuality.GOOD: 0>

>>> ash.display_amount(Item("big rock"))
6540

>>> ash.appearance_rates(Location("Barf Mountain"))
{Monster('none'): 0.0,
 Monster('angry tourist'): 33.333333333333336,
 Monster('horrible tourist family'): 33.333333333333336,
 Monster('garbage tourist'): 33.333333333333336}

>>> get_property("sourceTerminalEducate1")
'digitize.edu'

>>> get_property("_sourceTerminalDigitizeMonster", Monster)
Monster('Knob Goblin Embezzler')

>>> boxing_daycare.have()
True

>>> witchess.fights_left()
5
```

## Acknowledgements

This project was inspired by Samuel Gaus's [frattlesnake](https://github.com/gausie/frattlesnake) and tadpoleloop's [pymafia](https://github.com/tadpoleloop/pymafia) repositories.