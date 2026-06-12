from graphql import (
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode,
)

from ...types import AbstractScalar


class FieldSetScalar(AbstractScalar):
    """The _FieldSet scalar"""

    DESCRIPTION = (
        "A string serialized scalar represent a set of fields that's passes to "
        "a federated directive, such as @key, @requires, or @provides"
    )

    NAME = "_FieldSet"

    Type = GraphQLScalarType(
        name=NAME,
        description=DESCRIPTION
    )

    DefinitionNode = ScalarTypeDefinitionNode(
        name=NameNode(value=NAME),
        description=StringValueNode(value=DESCRIPTION),
    )
