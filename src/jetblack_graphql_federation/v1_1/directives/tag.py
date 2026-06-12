from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)


TagDirective = GraphQLDirective(
    name="tag",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.OBJECT,
        DirectiveLocation.UNION,
    ),
    description="Federation @tag directive",
)
