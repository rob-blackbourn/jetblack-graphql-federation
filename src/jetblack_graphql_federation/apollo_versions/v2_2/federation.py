from ..v2_1 import Federation as v2_1

from .directives import ShareableDirective


class Federation(v2_1):
    """Federation v2.2

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v22
    """

    VERSION = "v2.2"

    ShareableDirective = ShareableDirective
