from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLDirective,
    GraphQLNonNull,
    GraphQLBoolean,
    GraphQLString,
)

from ..scalars import FieldSet

from .v1_0 import ExtendsDirective


KeyDirective = GraphQLDirective(
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

RequiresDirective = GraphQLDirective(
    name="requires",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet))
    },  # Changed _FieldSet -> FieldSet
    description="Federation @requires directive",
)


ProvidesDirective = GraphQLDirective(
    name="provides",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "fields": GraphQLArgument(GraphQLNonNull(FieldSet))
    },  # Changed _FieldSet -> FieldSet
    description="Federation @provides directive",
)


ExternalDirective = GraphQLDirective(
    name="external",
    locations=(
        DirectiveLocation.OBJECT,  # Changed from v1.0
        DirectiveLocation.FIELD_DEFINITION,
    ),
    description="Federation @external directive",
)


ShareableDirective = GraphQLDirective(
    name="shareable",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
        DirectiveLocation.OBJECT,
    ),
    description="Federation @shareable directive",
)


OverrideDirective = GraphQLDirective(
    name="override",
    locations=(
        DirectiveLocation.FIELD_DEFINITION,
    ),
    args={
        "from": GraphQLArgument(GraphQLNonNull(GraphQLString)),
    },
    description="Federation @override directive",
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

TagDirective = GraphQLDirective(
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
            KeyDirective,
            RequiresDirective,
            ProvidesDirective,
            ExternalDirective,
            ShareableDirective,
            ExtendsDirective,  # From v1.0
            OverrideDirective,
            InaccessibleDirective,
            TagDirective,
        ]
    }
