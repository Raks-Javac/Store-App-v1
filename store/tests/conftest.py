import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticate_user(api_client):
    def pass_user(user):
        return api_client.force_authenticate(user=user)
    return pass_user