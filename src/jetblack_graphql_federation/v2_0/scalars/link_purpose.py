from graphql import (
    GraphQLEnumType,
    GraphQLEnumValue,
    EnumTypeDefinitionNode,
    EnumValueDefinitionNode,
    NameNode,
    StringValueNode
)

# Reference: https://www.apollographql.com/docs/federation/subgraph-spec/

_NAME = "link__Purpose"
_DESCRIPTION = (
    "An Enum to clarify the type of directives (security, execution) in the "
    "specification"
)

link_Purpose = GraphQLEnumType(
    name=_NAME,
    description=_DESCRIPTION,
    values={
        "SECURITY": GraphQLEnumValue(
            value="SECURITY",
            description="`SECURITY` features provide metadata necessary to securely resolve fields.",
        ),
        "EXECUTION": GraphQLEnumValue(
            value="EXECUTION",
            description="`EXECUTION` features provide metadata necessary for operation execution.",
        ),
    },
)

link_PurposeNode = EnumTypeDefinitionNode(
    name=NameNode(value=_NAME),
    values=(
        EnumValueDefinitionNode(
            name=NameNode(value="SECURITY"),
            description=StringValueNode(
                value="`SECURITY` features provide metadata necessary to securely resolve fields.")
        ),
        EnumValueDefinitionNode(
            name=NameNode(value='EXECUTION'),
            description=StringValueNode(
                value="`EXECUTION` features provide metadata necessary for operation execution.")
        )
    )
)
