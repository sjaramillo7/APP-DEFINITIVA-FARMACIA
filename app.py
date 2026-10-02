import streamlit as st
import random
import pandas as pd

# Configuración de página ancha y título
st.set_page_config(page_title="Simulador QF Élite", page_icon="⚕️", layout="wide")

# --- MANEJO DE ERRORES DE IMPORTACIÓN ---
try:
    from datos import datos_base
except Exception as e:
    st.error(f"🚨 ALERTA QF: Error al leer 'datos.py'. Detalles: {e}")
    datos_base = []
    
try:
    from vademecum import datos_vademecum
except Exception as e:
    st.error(f"🚨 ALERTA QF: Error al leer 'vademecum.py'. Detalles: {e}")
    datos_vademecum = []

# --- CSS PERSONALIZADO (PREGUNTADOS / GAMER STYLE) ---
st.markdown("""
<style>
    .stApp { background-color: #f0f2f6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .titulo-principal { font-size: 3.5rem; font-weight: 900; color: #1F618D; text-align: center; margin-bottom: 0px; letter-spacing: -1px; }
    .subtitulo { font-size: 1.2rem; color: #5D6D7E; text-align: center; margin-bottom: 40px; font-weight: bold; }
    
    /* Menú Cards */
    .card-menu { background-color: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); text-align: center; border-top: 6px solid #2980B9; height: 100%; transition: transform 0.3s ease; }
    .card-menu:hover { transform: translateY(-5px); }
    .card-menu h3 { color: #2980B9; margin-top: 0; font-weight: 800;}
    .card-menu-warning { border-top: 6px solid #E67E22; }
    .card-menu-warning h5 { color: #E67E22; margin-top: 0; font-weight: 700; }
    .card-menu-danger { border-top: 6px solid #C0392B; }
    .card-menu-danger h3 { color: #C0392B; margin-top: 0; font-weight: 800;}
    .card-menu-success { border-top: 6px solid #27AE60; }
    .card-menu-success h3 { color: #27AE60; margin-top: 0; font-weight: 800;}
    .card-menu-dark { border-top: 6px solid #34495E; }
    
    /* PREGUNTADOS STYLE - TARJETA DE PREGUNTA */
    .quiz-question {
        background-color: #ffffff;
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        font-size: 24px;
        font-weight: 700;
        color: #2C3E50;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 40px;
        border-bottom: 6px solid #D5D8DC;
        line-height: 1.4;
    }
    
    /* BOTONES DE OPCIONES (GRILLA 2x2) */
    div.stButton > button { 
        background-color: #ffffff; 
        color: #34495E; 
        border-radius: 15px; 
        font-weight: bold; 
        font-size: 16px;
        border: 2px solid #E5E7E9; 
        padding: 20px 10px; 
        width: 100%; 
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        white-space: normal;
        height: 100%;
        min-height: 100px;
    }
    div.stButton > button:hover { 
        background-color: #EBF5FB; 
        color: #2980B9; 
        border-color: #3498DB;
        transform: translateY(-3px); 
        box-shadow: 0 6px 15px rgba(52, 152, 219, 0.3); 
    }
</style>
""", unsafe_allow_html=True)

# --- INICIALIZACIÓN DE ESTADOS MAESTROS ---
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = "Inicio"
if 'modo_juego' not in st.session_state:
    st.session_state.modo_juego = "Examen Nacional"
if 'filtro_seleccionado' not in st.session_state:
    st.session_state.filtro_seleccionado = "Todas"

# Función de enrutamiento
def ir_a(pagina, modo="Examen Nacional", filtro="Todas"):
    st.session_state.pagina_actual = pagina
    st.session_state.modo_juego = modo
    st.session_state.filtro_seleccionado = filtro
    if pagina == "Simulador" and 'preguntas' in st.session_state:
        del st.session_state['preguntas']
    st.rerun()

# Extraer listas únicas de la base de datos
if datos_base:
    familias = sorted(list(set([d.get("familia", "General") for d in datos_base])))
    categorias = sorted(list(set([d.get("categoria", "General") for d in datos_base])))
else:
    familias = ["Sin datos"]
    categorias = ["Sin datos"]

# --- SIDEBAR (SÓLO STATUS Y BOTÓN DE RETORNO) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966486.png", width=90)
    st.markdown("## ⚙️ Base QF Élite")
    
    if st.session_state.pagina_actual != "Inicio":
        if st.button("🏠 Volver al Menú Principal", use_container_width=True):
            ir_a("Inicio")
            
    st.markdown("---")
    
    if st.session_state.pagina_actual == "Simulador" and 'vidas' in st.session_state:
        st.metric("Vidas Restantes ❤️", st.session_state.vidas)
        if 'preguntas' in st.session_state and len(st.session_state.preguntas) > 0:
            progreso = st.session_state.indice / len(st.session_state.preguntas)
            st.progress(progreso, text=f"Casos: {st.session_state.indice}/{len(st.session_state.preguntas)}")

