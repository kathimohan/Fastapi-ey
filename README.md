For installing dependencies ----     pip install -r requirements.txt

To run the application   ----        uvicorn app.main:app --reload

To test the application ----         pytest

For executing or get the docs at --- http://127.0.0.1:8000/docs#

curl -X 'POST' \
  'http://127.0.0.1:8000/api/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "batchid": "id0101",
  "payload": [[1, 2], [3, 4]]
}'

Response :  

{
  "batchid": "id0101",
  "response": [
    3,
    7
  ],
  "status": "complete",
  "started_at": "2024-06-01T05:14:39.141942",
  "completed_at": "2024-06-01T05:14:39.385636"
}
