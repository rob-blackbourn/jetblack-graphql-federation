from ..v2_5 import Federation as _Federation

from .directives import PolicyDirective
from .scalars import Policy, PolicyNode


class Federation(_Federation):
    """Federation v2.6

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v26
    """

    VERSION = "v2.6"

    # Scalars
    Policy = Policy
    PolicyNode = PolicyNode

    # Directives
    PolicyDirective = PolicyDirective
