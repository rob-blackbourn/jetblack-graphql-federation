from typing import ClassVar

from ..v2_4 import Federation as Federation_v2_4

from .directives import (
    AuthenticatedDirective,
    RequiresScopesDirective,
)
from .scalars import ScopeScalar

type ScopeScalarType = type[ScopeScalar]
type AuthenticatedDirectiveType = type[AuthenticatedDirective]
type RequiresScopesDirectiveType = type[RequiresScopesDirective]


class Federation(Federation_v2_4):
    """Federation v2.5

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v25
    """

    VERSION = "v2.5"

    # Scalars
    ScopeScalar: ClassVar[ScopeScalarType] = ScopeScalar

    # Directives
    AuthenticatedDirective: ClassVar[AuthenticatedDirectiveType] = AuthenticatedDirective
    RequiresScopesDirective: ClassVar[RequiresScopesDirectiveType] = RequiresScopesDirective
