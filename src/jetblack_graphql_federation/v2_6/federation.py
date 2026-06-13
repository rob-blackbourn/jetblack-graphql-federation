from typing import ClassVar

from ..v2_5 import Federation as Federation_v2_5

from .directives import PolicyDirective
from .scalars import PolicyScalar


type PolicyScalarType = type[PolicyScalar]
type PolicyDirectiveType = type[PolicyDirective]


class Federation(Federation_v2_5):
    """Federation v2.6

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v26
    """

    VERSION = "v2.6"

    # Scalars
    PolicyScalar: ClassVar[PolicyScalarType] = PolicyScalar

    # Directives
    PolicyDirective: ClassVar[PolicyDirectiveType] = PolicyDirective
