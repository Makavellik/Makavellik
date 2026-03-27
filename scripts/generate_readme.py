import random
from datetime import datetime


# =========================================================
# 📥 LOAD TEMPLATE
# =========================================================
def load_template():
    with open("README.template.md", "r", encoding="utf-8") as f:
        return f.read()


# =========================================================
# ⚡ GENERATE DYNAMIC DATA
# =========================================================
def generate_data():
    return {
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


# =========================================================
# 🔁 REPLACE TEMPLATE VALUES
# =========================================================
def render_template(template, data):
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))

    # ⚠️ Debug opcional
    if "{{" in template:
        print("⚠️ WARNING: placeholders no reemplazados detectados")

    return template


# =========================================================
# 📤 SAVE README
# =========================================================
def save_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)


# =========================================================
# 🎨 SIMPLE HUD (BÁSICO)
# =========================================================
def generate_simple_hud(data):
    return f"""
<svg width="400" height="100" xmlns="http://www.w3.org/2000/svg">
  <style>
    .text {{
      font-family: monospace;
      font-size: 16px;
      fill: #00ffff;
    }}
  </style>

  <rect width="100%" height="100%" fill="black"/>

  <text x="10" y="30" class="text">
    LATENCY: {data["LATENCY"]} ms
  </text>

  <text x="10" y="55" class="text">
    CPU: {data["CPU_LOAD"]}%
  </text>

  <text x="10" y="80" class="text">
    STATUS: {data["SECURITY_LEVEL"]}
  </text>

  <circle cx="350" cy="50" r="10" fill="cyan">
    <animate attributeName="r" values="10;15;10" dur="1s" repeatCount="indefinite"/>
  </circle>
</svg>
"""


# =========================================================
# 🔥 ADVANCED HUD (RADAR)
# =========================================================
def generate_radar_hud(data):
    return f"""
<svg width="420" height="420" viewBox="0 0 420 420" xmlns="http://www.w3.org/2000/svg">

<style>
  .bg {{ fill: #05070d; }}
  .grid {{ stroke: #0ff; stroke-opacity: 0.15; }}
  .pulse {{ fill: #00ffff; opacity: 0.7; }}
  .text {{ fill: #00ffff; font-family: monospace; font-size: 12px; }}
</style>

<rect width="100%" height="100%" class="bg"/>

<circle cx="210" cy="210" r="50" class="grid"/>
<circle cx="210" cy="210" r="100" class="grid"/>
<circle cx="210" cy="210" r="150" class="grid"/>

<line x1="210" y1="0" x2="210" y2="420" class="grid"/>
<line x1="0" y1="210" x2="420" y2="210" class="grid"/>

<line x1="210" y1="210" x2="210" y2="60" stroke="#00ffff" stroke-width="2">
  <animateTransform attributeName="transform"
    type="rotate"
    from="0 210 210"
    to="360 210 210"
    dur="2s"
    repeatCount="indefinite"/>
</line>

<circle cx="{random.randint(120,300)}" cy="{random.randint(120,300)}" r="4" class="pulse">
  <animate attributeName="r" values="4;8;4" dur="1s" repeatCount="indefinite"/>
</circle>

<text x="10" y="20" class="text">LATENCY: {data["LATENCY"]} ms</text>
<text x="10" y="40" class="text">CPU: {data["CPU_LOAD"]}%</text>
<text x="10" y="60" class="text">MEM: {data["MEMORY_USAGE"]}%</text>
<text x="10" y="80" class="text">SEC: {data["SECURITY_LEVEL"]}</text>
<text x="10" y="100" class="text">THREAT: {data["THREAT_LEVEL"]}</text>

<text x="210" y="215" text-anchor="middle" class="text">
  SYSTEM ACTIVE
</text>

</svg>
"""

