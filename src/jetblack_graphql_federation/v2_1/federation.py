from typing import ClassVar

from ..types import DirectiveType
from ..v2_0 import Federation as Federation_v2_0

from .directives import ComposeDirective, ComposeDirectiveKwargs

type ComposeDirectiveType = DirectiveType[ComposeDirectiveKwargs]


class Federation(Federation_v2_0):
    """Federation v2.1

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v21
    """

    VERSION = "v2.1"

    ComposeDirective: ClassVar[ComposeDirectiveType] = ComposeDirective
