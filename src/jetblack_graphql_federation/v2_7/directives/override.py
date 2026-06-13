from typing import TypedDict, Required, NotRequired

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


class OverrideDirectiveKwargs(TypedDict):
    from_: Required[str]
    label: NotRequired[str]


class OverrideDirective(AbstractDirective[OverrideDirectiveKwargs]):
    """The @override directive

    directive @override(from: String!, label: String) on FIELD_DEFINITION
    """

    NAME = 'override'
    ARG_FROM = 'from'
    ARG_LABEL = 'label'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        args={
            ARG_FROM: GraphQLArgument(GraphQLNonNull(GraphQLString)),
            ARG_LABEL: GraphQLArgument(GraphQLString),
        },
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_FROM),
                type=NonNullTypeNode(
                    type=NamedTypeNode(
                        name=NameNode(
                            value='String'
                        )
                    )
                )
            ),
            InputValueDefinitionNode(
                name=NameNode(value=ARG_FROM),
                type=NamedTypeNode(
                    name=NameNode(
                        value='String'
                    )
                )
            ),
        ),
        repeatable=True,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: OverrideDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_FROM),
                    value=StringValueNode(value=kwargs["from_"]),
                ),
                ArgumentNode(
                    name=NameNode(value=cls.ARG_LABEL),
                    value=StringValueNode(value=kwargs.get("label")),
                ),
            )
        )
