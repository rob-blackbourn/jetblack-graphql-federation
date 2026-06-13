from typing import ClassVar

from ..v2_7 import Federation as Federation_v2_7

from .directives import (
    ContextDirective,
    FromContextDirective,
)
from .scalars import ContextFieldValueScalar

type ContextFieldValueScalarType = type[ContextFieldValueScalar]
type ContextDirectiveType = type[ContextDirective]
type FromContextDirectiveType = type[FromContextDirective]


class Federation(Federation_v2_7):
    """Federation v2.8

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v28
    """

    VERSION = "v2.8"

    # Scalars
    ContextFieldValueScalar: ClassVar[ContextFieldValueScalarType] = ContextFieldValueScalar

    # Directives
    ContextDirective: ClassVar[ContextDirectiveType] = ContextDirective
    FromContextDirective: ClassVar[FromContextDirectiveType] = FromContextDirective
