# edge_assessment
python FastAPI Rest service to store and retrieve data from a PostgreSQL table.

SetUp server using the below command
```
python3 -m uvicorn app.main:app --host localhost --port 8000 --reload
```

**Api Endpoints:**

**/add_data:** Inserts record to table. Adds Value to frequency column as difference between from_date and to_date in minutes. Last_update_date will be time and date when the record is inserted

URL: http://localhost:8000/add_data?

HTTP Method: POST

Request Fields:
```
{
    "source":"dmart",
    "source_type":"offline",
    "source_tag":"dm",
    "from_date":"2021-12-31 13:59:00",
    "to_date":"2022-01-01 16:18:59"
}
```
Response:
```
{
    "status": "success"
}
```


**/update_data:** Updates from_date, to_date, last_update_date based on source_id. Updates frequency column as difference between from_date and to_date in minutes

URL: http://localhost:8000/update_data?

HTTP Method: PUT

Request Fields:
```
{
    "source_id":1,
    "from_date":"2022-06-03 22:00:00",
    "to_date":"2022-06-05 00:00:00"
}
```
Response:
```
{
    "status": "success"
}
```

**/get_data:** Fetches the record based on the given source id

URL: http://localhost:8000/get_data?source_id=1

HTTP Method: GET

Response:
```
{
    "source_id": 1,
    "source": "ajio",
    "source_tag": "aj",
    "from_date": "2022-06-04T12:00:00",
    "frequency": "5819M",
    "last_update_date": "2023-06-05T14:03:06.606355",
    "source_type": "online",
    "to_date": "2022-06-08T12:59:59"
}
```

**/get_data_trigger**: Fetches all the data for the given source_id. from_date will be from_date + frequency in minutes, to_date will be to_date + frequency in minutes

URL: http://localhost:8000/get_data_trigger?source_id=1

HTTP Method: GET


Response:
```
{
    "source_id": 1,
    "source": "ajio",
    "source_type": "online",
    "source_tag": "aj",
    "from_date": "2022-06-08T12:59:00",
    "to_date": "2022-06-12T13:58:59",
    "last_update_date": "2023-06-05T14:03:06.606355",
    "frequency": "5819M"
}
```
