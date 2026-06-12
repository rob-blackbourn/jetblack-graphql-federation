from jetblack_graphql_federation.v2_1 import Federation


def test_members() -> None:
    assert hasattr(Federation, 'KeyDirective')
