"""End-to-end tests for the GET /interactions endpoint."""
import httpx


def test_get_interactions_returns_200() -> None:
    """Test that GET /interactions returns status 200."""
    response = client.get("/interactions")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list() -> None:
    """Test that GET /interactions returns a list."""
    response = client.get("/interactions")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)