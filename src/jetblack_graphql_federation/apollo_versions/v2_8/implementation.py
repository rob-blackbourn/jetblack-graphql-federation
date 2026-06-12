from ..v2_7 import Federation as v2_7

from .directives import ContextDirective, FromContextDirective
from .scalars import ContextFieldValue


class Federation(v2_7):

    # Scalars
    ContextFieldValue = ContextFieldValue

    # Directives
    ContextDirective = ContextDirective
    FromContextDirective = FromContextDirective
