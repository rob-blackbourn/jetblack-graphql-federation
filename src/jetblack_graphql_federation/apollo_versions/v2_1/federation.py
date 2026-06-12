from ..v2_0 import Federation as v2_0

from .directives import ComposeDirective


class Federation(v2_0):
    """Federation v2.1

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v21
    """

    VERSION = "v2.1"

    ComposeDirective = ComposeDirective
