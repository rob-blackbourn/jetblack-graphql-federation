from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
)

from ..scalars import _FieldSet


key_directive = GraphQLDirective(
    name="key",
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @key directive",
    is_repeatable=True,
)

requires_directive = GraphQLDirective(
    name="requires",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @requires directive",
)


provides_directive = GraphQLDirective(
    name="provides",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={"fields": GraphQLArgument(GraphQLNonNull(_FieldSet))},
    description="Federation @provides directive",
)

external_directive = GraphQLDirective(
    name="external",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    description="Federation @external directive",
)

extends_directive = GraphQLDirective(
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
            key_directive,
            requires_directive,
            provides_directive,
            external_directive,
            extends_directive,
        ]
    }
