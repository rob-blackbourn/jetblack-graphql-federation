from graphql import (
    GraphQLObjectType,
    GraphQLField,
    GraphQLNonNull,
    GraphQLID,
    GraphQLString
)


User = GraphQLObjectType(
    'User',
    {
        'id': GraphQLField(
            GraphQLNonNull(GraphQLID),
        ),
        'username': GraphQLField(
            GraphQLNonNull(GraphQLString)
        ),
    }
)


def main() -> None:
    pass


if __name__ == '__main__':
    main()
