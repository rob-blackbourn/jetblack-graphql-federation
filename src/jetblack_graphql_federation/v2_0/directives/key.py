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
    """The @key directive

    directive @key(
      fields: FieldSet!,
      resolvable: Boolean = true
    ) repeatable on OBJECT | INTERFACE
    """

    NAME = "key"
    ARG_NAME_FIELDS = "fields"
    ARG_NAME_RESOLVABLE = "resolvable"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
        ),
        args={
            ARG_NAME_FIELDS: GraphQLArgument(GraphQLNonNull(FieldSet)),
            # Changed from v1.0
            ARG_NAME_RESOLVABLE: GraphQLArgument(GraphQLBoolean, default_value=True),
        },
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
                            value="FieldSet"
                        )

                    )
                )
            ),
            InputValueDefinitionNode(
                name=NameNode(value=ARG_NAME_RESOLVABLE),
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
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_FIELDS),
                    value=StringValueNode(
                        value=kwargs[cls.ARG_NAME_FIELDS], block=False),
                ),
                ArgumentNode(
                    name=NameNode(value=cls.ARG_NAME_RESOLVABLE),
                    value=BooleanValueNode(
                        value=kwargs[cls.ARG_NAME_RESOLVABLE]
                    ),
                ),
            )
        )
