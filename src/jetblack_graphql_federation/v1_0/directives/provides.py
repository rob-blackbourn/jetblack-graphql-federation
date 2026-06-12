from typing import TypedDict

from graphql import (
    DirectiveDefinitionNode,
    DirectiveLocation,
    DirectiveNode,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    NameNode
)

from ...types import AbstractDirective
from ..scalars import FieldSetScalar


class ProvidesKwargs(TypedDict):
    ...


class ProvidesDirective[ProvidesKwargs](AbstractDirective):
    """The @provides directive

    directive @provides(fields: _FieldSet!) on FIELD_DEFINITION
    """

    NAME = "provides"
    ARG_NAME_FIELDS = "fields"

    Type = GraphQLDirective(
        name=NAME,
        locations=(
            DirectiveLocation.FIELD_DEFINITION,
        ),
        args={
            ARG_NAME_FIELDS: GraphQLArgument(
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
    def Node(cls, **kwargs: ProvidesKwargs) -> DirectiveNode:
        return DirectiveNode(
            name=NameNode(value=cls.NAME),
            arguments=()
        )
