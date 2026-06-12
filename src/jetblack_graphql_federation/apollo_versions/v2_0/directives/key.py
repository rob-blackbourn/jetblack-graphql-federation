from graphql import (
    BooleanValueNode,
    DirectiveDefinitionNode,
    DirectiveLocation,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLDirective,
    GraphQLNonNull,
    InputValueDefinitionNode,
    NameNode,
    NamedTypeNode,
    NonNullTypeNode,
)

from ..scalars import FieldSet

KeyDirective = GraphQLDirective(
    name="key",
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet)),
        # Changed from v1.0
        "resolvable": GraphQLArgument(GraphQLBoolean, default_value=True),
    },
    description="Federation @key directive",
    is_repeatable=True,
)

# directive @key(fields: FieldSet!, resolvable: Boolean = true)
#     repeatable on OBJECT | INTERFACE
KeyDirectiveNode = DirectiveDefinitionNode(
    name=NameNode(value="key"),
    arguments=(
        InputValueDefinitionNode(
            name=NameNode(value="fields"),
            type=NonNullTypeNode(
                type=NamedTypeNode(
                    name=NameNode(
                        value="FieldSet"
                    )

                )
            )
        ),
        InputValueDefinitionNode(
            name=NameNode(value="resolvable"),
            type=NamedTypeNode(
                name=NameNode(value='Boolean')
            ),
            default_value=BooleanValueNode(
                value=True
            )

        ),
    ),
    repeatable=True,
    locations=(
        NameNode(value='OBJECT'),
        NameNode(value='INTERFACE')
    )
)
