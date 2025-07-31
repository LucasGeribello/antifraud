from collections import defaultdict
from datetime import datetime
from typing import Literal

user_last_transaction = defaultdict(dict)

def evaluate_transaction(tx) -> Literal["approve", "deny"]:
    flags = []

    if tx.amount > 10000:
        flags.append("high_amount")

    tx_time = datetime.fromisoformat(tx.timestamp)
    prev = user_last_transaction[tx.user_id]

    if prev:
        time_diff = (tx_time - prev['timestamp']).total_seconds()
        if time_diff < 30:
            flags.append("rapid_transactions")
        if tx.location != prev['location']:
            flags.append("location_change")
        if tx.device != prev['device']:
            flags.append("device_change")

    user_last_transaction[tx.user_id] = {
        'timestamp': tx_time,
        'location': tx.location,
        'device': tx.device
    }

    return "deny" if flags else "approve"
