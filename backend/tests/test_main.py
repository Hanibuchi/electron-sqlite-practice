from pathlib import Path
import sys
from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

# Allow importing backend/main.py when tests are run from backend/.
sys.path.append(str(Path(__file__).resolve().parents[1]))
import main  # noqa: E402


def _build_db_mocks():
    conn = MagicMock()
    cursor = MagicMock()
    conn.cursor.return_value = cursor
    return conn, cursor


def test_add_task_saves_content_and_returns_message():
    conn, cursor = _build_db_mocks()

    with patch.object(main.sqlite3, "connect", return_value=conn):
        client = TestClient(main.app)
        response = client.post("/add_task", json={"content": "Buy milk"})

    assert response.status_code == 200
    assert response.json() == {"message": "Saved: Buy milk"}
    cursor.execute.assert_called_once_with(
        "INSERT INTO tasks (content) VALUES (?)", ("Buy milk",)
    )
    conn.commit.assert_called_once()
    conn.close.assert_called_once()


def test_get_tasks_returns_task_list():
    conn, cursor = _build_db_mocks()
    cursor.fetchall.return_value = [("Task A",), ("Task B",)]

    with patch.object(main.sqlite3, "connect", return_value=conn):
        client = TestClient(main.app)
        response = client.get("/get_tasks")

    assert response.status_code == 200
    assert response.json() == {"tasks": ["Task A", "Task B"]}
    cursor.execute.assert_called_once_with("SELECT content FROM tasks")
    conn.close.assert_called_once()


def test_add_task_requires_content():
    conn, cursor = _build_db_mocks()

    with patch.object(main.sqlite3, "connect", return_value=conn):
        client = TestClient(main.app)
        response = client.post("/add_task", json={})

    assert response.status_code == 422
    cursor.execute.assert_not_called()
