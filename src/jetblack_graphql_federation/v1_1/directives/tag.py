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

from ...v1_0.scalars import FieldSetScalar


class TagKwargs(TypedDict):
    name: Required[str]


class TagDirective[TagKwargs](AbstractDirective):
    """The @tag directive

    directive @tag(name: String!) repeatable on
      | FIELD_DEFINITION
      | INTERFACE
      | OBJECT
      | UNION
    """

    NAME = 'tag'
    ARG_NAME_NAME = 'name'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.INTERFACE,
            DirectiveLocation.OBJECT,
            DirectiveLocation.UNION,
        ),
        args={
            ARG_NAME_NAME: GraphQLArgument(
                GraphQLNonNull(FieldSetScalar.Type))},
        is_repeatable=True,
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME_NAME),
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
    def Node(cls, **kwargs: TagKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_NAME),
                    value=StringValueNode(value=kwargs[cls.ARG_NAME_NAME]),
                ),
            )
        )
