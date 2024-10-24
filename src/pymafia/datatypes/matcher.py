from typing import Any

import wrapt


class Matcher(wrapt.ObjectProxy):
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.__wrapped__ == other.__wrapped__
        return super().__eq__(other)
