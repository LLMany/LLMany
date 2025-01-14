import sys
import json
import sqlite3

from llmany_backend.request_handler import RequestHandler
from llmany_backend.database_handler_factory import DatabaseHandlerFactory
from llmany_backend.model_handler_factory import ModelHandlerFactory


def main():
    database_handler_factory = DatabaseHandlerFactory()
    connection = sqlite3.connect("llmany_backend.db")
    model_handler_factory = ModelHandlerFactory()
    request_handler = RequestHandler(
        database_handler_factory, model_handler_factory, connection
    )
    for line in sys.stdin:
        try:
            request_dict = request_handler.parse(line)

            request_object = request_handler.create_request(request_dict)

            request_object.execute()

        except Exception as e:
            json.dump({"error": str(e)}, sys.stdout)

    connection.close()


if __name__ == "__main__":
    main()
