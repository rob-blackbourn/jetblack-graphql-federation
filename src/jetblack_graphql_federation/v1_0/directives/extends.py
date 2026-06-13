from typing import TypedDict

from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective


class ExtendsDirectiveKwargs(TypedDict):
    ...


class ExtendsDirective(AbstractDirective[ExtendsDirectiveKwargs]):
    """Te @extends directive

    directive @extends on OBJECT | INTERFACE
    """

    NAME = "extends"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
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
    def Node(cls, **kwargs: ExtendsDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=()
        )
