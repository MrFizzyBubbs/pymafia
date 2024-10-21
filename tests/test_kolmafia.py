import pytest

from pymafia.kolmafia import KoLmafiaError, km


def test_error_handling():
    with pytest.raises(KoLmafiaError, match="specific error message"):
        km.KoLmafia.updateDisplay(
            km.KoLConstants.MafiaState.ABORT, "specific error message"
        )
    assert km.KoLmafia.permitsContinue()
