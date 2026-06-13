from typing import TypedDict, Required

from graphql import (
    ArgumentNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLInt,
    GraphQLNonNull,
    InputValueDefinitionNode,
    IntValueNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
)

from ...types import AbstractDirective


class CostDirectiveKwargs(TypedDict):
    fields: Required[int]


class CostDirective(AbstractDirective[CostDirectiveKwargs]):
    """The @cost directive

    directive @cost(weight: Int!) on
      | ARGUMENT_DEFINITION
      | ENUM
      | FIELD_DEFINITION
      | INPUT_FIELD_DEFINITION
      | OBJECT
      | SCALAR;
    """

    NAME = 'cost'
    ARG_WEIGHT = 'weight'

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.ARGUMENT_DEFINITION,
            DirectiveLocation.ENUM,
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.INPUT_FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
            DirectiveLocation.SCALAR,
        ),
        args={
            ARG_WEIGHT: GraphQLArgument(GraphQLNonNull(GraphQLInt)),
        },
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_WEIGHT),
                type=NonNullTypeNode(
                    type=NamedTypeNode(
                        name=NameNode(
                            value=GraphQLInt.name
                        )
                    )
                )
            )
        ),
        repeatable=True,
        locations=(
            NameNode(value='ARGUMENT_DEFINITION'),
            NameNode(value='ENUM'),
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='INPUT_FIELD_DEFINITION'),
            NameNode(value='OBJECT'),
            NameNode(value='SCALAR'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: CostDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_WEIGHT),
                    value=IntValueNode(value=str(kwargs[cls.ARG_WEIGHT])),
                ),
            )
        )
