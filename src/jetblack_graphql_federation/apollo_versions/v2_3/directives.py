from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)

InterfaceObjectDirective = GraphQLDirective(
    name="interfaceObject",
    locations=(
        DirectiveLocation.OBJECT,
    ),
    description="Federation @interfaceObject directive",
)
