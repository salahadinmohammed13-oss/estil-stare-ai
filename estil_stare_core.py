# Estil Stare - FX AI Trading Assistant Core
# Supports Amharic and English for Text and Voice

def estil_greet(language="am"):
    if language == "am":
        return "ሰላም! እኔ Estil Stare ነኝ፤ የእርስዎ የ Forex Trading AI ረዳት። በድምፅ እና በጽሁፍ ልረዳዎ ዝግጁ ነኝ!"
    else:
        return "Hello! I am Estil Stare, your Forex Trading AI Assistant. Ready to help you with voice and text!"

if __name__ == "__main__":
    print(estil_greet("am"))
    print(estil_greet("en"))
