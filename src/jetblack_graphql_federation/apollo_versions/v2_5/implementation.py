from ..v2_4 import Federation as v2_4

from .directives import AuthenticatedDirective, RequiresScopeDirective
from .scalars import Scope, ScopeNode


class Federation(v2_4):

    # Scalars
    Scope = Scope
    ScopeNode = ScopeNode

    # Directives
    AuthenticatedDirective = AuthenticatedDirective
    RequiresScopeDirective = RequiresScopeDirective
