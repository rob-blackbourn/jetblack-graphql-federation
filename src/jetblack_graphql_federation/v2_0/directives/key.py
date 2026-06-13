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

from ..scalars import FieldSetScalar


class KeyDirectiveKwargs(TypedDict):
    fields: Required[str]
    resolvable: NotRequired[bool]


class KeyDirective(AbstractDirective[KeyDirectiveKwargs]):
    """The @key directive

    directive @key(
      fields: FieldSet!,
      resolvable: Boolean = true
    ) repeatable on OBJECT | INTERFACE
    """

    NAME = "key"
    ARG_FIELDS = "fields"
    ARG_RESOLVABLE = "resolvable"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
        ),
        args={
            ARG_FIELDS: GraphQLArgument(GraphQLNonNull(FieldSetScalar.Type)),
            # Changed from v1.0
            ARG_RESOLVABLE: GraphQLArgument(GraphQLBoolean, default_value=True),
        },
        description=f"Federation @{NAME} directive",
        is_repeatable=True,
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
            ),
            InputValueDefinitionNode(
                name=NameNode(value=ARG_RESOLVABLE),
                type=NamedTypeNode(
                    name=NameNode(value=GraphQLBoolean.name)
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
    def Node(cls, **kwargs: KeyDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_FIELDS),
                    value=StringValueNode(
                        value=kwargs[cls.ARG_FIELDS], block=False),
                ),
                ArgumentNode(
                    name=NameNode(value=cls.ARG_RESOLVABLE),
                    value=BooleanValueNode(
                        value=kwargs[cls.ARG_RESOLVABLE]
                    ),
                ),
            )
        )
