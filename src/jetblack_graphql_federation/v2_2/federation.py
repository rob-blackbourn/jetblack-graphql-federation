from .directives import ShareableDirective

from ..v2_1 import Federation as Federation_v2_1


class Federation(Federation_v2_1):
    """Federation v2.2

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v22
    """

    VERSION = "v2.2"

    ShareableDirective = ShareableDirective
