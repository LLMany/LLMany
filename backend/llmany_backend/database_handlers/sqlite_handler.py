import sqlite3

from llmany_backend.database_handler import DatabaseHandler, DatabaseError


class SQLiteHandler(DatabaseHandler):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection: sqlite3.Connection = connection
        self.ensure_tables_exist()

    def ensure_tables_exist(self) -> None:
        """
        Ensure that all required tables exist in the database.
        Creates them if they don't exist.

        Raises:
            DatabaseError: If table creation fails
        """
        create_chats_table = """
            CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, model_type TEXT, model TEXT)
            """
        create_messages_table = """
        CREATE TABLE IF NOT EXISTS messages (chat_id INT NOT NULL, message_id INT NOT NULL, role TEXT,message TEXT,PRIMARY KEY (chat_id, message_id));
        """
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(create_chats_table)
                cursor.execute(create_messages_table)
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to initialize database: {str(e)}")

    def get_model_for_chat(self, chat_id: str) -> dict[str, str]:
        cursor = self.connection.cursor()

        cursor.execute(
            "SELECT model_type, model FROM chats WHERE chat_id = ?",
            (chat_id,),
        )

        result = cursor.fetchone()

        cursor.close()

        dict_result = {"model_type": result[0], "model": result[1]}

        return dict_result

    def create_new_chat(self, model_type: str, model: str) -> int:
        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO chats (name, model_type, model) VALUES (?, ?, ?)",
            ("Test Chat", model_type, model),
        )

        chat_id = cursor.lastrowid

        self.connection.commit()
        cursor.close()
        if chat_id is None:
            raise DatabaseError("Failed to create new chat")
        return chat_id

    def add_message_to_chat(self, chat_id: int, role: str, message: str) -> None:
        cursor = self.connection.cursor()

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

    def remove_chat(self, chat_id: int) -> None:
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM chats WHERE chat_id = ?", (chat_id,))

        cursor.close()
