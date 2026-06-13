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

from ..scalars import ContextFieldValueScalar


class FromContextDirective:
    """The @fromContext directive

    scalar ContextFieldValue;
    directive @fromContext(field: ContextFieldValue) on ARGUMENT_DEFINITION;
    """

    NAME = 'fromContext'
    ARG_FIELD = 'field'

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
    def Node(cls, field: str) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=(
                ArgumentNode(
                    name=NameNode(value=cls.ARG_FIELD),
                    value=StringValueNode(value=field),
                ),
            )
        )
