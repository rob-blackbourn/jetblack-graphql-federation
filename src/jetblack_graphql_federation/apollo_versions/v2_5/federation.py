from ..v2_4 import Federation as v2_4

from .directives import AuthenticatedDirective, RequiresScopeDirective
from .scalars import Scope, ScopeNode


class Federation(v2_4):
    """Federation v2.5

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v25
    """

    VERSION = "2.5"

    # Scalars
    Scope = Scope
    ScopeNode = ScopeNode

    # Directives
    AuthenticatedDirective = AuthenticatedDirective
    RequiresScopeDirective = RequiresScopeDirective