def generate_ultra_hud(data):
    # 🎨 colores dinámicos según amenaza
    if data["THREAT_LEVEL"] == "CRITICAL":
        primary = "#ff0033"
        bg = "#0a0000"
        status_text = "⚠ SYSTEM UNDER THREAT"
    elif data["THREAT_LEVEL"] == "ELEVATED":
        primary = "#ffaa00"
        bg = "#0a0600"
        status_text = "⚡ ALERT MODE"
    else:
        primary = "#00ffff"
        bg = "#04060a"
        status_text = "✓ SYSTEM STABLE"

    # 🧠 estado "emocional"
    mood = random.choice([
        "ANALYZING...",
        "ADAPTING...",
        "LEARNING...",
        "SCANNING...",
        "EVOLVING..."
    ])

    return f"""
<svg width="500" height="500" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">

<style>
  .bg {{ fill: {bg}; }}
  .grid {{ stroke: {primary}; stroke-opacity: 0.12; }}
  .text {{ fill: {primary}; font-family: monospace; font-size: 12px; }}
  .glow {{ filter: drop-shadow(0 0 6px {primary}); }}
</style>

<!-- Fondo -->
<rect width="100%" height="100%" class="bg"/>

<!-- Núcleo -->
<circle cx="250" cy="250" r="18" fill="{primary}" class="glow">
  <animate attributeName="r" values="18;28;18" dur="1s" repeatCount="indefinite"/>
</circle>

<!-- Anillos -->
<circle cx="250" cy="250" r="70" class="grid"/>
<circle cx="250" cy="250" r="140" class="grid"/>
<circle cx="250" cy="250" r="200" class="grid"/>

<!-- Barrido radar -->
<line x1="250" y1="250" x2="250" y2="40" stroke="{primary}" stroke-width="2" class="glow">
  <animateTransform attributeName="transform"
    type="rotate"
    from="0 250 250"
    to="360 250 250"
    dur="2s"
    repeatCount="indefinite"/>
</line>

<!-- MULTI OBJETIVOS -->
{"".join([
    f'''
    <circle cx="{random.randint(60,440)}" cy="{random.randint(60,440)}" r="3" fill="{primary}">
      <animate attributeName="r" values="3;8;3" dur="{random.uniform(0.8,1.5)}s" repeatCount="indefinite"/>
    </circle>
    ''' for _ in range(4)
])}

<!-- BARRAS SISTEMA -->
<rect x="20" y="420" width="{data["CPU_LOAD"] * 3}" height="8" fill="{primary}" class="glow"/>
<rect x="20" y="440" width="{data["MEMORY_USAGE"] * 3}" height="8" fill="{primary}"/>

<!-- TEXTO -->
<text x="20" y="30" class="text">LATENCY: {data["LATENCY"]} ms</text>
<text x="20" y="50" class="text">CPU: {data["CPU_LOAD"]}%</text>
<text x="20" y="70" class="text">MEM: {data["MEMORY_USAGE"]}%</text>
<text x="20" y="90" class="text">SEC: {data["SECURITY_LEVEL"]}</text>
<text x="20" y="110" class="text">THREAT: {data["THREAT_LEVEL"]}</text>

<!-- ESTADO -->
<text x="250" y="255" text-anchor="middle" class="text glow">
  {status_text}
</text>

<!-- "MENTE" DEL SISTEMA -->
<text x="250" y="280" text-anchor="middle" class="text">
  {mood}
</text>

</svg>
"""
import random
from datetime import datetime

data = {
    # 🔥 SISTEMA BASE
    "STATUS": random.choice(["ONLINE", "STEALTH", "ACTIVE"]),
    "LAST_UPDATE": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    "ACTIVITY_LEVEL": random.choice(["ALTA", "MEDIA", "INTENSA"]),
    "NODE_ID": random.randint(1000, 9999),
    "SYSTEM_VERSION": f"v{random.randint(1,3)}.{random.randint(0,9)}",

    # 📊 ACTIVIDAD
    "COMMITS": random.randint(1, 10),
    "REPOS": random.randint(1, 5),
    "HOURS": random.randint(1, 12),

    # 🧠 MENSAJE
    "DAILY_MESSAGE": random.choice([
        "El sistema evoluciona...",
        "Nueva capa cargada...",
        "Expansión en proceso...",
        "Conciencia adaptativa activa..."
    ]),
}


# =========================================================
# 💾 SAVE HUD
# =========================================================
def save_hud(svg):
    with open("hud.svg", "w") as f:
        f.write(svg)


# =========================================================
# 🚀 MAIN EXECUTION
# =========================================================
def main():
    svg = generate_ultra_hud(data)
    template = load_template()
    data = generate_data()

    rendered = render_template(template, data)
    save_readme(rendered)

    # 🔥 elige el HUD que quieras
    svg = generate_radar_hud(data)  # o generate_simple_hud(data)

    save_hud(svg)

    print("✅ README y HUD generados correctamente")


if __name__ == "__main__":
    main()
