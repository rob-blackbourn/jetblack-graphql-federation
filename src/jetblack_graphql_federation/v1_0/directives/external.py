from graphql import (
    DirectiveLocation,
    GraphQLDirective,
)


FIELDS_NAME = "fields"

EXTERNALS_NAME = "external"

ExternalDirective = GraphQLDirective(
    name=EXTERNALS_NAME,
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    description="Federation @external directive",
)
