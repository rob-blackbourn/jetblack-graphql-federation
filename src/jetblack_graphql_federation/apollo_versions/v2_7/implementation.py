from ..v2_6 import Federation as v2_6

from .directives import OverrideDirective


class Federation(v2_6):

    # Directives
    OverrideDirective = OverrideDirective
