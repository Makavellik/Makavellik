import random
import requests
from datetime import datetime


# =========================================================
# 📥 LOAD TEMPLATE
# =========================================================
def load_template():
    with open("README.template.md", "r", encoding="utf-8") as f:
        return f.read()

def generate_clickable_repos():
    repos = [
        ("osint-core", "https://github.com/Makavellik/OsintInverso"),
        ("neural-scanner", "https://github.com/Makavellik/Observador-X-Ray"),
        ("stealth-engine", "https://github.com/Makavellik/OsintSignalsF"),
        ("ai-defense-system", "https://github.com/Makavellik/DnSAnalizadorIT"),
        ("ai-defense-system", "https://github.com/Makavellik/SENTINELA-v2-Vigilancia-Total"),
    ]

    return f"""
<svg width="900" height="300" xmlns="http://www.w3.org/2000/svg">

<style>
  .bg {{ fill: #04060a; }}
  .title {{ fill: #00ffff; font-size: 18px; font-family: monospace; }}
  .repo {{ fill: #00ffff; font-size: 14px; font-family: monospace; cursor: pointer; }}
  .repo:hover {{ fill: #ffffff; }}
  .glow {{ filter: drop-shadow(0 0 6px #00ffff); }}
</style>

<rect width="100%" height="100%" class="bg"/>

<!-- Título -->
<text x="20" y="30" class="title glow">
⚡ TACTICAL REPOSITORY ACCESS
</text>

<!-- Línea scan -->
<line x1="0" y1="50" x2="900" y2="50" stroke="#00ffff" stroke-width="1">
  <animate attributeName="y1" values="50;300;50" dur="3s" repeatCount="indefinite"/>
  <animate attributeName="y2" values="50;300;50" dur="3s" repeatCount="indefinite"/>
</line>

<!-- Repos clickeables -->
{"".join([
    f'''
    <a href="{url}" target="_blank">
      <text x="40" y="{90 + i*40}" class="repo glow">
        ▶ {name}
        <animate attributeName="opacity"
                 values="0;1"
                 dur="1s"
                 begin="{i * 0.3}s"
                 fill="freeze"/>
      </text>
    </a>
    ''' for i, (name, url) in enumerate(repos)
])}

</svg>
"""

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"❌ Error API: {response.status_code}")
            return []

        return response.json()

    except Exception as e:
        print(f"💀 Exception: {e}")
        return []

def analyze_repos(repos):
    if not repos or isinstance(repos, dict):
        return {
            "top_lang": "UNKNOWN",
            "total_repos": 0,
            "activity": "LOW"
        }

    languages = {}
    
    for repo in repos:
        lang = repo.get("language") or "UNKNOWN"
        languages[lang] = languages.get(lang, 0) + 1

    top_lang = max(languages, key=languages.get)

    total = len(repos)

    if total > 10:
        activity = "HIGH"
    elif total > 5:
        activity = "MEDIUM"
    else:
        activity = "LOW"

    return {
        "top_lang": top_lang,
        "total_repos": total,
        "activity": activity
    }

def generate_ai_analysis(data, analysis):
    return f"""
<svg width="900" height="260" xmlns="http://www.w3.org/2000/svg">

<style>
  .bg {{ fill: #05070d; }}
  .text {{ fill: #00ffff; font-family: monospace; font-size: 14px; }}
  .title {{ fill: #00ffff; font-size: 18px; }}
  .glow {{ filter: drop-shadow(0 0 6px #00ffff); }}
</style>

<rect width="100%" height="100%" class="bg"/>

<text x="20" y="30" class="title glow">
🧠 AI REPOSITORY ANALYSIS
</text>

<text x="20" y="70" class="text">
📦 Total repos: {analysis["total_repos"]}
</text>

<text x="20" y="100" class="text">
⚡ Activity level: {analysis["activity"]}
</text>

<text x="20" y="130" class="text">
🧬 Dominant language: {analysis["top_lang"]}
</text>

<text x="20" y="180" class="text glow">
> SYSTEM INTERPRETATION:
</text>

<text x="20" y="210" class="text">
{generate_ai_message(analysis)}
</text>

</svg>
"""

