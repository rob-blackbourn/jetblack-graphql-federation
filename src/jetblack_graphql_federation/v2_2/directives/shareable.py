from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective


class ShareableDirective[NoneType](AbstractDirective):

    Type = GraphQLDirective(
        name="shareable",
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
        ),
        description="Federation @shareable directive",
    )

    # directive @shareable repeatable on OBJECT | FIELD_DEFINITION
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value="shareable"),
        arguments=(),
        repeatable=True,  # Changed to be repeatable.
        locations=(
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='OBJECT'),
        )
    )

    @classmethod
    def Node(cls) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value='shareable'),
            arguments=(),
        )
