from typing import TypedDict

from graphql import (
    ArgumentNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLString,
    InputValueDefinitionNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    StringValueNode,
)

from ...types import AbstractDirective


class ComposeDirectiveKwargs(TypedDict):
    name: str


class ComposeDirective(AbstractDirective[ComposeDirectiveKwargs]):
    """The @compose directive

    directive @composeDirective(name: String!) repeatable on SCHEMA
    """

    NAME = "composeDirective"
    ARG_NAME = "name"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.SCHEMA,
        ),
        args={
            ARG_NAME: GraphQLArgument(GraphQLNonNull(GraphQLString)),
        },
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME),
                type=NonNullTypeNode(
                    type=NamedTypeNode(name=NameNode(value=GraphQLString.name))
                )
            ),
        ),
        repeatable=True,
        locations=(
            NameNode(value='SCHEMA')
        )
    )

    @classmethod
    def Node(cls, **kwargs: ComposeDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME),
                    value=StringValueNode(value=kwargs[cls.ARG_NAME]),
                ),
            )
        )
