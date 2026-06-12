from ..v2_7 import Federation as _Federation

from .directives import ContextDirective, FromContextDirective
from .scalars import ContextFieldValue


class Federation(_Federation):
    """Federation v2.8

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v28
    """

    VERSION = "v2.8"

    # Scalars
    ContextFieldValue = ContextFieldValue

    # Directives
    ContextDirective = ContextDirective
    FromContextDirective = FromContextDirective
