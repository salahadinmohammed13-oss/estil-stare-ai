# Estil Stare - Command & Voice Processing Handler
# Handles Amharic and English voice/text commands

def process_command(command: str, language: str = "am"):
    command_lower = command.lower()

    if language == "am":
        if "ሰላም" in command_lower or "እንደምን" in command_lower:
            return "ሰላም! እኔ Estil Stare ነኝ። የ Forex ገበያ ትንተና እና መሠረታዊ ጥያቄዎችን ለመመለስ ዝግጁ ነኝ!"
        elif "ገበያ" in command_lower or "ትሬዲንግ" in command_lower:
            return "የ Forex ገበያ መረጃዎችን እና የ MT5 የንግድ ሀሳቦችን ለማየት ዝግጁ ነኝ። ግልጽ ፈቃድዎን ይጠብቃል!"
        else:
            return f"የሰጡትን ትዕዛዝ ተቀብያለሁ: '{command}'። ተጨማሪ ትንተና እሰራለሁ።"
    else:
        if "hello" in command_lower or "hi" in command_lower:
            return "Hello! I am Estil Stare, ready to assist you with Forex analysis and market queries."
        else:
            return f"Command received: '{command}'. Processing request..."

if __name__ == "__main__":
    print(process_command("ሰላም Estil", "am"))
