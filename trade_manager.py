# Estil Stare - MT5 Trade Manager & Safety Approval Handler
# Ensures explicit user confirmation is required before any trade proposal

def create_trade_proposal(pair: str, action: str, lot_size: float):
    return {
        "status": "pending_approval",
        "pair": pair.upper(),
        "action": action.upper(),  # BUY or SELL
        "lot_size": lot_size,
        "warning_am": "ማስጠንቀቂያ፡ ይህ የንግድ ሀሳብ ስራ ላይ እንዲውል የእርስዎ ግልጽ ፈቃድ (Explicit Approval) ያስፈልጋል!",
        "warning_en": "WARNING: This trade proposal requires your explicit approval to execute!"
    }

if __name__ == "__main__":
    proposal = create_trade_proposal("EUR/USD", "BUY", 0.1)
    print(proposal)
