from ..v2_5 import Federation as v2_5

from .directives import PolicyDirective
from .scalars import Policy, PolicyNode


class Federation(v2_5):

    # Scalars
    Policy = Policy
    PolicyNode = PolicyNode

    # Directives
    PolicyDirective = PolicyDirective
