import sqlite3

from llmany_backend.database_handler import DatabaseHandler


class SQLiteHandler(DatabaseHandler):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection: sqlite3.Connection = connection

    def get_model_for_chat(self, chat_id: str) -> dict[str, str]:
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT model_type, model,FROM chats WHERE chat_id = ?",
            (chat_id,),
        )

        result = cursor.fetchone()

        cursor.close()

        dict_result = {"model_type": result[0], "model": result[1]}

        return dict_result

    def create_new_chat(self, model_type: str, model: str) -> int:
        cursor = self.connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY, name TEXT, model_type TEXT, model TEXT)"
        )
        self.connection.commit()

        cursor.execute("SELECT MAX(chat_id) AS max_id FROM chats")

        result = cursor.fetchone()

        chat_id: int = result[0] + 1 if result[0] is not None else 0

        cursor.execute(
            "INSERT INTO chats (chat_id, name, model_type, model) VALUES (?, ?, ?, ?)",
            (chat_id, "Test Chat", model_type, model),
        )

        self.connection.commit()
        cursor.close()
        return chat_id

    def add_message_to_chat(self, chat_id: int, role: str, message: str) -> None:
        cursor = self.connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS messages (chat_id INT NOT NULL, message_id INT NOT NULL, role TEXT,message TEXT,PRIMARY KEY (chat_id, message_id));"
        )
        self.connection.commit()

        cursor.execute(
            "SELECT MAX(message_id) AS max_id FROM messages WHERE chat_id = ?",
            (chat_id,),
        )

        result = cursor.fetchone()

        message_id = result[0] + 1 if result[0] is not None else 0

        cursor.execute(
            "INSERT INTO messages (chat_id, message_id, role, message) VALUES (?, ?, ?, ?)",
            (chat_id, message_id, role, message),
        )

        self.connection.commit()
        cursor.close()

    def get_chat_history(self, chat_id: int) -> list[dict[str, str]]:
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT role, message FROM messages WHERE chat_id = ? ORDER BY message_id",
            (chat_id,),
        )

        result = cursor.fetchall()

        cursor.close()

        dict_result = [{"role": role, "content": content} for role, content in result]

        return dict_result

    def get_all_chats(self) -> list[dict[str, str]]:
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT chat_id, model_type, model FROM chats",
        )

        result = cursor.fetchall()

        cursor.close()

        dict_result = [
            {"chat_id": chat_id, "model_type": model_type, "model": model}
            for chat_id, model_type, model in result
        ]

        return dict_result

    def remove_chat(self, chat_id: str) -> None:
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM chats WHERE chat_id = ?", (chat_id,))

        cursor.close()
