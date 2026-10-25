from fastapi import FastAPI
from commands import process_command
from market_analyzer import analyze_market
from trade_manager import create_trade_proposal

app = FastAPI(title="Estil Stare FX AI", version="1.0")

@app.get("/")
def read_root():
    return {
        "status": "active",
        "message_am": "ሰላም! Estil Stare FX AI በስራ ላይ ነው።",
        "message_en": "Hello! Estil Stare FX AI backend is running successfully."
    }

@app.get("/command")
def api_command(q: str, lang: str = "am"):
    response = process_command(q, lang)
    return {"query": q, "language": lang, "response": response}

@app.get("/market")
def api_market(pair: str = "EUR/USD", event: str = "Normal"):
    analysis = analyze_market(pair, event)
    return analysis

@app.post("/trade/propose")
def api_propose_trade(pair: str, action: str, lot_size: float):
    proposal = create_trade_proposal(pair, action, lot_size)
    return proposal
