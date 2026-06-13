from typing import Literal, TypedDict, Required

from graphql import (
    ArgumentNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    InputValueDefinitionNode,
    NameNode,
    NamedTypeNode,
    StringValueNode,
)

from ...types import AbstractDirective

from ..scalars import ContextFieldValueScalar


class FromContextDirectiveKwargs(TypedDict):
    field: Required[str]


class FromContextDirective(AbstractDirective[FromContextDirectiveKwargs]):
    """The @fromContext directive

    scalar ContextFieldValue;
    directive @fromContext(field: ContextFieldValue) on ARGUMENT_DEFINITION;
    """

    NAME = 'fromContext'
    ARG_FIELD: Literal['field'] = 'field'

    Type = GraphQLDirective(
        name=NAME,
        locations=[
            DirectiveLocation.ARGUMENT_DEFINITION,
        ],
        args={
            ARG_FIELD: GraphQLArgument(ContextFieldValueScalar.Type),
        },
        description=f"Federation @{NAME} directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(
            InputValueDefinitionNode(
                name=NameNode(value=ARG_FIELD),
                type=NamedTypeNode(
                    name=NameNode(
                        value=ContextFieldValueScalar.NAME
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
    def Node(cls, **kwargs: FromContextDirectiveKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_FIELD),
                    value=StringValueNode(value=kwargs[cls.ARG_FIELD]),
                ),
            )
        )
