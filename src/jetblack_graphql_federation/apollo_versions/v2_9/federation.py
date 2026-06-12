from ..v2_8 import Federation as v2_8

from .directives import ListSizeDirective, RequiresScopeDirective


class Federation(v2_8):
    """Federation v2.9

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v29
    """

    VERSION = "v2.9"

    # Directives
    ListSizeDirective = ListSizeDirective
    RequiresScopeDirective = RequiresScopeDirective
