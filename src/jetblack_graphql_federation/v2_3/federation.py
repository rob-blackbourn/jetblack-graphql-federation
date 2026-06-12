from ..v2_2 import Federation as _Federation

from .directives import InterfaceObjectDirective


class Federation(_Federation):
    """Federation v2.3

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v23
    """

    VERSION = "v2.3"

    InterfaceObjectDirective = InterfaceObjectDirective
