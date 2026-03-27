import random
from datetime import datetime

# 📥 leer template
with open("README.template.md", "r", encoding="utf-8") as f:
    template = f.read()

# ⚡ datos dinámicos
data = {
    "LATENCY": random.randint(20, 120),
    "CPU_LOAD": random.randint(10, 90),
    "MEMORY_USAGE": random.randint(20, 95),
    "SECURITY_LEVEL": random.choice(["LOW", "MEDIUM", "HIGH"]),
    "THREAT_LEVEL": random.choice(["STABLE", "ELEVATED", "CRITICAL"]),
    "TREND": random.choice(["UP", "DOWN", "STABLE"]),
    "STREAK": random.randint(1, 30),
    "AI_STATUS": random.choice(["ACTIVE", "LEARNING", "OPTIMIZING"]),
    "AUTOMATION_STATUS": random.choice(["RUNNING", "IDLE"]),
    "SECURITY_STATUS": random.choice(["SECURE", "MONITORING"]),
    "NETWORK_STATUS": random.choice(["STABLE", "LATENT"]),
    "EVOLUTION_STAGE": random.choice(["PHASE 1", "PHASE 2", "EXPANDING"]),
    "TIMEZONE": "UTC",
    "CURRENT_TIME": datetime.utcnow().strftime("%H:%M:%S"),
    "WEATHER": random.choice(["CLEAR", "CLOUDY", "UNKNOWN"]),
    "SYSTEM_EVENTS": "\n".join([
        "[SYS] Scan complete",
        "[AI] Pattern detected",
        "[NET] Stable connection"
    ])
}

# 🔁 reemplazo
for key, value in data.items():
    template = template.replace(f"{{{{{key}}}}}", str(value))

# 📤 escribir README final
with open("README.md", "w", encoding="utf-8") as f:
    f.write(template)
