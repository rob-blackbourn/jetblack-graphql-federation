from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)


ShareableDirective = GraphQLDirective(
    name="shareable",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
    ),
    description="Federation @shareable directive",
)
