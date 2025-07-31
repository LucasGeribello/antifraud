
# CloudWalk Anti-Fraud API (Parte 3.3)

Este projeto implementa um endpoint simples de antifraude para análise de transações financeiras.

## 🚀 Tecnologias
- Python
- FastAPI
- Uvicorn

## 🧠 Regras antifraude aplicadas
A transação será **negada** se:
1. O usuário já tiver tido *chargeback*.
2. O usuário tiver feito mais de 10 transações.
3. O valor da transação for maior que R$1000.

## 📦 Instalação

```bash
# Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

## ▶️ Execução

```bash
uvicorn main:app --reload
```

Acesse a documentação automática em: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📬 Exemplo de requisição

**POST** `/evaluate`

```json
{
  "transaction_id": 123,
  "merchant_id": 456,
  "user_id": 789,
  "card_number": "434505******9116",
  "transaction_date": "2025-07-31T14:33:00",
  "transaction_amount": 500,
  "device_id": 285475
}
```

**Resposta esperada:**
```json
{ 
  "transaction_id": 123,
  "recommendation": "approve"
}
```

---

## 📁 Estrutura

- `main.py`: Código da API
- `requirements.txt`: Dependências
- `README.md`: Instruções

---
