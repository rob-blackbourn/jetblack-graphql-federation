from typing import ClassVar

from .directives import (
    InaccessibleDirective,
    InaccessibleDirectiveKwargs,
    KeyDirective,
    KeyDirectiveKwargs,
    OverrideDirective,
    OverrideDirectiveKwargs,
    ShareableDirective,
    ShareableDirectiveKwargs,
)

from ..v1_1 import Federation as Federation_v1_1
from ..types import DirectiveType

from .scalars import FieldSetScalar

type FieldSetScalarType = type[FieldSetScalar]
type KeyDirectiveType = DirectiveType[KeyDirectiveKwargs]
type ShareableDirectiveType = DirectiveType[ShareableDirectiveKwargs]
type InaccessibleDirectiveType = DirectiveType[InaccessibleDirectiveKwargs]
type OverrideDirectiveType = DirectiveType[OverrideDirectiveKwargs]


class Federation:
    """Federation v2.0

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v20
    """

    VERSION = "v2.0"

    # Scalars
    FieldSetScalar: ClassVar[FieldSetScalarType] = FieldSetScalar

    # Directives
    KeyDirective: ClassVar[KeyDirectiveType] = KeyDirective
    ShareableDirective: ClassVar[ShareableDirectiveType] = ShareableDirective
    InaccessibleDirective: ClassVar[InaccessibleDirectiveType] = InaccessibleDirective
    OverrideDirective: ClassVar[OverrideDirectiveType] = OverrideDirective

    RequiresDirective = Federation_v1_1.RequiresDirective
    ProvidesDirective = Federation_v1_1.ProvidesDirective
    ExternalDirective = Federation_v1_1.ExternalDirective
    ExtendsDirective = Federation_v1_1.ExtendsDirective
    TagDirective = Federation_v1_1.TagDirective
