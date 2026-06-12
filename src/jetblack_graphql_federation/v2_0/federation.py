from typing import ClassVar

from ..v1_0 import Federation as v1_0

from .directives import (
    ExternalDirective,
    ExternalKwargs,
    InaccessibleDirective,
    KeyDirective,
    KeyKwargs,
    OverrideDirective,
    ProvidesDirective,
    RequiresDirective,
    ShareableDirective,
    ShareableKwargs,
    TagDirective
)

from ..types import AbstractDirective

from .scalars import FieldSet, FieldSetNode

type KeyDirectiveType = type[AbstractDirective[KeyKwargs]]


class Federation:
    """Federation v2.0

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v20
    """

    VERSION = "v2.0"

    # Scalars
    FieldSet = FieldSet

    # Directives
    KeyDirective: ClassVar[KeyDirectiveType] = KeyDirective
    RequiresDirective = RequiresDirective
    ProvidesDirective = ProvidesDirective
    ExternalDirective: type[AbstractDirective[ExternalKwargs]
                            ] = ExternalDirective
    ShareableDirective: type[AbstractDirective[ShareableKwargs]
                             ] = ShareableDirective
    ExtendsDirective = v1_0.ExtendsDirective
    OverrideDirective = OverrideDirective
    InaccessibleDirective = InaccessibleDirective
    TagDirective = TagDirective

    # Scalar Nodes
    FieldSetNode = FieldSetNode
