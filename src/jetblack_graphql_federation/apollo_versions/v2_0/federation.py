from ..v1_0 import Federation as v1_0

from .directives import (
    ExternalDirective,
    InaccessibleDirective,
    KeyDirective,
    OverrideDirective,
    ProvidesDirective,
    RequiresDirective,
    ShareableDirective,
    TagDirective
)

from .scalars import FieldSet


class Federation:
    """Federation v2.0

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v20
    """

    VERSION = "v2.0"

    # Scalars
    FieldSet = FieldSet

    # Directives
    KeyDirective = KeyDirective
    RequiresDirective = RequiresDirective
    ProvidesDirective = ProvidesDirective
    ExternalDirective = ExternalDirective
    ShareableDirective = ShareableDirective
    ExtendsDirective = v1_0.ExtendsDirective
    OverrideDirective = OverrideDirective
    InaccessibleDirective = InaccessibleDirective
    TagDirective = TagDirective
