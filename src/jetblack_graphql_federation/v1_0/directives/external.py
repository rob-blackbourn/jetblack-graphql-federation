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
    """The @external directive

    directive @external on FIELD_DEFINITION
    """

    NAME = "external"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(),
        repeatable=False,
        locations=(
            NameNode(value='OBJECT'),
            NameNode(value='INTERFACE'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: ExternalKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=()
        )
