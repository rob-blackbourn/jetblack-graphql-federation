from typing import TypedDict, Required, NotRequired

from graphql import (
    ArgumentNode,
    BooleanValueNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLDirective,
    GraphQLNonNull,
    InputValueDefinitionNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    StringValueNode,
)

from ...types import AbstractDirective

from ..scalars import FieldSet


class KeyKwargs(TypedDict):
    fields: Required[str]
    resolvable: NotRequired[bool]


class KeyDirective[KeyKwargs](AbstractDirective):

    Type = GraphQLDirective(
        name="key",
        locations=(
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
        ),
        args={
            "fields": GraphQLArgument(GraphQLNonNull(FieldSet)),
            # Changed from v1.0
            "resolvable": GraphQLArgument(GraphQLBoolean, default_value=True),
        },
        description="Federation @key directive",
        is_repeatable=True,
    )

    # directive @key(
    #   fields: FieldSet!,
    #   resolvable: Boolean = true
    # ) repeatable on OBJECT | INTERFACE
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value="key"),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value="fields"),
                type=NonNullTypeNode(
                    type=NamedTypeNode(
                        name=NameNode(
                            value="FieldSet"
                        )

                    )
                )
            ),
            InputValueDefinitionNode(
                name=NameNode(value="resolvable"),
                type=NamedTypeNode(
                    name=NameNode(value='Boolean')
                ),
                default_value=BooleanValueNode(
                    value=True
                )

            ),
        ),
        repeatable=True,
        locations=(
            NameNode(value='OBJECT'),
            NameNode(value='INTERFACE')
        )
    )

    @classmethod
    def Node(cls, **kwargs: KeyKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value='key'),
            arguments=(
                ArgumentNode(
                    name=NameNode(value='fields'),
                    value=StringValueNode(value=kwargs['fields'], block=False),
                ),
                ArgumentNode(
                    name=NameNode(value='resolvable'),
                    value=BooleanValueNode(value=kwargs['resolvable']),
                ),
            )
        )
