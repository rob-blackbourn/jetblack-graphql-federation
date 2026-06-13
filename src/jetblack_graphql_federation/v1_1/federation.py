from typing import ClassVar

from ..v1_0 import Federation as Federation_v1_0

from .directives import TagDirective

type TagDirectiveType = type[TagDirective]


class Federation(Federation_v1_0):
    """Federation v1.1

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v11
    """

    VERSION = "v1.1"

    # Directives
    TagDirective: ClassVar[TagDirectiveType] = TagDirective
