# -*- coding: utf-8 -*-

from numpy import pi

from ....Methods.Slot.Slot.check import SlotCheckError


def check(self):
    """Check that the HoleM53 object is correct

    Parameters
    ----------
    self : HoleM53
        A HoleM53 object

    Returns
    -------
    None

    Raises
    -------
    S53_Rbo0CheckError
        You must have H0 < Rbo
    S53_Rbo1CheckError
        You must have H1 < Rbo
    S53_W4CheckError
        You must have W4 < pi/2
    S53_W5CheckError
        You must have W5 >=0
    """

    # Check that everything is set
    if self.W1 is None:
        raise S53_NoneError("You must set W1 !")
    elif self.W2 is None:
        raise S53_NoneError("You must set W2 !")
    elif self.W3 is None:
        raise S53_NoneError("You must set W3 !")
    elif self.W4 is None:
        raise S53_NoneError("You must set W4 !")
    elif self.H0 is None:
        raise S53_NoneError("You must set H0 !")
    elif self.H1 is None:
        raise S53_NoneError("You must set H1 !")
    elif self.H2 is None:
        raise S53_NoneError("You must set H2 !")
    elif self.H3 is None:
        raise S53_NoneError("You must set H3 !")

    Rbo = self.get_Rbo()

    if Rbo <= self.H0:
        raise S53_Rbo0CheckError("You must have H0 < Rbo")

    if Rbo <= self.H1:
        raise S53_Rbo1CheckError("You must have H1 < Rbo")

    if pi / 2 <= self.W4:
        raise S53_W4CheckError("You must have W4 < pi/2")

    if self.comp_W5() < 0:
        raise S53_W5CheckError("You must have W5 >=0")


class S53_NoneError(SlotCheckError):
    """Raised when a propery of HoleM53 is None"""

    pass


class S53_Rbo0CheckError(SlotCheckError):
    """ """

    pass


class S53_Rbo1CheckError(SlotCheckError):
    """ """

    pass


class S53_W4CheckError(SlotCheckError):
    """ """

    pass


class S53_W5CheckError(SlotCheckError):
    """ """

    pass
