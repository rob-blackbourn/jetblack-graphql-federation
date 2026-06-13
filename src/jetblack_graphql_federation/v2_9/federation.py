from typing import ClassVar

from ..v2_8 import Federation as Federation_v2_8

from .directives import (
    ListSizeDirective,
    CostDirective,
)

type ListSizeDirectiveType = type[ListSizeDirective]
type CostDirectiveType = type[CostDirective]


class Federation(Federation_v2_8):
    """Federation v2.9

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v29
    """

    VERSION = "v2.9"

    # Directives
    ListSizeDirective: ClassVar[ListSizeDirectiveType] = ListSizeDirective
    RequiresScopeDirective: ClassVar[CostDirectiveType] = CostDirective
