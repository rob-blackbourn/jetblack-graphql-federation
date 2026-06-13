from typing import ClassVar

from .directives import (
    ExtendsDirective,
    ExternalDirective,
    KeyDirective,
    ProvidesDirective,
    RequiresDirective,
)

from ..types import AbstractScalar
from .scalars import (
    FieldSetScalar,
)

type KeyDirectiveType = type[KeyDirective]
type RequiresDirectiveType = type[RequiresDirective]
type ProvidesDirectiveType = type[ProvidesDirective]
type ExternalDirectiveType = type[ExternalDirective]
type ExtendsDirectiveType = type[ExtendsDirective]


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
