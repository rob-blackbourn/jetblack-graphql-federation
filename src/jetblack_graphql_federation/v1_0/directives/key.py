from typing import TypedDict, Required

from graphql import (
    ArgumentNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    InputValueDefinitionNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    StringValueNode,
)

from ...types import AbstractDirective
from ..scalars import FieldSetScalar


class KeyKwargs(TypedDict):
    fields: Required[str]


class KeyDirective[KeyKwargs](AbstractDirective):
    """The @key directive

    directive @key(fields: _FieldSet!) repeatable on OBJECT | INTERFACE
    """

    NAME = "key"
    ARG_NAME_FIELDS = "fields"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
        ),
        args={ARG_NAME_FIELDS: GraphQLArgument(
            GraphQLNonNull(FieldSetScalar.Type))},
        description=f"Federation @{NAME} directive",
        is_repeatable=True,
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME_FIELDS),
                type=NonNullTypeNode(
                    type=NamedTypeNode(
                        name=NameNode(
                            value=FieldSetScalar.NAME
                        )

                    )
                )
            )
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
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_FIELDS),
                    value=StringValueNode(value=kwargs[cls.ARG_NAME_FIELDS]),
                ),
            )
        )
