from app import app
from unittest.mock import patch, MagicMock

def test_home():
    with patch("app.get_db_connection") as mock_conn:
        mock_conn.return_value = MagicMock()
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200
        assert b"task 4 completed" in response.data
