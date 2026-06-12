from ..v2_8 import Federation as v2_8

from .directives import ListSizeDirective, RequiresScopeDirective


class Federation(v2_8):

    # Directives
    ListSizeDirective = ListSizeDirective
    RequiresScopeDirective = RequiresScopeDirective
