from ..v2_4 import Federation as _Federation

from .directives import AuthenticatedDirective, RequiresScopeDirective
from .scalars import Scope, ScopeNode


class Federation(_Federation):
    """Federation v2.5

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v25
    """

    VERSION = "v2.5"

    # Scalars
    Scope = Scope
    ScopeNode = ScopeNode

    # Directives
    AuthenticatedDirective = AuthenticatedDirective
    RequiresScopeDirective = RequiresScopeDirective