def generate_ai_message(analysis):
    if analysis["activity"] == "HIGH":
        return "ACTIVE BUILDER • CONTINUOUS EVOLUTION DETECTED"
    elif analysis["activity"] == "MEDIUM":
        return "STABLE DEVELOPMENT • PATTERN CONSISTENCY"
    else:
        return "LOW SIGNAL • POTENTIAL UNDER UTILIZATION"

# =========================================================
# ⚡ GENERATE DYNAMIC DATA (TODO UNIFICADO)
# =========================================================
def generate_data():
    return {
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

        # 🧠 TELEMETRÍA
        "LATENCY": random.randint(20, 120),
        "CPU_LOAD": random.randint(10, 90),
        "MEMORY_USAGE": random.randint(20, 95),
        "SECURITY_LEVEL": random.choice(["LOW", "MEDIUM", "HIGH"]),
        "THREAT_LEVEL": random.choice(["STABLE", "ELEVATED", "CRITICAL"]),

        # ⚡ SISTEMA AVANZADO
        "TREND": random.choice(["UP", "DOWN", "STABLE"]),
        "STREAK": random.randint(1, 30),

        "AI_STATUS": random.choice(["ACTIVE", "LEARNING", "OPTIMIZING"]),
        "AUTOMATION_STATUS": random.choice(["RUNNING", "IDLE"]),
        "SECURITY_STATUS": random.choice(["SECURE", "MONITORING"]),
        "NETWORK_STATUS": random.choice(["STABLE", "LATENT"]),
        "EVOLUTION_STAGE": random.choice(["PHASE 1", "PHASE 2", "EXPANDING"]),

        # 🌍 ENTORNO
        "TIMEZONE": "UTC",
        "CURRENT_TIME": datetime.utcnow().strftime("%H:%M:%S"),
        "WEATHER": random.choice(["CLEAR", "CLOUDY", "UNKNOWN"]),

        # 🧬 MENSAJE
        "DAILY_MESSAGE": random.choice([
            "El sistema evoluciona...",
            "Nueva capa cargada...",
            "Expansión en proceso...",
            "Conciencia adaptativa activa..."
        ]),

        # 📡 EVENTOS
        "SYSTEM_EVENTS": "\n".join([
            "[SYS] Scan complete",
            "[AI] Pattern detected",
            "[NET] Stable connection"
        ])
    }


# =========================================================
# 🔁 RENDER TEMPLATE
# =========================================================
def render_template(template, data):
    for key, value in data.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))

    if "{{" in template:
        print("⚠️ WARNING: placeholders no reemplazados")

    return template


# =========================================================
# 📤 SAVE README
# =========================================================
def save_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)


# =========================================================
# 🔥 ULTRA HUD FINAL
# =========================================================
def generate_ultra_hud(data):
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

<rect width="100%" height="100%" class="bg"/>

<circle cx="250" cy="250" r="18" fill="{primary}" class="glow">
  <animate attributeName="r" values="18;28;18" dur="1s" repeatCount="indefinite"/>
</circle>

<circle cx="250" cy="250" r="70" class="grid"/>
<circle cx="250" cy="250" r="140" class="grid"/>
<circle cx="250" cy="250" r="200" class="grid"/>

<line x1="250" y1="250" x2="250" y2="40" stroke="{primary}" stroke-width="2" class="glow">
  <animateTransform attributeName="transform"
    type="rotate"
    from="0 250 250"
    to="360 250 250"
    dur="2s"
    repeatCount="indefinite"/>
</line>

{"".join([
    f'''
    <circle cx="{random.randint(60,440)}" cy="{random.randint(60,440)}" r="3" fill="{primary}">
      <animate attributeName="r" values="3;8;3" dur="{random.uniform(0.8,1.5)}s" repeatCount="indefinite"/>
    </circle>
    ''' for _ in range(4)
])}

