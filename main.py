from fastapi import FastAPI

app = FastAPI(title="Estil Stare FX AI", version="1.0")

@app.get("/")
def read_root():
    return {
        "status": "active",
        "message_am": "ሰላም! Estil Stare FX AI በስራ ላይ ነው።",
        "message_en": "Hello! Estil Stare FX AI backend is running successfully."
    }
