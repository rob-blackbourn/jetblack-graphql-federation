from ..v2_6 import Federation as v2_6

from .directives import OverrideDirective


class Federation(v2_6):
    """Federation v2.7

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v27
    """

    VERSION = "v2.7"

    # Directives
    OverrideDirective = OverrideDirective