# ==========================================
# PÁGINA 1: MENÚ DE INICIO
# ==========================================
if st.session_state.pagina_actual == "Inicio":
    st.markdown('<p class="titulo-principal">SIMULADOR CLÍNICO QF</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">Red Integrada de Salud Ñuble • Nivel Avanzado</p>', unsafe_allow_html=True)
    
    st.markdown("### ⚔️ Modos de Simulación")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card-menu card-menu-danger"><h3>🌪️ SUPERVIVENCIA</h3><p>Examen aleatorizado. Todas las familias y categorías mezcladas. Caos total de urgencia.</p></div>', unsafe_allow_html=True)
        st.write("") 
        if st.button("🚀 INICIAR SUPERVIVENCIA", use_container_width=True):
            ir_a("Simulador", "Examen Nacional")
            
    with c2:
        st.markdown('<div class="card-menu card-menu-success"><h3>💊 ESPECIALIDAD</h3><p>Filtra tu entrenamiento por una familia farmacológica en específico (Ej: AINEs).</p></div>', unsafe_allow_html=True)
        familia_sel = st.selectbox("Familia Farmacológica:", familias, label_visibility="collapsed")
        if st.button("🔬 ENTRENAR FAMILIA", use_container_width=True):
            ir_a("Simulador", "Por Familia", familia_sel)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 Entrenamiento Aislado por Módulos")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="card-menu card-menu-warning"><h5>⚙️️ Mecanismo</h5></div>', unsafe_allow_html=True)
        if st.button("Entrenar Mecanismo", use_container_width=True): ir_a("Simulador", "Por Categoría", "⚙️ Mecanismo")
    with m2:
        st.markdown('<div class="card-menu card-menu-warning"><h5>🔄 Interacciones</h5></div>', unsafe_allow_html=True)
        if st.button("Entrenar Interacc.", use_container_width=True): ir_a("Simulador", "Por Categoría", "🔄 Interacciones")
    with m3:
        st.markdown('<div class="card-menu card-menu-warning"><h5>⚠️ RAMs</h5></div>', unsafe_allow_html=True)
        if st.button("Entrenar RAMs", use_container_width=True): ir_a("Simulador", "Por Categoría", "⚠️ RAMs")
    with m4:
        st.markdown('<div class="card-menu card-menu-warning"><h5>🏥 Casos Clínicos</h5></div>', unsafe_allow_html=True)
        if st.button("Entrenar Casos", use_container_width=True): ir_a("Simulador", "Por Categoría", "🏥 Caso Clínico")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 🛠️ Herramientas Clínicas")
    h1, h2 = st.columns(2)
    with h1:
        st.markdown('<div class="card-menu card-menu-dark"><h3>📚 VADEMÉCUM</h3><p>Estudia los perfiles clínicos, cinética, y RAMs antes del turno.</p></div>', unsafe_allow_html=True)
        st.write("")
        if st.button("Abrir Biblioteca", use_container_width=True): ir_a("Vademecum")
    with h2:
        st.markdown('<div class="card-menu card-menu-dark"><h3>📊 VISOR DE DATOS</h3><p>Analiza los Excels crudos de la red MINSAL directamente aquí.</p></div>', unsafe_allow_html=True)
        st.write("")
        if st.button("Cargar Arsenales", use_container_width=True): ir_a("Visor")

