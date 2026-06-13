from typing import TypedDict

from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective


class ShareableDirectiveKwargs(TypedDict):
    ...


class ShareableDirective(AbstractDirective[ShareableDirectiveKwargs]):
    """The @shareable directive

    directive @shareable on FIELD_DEFINITION | OBJECT
    """

    NAME = "shareable"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
        ),
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(),
        repeatable=False,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='OBJECT'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: ShareableDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(),
        )
