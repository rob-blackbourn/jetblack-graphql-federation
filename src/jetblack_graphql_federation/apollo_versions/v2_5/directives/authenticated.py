from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)


AuthenticatedDirective = GraphQLDirective(
    name="authenticated",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.SCALAR,
        DirectiveLocation.ENUM,
    ),
    description="Federation @authenticated directive",
)
