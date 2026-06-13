from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)


class ShareableDirective:
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
    def Node(cls) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(),
        )
