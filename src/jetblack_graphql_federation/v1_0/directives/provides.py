from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    NameNode
)

from ..scalars import FieldSetScalar


class ProvidesDirective:
    """The @provides directive

    directive @provides(fields: _FieldSet!) on FIELD_DEFINITION
    """

    NAME = "provides"
    ARG_FIELDS = "fields"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        args={
            ARG_FIELDS: GraphQLArgument(
                GraphQLNonNull(FieldSetScalar.Type)
            )
        },
        description="Federation @provides directive",
    )

    DefinitionNode = DirectiveDefinitionNode(
        name=NameNode(value=NAME),
        arguments=(),
        repeatable=False,
        locations=(
            NameNode(value='FIELD_DEFINITION'),
        )
    )

    @classmethod
    def Node(cls) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=()
        )
