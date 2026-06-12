from typing import TypedDict

from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective


class ShareableKwargs(TypedDict):
    ...


class ShareableDirective[ShareableKwargs](AbstractDirective):

    Type = GraphQLDirective(
        name="shareable",
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
        ),
        description="Federation @shareable directive",
    )

    # directive @shareable on FIELD_DEFINITION | OBJECT
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value="shareable"),
        arguments=(),
        repeatable=False,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='OBJECT'),
        )
    )

    @classmethod
    def Node(cls, **_kwargs: ShareableKwargs) -> DirectiveNode:  # pylint: disable=arguments-differ
        return DirectiveNode(
            name=NameNode(value='shareable'),
            arguments=(),
        )
