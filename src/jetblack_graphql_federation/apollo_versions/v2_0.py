from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLBoolean,
    GraphQLString,
)

from ..scalars import FieldSet

from .v1_0 import extends_directive


key_directive = GraphQLDirective(
    name="key",
    locations=(
        DirectiveLocation.OBJECT,
        DirectiveLocation.INTERFACE,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet)),
        # Changed from v1.0
        "resolvable": GraphQLArgument(GraphQLBoolean, default_value=True),
    },
    description="Federation @key directive",
    is_repeatable=True,
)

requires_directive = GraphQLDirective(
    name="requires",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet))
    },  # Changed _FieldSet -> FieldSet
    description="Federation @requires directive",
)


provides_directive = GraphQLDirective(
    name="provides",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet))
    },  # Changed _FieldSet -> FieldSet
    description="Federation @provides directive",
)


external_directive = GraphQLDirective(
    name="external",
    locations=(
        DirectiveLocation.OBJECT,  # Changed from v1.0
        DirectiveLocation.FIELD_DEFINITION,
    ),
    description="Federation @external directive",
)


shareable_directive = GraphQLDirective(
    name="shareable",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
    ),
    description="Federation @shareable directive",
)


override_directive = GraphQLDirective(
    name="override",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "from": GraphQLArgument(GraphQLNonNull(GraphQLString)),
    },
    description="Federation @override directive",
)

inaccessible_directive = GraphQLDirective(
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

tag_directive = GraphQLDirective(
    name="tag",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.INTERFACE,
        DirectiveLocation.OBJECT,
        DirectiveLocation.UNION,
        DirectiveLocation.ARGUMENT_DEFINITION,
        DirectiveLocation.SCALAR,
        DirectiveLocation.ENUM,
        DirectiveLocation.ENUM_VALUE,
        DirectiveLocation.INPUT_OBJECT,
        DirectiveLocation.INPUT_FIELD_DEFINITION,
    ),
    description="Federation @tag directive",
)


def get_directives() -> dict[str, GraphQLDirective]:
    return {
        directive.name: directive
        for directive in [
            key_directive,
            requires_directive,
            provides_directive,
            external_directive,
            shareable_directive,
            extends_directive,  # From v1.0
            override_directive,
            inaccessible_directive,
            tag_directive,
        ]
    }
