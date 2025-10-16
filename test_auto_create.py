from elasticsearch import Elasticsearch


def test_add_index():
    es = Elasticsearch(
        ["http://localhost:9200"],
        request_timeout=30,
        max_retries=3,
        retry_on_timeout=True
    )

    test_index = "test_1"

    try:
        document = {
            "message": "Это тестовое сообщение",
            "timestamp": "2024-01-01T12:00:00",
            "user": "test_user"
        }

        response = es.index(
            index=test_index,
            document=document
        )

        print(response)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    test_add_index()
