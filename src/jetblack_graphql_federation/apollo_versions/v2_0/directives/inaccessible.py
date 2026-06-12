from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)


InaccessibleDirective = GraphQLDirective(
    name="inaccessible",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.UNION,
        DirectiveLocation.ENUM,
        DirectiveLocation.ENUM_VALUE,
        DirectiveLocation.SCALAR,
        DirectiveLocation.INPUT_OBJECT,
        DirectiveLocation.INPUT_FIELD_DEFINITION,
        DirectiveLocation.ARGUMENT_DEFINITION,
    ),
    description="Federation @inaccessible directive",
)
