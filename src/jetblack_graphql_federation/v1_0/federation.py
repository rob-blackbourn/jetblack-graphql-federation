from .directives import (
    ExtendsDirective,
    ExtendsDirectiveNode,
    ExternalDirective,
    KeyDirective,
    ProvidesDirective,
    RequiresDirective,
)
from .scalars import (
    _FieldSet,
    _FieldSetNode
)


class Federation:
    """Federation v1.0

    See: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#v10
    """

    VERSION = "v1.0"

    # Scalars
    FieldSet = _FieldSet
    FieldSetNode = _FieldSetNode

    # Directives
    KeyDirective = KeyDirective
    RequiresDirective = RequiresDirective
    ProvidesDirective = ProvidesDirective
    ExternalDirective = ExternalDirective
    ExtendsDirective = ExtendsDirective

    # Directive Definition Nodes
    ExtendsDirectiveNode = ExtendsDirectiveNode
