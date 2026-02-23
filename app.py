# ___________________________________________________
#         Proyecto Aplicado en Streamlit  
# NOMBRE: JORGE AUGUSTO ZAVALETA QUINTANA
# CURSO: FUNDAMENTOS DE PROGRAMACIÓN
# __________________________________________________

import streamlit as st
import pandas as pd

# ____________  CONFIGURACIÓN DE PÁGINA ____________

st.set_page_config(
    page_title="Python Fundamentals · Módulo 1",
    page_icon="🦂",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&display=swap');

/* ── Root variables ── */
:root {
    --bg:       #0a0a0f;
    --surface:  #111118;
    --border:   #1e1e2e;
    --accent1:  #7c3aed;
    --accent2:  #06b6d4;
    --accent3:  #f59e0b;
    --danger:   #ef4444;
    --success:  #10b981;
    --text:     #e2e8f0;
    --muted:    #64748b;
    --glow1: 0 0 40px rgba(124,58,237,.35);
    --glow2: 0 0 40px rgba(6,182,212,.35);
}

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: var(--bg);
    color: var(--text);
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1100px;}

/* ── Animated noise overlay ── */
body::before {
    content: "";
    position: fixed; inset: 0; z-index: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
    background-repeat: repeat;
    background-size: 200px 200px;
    pointer-events: none;
    opacity: .6;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d18 0%, #0a0a0f 100%);
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {color: var(--text) !important;}

/* ── Inputs ── */
input[type="number"], input[type="text"], .stTextInput input, .stNumberInput input {
    background: #13131f !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
}
input:focus { border-color: var(--accent1) !important; box-shadow: var(--glow1) !important; }

/* ── Selectbox ── */
.stSelectbox > div > div {
    background: #13131f !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--accent1), #4f46e5) !important;
    border: none !important;
    border-radius: 8px !important;
    color: #fff !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: .05em !important;
    padding: .6rem 1.6rem !important;
    transition: all .25s ease !important;
    box-shadow: 0 4px 20px rgba(124,58,237,.4) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(124,58,237,.6) !important;
}

/* ── Slider ── */
.stSlider .rc-slider-track { background: var(--accent1) !important; }
.stSlider .rc-slider-handle {
    border-color: var(--accent1) !important;
    background: var(--accent1) !important;
    box-shadow: var(--glow1) !important;
}

/* ── Success / Warning / Error ── */
.stSuccess {background: rgba(16,185,129,.12) !important; border-left: 4px solid var(--success) !important; border-radius: 8px !important;}
.stWarning {background: rgba(245,158,11,.12) !important; border-left: 4px solid var(--accent3) !important; border-radius: 8px !important;}
.stError   {background: rgba(239,68,68,.12) !important;  border-left: 4px solid var(--danger)  !important; border-radius: 8px !important;}
.stInfo    {background: rgba(6,182,212,.12) !important;  border-left: 4px solid var(--accent2) !important; border-radius: 8px !important;}

/* ── Dataframe ── */
.stDataFrame { border: 1px solid var(--border) !important; border-radius: 12px !important; overflow: hidden; }

/* ── Divider ── */
hr { border-color: var(--border) !important; }

/* ── Metric ── */
[data-testid="stMetricValue"] {
    color: var(--accent2) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 1.8rem !important;
}
[data-testid="stMetricLabel"] { color: var(--muted) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent1); }
</style>
""", unsafe_allow_html=True)


# __________________ UI REUSABLE  __________________

def page_header(title: str, subtitle: str, icon: str = "🦂"):
    st.markdown(f"""
    <div style="margin-bottom:2rem;">
        <div style="display:flex;align-items:center;gap:.75rem;margin-bottom:.5rem;">
            <span style="font-size:2rem;filter:drop-shadow(0 0 12px rgba(124,58,237,.8))">{icon}</span>
            <h1 style="margin:0;font-family:'Syne',sans-serif;font-weight:800;font-size:2.2rem;
                       background:linear-gradient(135deg,#a78bfa,#38bdf8);
                       -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
                {title}
            </h1>
        </div>
        <p style="margin:0;color:#64748b;font-size:.95rem;letter-spacing:.05em;">{subtitle}</p>
        <div style="margin-top:1rem;height:2px;
                    background:linear-gradient(90deg,#7c3aed,#06b6d4,transparent);
                    border-radius:1px;"></div>
    </div>
    """, unsafe_allow_html=True)


def card(content_html: str, border_color: str = "#1e1e2e", glow: str = ""):
    glow_style = f"box-shadow: 0 0 30px {glow};" if glow else ""
    st.markdown(f"""
    <div style="background:#111118;border:1px solid {border_color};border-radius:16px;
                padding:1.5rem 1.75rem;margin-bottom:1.25rem;{glow_style}
                transition:all .3s ease;">
        {content_html}
    </div>
    """, unsafe_allow_html=True)


def badge(text: str, color: str):
    return f'<span style="background:{color}22;color:{color};border:1px solid {color}55;border-radius:999px;padding:.2rem .75rem;font-size:.75rem;font-family:\'Space Mono\',monospace;font-weight:700;letter-spacing:.05em;">{text}</span>'


def section_tag(label: str):
    st.markdown(f"""
    <div style="display:inline-flex;align-items:center;gap:.5rem;
                background:rgba(124,58,237,.15);border:1px solid rgba(124,58,237,.3);
                border-radius:999px;padding:.3rem 1rem;margin-bottom:1.25rem;">
        <div style="width:6px;height:6px;border-radius:50%;background:#7c3aed;
                    box-shadow:0 0 8px #7c3aed;"></div>
        <span style="font-size:.8rem;font-weight:700;letter-spacing:.1em;
                     color:#a78bfa;text-transform:uppercase;">{label}</span>
    </div>
    """, unsafe_allow_html=True)


# _______________  BARRA DE NAVEGACIÓN _______________

with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 0 1rem;">
        <div style="font-size:2.5rem;margin-bottom:.5rem;
                    filter:drop-shadow(0 0 16px rgba(124,58,237,1));">⚡</div>
        <div style="font-family:'Syne',sans-serif;font-weight:800;font-size:1.1rem;
                    background:linear-gradient(135deg,#a78bfa,#38bdf8);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            Python Fundamentals
        </div>
        <div style="color:#64748b;font-size:.75rem;letter-spacing:.1em;margin-top:.25rem;">
            MÓDULO 1 · 2025
        </div>
    </div>
    <hr style="border-color:#1e1e2e;margin:.5rem 0 1.5rem;"/>
    """, unsafe_allow_html=True)

    menu = st.selectbox(
        "Navegación",
        ["🏠  Home", "📊  Ejercicio 1 – Variables y Condicionales",
         "📋  Ejercicio 2 – Listas y Diccionarios",
         "🔧  Ejercicio 3 – Funciones y Map/Lambda",
         "🏛️  Ejercicio 4 – Programación Orientada a Objetos"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <hr style="border-color:#1e1e2e;margin:1.5rem 0 1rem;"/>
    <div style="color:#64748b;font-size:.72rem;text-align:center;line-height:1.6;">
        Especialización en Python for Analytics<br>
        <span style="color:#a78bfa;">MSc. Carlos Carrillo Villavicencio</span>
    </div>
    """, unsafe_allow_html=True)

page = menu.split("  ")[-1] if "  " in menu else menu

# ______________________________________________
#                     HOME  
# ______________________________________________

if "Home" in menu:
    # Hero banner
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0d0d18 0%,#13101f 50%,#0a0f1a 100%);
                border:1px solid #1e1e2e;border-radius:20px;padding:3rem 2.5rem;
                margin-bottom:2rem;position:relative;overflow:hidden;">
        <!-- decorative circles -->
        <div style="position:absolute;top:-60px;right:-60px;width:220px;height:220px;
                    border-radius:50%;background:radial-gradient(circle,rgba(124,58,237,.25),transparent 70%);
                    pointer-events:none;"></div>
        <div style="position:absolute;bottom:-40px;left:30px;width:160px;height:160px;
                    border-radius:50%;background:radial-gradient(circle,rgba(6,182,212,.2),transparent 70%);
                    pointer-events:none;"></div>
        <div style="position:relative;z-index:1;">
            <div style="font-family:'Space Mono',monospace;color:#7c3aed;font-size:.85rem;
                        letter-spacing:.2em;margin-bottom:1rem;">// PROYECTO APLICADO · 2025</div>
            <h1 style="font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(2rem,4vw,3rem);
                        margin:0 0 .5rem;
                        background:linear-gradient(135deg,#fff 30%,#a78bfa 70%,#38bdf8 100%);
                        -webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1.1;">
                Fundamentos de<br>Programación en Python
            </h1>
            <p style="color:#94a3b8;font-size:1.05rem;margin:.75rem 0 1.5rem;max-width:600px;">
                Aplicación interactiva desarrollada con <strong style="color:#a78bfa;">Streamlit</strong>
                que integra variables, estructuras de datos, control de flujo, funciones,
                programación funcional y POO.
            </p>
            <div style="display:flex;gap:.75rem;flex-wrap:wrap;">
    """ + badge("Python 3.11", "#f59e0b") + badge("Streamlit", "#06b6d4") +
    badge("Pandas", "#10b981") + badge("POO", "#7c3aed") + """
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        section_tag("Sobre el proyecto")
        card("""
        <div style="font-family:'Space Mono',monospace;font-size:.8rem;color:#64748b;margin-bottom:.75rem;">
            AUTOR &amp; CURSO
        </div>
        <table style="width:100%;border-collapse:collapse;font-size:.9rem;">
            <tr><td style="color:#64748b;padding:.4rem 0;width:40%;">Estudiante</td>
                <td style="color:#e2e8f0;font-weight:600;">Tu Nombre Aquí</td></tr>
            <tr><td style="color:#64748b;padding:.4rem 0;">Módulo</td>
                <td style="color:#a78bfa;font-weight:600;">Módulo 1 – Python Fundamentals</td></tr>
            <tr><td style="color:#64748b;padding:.4rem 0;">Programa</td>
                <td style="color:#e2e8f0;">Especialización Python for Analytics</td></tr>
            <tr><td style="color:#64748b;padding:.4rem 0;">Institución</td>
                <td style="color:#e2e8f0;">DMC Institute</td></tr>
            <tr><td style="color:#64748b;padding:.4rem 0;">Año</td>
                <td style="color:#38bdf8;font-family:'Space Mono',monospace;">2025</td></tr>
        </table>
        """, border_color="#7c3aed44", glow="rgba(124,58,237,.15)")

    with col2:
        section_tag("Contenido del módulo")
        exercises = [
            ("01", "Variables y Condicionales", "#7c3aed", "Verificador de presupuesto interactivo"),
            ("02", "Listas y Diccionarios", "#06b6d4", "Registro de actividades financieras"),
            ("03", "Funciones & Map/Lambda", "#f59e0b", "Cálculo de retorno con prog. funcional"),
            ("04", "POO", "#10b981", "Clase Actividad con métodos propios"),
        ]
        for num, title, color, desc in exercises:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:1rem;
                        background:#0d0d18;border:1px solid #1e1e2e;
                        border-radius:12px;padding:.85rem 1.1rem;margin-bottom:.6rem;
                        border-left:3px solid {color};transition:all .2s;">
                <div style="font-family:'Space Mono',monospace;font-size:.75rem;
                            color:{color};font-weight:700;min-width:28px;">{num}</div>
                <div>
                    <div style="font-weight:700;font-size:.9rem;color:#e2e8f0;">{title}</div>
                    <div style="font-size:.78rem;color:#64748b;margin-top:.15rem;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:linear-gradient(135deg,rgba(124,58,237,.08),rgba(6,182,212,.08));
                border:1px solid #1e1e2e;border-radius:16px;padding:1.5rem 2rem;margin-top:1rem;">
        <div style="font-family:'Space Mono',monospace;font-size:.75rem;color:#64748b;
                    margin-bottom:.5rem;">// STACK TECNOLÓGICO</div>
        <div style="display:flex;gap:2.5rem;flex-wrap:wrap;">
            <div><span style="color:#f59e0b;font-weight:700;">Python</span>
                 <span style="color:#64748b;font-size:.82rem;display:block;">Lenguaje base</span></div>
            <div><span style="color:#06b6d4;font-weight:700;">Streamlit</span>
                 <span style="color:#64748b;font-size:.82rem;display:block;">Frontend web</span></div>
            <div><span style="color:#10b981;font-weight:700;">Pandas</span>
                 <span style="color:#64748b;font-size:.82rem;display:block;">Tablas de datos</span></div>
            <div><span style="color:#7c3aed;font-weight:700;">POO</span>
                 <span style="color:#64748b;font-size:.82rem;display:block;">Orientación a objetos</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#           EJERCICIO 1 – VARIABLES Y CONDICIONALES
# ═══════════════════════════════════════════════════════════
elif "Ejercicio 1" in menu:
    page_header("Variables y Condicionales", "Verificador inteligente de presupuesto", "📊")

    st.markdown("""
    <div style="background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.2);
                border-radius:12px;padding:1rem 1.25rem;margin-bottom:1.75rem;font-size:.88rem;color:#94a3b8;">
        💡 Ingresa un presupuesto y un gasto para evaluar si el gasto se mantiene dentro del límite establecido.
        El sistema aplica <strong style="color:#a78bfa;">variables, condicionales y operadores aritméticos</strong>.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        section_tag("Parámetros de entrada")
        presupuesto = st.number_input(
            "💰 Presupuesto disponible ($)",
            min_value=0.0, value=1000.0, step=50.0,
            help="Monto máximo que deseas gastar"
        )
    with col2:
        st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
        gasto = st.number_input(
            "🛒 Gasto real ($)",
            min_value=0.0, value=750.0, step=50.0,
            help="Monto que efectivamente se gastó"
        )

    st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
    evaluar = st.button("⚡ Evaluar presupuesto", use_container_width=False)

    if evaluar:
        diferencia = presupuesto - gasto
        porcentaje = (gasto / presupuesto * 100) if presupuesto > 0 else 0
        restante_pct = max(0, 100 - porcentaje)

        st.markdown("<hr style='border-color:#1e1e2e;margin:1.5rem 0;'/>", unsafe_allow_html=True)
        section_tag("Resultado del análisis")

        # Metrics row
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Presupuesto", f"${presupuesto:,.2f}")
        with m2:
            st.metric("Gasto real", f"${gasto:,.2f}")
        with m3:
            delta_color = "normal" if diferencia >= 0 else "inverse"
            st.metric("Diferencia", f"${abs(diferencia):,.2f}",
                      delta=f"{'Ahorro' if diferencia>=0 else 'Exceso'}: ${abs(diferencia):,.2f}",
                      delta_color=delta_color)

        # Progress bar visual
        bar_color = "#10b981" if porcentaje <= 100 else "#ef4444"
        bar_width = min(porcentaje, 100)
        st.markdown(f"""
        <div style="margin:1.25rem 0;">
            <div style="display:flex;justify-content:space-between;font-size:.8rem;
                        color:#64748b;margin-bottom:.4rem;">
                <span>Uso del presupuesto</span>
                <span style="font-family:'Space Mono',monospace;color:{bar_color};">
                    {porcentaje:.1f}%
                </span>
            </div>
            <div style="background:#1e1e2e;border-radius:999px;height:10px;overflow:hidden;">
                <div style="width:{bar_width}%;height:100%;border-radius:999px;
                            background:linear-gradient(90deg,{bar_color},{bar_color}88);
                            transition:width .6s ease;box-shadow:0 0 12px {bar_color}88;">
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Verdict
        if gasto <= presupuesto:
            st.success(f"✅ **¡Dentro del presupuesto!** — Tienes un margen disponible de **${diferencia:,.2f}** ({restante_pct:.1f}% restante).")
        else:
            st.warning(f"⚠️ **Presupuesto excedido** — Has superado el límite por **${abs(diferencia):,.2f}** ({porcentaje-100:.1f}% de exceso).")

        # Python code display
        with st.expander("🔍 Ver lógica Python aplicada"):
            st.code(f"""
# Variables
presupuesto = {presupuesto}
gasto       = {gasto}

# Condicional
diferencia = presupuesto - gasto
if gasto <= presupuesto:
    print(f"Dentro del presupuesto. Margen: {{diferencia:.2f}}")
else:
    print(f"Excedido por: {{abs(diferencia):.2f}}")
            """, language="python")


# ═══════════════════════════════════════════════════════════
#               EJERCICIO 2 – LISTAS Y DICCIONARIOS
# ═══════════════════════════════════════════════════════════
elif "Ejercicio 2" in menu:
    page_header("Listas y Diccionarios", "Registro de actividades financieras", "📋")

    # Session state init
    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    st.markdown("""
    <div style="background:rgba(6,182,212,.08);border:1px solid rgba(6,182,212,.2);
                border-radius:12px;padding:1rem 1.25rem;margin-bottom:1.75rem;font-size:.88rem;color:#94a3b8;">
        💡 Registra actividades financieras. Cada una se almacena como un
        <strong style="color:#38bdf8;">diccionario dentro de una lista</strong>.
        El sistema evalúa automáticamente el cumplimiento del presupuesto.
    </div>
    """, unsafe_allow_html=True)

    section_tag("Agregar actividad")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        nombre = st.text_input("📌 Nombre de la actividad", placeholder="Ej: Campaña Digital Q1")
        tipo = st.selectbox("🏷️ Tipo de actividad",
                            ["Marketing", "Operaciones", "Tecnología", "Recursos Humanos",
                             "Ventas", "Infraestructura", "Investigación", "Otro"])
    with col2:
        presupuesto_act = st.number_input("💰 Presupuesto ($)", min_value=0.0, value=5000.0, step=100.0)
        gasto_real = st.number_input("💸 Gasto real ($)", min_value=0.0, value=4200.0, step=100.0)

    agregar = st.button("➕ Agregar actividad", use_container_width=False)

    if agregar:
        if nombre.strip():
            actividad = {
                "nombre": nombre.strip(),
                "tipo": tipo,
                "presupuesto": presupuesto_act,
                "gasto_real": gasto_real,
            }
            st.session_state.actividades.append(actividad)
            st.success(f"✅ Actividad **{nombre}** registrada correctamente.")
        else:
            st.warning("⚠️ Por favor ingresa un nombre para la actividad.")

    st.markdown("<hr style='border-color:#1e1e2e;margin:1.5rem 0;'/>", unsafe_allow_html=True)

    if st.session_state.actividades:
        section_tag(f"Actividades registradas · {len(st.session_state.actividades)}")

        # Build dataframe with estado
        rows = []
        for a in st.session_state.actividades:
            diferencia = a["presupuesto"] - a["gasto_real"]
            estado = "✅ En presupuesto" if a["gasto_real"] <= a["presupuesto"] else "⚠️ Excedido"
            pct = a["gasto_real"] / a["presupuesto"] * 100 if a["presupuesto"] > 0 else 0
            rows.append({
                "Actividad": a["nombre"],
                "Tipo": a["tipo"],
                "Presupuesto $": a["presupuesto"],
                "Gasto Real $": a["gasto_real"],
                "Diferencia $": diferencia,
                "Uso %": round(pct, 1),
                "Estado": estado,
            })
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Summary metrics
        st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
        s1, s2, s3, s4 = st.columns(4)
        total_presup = sum(a["presupuesto"] for a in st.session_state.actividades)
        total_gasto  = sum(a["gasto_real"]  for a in st.session_state.actividades)
        en_presup    = sum(1 for a in st.session_state.actividades if a["gasto_real"] <= a["presupuesto"])
        s1.metric("Total presupuesto", f"${total_presup:,.0f}")
        s2.metric("Total gastado",     f"${total_gasto:,.0f}")
        s3.metric("En presupuesto",    f"{en_presup}/{len(st.session_state.actividades)}")
        s4.metric("Diferencia neta",   f"${total_presup - total_gasto:,.0f}")

        # Detail cards
        st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
        section_tag("Detalle por actividad")
        for a in st.session_state.actividades:
            diferencia = a["presupuesto"] - a["gasto_real"]
            ok = a["gasto_real"] <= a["presupuesto"]
            color = "#10b981" if ok else "#f59e0b"
            pct = a["gasto_real"] / a["presupuesto"] * 100 if a["presupuesto"] > 0 else 0
            st.markdown(f"""
            <div style="background:#0d0d18;border:1px solid {color}44;border-left:4px solid {color};
                        border-radius:12px;padding:1rem 1.25rem;margin-bottom:.75rem;
                        display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.5rem;">
                <div>
                    <div style="font-weight:700;font-size:.95rem;color:#e2e8f0;">{a['nombre']}</div>
                    <div style="font-size:.78rem;color:#64748b;margin-top:.2rem;">
                        {a['tipo']} · Presupuesto: <span style="color:#a78bfa;">${a['presupuesto']:,.0f}</span>
                        · Gasto: <span style="color:{color};">${a['gasto_real']:,.0f}</span>
                        · Uso: <span style="color:{color};">{pct:.1f}%</span>
                    </div>
                </div>
                <div style="background:{color}22;border:1px solid {color}55;border-radius:999px;
                            padding:.3rem .9rem;font-size:.8rem;color:{color};font-weight:700;">
                    {'✅ En presupuesto' if ok else '⚠️ Excedido'}
                </div>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🗑️ Limpiar todas las actividades"):
            st.session_state.actividades = []
            st.rerun()

        with st.expander("🔍 Ver lógica Python aplicada"):
            st.code("""
# Estructura de datos
actividades = []   # lista de diccionarios

# Agregar actividad
actividad = {
    "nombre": nombre,
    "tipo": tipo,
    "presupuesto": presupuesto,
    "gasto_real": gasto_real,
}
actividades.append(actividad)

# Evaluar cada actividad con bucle for
for act in actividades:
    diferencia = act["presupuesto"] - act["gasto_real"]
    if act["gasto_real"] <= act["presupuesto"]:
        print(f"{act['nombre']}: ✅ En presupuesto. Margen: {diferencia:.2f}")
    else:
        print(f"{act['nombre']}: ⚠️ Excedido por {abs(diferencia):.2f}")
            """, language="python")
    else:
        st.markdown("""
        <div style="text-align:center;padding:3rem;color:#64748b;">
            <div style="font-size:2.5rem;margin-bottom:.75rem;">📭</div>
            <div style="font-size:.95rem;">No hay actividades registradas aún.</div>
            <div style="font-size:.82rem;margin-top:.25rem;">Usa el formulario de arriba para agregar la primera.</div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#       EJERCICIO 3 – FUNCIONES Y PROGRAMACIÓN FUNCIONAL
# ═══════════════════════════════════════════════════════════
elif "Ejercicio 3" in menu:
    page_header("Funciones y Programación Funcional", "Cálculo de retorno con map & lambda", "🔧")

    st.markdown("""
    <div style="background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);
                border-radius:12px;padding:1rem 1.25rem;margin-bottom:1.75rem;font-size:.88rem;color:#94a3b8;">
        💡 Se definen actividades base y se aplica la función
        <strong style="color:#f59e0b;">calcular_retorno()</strong> sobre todas ellas usando
        <strong style="color:#f59e0b;">map() + lambda</strong>.
        Fórmula: <code style="color:#fbbf24;background:#1e1e2e;padding:.1rem .4rem;border-radius:4px;">
        Retorno = presupuesto × tasa × meses</code>
    </div>
    """, unsafe_allow_html=True)

    # Activities for this exercise (use session state from ex2 or default)
    actividades_base = st.session_state.get("actividades", [])
    if not actividades_base:
        actividades_base = [
            {"nombre": "Campaña Digital",    "tipo": "Marketing",    "presupuesto": 8000,  "gasto_real": 7200},
            {"nombre": "Servidor Cloud",     "tipo": "Tecnología",   "presupuesto": 12000, "gasto_real": 11500},
            {"nombre": "Capacitación RRHH",  "tipo": "Recursos Humanos", "presupuesto": 5000, "gasto_real": 4800},
            {"nombre": "Expansión Ventas",   "tipo": "Ventas",       "presupuesto": 15000, "gasto_real": 16000},
        ]

    col1, col2 = st.columns(2, gap="large")
    with col1:
        section_tag("Parámetros del cálculo")
        tasa = st.slider(
            "📈 Tasa de retorno mensual (%)",
            min_value=0.5, max_value=20.0, value=5.0, step=0.5,
            help="Porcentaje de retorno esperado por mes"
        )
        tasa_decimal = tasa / 100
    with col2:
        st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
        meses = st.number_input(
            "📅 Número de meses",
            min_value=1, max_value=60, value=12, step=1,
            help="Horizonte temporal del cálculo"
        )

    calcular = st.button("⚡ Calcular retornos con map & lambda", use_container_width=False)

    if calcular:
        # ── Programación funcional ──
        def calcular_retorno(actividad, tasa, meses):
            return actividad["presupuesto"] * tasa * meses

        retornos = list(map(
            lambda act: calcular_retorno(act, tasa_decimal, meses),
            actividades_base
        ))

        st.markdown("<hr style='border-color:#1e1e2e;margin:1.5rem 0;'/>", unsafe_allow_html=True)
        section_tag("Resultados del cálculo funcional")

        # Summary
        total_presup  = sum(a["presupuesto"] for a in actividades_base)
        total_retorno = sum(retornos)
        roi_global    = (total_retorno / total_presup * 100) if total_presup > 0 else 0

        m1, m2, m3 = st.columns(3)
        m1.metric("Total presupuesto", f"${total_presup:,.0f}")
        m2.metric("Retorno total esperado", f"${total_retorno:,.0f}")
        m3.metric("ROI acumulado", f"{roi_global:.1f}%")

        st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)

        # Cards per activity
        for act, retorno in zip(actividades_base, retornos):
            roi_act = retorno / act["presupuesto"] * 100 if act["presupuesto"] > 0 else 0
            st.markdown(f"""
            <div style="background:#0d0d18;border:1px solid rgba(245,158,11,.2);
                        border-left:4px solid #f59e0b;border-radius:12px;
                        padding:1rem 1.4rem;margin-bottom:.75rem;">
                <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem;">
                    <div>
                        <div style="font-weight:700;font-size:.95rem;color:#e2e8f0;">{act['nombre']}</div>
                        <div style="font-size:.78rem;color:#64748b;margin-top:.2rem;">
                            {act['tipo']} · Presupuesto:
                            <span style="color:#a78bfa;">${act['presupuesto']:,.0f}</span>
                            · Tasa: <span style="color:#f59e0b;">{tasa}%</span>
                            · Meses: <span style="color:#38bdf8;">{meses}</span>
                        </div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-family:'Space Mono',monospace;font-size:1.1rem;
                                    color:#f59e0b;font-weight:700;">${retorno:,.2f}</div>
                        <div style="font-size:.75rem;color:#64748b;">ROI: {roi_act:.1f}%</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # DataFrame
        df3 = pd.DataFrame([
            {
                "Actividad": a["nombre"],
                "Tipo": a["tipo"],
                "Presupuesto $": a["presupuesto"],
                f"Retorno ({meses}m) $": round(r, 2),
                "ROI %": round(r / a["presupuesto"] * 100, 2) if a["presupuesto"] > 0 else 0,
            }
            for a, r in zip(actividades_base, retornos)
        ])
        st.dataframe(df3, use_container_width=True, hide_index=True)

        with st.expander("🔍 Ver lógica Python aplicada"):
            st.code(f"""
# ── Definición de función ──
def calcular_retorno(actividad, tasa, meses):
    return actividad["presupuesto"] * tasa * meses

# ── Programación funcional con map + lambda ──
tasa   = {tasa_decimal}   # {tasa}% mensual
meses  = {meses}

retornos = list(map(
    lambda act: calcular_retorno(act, tasa, meses),
    actividades
))

# Resultado
for act, retorno in zip(actividades, retornos):
    print(f"{{act['nombre']}}: ${{retorno:,.2f}}")
            """, language="python")

    if not calcular:
        st.markdown("""
        <div style="text-align:center;padding:3rem;color:#64748b;">
            <div style="font-size:2.5rem;margin-bottom:.75rem;">🔧</div>
            <div>Ajusta los parámetros y presiona <strong style="color:#f59e0b;">Calcular retornos</strong>.</div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#        EJERCICIO 4 – PROGRAMACIÓN ORIENTADA A OBJETOS
# ═══════════════════════════════════════════════════════════
elif "Ejercicio 4" in menu:
    page_header("Programación Orientada a Objetos", "Clase Actividad · atributos & métodos", "🏛️")

    st.markdown("""
    <div style="background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);
                border-radius:12px;padding:1rem 1.25rem;margin-bottom:1.75rem;font-size:.88rem;color:#94a3b8;">
        💡 Se implementa la <strong style="color:#34d399;">clase Actividad</strong> con atributos y métodos propios:
        <code style="color:#34d399;background:#1e1e2e;padding:.1rem .4rem;border-radius:4px;">esta_en_presupuesto()</code> y
        <code style="color:#34d399;background:#1e1e2e;padding:.1rem .4rem;border-radius:4px;">mostrar_info()</code>.
        Los registros del Ejercicio 2 se convierten en objetos.
    </div>
    """, unsafe_allow_html=True)

    # ── Clase Actividad ──
    class Actividad:
        def __init__(self, nombre: str, tipo: str, presupuesto: float, gasto_real: float):
            self.nombre      = nombre
            self.tipo        = tipo
            self.presupuesto = presupuesto
            self.gasto_real  = gasto_real

        def esta_en_presupuesto(self) -> bool:
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self) -> dict:
            diferencia = self.presupuesto - self.gasto_real
            porcentaje = (self.gasto_real / self.presupuesto * 100) if self.presupuesto > 0 else 0
            return {
                "nombre":     self.nombre,
                "tipo":       self.tipo,
                "presupuesto": self.presupuesto,
                "gasto_real": self.gasto_real,
                "diferencia": diferencia,
                "porcentaje": round(porcentaje, 2),
                "estado":     "En presupuesto" if self.esta_en_presupuesto() else "Excedido",
            }

    # ── Data source ──
    actividades_raw = st.session_state.get("actividades", [])
    if not actividades_raw:
        actividades_raw = [
            {"nombre": "Campaña Digital",    "tipo": "Marketing",        "presupuesto": 8000,  "gasto_real": 7200},
            {"nombre": "Servidor Cloud",     "tipo": "Tecnología",       "presupuesto": 12000, "gasto_real": 11500},
            {"nombre": "Capacitación RRHH",  "tipo": "Recursos Humanos", "presupuesto": 5000,  "gasto_real": 4800},
            {"nombre": "Expansión Ventas",   "tipo": "Ventas",           "presupuesto": 15000, "gasto_real": 16200},
        ]

    # Instanciar objetos
    objetos: list[Actividad] = [
        Actividad(a["nombre"], a["tipo"], a["presupuesto"], a["gasto_real"])
        for a in actividades_raw
    ]

    # Metrics globales
    total = len(objetos)
    en_presup = sum(1 for o in objetos if o.esta_en_presupuesto())
    excedidos = total - en_presup

    m1, m2, m3 = st.columns(3)
    m1.metric("Objetos creados", str(total))
    m2.metric("En presupuesto", str(en_presup))
    m3.metric("Excedidos", str(excedidos))

    st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
    section_tag("Instancias de la clase Actividad")

    for obj in objetos:
        info   = obj.mostrar_info()
        ok     = obj.esta_en_presupuesto()
        color  = "#10b981" if ok else "#f59e0b"
        icon   = "✅" if ok else "⚠️"
        bar_w  = min(info["porcentaje"], 100)

        st.markdown(f"""
        <div style="background:#0d0d18;border:1px solid {color}44;border-radius:16px;
                    padding:1.25rem 1.5rem;margin-bottom:1rem;
                    box-shadow:0 0 20px {color}10;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;
                        flex-wrap:wrap;gap:.5rem;margin-bottom:.85rem;">
                <div>
                    <span style="font-family:'Space Mono',monospace;font-size:.7rem;
                                 color:#64748b;letter-spacing:.1em;">
                        OBJETO · Actividad
                    </span>
                    <div style="font-weight:800;font-size:1.1rem;color:#e2e8f0;margin-top:.15rem;">
                        {obj.nombre}
                    </div>
                    <div style="font-size:.78rem;color:#64748b;margin-top:.2rem;">
                        Tipo: <strong style="color:#a78bfa;">{obj.tipo}</strong>
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="background:{color}22;border:1px solid {color}55;border-radius:999px;
                                padding:.3rem 1rem;font-size:.82rem;color:{color};font-weight:700;">
                        {icon} {info['estado']}
                    </div>
                    <div style="font-size:.72rem;color:#64748b;margin-top:.35rem;">
                        esta_en_presupuesto() → <span style="color:{color};">
                        {'True' if ok else 'False'}</span>
                    </div>
                </div>
            </div>
            <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem;
                        margin-bottom:.85rem;">
                <div style="background:#111118;border-radius:8px;padding:.6rem .9rem;">
                    <div style="font-size:.7rem;color:#64748b;margin-bottom:.2rem;">presupuesto</div>
                    <div style="font-family:'Space Mono',monospace;color:#a78bfa;font-weight:700;">
                        ${info['presupuesto']:,.0f}
                    </div>
                </div>
                <div style="background:#111118;border-radius:8px;padding:.6rem .9rem;">
                    <div style="font-size:.7rem;color:#64748b;margin-bottom:.2rem;">gasto_real</div>
                    <div style="font-family:'Space Mono',monospace;color:{color};font-weight:700;">
                        ${info['gasto_real']:,.0f}
                    </div>
                </div>
                <div style="background:#111118;border-radius:8px;padding:.6rem .9rem;">
                    <div style="font-size:.7rem;color:#64748b;margin-bottom:.2rem;">diferencia</div>
                    <div style="font-family:'Space Mono',monospace;color:{color};font-weight:700;">
                        ${info['diferencia']:,.0f}
                    </div>
                </div>
            </div>
            <div style="margin-top:.25rem;">
                <div style="display:flex;justify-content:space-between;font-size:.75rem;
                            color:#64748b;margin-bottom:.3rem;">
                    <span>Uso del presupuesto</span>
                    <span style="font-family:'Space Mono',monospace;color:{color};">
                        {info['porcentaje']}%
                    </span>
                </div>
                <div style="background:#1e1e2e;border-radius:999px;height:7px;overflow:hidden;">
                    <div style="width:{bar_w}%;height:100%;border-radius:999px;
                                background:linear-gradient(90deg,{color},{color}88);">
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Class definition display
    with st.expander("🔍 Ver definición de la clase Actividad"):
        st.code("""
class Actividad:
    def __init__(self, nombre: str, tipo: str,
                 presupuesto: float, gasto_real: float):
        self.nombre      = nombre
        self.tipo        = tipo
        self.presupuesto = presupuesto
        self.gasto_real  = gasto_real

    def esta_en_presupuesto(self) -> bool:
        \"\"\"Retorna True si el gasto es <= presupuesto.\"\"\"
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self) -> dict:
        \"\"\"Retorna un resumen completo de la actividad.\"\"\"
        diferencia = self.presupuesto - self.gasto_real
        porcentaje = (self.gasto_real / self.presupuesto * 100
                      if self.presupuesto > 0 else 0)
        return {
            "nombre":     self.nombre,
            "tipo":       self.tipo,
            "presupuesto": self.presupuesto,
            "gasto_real": self.gasto_real,
            "diferencia": diferencia,
            "porcentaje": round(porcentaje, 2),
            "estado": ("En presupuesto" if self.esta_en_presupuesto()
                       else "Excedido"),
        }

# Instanciar objetos desde lista de diccionarios
objetos = [
    Actividad(a["nombre"], a["tipo"], a["presupuesto"], a["gasto_real"])
    for a in actividades
]

# Usar métodos
for obj in objetos:
    info = obj.mostrar_info()
    if obj.esta_en_presupuesto():
        print(f"✅ {obj.nombre}: dentro del presupuesto")
    else:
        print(f"⚠️ {obj.nombre}: excedido por ${abs(info['diferencia']):,.2f}")
        """, language="python")
