from typing import ClassVar

from .directives import (
    ExtendsDirective,
    ExtendsKwargs,
    ExternalDirective,
    ExternalKwargs,
    KeyDirective,
    KeyKwargs,
    ProvidesDirective,
    ProvidesKwargs,
    RequiresDirective,
    RequiresKwargs,
)

from ..types import AbstractDirective, AbstractScalar
from .scalars import (
    FieldSetScalar,
)

type KeyDirectiveType = type[AbstractDirective[KeyKwargs]]
type RequiresDirectiveType = type[RequiresDirective[RequiresKwargs]]
type ProvidesDirectiveType = type[ProvidesDirective[ProvidesKwargs]]
type ExternalDirectiveType = type[ExternalDirective[ExternalKwargs]]
type ExtendsDirectiveType = type[ExtendsDirective[ExtendsKwargs]]


class Federation:
    """Federation v1.0

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v10
    """

    VERSION = "v1.0"

    # Scalars
    FieldSetScalar: type[AbstractScalar] = FieldSetScalar

    # Directives
    KeyDirective: ClassVar[KeyDirectiveType] = KeyDirective
    RequiresDirective: ClassVar[RequiresDirectiveType] = RequiresDirective
    ProvidesDirective: ClassVar[ProvidesDirectiveType] = ProvidesDirective
    ExternalDirective: ClassVar[ExternalDirectiveType] = ExternalDirective
    ExtendsDirective: ClassVar[ExtendsDirectiveType] = ExtendsDirective
