import sqlite3
import os
import pytest

from llmany_backend.database_handlers.sqlite_handler import SQLiteHandler

@pytest.mark.parametrize("chat_id, model_type, model", [
    (1, "OpenAI",  "gpt-4o"),
    (2, "Anthropic", "claude-3.5"),
    (3, "OpenAI",  "gpt-4"),
    (4, "Anthropic", "claude-2.5"),
    (5, "Google", "Gemini 1.5")
])
def test_get_model_for_chat(chat_id, model_type, model):
    connection = sqlite3.connect("test.db")
    cursor= connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY, name TEXT, model_type TEXT, model TEXT)")
    connection.commit()

    cursor.execute("INSERT INTO chats (chat_id, name, model_type, model) VALUES (?, ?, ?, ?)", (chat_id, "Test Chat", model_type, model))
    cursor.commit()

    handler = SQLiteHandler(connection)
    result = handler.get_model_for_chat(chat_id)

    assert isinstance(result, tuple)
    returned_model_type, returned_model = result

    assert returned_model_type == model_type
    assert returned_model == model

    connection.close()
    os.remove("test.db")



@pytest.mark.parametrize("model_list", [
    [(1, "OpenAI",  "gpt-4o")],
    [(2, "Anthropic", "claude-3.5"),
    (3, "OpenAI",  "gpt-4")],
    [(4, "Anthropic", "claude-2.5"),
    (2, "Google", "Gemini 1.5"),
    (1, "Google, Gemini 1.5 ")]
])
def test_create_new_chat(model_list):
    connection = sqlite3.connect("test.db")
    cursor= connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS chats (chat_id INTEGER PRIMARY KEY, name TEXT, model_type TEXT, model TEXT)")
    connection.commit()

    for entry in model_list:
        model_type, model = entry
        handler = SQLiteHandler(connection)
        chat_id = handler.create_new_chat(model_type, model)

        assert isinstance(chat_id, str)

        result = handler.get_model_for_chat(chat_id)
        
        returned_model_type, returned_model = result

        assert returned_model_type == model_type
        assert returned_model == model

    connection.close()
    os.remove("test.db")


def test_add_message_to_chat():


@pytest.mark.parametrize("expected_chat_history",(
    {}
))
def test_get_chat_history(expected_chat_history): 
    connection = sqlite3.connect("test.db")
    cursor= connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages" 
                   "(chat_id INTEGER PRIMARY KEY, message_id INT, role TEXT, message TEXT, PRIMARY_KEY (chat_id, message_id))")
    connection.commit()

    cursor.executemany("INSERT INTO messages (chat_id, message_id, role, message) VALUES (?, ?, ?, ?)", expected_chat_history)
    cursor.commit()

    handler = SQLiteHandler(connection)
    result = handler.get_model_for_chat(chat_id)

    assert isinstance(result, tuple)
    returned_model_type, returned_model = result

    assert returned_model_type == model_type
    assert returned_model == model

    connection.close()
    os.remove("test.db")

def test_get_all_chats(): 
def test_remove_chat(): 
