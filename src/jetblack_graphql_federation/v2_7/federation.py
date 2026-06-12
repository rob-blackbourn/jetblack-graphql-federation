from ..v2_6 import Federation as _Federation

from .directives import OverrideDirective


class Federation(_Federation):
    """Federation v2.7

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v27
    """

    VERSION = "v2.7"

    # Directives
    OverrideDirective = OverrideDirective
