from typing import ClassVar

from .directives import (
    ExtendsDirective,
    ExtendsDirectiveKwargs,
    ExternalDirective,
    ExternalDirectiveKwargs,
    KeyDirective,
    KeyDirectiveKwargs,
    ProvidesDirective,
    ProvidesDirectiveKwargs,
    RequiresDirective,
    RequiresDirectiveKwargs,
)

from ..types import AbstractScalar, DirectiveType
from .scalars import (
    FieldSetScalar,
)

type KeyDirectiveType = DirectiveType[KeyDirectiveKwargs]
type RequiresDirectiveType = DirectiveType[RequiresDirectiveKwargs]
type ProvidesDirectiveType = DirectiveType[ProvidesDirectiveKwargs]
type ExternalDirectiveType = DirectiveType[ExternalDirectiveKwargs]
type ExtendsDirectiveType = DirectiveType[ExtendsDirectiveKwargs]


class Federation:
    """Federation v1.0

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v10
    """

    VERSION: ClassVar[str] = "v1.0"

    # Scalars
    FieldSetScalar: type[AbstractScalar] = FieldSetScalar

    # Directives
    KeyDirective: ClassVar[KeyDirectiveType] = KeyDirective
    RequiresDirective: ClassVar[RequiresDirectiveType] = RequiresDirective
    ProvidesDirective: ClassVar[ProvidesDirectiveType] = ProvidesDirective
    ExternalDirective: ClassVar[ExternalDirectiveType] = ExternalDirective
    ExtendsDirective: ClassVar[ExtendsDirectiveType] = ExtendsDirective
