from typing import TypedDict

from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLDirective,
    NameNode,
)

from ...types import AbstractDirective


class InterfaceObjectDirectiveKwargs(TypedDict):
    ...


class InterfaceObjectDirective(AbstractDirective[InterfaceObjectDirectiveKwargs]):
    """The @interfaceObject directive

    directive @interfaceObject on OBJECT
    """

    NAME = "interfaceObject"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.OBJECT,
        ),
        description=f"Federation @{NAME} directive",
    )
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(),
        repeatable=False,
        locations=(
            NameNode(value='OBJECT'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: InterfaceObjectDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(),
        )
