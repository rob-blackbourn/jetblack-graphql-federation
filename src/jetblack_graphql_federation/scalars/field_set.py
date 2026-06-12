from graphql import (
    GraphQLScalarType,
    NameNode,
    ScalarTypeDefinitionNode,
    StringValueNode
)

FIELD_SET_DESCRIPTION = (
    "A string serialized scalar represent a set of fields that's passes to "
    "a federated directive, such as @key, @requires, or @provides"
)

FIELD_SET_NAME = "FieldSet"

FieldSet = GraphQLScalarType(
    name=FIELD_SET_NAME,
    description=FIELD_SET_DESCRIPTION
)

FieldSetNode = ScalarTypeDefinitionNode(
    name=NameNode(value=FIELD_SET_NAME),
    description=StringValueNode(value=FIELD_SET_DESCRIPTION),
)