<rect x="20" y="420" width="{data["CPU_LOAD"] * 3}" height="8" fill="{primary}" class="glow"/>
<rect x="20" y="440" width="{data["MEMORY_USAGE"] * 3}" height="8" fill="{primary}"/>

<text x="20" y="30" class="text">LATENCY: {data["LATENCY"]} ms</text>
<text x="20" y="50" class="text">CPU: {data["CPU_LOAD"]}%</text>
<text x="20" y="70" class="text">MEM: {data["MEMORY_USAGE"]}%</text>
<text x="20" y="90" class="text">SEC: {data["SECURITY_LEVEL"]}</text>
<text x="20" y="110" class="text">THREAT: {data["THREAT_LEVEL"]}</text>

<text x="250" y="255" text-anchor="middle" class="text glow">
  {status_text}
</text>

<text x="250" y="280" text-anchor="middle" class="text">
  {mood}
</text>

</svg>
"""

def generate_identity_banner(data):
    name = "WILLIAM AYALA"

    return f"""
<svg width="900" height="220" viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg">

<style>
  .bg {{
    fill: #05070d;
  }}

  .title {{
    font-family: 'Orbitron', monospace;
    font-size: 34px;
    fill: #00ffff;
    letter-spacing: 3px;
  }}

  .subtitle {{
    font-family: monospace;
    font-size: 14px;
    fill: #00ffff;
    opacity: 0.7;
  }}

  .glow {{
    filter: drop-shadow(0 0 8px #00ffff);
  }}

  .line {{
    stroke: #00ffff;
    stroke-width: 1;
    stroke-dasharray: 4;
    opacity: 0.4;
  }}
</style>

<!-- Fondo -->
<rect width="100%" height="100%" class="bg"/>

<!-- Líneas animadas -->
<line x1="0" y1="40" x2="900" y2="40" class="line">
  <animate attributeName="x2" from="0" to="900" dur="2s" repeatCount="indefinite"/>
</line>

<line x1="0" y1="180" x2="900" y2="180" class="line">
  <animate attributeName="x2" from="0" to="900" dur="3s" repeatCount="indefinite"/>
</line>

<!-- Nombre -->
<text x="50%" y="90" text-anchor="middle" class="title glow">
  {name}
  <animate attributeName="opacity" values="0;1;1" dur="2s"/>
</text>

<!-- Estado IA -->
<text x="50%" y="120" text-anchor="middle" class="subtitle">
  ⚡ AI SYSTEM ACTIVE • {data["AI_STATUS"]}
</text>

<!-- Datos -->
<text x="50%" y="145" text-anchor="middle" class="subtitle">
  🧠 CPU: {data["CPU_LOAD"]}% • 💾 MEM: {data["MEMORY_USAGE"]}% • 📡 LAT: {data["LATENCY"]}ms
</text>

<!-- Redes -->
<text x="50%" y="175" text-anchor="middle" class="subtitle">
  🌐 GitHub: Makavellik • ⚡ OSINT • 🛡️ Cyber Intelligence
</text>

</svg>
"""

# =========================================================
# 💾 SAVE HUD
# =========================================================
def save_hud(svg):
    with open("hud.svg", "w") as f:
        f.write(svg)
        

# =========================================================
# 🚀 MAIN
# =========================================================
def main():
    data = generate_data()

    template = load_template()
    rendered = render_template(template, data)
    save_readme(rendered)

    svg = generate_ultra_hud(data)
    save_hud(svg)
    
    # Add these lines here
    banner = generate_identity_banner(data)
    with open("banner.svg", "w") as f:
        f.write(banner)

    repos = fetch_repos("Makavellik")
    analysis = analyze_repos(repos)

    ai_svg = generate_ai_analysis(data, analysis)
    with open("ai.svg", "w") as f:
        f.write(ai_svg)

    repo_ui = generate_clickable_repos()
    with open("repos_clickable.svg", "w") as f:
        f.write(repo_ui)    

    print("✅ README y HUD generados correctamente")


if __name__ == "__main__":
    main()
