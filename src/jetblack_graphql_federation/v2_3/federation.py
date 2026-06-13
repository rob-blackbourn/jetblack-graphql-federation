from typing import ClassVar

from ..v2_2 import Federation as Federation_v2_2

from .directives import InterfaceObjectDirective


type InterfaceObjectDirectiveType = type[InterfaceObjectDirective]


class Federation(Federation_v2_2):
    """Federation v2.3

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v23
    """

    VERSION = "v2.3"

    InterfaceObjectDirective: ClassVar[InterfaceObjectDirectiveType] = InterfaceObjectDirective
