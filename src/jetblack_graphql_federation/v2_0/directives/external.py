from typing import TypedDict

from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective


class ExternalKwargs(TypedDict):
    ...


class ExternalDirective[ExternalKwargs](AbstractDirective):

    Type = GraphQLDirective(
        name="external",
        locations=(
            DirectiveLocation.OBJECT,  # Changed from v1.0
            DirectiveLocation.FIELD_DEFINITION,
        ),
        description="Federation @external directive",
    )

    # directive @external on FIELD_DEFINITION
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value="external"),
        arguments=(),
        repeatable=False,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
        )
    )

    @classmethod
    def Node(cls, **_kwargs: ExternalKwargs) -> DirectiveNode:  # pylint: disable=arguments-differ
        return DirectiveNode(
            name=NameNode(value='external'),
            arguments=(),
        )
