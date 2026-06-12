from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)

EXTENDS_NAME = "extends"

ExtendsDirective = GraphQLDirective(
    name=EXTENDS_NAME,
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    description="Federation @extends directive",
)
