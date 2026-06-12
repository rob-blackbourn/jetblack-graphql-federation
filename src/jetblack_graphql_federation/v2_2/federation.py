from ..v2_1 import Federation as _Federation

from .directives import ShareableDirective


class Federation(_Federation):
    """Federation v2.2

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v22
    """

    VERSION = "v2.2"

    ShareableDirective = ShareableDirective
