from typing import ClassVar

from ..v1_0 import Federation as v1_0
from ..types import AbstractDirective

from .directives import TagDirective, TagKwargs

type TagDirectiveType = type[AbstractDirective[TagKwargs]]


class Federation(v1_0):
    """Federation v1.1

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v11
    """

    VERSION = "v1.1"

    # Directives
    TagDirective: ClassVar[TagDirectiveType] = TagDirective
