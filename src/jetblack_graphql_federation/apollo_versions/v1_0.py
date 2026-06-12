from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import _FieldSet


KeyDirective = GraphQLDirective(
    name="key",
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @key directive",
    is_repeatable=True,
)

RequiresDirective = GraphQLDirective(
    name="requires",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @requires directive",
)


ProvidesDirective = GraphQLDirective(
    name="provides",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @provides directive",
)

ExternalDirective = GraphQLDirective(
    name="external",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    description="Federation @external directive",
)

ExtendsDirective = GraphQLDirective(
    name="extends",
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    description="Federation @extends directive",
)


def get_directives() -> dict[str, GraphQLDirective]:
    return {
        directive.name: directive
        for directive in [
            KeyDirective,
            RequiresDirective,
            ProvidesDirective,
            ExternalDirective,
            ExtendsDirective,
        ]
    }