# ==========================================
# PÁGINA 2: SIMULADOR DE JUEGO (STYLE PREGUNTADOS)
# ==========================================
elif st.session_state.pagina_actual == "Simulador":
    st.header(f"🎮 Turno: {st.session_state.modo_juego}")
    st.caption(f"Filtro Activo: **{st.session_state.filtro_seleccionado}**")
    st.markdown("---")
    
    if 'preguntas' not in st.session_state:
        if st.session_state.modo_juego == "Por Familia":
            st.session_state.preguntas = [p for p in datos_base if p.get("familia") == st.session_state.filtro_seleccionado]
        elif st.session_state.modo_juego == "Por Categoría":
            st.session_state.preguntas = [p for p in datos_base if p.get("categoria") == st.session_state.filtro_seleccionado]
        else:
            st.session_state.preguntas = datos_base.copy()
            
        if st.session_state.preguntas:
            random.shuffle(st.session_state.preguntas)
            # Shuffle options for each question to avoid predictable patterns
            for p in st.session_state.preguntas:
                random.shuffle(p['opciones'])
        st.session_state.indice = 0
        st.session_state.vidas = 3
        st.session_state.respondido = False

    en_juego = (st.session_state.vidas > 0) or (st.session_state.vidas <= 0 and st.session_state.get('respondido', False))

    if not st.session_state.preguntas:
        st.warning("🚧 No hay preguntas cargadas para este filtro específico.")
    elif en_juego and st.session_state.indice < len(st.session_state.preguntas):
        p_actual = st.session_state.preguntas[st.session_state.indice]
        
        # Ocultar "Variación X: " de la vista del usuario
        texto_pregunta = p_actual['pregunta']
        if "Variación" in texto_pregunta and ":" in texto_pregunta:
            texto_pregunta = texto_pregunta.split(":", 1)[1].strip()
            
        st.markdown(f"<h4 style='text-align: center; color: #7F8C8D;'>🏷️ {p_actual.get('categoria', 'Clínica')} | {p_actual.get('familia', 'N/A')}</h4>", unsafe_allow_html=True)
        
        # TARJETA GIGANTE
        st.markdown(f'<div class="quiz-question">{texto_pregunta}</div>', unsafe_allow_html=True)
        
        opciones = p_actual['opciones']
        
        # Callback para registrar respuesta instantánea
        def procesar_respuesta(opcion_seleccionada):
            st.session_state.respondido = True
            st.session_state.opcion_elegida = opcion_seleccionada
            if opcion_seleccionada == st.session_state.preguntas[st.session_state.indice]['respuesta']:
                st.session_state.es_correcta = True
            else:
                st.session_state.es_correcta = False
                st.session_state.vidas -= 1

        # GRILLA 2x2 DE BOTONES
        if not st.session_state.get('respondido'):
            col1, col2 = st.columns(2)
            with col1:
                st.button(opciones[0], key=f"op0_{st.session_state.indice}", on_click=procesar_respuesta, args=(opciones[0],), use_container_width=True)
                st.write("") # Espaciador
                st.button(opciones[2], key=f"op2_{st.session_state.indice}", on_click=procesar_respuesta, args=(opciones[2],), use_container_width=True)
            with col2:
                st.button(opciones[1], key=f"op1_{st.session_state.indice}", on_click=procesar_respuesta, args=(opciones[1],), use_container_width=True)
                st.write("") # Espaciador
                st.button(opciones[3], key=f"op3_{st.session_state.indice}", on_click=procesar_respuesta, args=(opciones[3],), use_container_width=True)

        # RESOLUCIÓN Y FEEDBACK
        if st.session_state.get('respondido'):
            if st.session_state.es_correcta:
                st.success("🎯 **¡EXCELENTE! Intervención clínica correcta.**")
            else:
                st.error(f"❌ **ERROR CRÍTICO.** Elegiste: *{st.session_state.opcion_elegida}*")
                
            st.info(f"**💡 Resolución QF:** {st.session_state.preguntas[st.session_state.indice]['feedback']}")
            
            texto_boton = "Avanzar al Siguiente Caso ➡️" if st.session_state.vidas > 0 else "Ver Reporte de Fatalidad 💀"
            
            _, col_centro, _ = st.columns([1, 2, 1])
            with col_centro:
                if st.button(texto_boton, use_container_width=True):
                    st.session_state.indice += 1
                    st.session_state.respondido = False
                    st.rerun()
                
    elif st.session_state.get('vidas', 0) <= 0:
        st.error("💥 Has perdido todas tus vidas. Los pacientes se han descompensado.")
    elif st.session_state.get('indice', 0) >= len(st.session_state.preguntas):
        st.balloons()
        st.success("🏆 ¡Turno terminado con éxito! Eres un QF Élite comprobado.")

# ==========================================
# PÁGINA 3: VADEMÉCUM
# ==========================================
elif st.session_state.pagina_actual == "Vademecum":
    st.header("📚 Vademécum Clínico")
    st.markdown("Consulta rápida de perfiles farmacológicos antes del turno.")
    
    if not datos_vademecum:
        st.info("🚧 Base de datos vacía.")
    else:
        filtro_vademecum = st.selectbox("Filtrar Familia:", ["Todas"] + familias)
        v_filtrado = datos_vademecum if filtro_vademecum == "Todas" else [f for f in datos_vademecum if f.get("familia") == filtro_vademecum]
        
        farmaco_sel = st.selectbox("Selecciona Fármaco:", [f["nombre"] for f in v_filtrado])
        ficha = next((f for f in v_filtrado if f["nombre"] == farmaco_sel), None)
        
        if ficha:
            st.markdown(f"## 💊 {ficha['nombre']}")
            st.markdown("---")
            c1, c2 = st.columns(2)
            with c1:
                st.success(f"**⚙️ Mecanismo:**\n\n{ficha['mecanismo']}")
                st.info(f"**🏥 Uso Clínico:**\n\n{ficha['uso']}")
            with c2:
                st.warning(f"**🔄 Cinética:**\n\n{ficha['cinetica']}")
                st.error(f"**⚠️ RAMs e Interacciones:**\n\n{ficha['interacciones']}")

# ==========================================
# PÁGINA 4: VISOR DE DATOS
# ==========================================
elif st.session_state.pagina_actual == "Visor":
    st.header("📊 Explorador de Arsenales (Excels)")
    st.markdown("Sube tus archivos de red pública aquí para analizarlos.")
    archivos_subidos = st.file_uploader("Sube Excels (APS, HCHM):", type=["xls", "xlsx"], accept_multiple_files=True)
    
    if archivos_subidos:
        for archivo in archivos_subidos:
            st.subheader(f"📄 {archivo.name}")
            try:
                xls = pd.ExcelFile(archivo)
                hoja = st.selectbox(f"Selecciona hoja de {archivo.name}:", xls.sheet_names, key=f"hoja_{archivo.name}")
                st.dataframe(pd.read_excel(xls, sheet_name=hoja).head(50))
            except Exception as e:
                st.error(f"Error al leer el Excel: {e}")