from typing import Required, TypedDict, Unpack

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

from ..scalars import FieldSetScalar


class RequiresDirectiveKwargs(TypedDict):
    fields: Required[str]


class RequiresDirective:
    """The @requires directive

    directive @requires(fields: _FieldSet!) on FIELD_DEFINITION
    """

    NAME = "requires"
    ARG_FIELDS = "fields"

    RequiresDirective = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        args={
            ARG_FIELDS: GraphQLArgument(
                GraphQLNonNull(FieldSetScalar.Type))
        },
        description=f"Federation @{NAME} directive",
    )
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_FIELDS),
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
            NameNode(value='FIELD_DEFINITION'),
        )
    )

    @classmethod
    def Node(cls, fields: str) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_FIELDS),
                    value=StringValueNode(value=fields),
                ),
            )
        )
