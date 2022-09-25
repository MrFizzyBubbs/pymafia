# pymafia

A Python module and bridge for reflecting KoLmafia's Java environment.

## Overview

The aim of the `pymafia` module is to provide an easy-to-use environment for scripting [Kingdom of Loathing](https://www.kingdomofloathing.com/) in Python. It achieves this by reflecting and wrapping the community-developed [KoLmafia](https://github.com/kolmafia/kolmafia) desktop tool. While [other languages](https://loathing-associates-scripting-society.github.io/KoL-Scripting-Resources/) for scripting KoL exist, they are arguably less approachable to non-developers than Python (although the efforts of [LASS](https://github.com/Loathing-Associates-Scripting-Society) have made this less so). This project was inspired by Samuel Gaus's [frattlesnake repository](https://github.com/gausie/frattlesnake).

## Installation

```
pip install pymafia
```
The `pymafia` module uses [PyJNIus](https://github.com/kivy/pyjnius) to access Java classes, so make sure a Java Development Kit (JDK) is installed on your operating system. On windows, make sure `JAVA_HOME` points to your java installation so PyJNIus can locate the `jvm.dll` file to start java. For more information see https://pyjnius.readthedocs.io/en/stable/installation.html.

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
