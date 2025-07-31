# 🛡️ Anti-Fraud API

A simple rule-based anti-fraud system built with FastAPI that detects suspicious transactions.

## 🚀 Features

- Rule-based fraud detection (amount, time, location, device)
- `/check_transaction` API endpoint to approve or deny transactions

## ▶️ Running the Project

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
uvicorn app.main:app --reload
```

3. Test the endpoint:
```bash
curl -X POST http://localhost:8000/check_transaction \
  -H "Content-Type: application/json" \
  -d '{
        "transaction_id": 1,
        "user_id": 101,
        "timestamp": "2025-07-25T15:30:00",
        "amount": 12000,
        "location": "New York",
        "device": "iPhone"
      }'
```

## ✅ Response
```json
{
  "transaction_id": 1,
  "user_id": 101,
  "decision": "deny"
}
```
