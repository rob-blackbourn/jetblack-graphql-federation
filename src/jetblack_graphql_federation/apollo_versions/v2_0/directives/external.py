from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)


ExternalDirective = GraphQLDirective(
    name="external",
    locations=(
        DirectiveLocation.OBJECT,  # Changed from v1.0
        DirectiveLocation.FIELD_DEFINITION,
    ),
    description="Federation @external directive",
)
