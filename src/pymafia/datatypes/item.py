from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, ClassVar

from jpype import JClass

from pymafia.kolmafia import km

if TYPE_CHECKING:
    from pymafia.datatypes.coinmaster import Coinmaster
    from pymafia.datatypes.skill import Skill

EnumSet = JClass("java.util.EnumSet")


class CandyType(Enum):
    NONE = km.CandyDatabase.CandyType.NONE
    UNSPADED = km.CandyDatabase.CandyType.UNSPADED
    SIMPLE = km.CandyDatabase.CandyType.SIMPLE
    COMPLEX = km.CandyDatabase.CandyType.COMPLEX


@dataclass(frozen=True, order=True)
class Item:
    NONE: ClassVar[Item]

    id: int = km.DataTypes.ITEM_INIT.contentLong
    name: str = km.DataTypes.ITEM_INIT.contentString

    def __init__(self, key: int | str | None = None):
        if (isinstance(key, str) and key.casefold() == self.name.casefold()) or key in (
            self.id,
            None,
        ):
            return

        id = km.ItemDatabase.getItemId(key) if isinstance(key, str) else key
        name = km.ItemDatabase.getItemDataName(id)
        if name is None:
            raise ValueError(f"{type(self).__name__} {key!r} not found")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name)

    def __str__(self) -> str:
        ids = km.ItemDatabase.getItemIds(self.name, 1, False)
        return f"[{self.id}]{self.name}" if len(ids) > 1 else self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}({str(self)!r})"

    def __bool__(self) -> bool:
        return self != type(self)()

    @classmethod
    def all(cls) -> list[Item]:
        from pymafia.ash.conversion import from_java

        values = km.DataTypes.ITEM_TYPE.allValues()
        return sorted(from_java(values))

    @property
    def tcrs_name(self) -> str:
        """Return the name of the Item as it appears in your current Two Crazy Random Summer run. If you are not in a TCRS run, the regular Item name is returned."""
        return km.TCRSDatabase.getTCRSName(self.id) or ""

    @property
    def plural(self) -> str:
        """Return the plural of the Item. If the official plural is not known, return the name of the Item with an "s" appended."""
        return km.ItemDatabase.getPluralName(self.id)

    @property
    def descid(self) -> str:
        """Return the descid of the Item. This is the identifier used to see the description of the Item."""
        return km.ItemDatabase.getDescriptionId(self.id)

    @property
    def image(self) -> str:
        """Return the filename of the image associated with the Item."""
        return km.ItemDatabase.getImage(self.id)

    @property
    def smallimage(self) -> str:
        """Returns the filename of the small image associated with the Item. For items with an image that is usually larger than 30x30, returns their 30x30 equivalent.

        For example, "folders" from the "over-the-shoulder Folder Holder" will normally return a 100x100 image but a 30x30 image here.
        """
        return km.ItemDatabase.getSmallImage(self.id)

    @property
    def levelreq(self) -> int:
        """Return the level requirement for consuming or equipping the Item."""
        return km.ConsumablesDatabase.getLevelReqByName(self.name) or 0

    @property
    def quality(self) -> str:
        """Return the quality of the Item if it is a consumable."""
        return km.ConsumablesDatabase.getQuality(self.name).getName()

    @property
    def adventures(self) -> str:
        """Return the range of adventures gained from consuming the Item. The string will either contain the adventures for invariant gains, or a hyphen-separated minimum and maximum for variant gains."""
        return km.ConsumablesDatabase.getBaseAdventureRange(self.name)

    @property
    def muscle(self) -> str:
        """Return the range of muscle substats gained from consuming the Item. The string will either contain the substats for invariant gains, or a hyphen-separated minimum and maximum for variant gains. Note that substat gains can be negative."""
        return km.ConsumablesDatabase.getBaseMuscleByName(self.name)

    @property
    def mysticality(self) -> str:
        """Return the range of mysticality substats gained from consuming the Item. The string will either contain the substats for invariant gains, or a hyphen-separated minimum and maximum for variant gains. Note that substat gains can be negative."""
        return km.ConsumablesDatabase.getBaseMysticalityByName(self.name)

    @property
    def moxie(self) -> str:
        """Return the range of moxie substats gained from consuming the Item. The string will either contain the substats for invariant gains, or a hyphen-separated minimum and maximum for variant gains. Note that substat gains can be negative."""
        return km.ConsumablesDatabase.getBaseMoxieByName(self.name)

    @property
    def fullness(self) -> int:
        """Return the stomach size of Item. If the Item is not edible, return 0."""
        return km.ConsumablesDatabase.getFullness(self.name)

    @property
    def inebriety(self) -> int:
        """Return the liver size of Item. If the Item is not drinkable, return 0."""
        return km.ConsumablesDatabase.getInebriety(self.name)

    @property
    def spleen(self) -> int:
        """Return the spleen size of Item. If the Item is not chewable, return 0."""
        return km.ConsumablesDatabase.getSpleenHit(self.name)

    @property
    def minhp(self) -> int:
        """Return the minimum HP restored by consuming this Item."""
        return km.RestoresDatabase.getHPMin(self.name)

    @property
    def maxhp(self) -> int:
        """Return the maximum HP restored by consuming this Item."""
        return km.RestoresDatabase.getHPMax(self.name)

    @property
    def minmp(self) -> int:
        """Return the minimum MP restored by consuming this Item."""
        return km.RestoresDatabase.getMPMin(self.name)

    @property
    def maxmp(self) -> int:
        """Return the maximum MP restored by consuming this Item."""
        return km.RestoresDatabase.getMPMax(self.name)

    @property
    def dailyusesleft(self) -> int:
        """Return the number of daily uses remaining for this Item."""
        return km.UseItemRequest.maximumUses(self.id)

    @property
    def notes(self) -> str:
        """Return any notes that exist for the Item. Examples of (comma-separated) contents are:

        - The name and duration of any effects granted by consumption, if applicable.
        - Items dropped when the item is consumed, if applicable.
        - Tags relevant to game mechanics (such as "MARTINI", "BEER" and "SAUCY")
        - "Unspaded"
        """
        return km.ConsumablesDatabase.getNotes(self.name) or ""

    @property
    def quest(self) -> bool:
        """Return True if the Item is a quest item, else False."""
        return km.ItemDatabase.isQuestItem(self.id)

    @property
    def gift(self) -> bool:
        """Return True if the Item is a gift item, else False."""
        return km.ItemDatabase.isGiftItem(self.id)

    @property
    def tradeable(self) -> bool:
        """Return True if the Item is tradeable, else False."""
        return km.ItemDatabase.isTradeable(self.id)

    @property
    def discardable(self) -> bool:
        """Return True if the Item is discardable, else False."""
        return km.ItemDatabase.isDiscardable(self.id)

    @property
    def combat(self) -> bool:
        """Return True if the Item is usable in combat, else False. This returns True whether the Item is consumed by being used or not."""
        mask = EnumSet.of(
            km.ItemDatabase.Attribute.COMBAT,
            km.ItemDatabase.Attribute.COMBAT_REUSABLE,
        )
        return km.ItemDatabase.getAttribute(self.id, mask)

    @property
    def combat_reusable(self) -> bool:
        """Return True if the Item is usable in combat and is not consumed when doing so, else False."""
        return km.ItemDatabase.getAttribute(
            self.id, km.ItemDatabase.Attribute.COMBAT_REUSABLE
        )

    @property
    def usable(self) -> bool:
        """Return True if the Item is usable, else False. This returns True whether the Item is consumed by being used or not."""
        return km.ItemDatabase.isUsable(self.id)

    @property
    def reusable(self) -> bool:
        """Return True if the Item is usable and is not consumed when doing so, else False."""
        return km.ItemDatabase.getConsumptionType(
            self.id
        ) == km.KoLConstants.ConsumptionType.USE_INFINITE or km.ItemDatabase.getAttribute(
            self.id, km.ItemDatabase.Attribute.REUSABLE
        )

    @property
    def multi(self) -> bool:
        """Return True if the Item is multiusable, else False."""
        return km.ItemDatabase.isMultiUsable(self.id)

    @property
    def fancy(self) -> bool:
        """Return True if the Item is a "fancy" ingredient, else False."""
        return km.ItemDatabase.isFancyItem(self.id)

    @property
    def pasteable(self) -> bool:
        """Return True if the Item is a meatpasting ingredient, else False."""
        return km.ItemDatabase.isPasteable(self.id)

    @property
    def smithable(self) -> bool:
        """Return True if the Item is a meatsmithing ingredient, else False."""
        return km.ItemDatabase.isSmithable(self.id)

    @property
    def cookable(self) -> bool:
        """Return True if the Item is a cooking ingredient, else False."""
        return km.ItemDatabase.isCookable(self.id)

    @property
    def mixable(self) -> bool:
        """Return True if the Item is a cocktailcrafting ingredient, else False."""
        return km.ItemDatabase.isMixable(self.id)

    @property
    def candy(self) -> bool:
        """Return True if the Item is a candy, else False."""
        return km.ItemDatabase.isCandyItem(self.id)

    @property
    def candy_type(self) -> CandyType:
        """Return the candy type of the Item."""
        return CandyType(km.CandyDatabase.getCandyType(self.id))

    @property
    def chocolate(self) -> bool:
        """Return True if the Item is a chocolate, else False."""
        return km.ItemDatabase.isChocolateItem(self.id)

    @property
    def potion(self) -> bool:
        """Return True if the Item is a potion, else False."""
        return km.ItemDatabase.isPotion(self.id)

    @property
    def seller(self) -> Coinmaster:
        """Return which Coinmaster sells this Item, if any."""
        from pymafia.datatypes.coinmaster import Coinmaster

        data = km.CoinmasterRegistry.findSeller(self.id)
        return Coinmaster(data.getMaster()) if data is not None else Coinmaster()

    @property
    def buyer(self) -> Coinmaster:
        """Return which Coinmaster buys this Item, if any."""
        from pymafia.datatypes.coinmaster import Coinmaster

        data = km.CoinmasterRegistry.findBuyer(self.id)
        return Coinmaster(data.getMaster()) if data is not None else Coinmaster()

    @property
    def name_length(self) -> int:
        """Return the length of the Item's display name."""
        return km.ItemDatabase.getNameLength(self.id)

    @property
    def noob_skill(self) -> Skill:
        """Return the noob Skill granted by absorbing this Item."""
        from pymafia.datatypes.skill import Skill

        try:
            return Skill(km.ItemDatabase.getNoobSkillId(self.id))
        except ValueError:
            return Skill()


Item.NONE = Item()
