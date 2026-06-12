from graphql import (
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode
)

_DESCRIPTION = (
    "A string serialized scalar represent a set of fields that's passes to "
    "a federated directive, such as @key, @requires, or @provides"
)

_NAME_V1 = "_FieldSet"

_FieldSet = GraphQLScalarType(
    name=_NAME_V1,
    description=_DESCRIPTION
)

_FieldSetNode = ScalarTypeDefinitionNode(
    name=NameNode(value=_NAME_V1),
    description=StringValueNode(value=_DESCRIPTION),
)

_NAME_V2 = "FieldSet"

FieldSet = GraphQLScalarType(
    name=_NAME_V2,
    description=_DESCRIPTION
)

FieldSetNode = ScalarTypeDefinitionNode(
    name=NameNode(value=_NAME_V2),
    description=StringValueNode(value=_DESCRIPTION),
)
