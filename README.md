Репозиторий созданный для тестирования action.auto_create_index.

Устанаваливаем зависимости
```bash
pip install -r requirements.txt
```

Поднимаем эластик и кибану
```bash
docker-compose up -d
```

Дальше уже ставим флаг true или false тут action.auto_create_index.
Можно указать какие-то определённые шаблоны или запретить создание индексов.
