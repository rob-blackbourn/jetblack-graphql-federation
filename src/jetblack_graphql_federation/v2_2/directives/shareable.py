from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective
from ...v2_0.directives import ShareableDirectiveKwargs


class ShareableDirective(AbstractDirective[ShareableDirectiveKwargs]):
    """The @shareable directive

    ## Directive changes

    Added `repeatable` to the directive definition.

    ```graphql    
    directive @shareable repeatable on OBJECT | FIELD_DEFINITION
    ```
    """

    NAME = "shareable"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.OBJECT,
            DirectiveLocation.FIELD_DEFINITION,
        ),
        is_repeatable=True,
        description=f"Federation @{NAME} directive",
    )

    # directive @shareable repeatable on OBJECT | FIELD_DEFINITION
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(),
        repeatable=True,  # Changed to be repeatable.
        locations=(
            NameNode(value='OBJECT'),
            NameNode(value='FIELD_DEFINITION'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: ShareableDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(),
        )
