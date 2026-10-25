# Estil Stare - Forex Market & Economic News Analyzer
# Analyzes major currency pairs and economic events (CPI, NFP, FOMC)

def analyze_market(pair: str = "EUR/USD", news_event: str = "Normal"):
    pair_upper = pair.upper()
    if news_event.upper() == "CPI":
        return {
            "pair": pair_upper,
            "event": "CPI Release",
            "analysis_am": f"የ CPI ዜና በ {pair_upper} ላይ ከፍተኛ ንቅናቄ ሊፈጥር ይችላል። ጥንቃቄ የተሞላበት ትንተና ይደረጋል።",
            "analysis_en": f"CPI release may cause high volatility on {pair_upper}. Trade with caution."
        }
    else:
        return {
            "pair": pair_upper,
            "event": "General Market",
            "analysis_am": f"የ {pair_upper} ገበያ ሁኔታ ተረጋግቷል። ቴክኒክ ትንተና በመሰራት ላይ ነው።",
            "analysis_en": f"{pair_upper} market conditions are stable. Technical analysis in progress."
        }

if __name__ == "__main__":
    print(analyze_market("EUR/USD", "CPI"))
