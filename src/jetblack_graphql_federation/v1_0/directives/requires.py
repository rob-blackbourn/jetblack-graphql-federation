from typing import Required, TypedDict

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


class RequiresKwargs(TypedDict):
    fields: Required[str]


class RequiresDirective[RequiresKwargs](AbstractDirective):
    """The @requires directive

    directive @requires(fields: _FieldSet!) on FIELD_DEFINITION
    """

    NAME = "requires"
    ARG_NAME_FIELDS = "fields"

    RequiresDirective = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        args={
            ARG_NAME_FIELDS: GraphQLArgument(
                GraphQLNonNull(FieldSetScalar.Type))
        },
        description=f"Federation @{NAME} directive",
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
    def Node(cls, **kwargs: RequiresKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_FIELDS),
                    value=StringValueNode(value=kwargs[cls.ARG_NAME_FIELDS]),
                ),
            )
        )
