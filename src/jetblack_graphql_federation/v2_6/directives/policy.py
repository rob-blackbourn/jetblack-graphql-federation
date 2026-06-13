from typing import Literal, TypedDict, Required

from graphql import (
    ArgumentNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLList,
    GraphQLNonNull,
    InputValueDefinitionNode,
    ListTypeNode,
    ListValueNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
    StringValueNode,
)

from ...types import AbstractDirective

from ..scalars import PolicyScalar


class PolicyDirectiveKwargs(TypedDict):
    fields: Required[list[str]]


class PolicyDirective(AbstractDirective[PolicyDirectiveKwargs]):
    """The @policy directive

    directive @policy(policies: [[federation__Policy!]!]!) on
      | FIELD_DEFINITION
      | OBJECT
      | INTERFACE
      | SCALAR
      | ENUM
    """

    NAME = "policy"
    ARG_POLICIES: Literal['policies'] = 'policies'

    PolicyDirective = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
            DirectiveLocation.OBJECT,
            DirectiveLocation.INTERFACE,
            DirectiveLocation.SCALAR,
            DirectiveLocation.ENUM,
        ),
        args={
            ARG_POLICIES: GraphQLArgument(
                GraphQLNonNull(
                    GraphQLList(GraphQLNonNull(
                        GraphQLList(GraphQLNonNull(PolicyScalar.Type))))
                )
            ),
        },
        description=f"Federation @{NAME} directive",
    )
    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_POLICIES),
                type=NonNullTypeNode(
                    type=ListTypeNode(
                        type=NonNullTypeNode(
                            type=NamedTypeNode(
                                name=NameNode(
                                    value=PolicyScalar.NAME
                                )
                            )
                        )
                    )
                )
            )
        ),
        repeatable=True,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
            NameNode(value='OBJECT'),
            NameNode(value='INTERFACE'),
            NameNode(value='SCALAR'),
            NameNode(value='ENUM'),
        )
    )

    @classmethod
    def Node(cls, **kwargs: PolicyDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_POLICIES),
                    value=ListValueNode(
                        values=tuple(
                            StringValueNode(value=policy)
                            for policy in kwargs[cls.ARG_POLICIES]
                        ),
                    ),
                )
            )
        )
