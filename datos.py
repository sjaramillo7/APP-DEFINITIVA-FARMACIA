# ==========================================
# BASE DE DATOS - QF ÉLITE RED PÚBLICA
# ==========================================

datos_base = [
    # ==========================================
    # LOTE 1: ENALAPRIL (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: MECANISMO ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: ¿Cuál es el mecanismo de acción exacto del Enalapril y su efecto inmediato en la cascada del SRAA?",
        "opciones": [
            "Es un profármaco que, al hidrolizarse a enalaprilato, inhibe la ECA, frenando el paso de Angiotensina I a Angiotensina II.",
            "Bloquea directamente el receptor AT1 de la Angiotensina II en el músculo liso vascular.",
            "Inhibe la liberación de renina desde el aparato yuxtaglomerular mediante un bloqueo simpático.",
            "Estimula la enzima convertidora de angiotensina 2 (ECA2), aumentando la producción de Angiotensina 1-7 vasodilatadora."
        ],
        "respuesta": "Es un profármaco que, al hidrolizarse a enalaprilato, inhibe la ECA, frenando el paso de Angiotensina I a Angiotensina II.",
        "feedback": "El Enalapril en sí mismo es inactivo. Requiere hidrólisis hepática para convertirse en enalaprilato (su forma activa). Al inhibir la ECA, corta el suministro del principal vasoconstrictor del cuerpo (Ang II), reduciendo la resistencia vascular periférica sin aumentar la frecuencia cardíaca."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: Además de disminuir los niveles de Angiotensina II, la inhibición de la ECA por el Enalapril tiene un efecto secundario clave sobre otro péptido vasoactivo. ¿Cuál es?",
        "opciones": [
            "Inhibe la degradación de bradicinina, promoviendo la vasodilatación mediada por óxido nítrico y prostaciclinas.",
            "Aumenta el metabolismo de la endotelina-1, disminuyendo la vasoconstricción local.",
            "Bloquea la síntesis de péptido natriurético auricular (ANP), reteniendo sodio.",
            "Acelera la destrucción de la sustancia P en el sistema nervioso central."
        ],
        "respuesta": "Inhibe la degradación de bradicinina, promoviendo la vasodilatación mediada por óxido nítrico y prostaciclinas.",
        "feedback": "La enzima ECA (también llamada cininasa II) tiene dos trabajos: crear Ang II y destruir bradicinina. Al inhibirla, la bradicinina se acumula. Esto es positivo para la presión (es un potente vasodilatador), pero es la causa principal de la tos seca y el angioedema."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: ¿Cómo afecta el mecanismo del Enalapril a la homeostasis del potasio?",
        "opciones": [
            "Al disminuir la Angiotensina II, cae la secreción de aldosterona, lo que reduce la excreción de potasio en el túbulo distal.",
            "Aumenta la secreción de potasio en el túbulo proximal por un efecto osmótico directo del enalaprilato.",
            "Activa la bomba Na+/K+ ATPasa en el músculo esquelético, metiendo el potasio a las células.",
            "No tiene impacto en el potasio, solo afecta el balance de sodio y agua."
        ],
        "respuesta": "Al disminuir la Angiotensina II, cae la secreción de aldosterona, lo que reduce la excreción de potasio en el túbulo distal.",
        "feedback": "La Ang II es el estímulo fisiológico para que la glándula suprarrenal secrete aldosterona. Al bloquear la Ang II, la aldosterona cae. Como la aldosterona normalmente bota potasio y retiene sodio, su ausencia provoca que el riñón retenga potasio (riesgo de hiperkalemia)."
    },

    # --- CATEGORÍA: DOSIS ---
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: En la APS dispones de Enalapril en comprimidos de 10mg. ¿Cuál es la conducta clínica recomendada al iniciar este fármaco en un paciente adulto mayor?",
        "opciones": [
            "Iniciar con dosis bajas (ej. 5mg) e ir titulando, vigilando la función renal y la kalemia a las 2-4 semanas.",
            "Iniciar inmediatamente con la dosis máxima de 40mg para evitar el remodelamiento cardíaco temprano.",
            "Administrar siempre junto con un diurético tiazídico para evitar el efecto de primera dosis.",
            "Tomarlo exclusivamente en ayunas, ya que los alimentos reducen su absorción a casi cero."
        ],
        "respuesta": "Iniciar con dosis bajas (ej. 5mg) e ir titulando, vigilando la función renal y la kalemia a las 2-4 semanas.",
        "feedback": "El famoso inicio 'start low, go slow'. En adultos mayores o pacientes deplecionados de volumen, la primera dosis de un IECA puede causar una hipotensión aguda severa. Además, como altera la hemodinámica glomerular, el control de creatinina y potasio es obligatorio."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: ¿Cuál es la justificación farmacocinética de que el Enalapril a menudo se recete cada 12 horas en lugar de una vez al día?",
        "opciones": [
            "La vida media efectiva de acumulación del enalaprilato es de unas 11 horas, por lo que a veces no cubre las 24 horas completas.",
            "El hígado regenera la enzima ECA cada 8 horas, requiriendo dosis múltiples para mantener la inhibición.",
            "Para evitar el riesgo de hepatotoxicidad fulminante asociada a dosis únicas elevadas.",
            "Porque en dosis únicas diarias pierde su efecto nefroprotector y solo mantiene el efecto hipotensor."
        ],
        "respuesta": "La vida media efectiva de acumulación del enalaprilato es de unas 11 horas, por lo que a veces no cubre las 24 horas completas.",
        "feedback": "Aunque en muchos pacientes leves una dosis diaria de 20mg basta, en hipertensos más severos la presión tiende a subir antes de la siguiente dosis (fenómeno de escape). Dividir la dosis en cada 12 horas (ej. 10mg AM y 10mg PM) asegura niveles plasmáticos estables de enalaprilato."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Tienes un paciente hipertenso con Insuficiencia Renal Crónica avanzada (ClCr < 30 mL/min). ¿Qué ajuste posológico requiere el Enalapril?",
        "opciones": [
            "Aumentar el intervalo de dosificación o reducir la dosis, ya que el enalaprilato se excreta principalmente por vía renal.",
            "Aumentar la dosis, ya que la uremia disminuye la absorción gastrointestinal del fármaco.",
            "No requiere ajuste de dosis, ya que se elimina casi por completo a través de la bilis y las heces.",
            "Está absolutamente contraindicado en ClCr < 30 mL/min; debe cambiarse a un ARA II."
        ],
        "respuesta": "Aumentar el intervalo de dosificación o reducir la dosis, ya que el enalaprilato se excreta principalmente por vía renal.",
        "feedback": "El enalaprilato es de eliminación 100% renal. En pacientes con falla renal, el fármaco se acumula peligrosamente, aumentando el riesgo de hipotensión severa e hiperkalemia tóxica. Se debe bajar la dosis inicial (ej. a 2.5mg) y ajustar según tolerancia."
    },

    # --- CATEGORÍA: INTERACCIONES ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: ¿Por qué la combinación de Enalapril con un AINE (como Ibuprofeno) genera un alto riesgo de insuficiencia renal aguda?",
        "opciones": [
            "Porque el AINE vasoconstriñe la arteriola aferente y el Enalapril vasodilata la eferente, colapsando la presión de filtración.",
            "Porque ambos fármacos precipitan cristales insolubles en los túbulos renales.",
            "Porque el Ibuprofeno inhibe las esterasas hepáticas, impidiendo la formación de enalaprilato.",
            "Porque causan una necrosis papilar sinérgica mediada por leucotrienos."
        ],
        "respuesta": "Porque el AINE vasoconstriñe la arteriola aferente y el Enalapril vasodilata la eferente, colapsando la presión de filtración.",
        "feedback": "Interacción hemodinámica crítica. Para filtrar, el riñón necesita presión. Las prostaglandinas mantienen abierta la entrada (aferente) y la Ang II mantiene apretada la salida (eferente). AINE + IECA destruye ambos mecanismos de control: no entra sangre y la poca que entra sale rápido."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente psiquiátrico en tratamiento con Litio inicia Enalapril. ¿Qué riesgo toxicológico ocurre y por qué?",
        "opciones": [
            "Toxicidad por litio: La reducción de aldosterona provoca pérdida de sodio, lo que fuerza al túbulo proximal a reabsorber litio compensatoriamente.",
            "Falla terapéutica del litio: El enalapril induce el aclaramiento renal del litio, bajando sus niveles plasmáticos.",
            "Síndrome serotoninérgico: Ambos fármacos compiten por las enzimas MAO en el sistema nervioso central.",
            "Hemorragia intracraneal: El litio potencia el efecto anticoagulante intrínseco del enalapril."
        ],
        "respuesta": "Toxicidad por litio: La reducción de aldosterona provoca pérdida de sodio, lo que fuerza al túbulo proximal a reabsorber litio compensatoriamente.",
        "feedback": "El riñón confunde el Litio con el Sodio. Al perder sodio por el Enalapril, el riñón entra en estado de conservación y reabsorbe masivamente todo el sodio (y el litio) en el túbulo proximal, elevando los niveles de litio a rangos neurotóxicos."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: ¿Qué combinación de polifarmacia con Enalapril es la causa más frecuente de arritmias letales en el servicio de urgencias?",
        "opciones": [
            "Enalapril + Espironolactona + Suplementos de Potasio.",
            "Enalapril + Amlodipino + Atorvastatina.",
            "Enalapril + Furosemida + Omeprazol.",
            "Enalapril + Ácido Acetilsalicílico + Clopidogrel."
        ],
        "respuesta": "Enalapril + Espironolactona + Suplementos de Potasio.",
        "feedback": "La tormenta perfecta para la Hiperkalemia. El IECA ya retiene potasio. Si le sumas Espironolactona (diurético ahorrador de potasio) y peor aún, suplementos de potasio orales (o sales dietéticas sin sodio), el potasio plasmático se dispara causando bloqueos cardíacos o fibrilación ventricular."
    },

    # --- CATEGORÍA: RAMs ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Paciente de 55 años a las 3 semanas de iniciar Enalapril presenta tos seca nocturna incontrolable sin otros síntomas. ¿Cuál es el manejo correcto?",
        "opciones": [
            "Suspender el Enalapril y cambiar por un ARA II (ej. Losartán), ya que la tos es mediada por bradicinina y no responde a antitusivos.",
            "Mantener el Enalapril y recetar Dextrometorfano, ya que la tos es transitoria y desaparece al mes.",
            "Derivar a neumología por sospecha de fibrosis pulmonar inducida por IECA.",
            "Cambiar a Captopril, ya que al tener un grupo sulfhidrilo no produce este efecto adverso."
        ],
        "respuesta": "Suspender el Enalapril y cambiar por un ARA II (ej. Losartán), ya que la tos es mediada por bradicinina y no responde a antitusivos.",
        "feedback": "La tos por IECAs ocurre en hasta un 20% de los pacientes (más en mujeres). Es mediada por el acúmulo de bradicinina en el tejido pulmonar. No sirve dar jarabes ni antibióticos; la única solución definitiva es rotar a un ARA II que no interfiere con el metabolismo de la bradicinina."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: Durante el embarazo, el uso de Enalapril está contraindicado (Especialmente 2do y 3er trimestre). ¿Qué daño fisiopatológico específico le causa al feto?",
        "opciones": [
            "Causa insuficiencia renal anúrica en el feto, lo que lleva a oligohidramnios y deformaciones craneofaciales.",
            "Cierra prematuramente el ductus arterioso, causando falla cardíaca derecha en el feto.",
            "Inhibe la organogénesis hepática, causando atresia biliar congénita.",
            "Induce hipotiroidismo fetal severo por bloqueo de la peroxidasa tiroidea."
        ],
        "respuesta": "Causa insuficiencia renal anúrica en el feto, lo que lleva a oligohidramnios y deformaciones craneofaciales.",
        "feedback": "El feto depende de la Angiotensina II para mantener la perfusión de sus propios riñones en desarrollo. Al bloquearla, el feto hace falla renal, deja de orinar (oligohidramnios) y la falta de líquido amniótico impide el desarrollo pulmonar y deforma las extremidades."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: Un paciente llega a urgencias con los labios y la lengua severamente hinchados tras 2 meses de uso de Enalapril. ¿Cuál es el diagnóstico y el mecanismo subyacente?",
        "opciones": [
            "Angioedema por acumulación de bradicinina; es una emergencia médica que puede obstruir la vía aérea.",
            "Reacción anafiláctica mediada por IgE; se trata exclusivamente con antihistamínicos.",
            "Síndrome de Cushing inducido; debido al aumento secundario de cortisol.",
            "Estomatitis herpética secundaria a la inmunosupresión generada por el fármaco."
        ],
        "respuesta": "Angioedema por acumulación de bradicinina; es una emergencia médica que puede obstruir la vía aérea.",
        "feedback": "El angioedema (hinchazón rápida de dermis y mucosas) es la RAM más temida de los IECAs. A diferencia de las alergias, NO es mediado por histamina (por eso los antialérgicos no sirven mucho aquí), sino por bradicinina. El paciente debe suspender el fármaco de por vida."
    },

    # --- CATEGORÍA: CASO CLÍNICO ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Paciente hipertenso recién diagnosticado con diabetes tipo 2. ¿Por qué el médico elige Enalapril como primera línea en vez de Amlodipino?",
        "opciones": [
            "Por su potente efecto nefroprotector: al dilatar la arteriola eferente, disminuye la presión intraglomerular, frenando la microalbuminuria.",
            "Porque aumenta la secreción pancreática de insulina mediante la activación de canales de calcio.",
            "Porque el Amlodipino está contraindicado en todos los pacientes diabéticos por riesgo de cetoacidosis.",
            "Porque el Enalapril revierte la resistencia a la insulina a nivel del receptor muscular GLUT4."
        ],
        "respuesta": "Por su potente efecto nefroprotector: al dilatar la arteriola eferente, disminuye la presión intraglomerular, frenando la microalbuminuria.",
        "feedback": "El glomérulo diabético sufre de hiperfiltración (mucha presión adentro). El Enalapril abre la 'puerta de salida' (arteriola eferente), bajando la presión de la cañería. Esto evita que las proteínas (albúmina) se cuelen hacia la orina, protegiendo el riñón a largo plazo."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Llega a urgencias un paciente hipertenso al que se le acaba de diagnosticar Estenosis Bilateral de la Arteria Renal. ¿Por qué está absolutamente contraindicado darle Enalapril?",
        "opciones": [
            "Porque la perfusión de ese riñón depende críticamente de la vasoconstricción eferente por Angiotensina II; si se bloquea, la tasa de filtración cae a cero.",
            "Porque induciría la ruptura espontánea de las placas de ateroma en la arteria renal.",
            "Porque en estenosis bilateral, los IECAs generan hipertensión de rebote fulminante por activación simpática.",
            "Porque el fármaco no podría excretarse, causando toxicidad neurológica aguda."
        ],
        "respuesta": "Porque la perfusión de ese riñón depende críticamente de la vasoconstricción eferente por Angiotensina II; si se bloquea, la tasa de filtración cae a cero.",
        "feedback": "Un riñón con la arteria tapada recibe muy poca sangre. Para seguir filtrando orina, el riñón cierra al máximo su arteriola eferente usando Angiotensina II (hace un 'taco' para subir la presión). Si das Enalapril, quitas ese tapón salvavidas y el riñón deja de funcionar al instante."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Paciente post-Infarto Agudo al Miocardio (IAM). Ya está sin dolor y normotenso. ¿Por qué el cardiólogo de turno decide iniciar Enalapril en dosis bajas antes del alta médica?",
        "opciones": [
            "Para prevenir el remodelamiento cardíaco adverso (dilatación y fibrosis) mediado por la Angiotensina II a largo plazo.",
            "Exclusivamente para evitar arritmias ventriculares inducidas por hipokalemia.",
            "Para disolver el trombo coronario remanente mediante la activación del plasminógeno.",
            "Para aumentar la fuerza de contracción del ventrículo izquierdo a través de un efecto inotrópico positivo."
        ],
        "respuesta": "Para prevenir el remodelamiento cardíaco adverso (dilatación y fibrosis) mediado por la Angiotensina II a largo plazo.",
        "feedback": "Después de un infarto, el corazón intenta cicatrizar, pero la Angiotensina II y la Aldosterona causan una hipertrofia patológica y fibrosis (el corazón se agranda y se pone rígido, llevando a Insuficiencia Cardíaca). El Enalapril frena este remodelamiento."
    },

    # ==========================================
    # LOTE 2: LOSARTÁN (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: MECANISMO ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: ¿Sobre qué receptor específico actúa el Losartán y cuál es la ventaja fisiopatológica de esta selectividad?",
        "opciones": [
            "Antagoniza el receptor AT1 bloqueando la vasoconstricción, pero deja libre el AT2 que promueve vasodilatación.",
            "Antagoniza los receptores AT1 y AT2 por igual, logrando un bloqueo total del sistema renina-angiotensina.",
            "Agoniza el receptor AT2 e inhibe competitivamente a la renina a nivel del aparato yuxtaglomerular.",
            "Bloquea el receptor mineralocorticoide, impidiendo la transcripción genética de canales de sodio."
        ],
        "respuesta": "Antagoniza el receptor AT1 bloqueando la vasoconstricción, pero deja libre el AT2 que promueve vasodilatación.",
        "feedback": "El Losartán es un ARA II altamente selectivo por el receptor AT1 (donde ocurren los efectos dañinos de la Angiotensina II: vasoconstricción, hipertrofia). Al dejar libre el receptor AT2, la Angiotensina II circulante se une a este último, estimulando la liberación de óxido nítrico y bradicinina protectora."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: A diferencia de un IECA (como Enalapril), ¿cuál es el efecto del Losartán sobre los niveles circulantes de bradicinina?",
        "opciones": [
            "No los altera directamente, ya que no inhibe a la enzima convertidora de angiotensina (ECA o cininasa II).",
            "Aumenta la bradicinina al bloquear su degradación en los pulmones.",
            "Disminuye la bradicinina al inducir su metabolismo por enzimas hepáticas.",
            "Sintetiza bradicinina directamente a nivel endotelial."
        ],
        "respuesta": "No los altera directamente, ya que no inhibe a la enzima convertidora de angiotensina (ECA o cininasa II).",
        "feedback": "El Losartán actúa 'aguas abajo' en la cascada. La ECA sigue funcionando normalmente, por lo que la bradicinina se sigue destruyendo a su ritmo habitual. Por esto, los ARA II tienen una incidencia casi nula de tos seca."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: ¿Qué efecto tiene el bloqueo del receptor AT1 por Losartán sobre la secreción de aldosterona?",
        "opciones": [
            "Inhibe la liberación de aldosterona, promoviendo la natriuresis y retención de potasio.",
            "Estimula la liberación de aldosterona por un mecanismo de retroalimentación positiva.",
            "No tiene efecto sobre la aldosterona, solo actúa en el músculo liso vascular.",
            "Aumenta la sensibilidad de la glándula suprarrenal al potasio, secretando más aldosterona."
        ],
        "respuesta": "Inhibe la liberación de aldosterona, promoviendo la natriuresis y retención de potasio.",
        "feedback": "La Angiotensina II necesita unirse al receptor AT1 en la corteza suprarrenal para ordenar la secreción de aldosterona. Al bloquear este receptor con Losartán, cae la aldosterona, lo que ayuda a botar sodio (bajando la PA) pero obliga al riñón a retener potasio."
    },

    # --- CATEGORÍA: DOSIS ---
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: En el arsenal de APS, la presentación principal es Losartán comprimidos de 50mg. ¿Cómo es el perfil metabólico necesario para que esta dosis ejerza su efecto máximo?",
        "opciones": [
            "Sufre un extenso metabolismo de primer paso (CYP2C9 y 3A4) formando el metabolito E-3174, que es 10 a 40 veces más activo que el propio Losartán.",
            "Se absorbe y actúa directamente sin necesidad de metabolismo hepático, siendo seguro en cirrosis severa.",
            "Es un profármaco que se hidroliza exclusivamente en el plasma sanguíneo a través de esterasas.",
            "Su absorción requiere un pH ácido y se inhibe por completo si se administra con alimentos."
        ],
        "respuesta": "Sufre un extenso metabolismo de primer paso (CYP2C9 y 3A4) formando el metabolito E-3174, que es 10 a 40 veces más activo que el propio Losartán.",
        "feedback": "¡Ojo clínico! El 14% del Losartán oral se biotransforma en el hígado. Su metabolito (E-3174) tiene una vida media más larga y es el verdadero responsable del efecto antihipertensivo prolongado. En pacientes con falla hepática grave, este fármaco es errático."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente hipertenso de 45 años sin comorbilidades. ¿Cuál es el límite máximo de dosis diaria de Losartán que suele manejarse antes de considerar la terapia inefectiva y añadir otro fármaco?",
        "opciones": [
            "100 mg al día (generalmente divididos en dos tomas o dosis única).",
            "50 mg al día.",
            "150 mg al día.",
            "200 mg al día."
        ],
        "respuesta": "100 mg al día (generalmente divididos en dos tomas o dosis única).",
        "feedback": "La dosis tope habitual en HTA es 100 mg/día. Si el paciente no controla con esto, subir la dosis a 150 mg no aporta beneficio hipotensor significativo (efecto techo), pero sí eleva el riesgo de RAMs. Es momento de asociar a un calcioantagonista (Amlodipino) o un diurético (HCTZ)."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: ¿Qué ajuste de dosis requiere el Losartán en un paciente con insuficiencia renal crónica (ClCr < 30 mL/min) sin diálisis?",
        "opciones": [
            "Generalmente no requiere ajuste de dosis inicial, pero exige estricto monitoreo de la creatinina y el potasio.",
            "Debe reducirse la dosis a la mitad (25 mg) debido a la acumulación tóxica de su metabolito activo.",
            "Está absolutamente contraindicado, debe cambiarse a Amlodipino.",
            "Debe aumentarse la dosis, ya que la falla renal disminuye la sensibilidad del receptor AT1."
        ],
        "respuesta": "Generalmente no requiere ajuste de dosis inicial, pero exige estricto monitoreo de la creatinina y el potasio.",
        "feedback": "El Losartán se excreta de forma dual (biliar y renal). Aunque la falla renal prolonga un poco la vida media, no obliga a ajustar la dosis de entrada. Sin embargo, como relaja la arteriola eferente y retiene potasio, el control de laboratorio a los 15 días es mandatorio."
    },

    # --- CATEGORÍA: INTERACCIONES ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: ¿Por qué la combinación de Losartán con un AINE (ej. Naproxeno) es una 'Red Flag' de polifarmacia en APS?",
        "opciones": [
            "Interacción hemodinámica renal: El AINE vasoconstriñe la aferente y Losartán vasodilata la eferente, colapsando la tasa de filtración glomerular.",
            "El Naproxeno induce enzimas hepáticas que destruyen al Losartán en horas, generando crisis hipertensivas.",
            "Ambos fármacos compiten por el mismo transportador en el estómago, impidiendo la absorción del Losartán.",
            "Sinergismo tóxico: Ambos deprimen la médula ósea generando agranulocitosis."
        ],
        "respuesta": "Interacción hemodinámica renal: El AINE vasoconstriñe la aferente y Losartán vasodilata la eferente, colapsando la tasa de filtración glomerular.",
        "feedback": "El famoso 'Triple Whammy' (cuando se suma un diurético). El riñón pierde su mecanismo de defensa compensatorio. El AINE le corta el flujo de entrada (bloqueo COX) y el ARA II le abre la llave de salida. Resultado: isquemia glomerular e insuficiencia renal aguda."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente en tratamiento con Losartán 50mg/día. El psiquiatra le receta Litio para trastorno bipolar. ¿Qué precaución farmacocinética crítica debes tener como QF?",
        "opciones": [
            "El Losartán disminuye la excreción renal del litio (al inducir pérdida de sodio, el riñón reabsorbe el litio compensatoriamente), aumentando el riesgo de toxicidad neurológica.",
            "El Losartán acelera el aclaramiento del litio, requiriendo triplicar la dosis del psiquiatra.",
            "No hay interacción porque el litio es de eliminación renal y el Losartán es de metabolismo hepático.",
            "El litio bloquea irreversiblemente los receptores AT1, anulando el efecto del Losartán."
        ],
        "respuesta": "El Losartán disminuye la excreción renal del litio (al inducir pérdida de sodio, el riñón reabsorbe el litio compensatoriamente), aumentando el riesgo de toxicidad neurológica.",
        "feedback": "El riñón no sabe distinguir bien entre el Sodio y el Litio. Al dar un ARA II (cae aldosterona, se bota sodio distal), el túbulo proximal se desespera por el volumen perdido y reabsorbe de todo: agua, sodio, y todo el Litio que pille. Toxicidad asegurada si no se miden niveles plasmáticos de litio."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: ¿Qué ocurre fisiológicamente si se prescribe Losartán junto con Espironolactona en un paciente con insuficiencia cardíaca sin control de laboratorio?",
        "opciones": [
            "Riesgo extremo de hiperkalemia letal, ya que ambos fármacos convergen en inhibir la excreción de potasio mediada por aldosterona.",
            "Riesgo de hiponatremia dilucional aguda por exceso de secreción de hormona antidiurética (ADH).",
            "Duplicidad terapéutica inútil, ya que la espironolactona anula el efecto del Losartán en el miocardio.",
            "Taquicardia ventricular sostenida por alargamiento del intervalo QT dependiente de calcio."
        ],
        "respuesta": "Riesgo extremo de hiperkalemia letal, ya que ambos fármacos convergen en inhibir la excreción de potasio mediada por aldosterona.",
        "feedback": "Losartán baja la producción de aldosterona. Espironolactona bloquea el receptor de la aldosterona que queda. Es un bloqueo dual sobre el potasio. Si el paciente tiene función renal al límite o come muchos alimentos ricos en potasio, puede llegar a un paro cardíaco."
    },

    # --- CATEGORÍA: RAMs ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Una de las contraindicaciones absolutas del Losartán (y todos los ARA II) es durante el embarazo. ¿Qué daño específico causan en el feto durante el segundo y tercer trimestre?",
        "opciones": [
            "Oligohidramnios, falla renal fetal y malformaciones craneofaciales (fetopatía por bloqueo del SRAA).",
            "Cierre prematuro del ductus arterioso, causando hipertensión pulmonar primaria fetal.",
            "Teratogénesis cardíaca temprana (Tetralogía de Fallot).",
            "Agenesia hepática y defectos del tubo neural por depleción de folato."
        ],
        "respuesta": "Oligohidramnios, falla renal fetal y malformaciones craneofaciales (fetopatía por bloqueo del SRAA).",
        "feedback": "El feto necesita su SRAA intacto para mantener el flujo sanguíneo hacia sus propios riñones. Si la madre toma ARA II, el feto hace falla renal, deja de orinar (el líquido amniótico es orina fetal, por ende ocurre oligohidramnios) y la falta de líquido causa compresión y malformaciones."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: Paciente hipertenso debuta con estenosis bilateral de la arteria renal (aterosclerosis severa). ¿Qué RAM devastadora ocurrirá si le inicias Losartán?",
        "opciones": [
            "Insuficiencia renal aguda anúrica irreversible por colapso de la presión de filtración.",
            "Rotura de aneurisma aórtico abdominal por aumento súbito de la presión intraluminal.",
            "Edema agudo de pulmón por retención hidrosalina paradójica.",
            "Infarto agudo al miocardio por robo coronario masivo."
        ],
        "respuesta": "Insuficiencia renal aguda anúrica irreversible por colapso de la presión de filtración.",
        "feedback": "Si las arterias renales están tapadas, la presión de sangre que llega al glomérulo es bajísima. El riñón sobrevive contrayendo a muerte la arteriola eferente (gracias a la Angiotensina II) para hacer un 'taco' y poder filtrar. Si das Losartán, relajas esa arteriola, la presión cae a cero y el riñón se apaga."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: Aunque es raro comparado con los IECAs, los ARA II como el Losartán aún pueden presentar un riesgo mínimo de angioedema. ¿A qué se debe esto si no inhiben la degradación de bradicinina?",
        "opciones": [
            "Puede deberse a un aumento compensatorio de otras cininas vasoactivas o una sensibilidad genética cruzada.",
            "Es causado por la acumulación de sustancia P en el tejido subcutáneo maxilofacial.",
            "Se produce por degranulación directa de mastocitos mediados por el metabolito E-3174.",
            "Es un efecto mediado por la activación excesiva de receptores AT2 en los capilares labiales."
        ],
        "respuesta": "Puede deberse a un aumento compensatorio de otras cininas vasoactivas o una sensibilidad genética cruzada.",
        "feedback": "El angioedema por ARA II ocurre en menos del 0.1% (vs 0.3% en IECAs). Si un paciente hizo angioedema severo (hinchazón de cara/garganta) con Enalapril, el cambio a Losartán exige extrema precaución, ya que existe un pequeño riesgo de reactividad cruzada por mecanismos cinínicos secundarios."
    },

    # --- CATEGORÍA: CASO CLÍNICO ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Paciente diabético tipo 2 con microalbuminuria (++). Está hipertenso y le indican Losartán. Semanas después, su creatinina sube de 1.0 a 1.2 mg/dL. ¿Qué decisión clínica tomas?",
        "opciones": [
            "Es un alza esperada y hemodinámica (hasta un 30% es tolerable). Mantengo el fármaco por su efecto nefroprotector a largo plazo.",
            "Suspendo inmediatamente; el fármaco está destruyendo el parénquima renal (falla intrínseca).",
            "Agrego un AINE para intentar contraer la arteriola aferente y forzar la filtración.",
            "Cambio Losartán por Atenolol, ya que los betabloqueadores son los nefroprotectores de elección en diabetes."
        ],
        "respuesta": "Es un alza esperada y hemodinámica (hasta un 30% es tolerable). Mantengo el fármaco por su efecto nefroprotector a largo plazo.",
        "feedback": "El Losartán baja la presión dentro del glomérulo (relajando la salida). Esto baja las proteínas en la orina (nefroprotección), pero lógicamente baja un poco la velocidad a la que se filtra la sangre, elevando la creatinina un poco al principio. Es un efecto hemodinámico funcional, no daño tisular."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Paciente de 70 años con HTA resistente. Trae receta de APS con: Losartán 100 mg/día + Enalapril 20 mg/día. Según evidencia clínica (Estudio ONTARGET), ¿por qué esta dupla debe evitarse?",
        "opciones": [
            "Porque el bloqueo dual del SRAA no aporta mayor reducción de mortalidad cardiovascular, pero sí aumenta críticamente la falla renal e hiperkalemia.",
            "Porque ambos fármacos compiten por el citocromo CYP3A4, anulándose mutuamente en el plasma.",
            "Porque el Enalapril agota los receptores AT1, dejando al Losartán sin un sitio de acción efectivo.",
            "Porque inducen una hipotensión tan rápida que generan isquemia cerebral isquémica aguda irreversible en todos los pacientes mayores."
        ],
        "respuesta": "Porque el bloqueo dual del SRAA no aporta mayor reducción de mortalidad cardiovascular, pero sí aumenta críticamente la falla renal e hiperkalemia.",
        "feedback": "Regla de oro de la cardiología moderna: NUNCA mezclar IECA + ARA II. Tienes todos los riesgos del bloqueo del sistema (el riñón se queda sin mecanismos de defensa, el potasio sube) sin ningún beneficio clínico extra. O usas uno, o usas el otro."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Llega al mesón un paciente diagnosticado hace poco de gota (ácido úrico elevado) que además es hipertenso. Entre Hidroclorotiazida y Losartán, ¿cuál recomiendas al médico como terapia antihipertensiva ideal y por qué?",
        "opciones": [
            "Losartán, porque es el único ARA II que tiene propiedades uricosúricas (ayuda a excretar ácido úrico) mediante la inhibición del transportador URAT1.",
            "Hidroclorotiazida, porque estimula la secreción de ácido úrico a nivel del túbulo distal.",
            "Ambos están contraindicados en gota, debiendo preferirse un betabloqueador.",
            "Losartán, porque alcaliniza la orina evitando la cristalización del ácido úrico en las articulaciones."
        ],
        "respuesta": "Losartán, porque es el único ARA II que tiene propiedades uricosúricas (ayuda a excretar ácido úrico) mediante la inhibición del transportador URAT1.",
        "feedback": "El Losartán es una joya para el paciente hipertenso con gota. A diferencia de las tiazidas (que causan hiperuricemia y desatan ataques de gota), el Losartán inhibe el transportador URAT1 en el túbulo proximal, promoviendo la botada de ácido úrico en la orina."
    },

    # ==========================================
    # LOTE 3: ÁCIDO ACETILSALICÍLICO (AAS) (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "AINEs",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: ¿Cuál es el mecanismo de acción distintivo del Ácido Acetilsalicílico (AAS) que lo diferencia del resto de los AINEs disponibles en la red APS?",
        "opciones": [
            "Inhibición reversible y competitiva de la enzima COX-1 a nivel gástrico.",
            "Acetilación irreversible del residuo de serina 529 de la COX-1, inactivando la enzima por el resto de la vida útil de la plaqueta.",
            "Bloqueo selectivo de la COX-2 a nivel endotelial, disminuyendo la síntesis de prostaciclina sin afectar el tromboxano.",
            "Inhibición directa de los receptores plaquetarios P2Y12 dependientes de ADP."
        ],
        "respuesta": "Acetilación irreversible del residuo de serina 529 de la COX-1, inactivando la enzima por el resto de la vida útil de la plaqueta.",
        "feedback": "¡Clave clínica! Mientras fármacos como Ibuprofeno o Ketoprofeno se unen a la COX y luego se sueltan (reversible), el AAS le 'pega' un grupo acetilo a la enzima y la destruye para siempre. Como la plaqueta no tiene núcleo, no puede sintetizar nueva COX-1. Su efecto dura de 7 a 10 días (vida de la plaqueta)."
    },
    {
        "familia": "AINEs",
        "categoria": "⚙ Mecanismo",
        "pregunta": "Variación 2: El endotelio vascular también produce prostaglandinas (Prostaciclina/PGI2) que evitan la trombosis. Si el AAS inhibe la COX en todo el cuerpo, ¿por qué logra un efecto neto antitrombótico y no protrombótico?",
        "opciones": [
            "Porque el AAS no tiene afinidad por la COX endotelial, solo actúa en plaquetas.",
            "Porque las células endoteliales tienen núcleo y resintetizan rápidamente nueva enzima COX, recuperando la producción de PGI2, mientras que las plaquetas no pueden resintetizar TxA2.",
            "Porque la PGI2 se sintetiza exclusivamente por la vía de la lipooxigenasa, la cual no es afectada por el AAS.",
            "Porque el AAS estimula directamente la liberación de óxido nítrico endotelial compensatorio."
        ],
        "respuesta": "Porque las células endoteliales tienen núcleo y resintetizan rápidamente nueva enzima COX, recuperando la producción de PGI2, mientras que las plaquetas no pueden resintetizar TxA2.",
        "feedback": "El balance es oro. El AAS 'mata' la COX tanto en plaquetas (que hacen Tromboxano A2, que agrega) como en el endotelio (que hace Prostaciclina, que antiagrega). Pero el endotelio tiene ADN; en horas fabrica nueva COX y vuelve a producir Prostaciclina. La plaqueta, al ser un fragmento celular sin núcleo, queda inutilizada de por vida."
    },
    {
        "familia": "AINEs",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: La farmacocinética del AAS presenta un fenómeno de dosis-dependencia. A dosis antiinflamatorias altas (ej. > 3g al día), ¿qué cambio ocurre en su metabolismo hepático?",
        "opciones": [
            "Sufre inducción enzimática del CYP3A4, aumentando su propio aclaramiento plasmático.",
            "Pasa de una cinética de eliminación de primer orden a una de orden cero (saturación de las vías de conjugación hepática con glicina).",
            "Aumenta su unión a proteínas plasmáticas al 99%, reduciendo la fracción libre activa.",
            "Se inactiva por hidrólisis espontánea en el plasma antes de llegar al hígado."
        ],
        "respuesta": "Pasa de una cinética de eliminación de primer orden a una de orden cero (saturación de las vías de conjugación hepática con glicina).",
        "feedback": "A dosis bajas (100mg), el hígado metaboliza el AAS fácilmente (cinética lineal/primer orden). A dosis altísimas (uso reumatológico antiguo), las enzimas hepáticas se saturan. El cuerpo ya no elimina un porcentaje, sino una cantidad fija por hora (orden cero). Un pequeño aumento de dosis dispara los niveles plasmáticos a rangos tóxicos (salicilismo)."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "AINEs",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: En APS de Ñuble, se dispone de AAS de 100 mg y 500 mg. ¿Por qué la dosis de 100 mg es suficiente para inhibir la agregación plaquetaria sistémica si apenas alcanza a entrar a la circulación general?",
        "opciones": [
            "Porque se absorbe directamente en la mucosa oral sin pasar por el hígado.",
            "Porque acetila las plaquetas en la circulación portal antes de sufrir el intenso metabolismo hepático de primer paso.",
            "Porque a dosis bajas se convierte en un metabolito mil veces más potente en la sangre venosa.",
            "Porque activa al plasminógeno tisular exclusivamente a nivel intestinal."
        ],
        "respuesta": "Porque acetila las plaquetas en la circulación portal antes de sufrir el intenso metabolismo hepático de primer paso.",
        "feedback": "Es una genialidad farmacocinética. Cuando te tomas 100mg de AAS, casi todo se destruye en el hígado (primer paso). PERO, antes de llegar al hígado, pasa por la vena porta. Ahí se encuentra con las plaquetas y las 'acetila' irreversiblemente. Las plaquetas quedan inútiles antes de que el fármaco se degrade."
    },
    {
        "familia": "AINEs",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente cursando Síndrome Coronario Agudo (SCA) en el SAR o SAPU. La guía MINSAL indica administrar de inmediato AAS. ¿Cuál es la dosis de carga y la instrucción de administración obligatoria?",
        "opciones": [
            "100 mg por vía sublingual.",
            "300 a 500 mg tragados enteros con abundante agua.",
            "300 a 500 mg masticados (o triturados) para rápida absorción bucal e intestinal.",
            "500 mg por vía rectal para evitar el metabolismo hepático."
        ],
        "respuesta": "300 a 500 mg masticados (o triturados) para rápida absorción bucal e intestinal.",
        "feedback": "En el infarto, el tiempo es músculo. Si el paciente traga la pastilla entera, tarda horas en disolverse en el estómago y absorberse. Masticarla rompe la matriz del comprimido, permitiendo absorción a través de la mucosa bucal y acelerando drásticamente el Tmax y el efecto antiplaquetario."
    },
    {
        "familia": "AINEs",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Se prescribe AAS 150 mg diarios (off-label) a una embarazada de 14 semanas en su control de CESFAM. ¿Cuál es la indicación clínica respaldada por evidencia para esta posología específica?",
        "opciones": [
            "Profilaxis de preeclampsia en pacientes de alto riesgo (altera el balance tromboxano/prostaciclina placentario).",
            "Manejo del dolor pélvico asociado a contracciones uterinas prematuras.",
            "Prevención de malformaciones del tubo neural como coadyuvante del ácido fólico.",
            "Tratamiento de primera línea para la diabetes gestacional incipiente."
        ],
        "respuesta": "Profilaxis de preeclampsia en pacientes de alto riesgo (altera el balance tromboxano/prostaciclina placentario).",
        "feedback": "En mujeres con factores de riesgo para preeclampsia, el problema es que la placenta produce demasiado Tromboxano (vasoconstrictor) y poca Prostaciclina (vasodilatador). El AAS a dosis bajas (iniciado antes de las 16 semanas) bloquea selectivamente el tromboxano plaquetario/placentario, mejorando la perfusión y bajando el riesgo de preeclampsia severa."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "AINEs",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Un paciente con antecedente de IAM toma AAS 100 mg todos los días al desayuno. Sufre un esguince y el médico le receta Ibuprofeno 400 mg cada 8 horas. ¿Cuál es la interacción farmacodinámica crítica que el QF debe advertir?",
        "opciones": [
            "El Ibuprofeno aumenta drásticamente el riesgo de hemorragia cerebral por sinergismo antiplaquetario.",
            "El Ibuprofeno causa impedimento estérico (bloquea el canal de la COX-1), impidiendo que el AAS acetile la enzima irreversiblemente, anulando su efecto cardioprotector.",
            "Ambos fármacos compiten a nivel renal, generando una cristaluria tóxica.",
            "El AAS induce el metabolismo del Ibuprofeno, haciéndolo ineficaz para el dolor."
        ],
        "respuesta": "El Ibuprofeno causa impedimento estérico (bloquea el canal de la COX-1), impidiendo que el AAS acetile la enzima irreversiblemente, anulando su efecto cardioprotector.",
        "feedback": "Interacción letal a largo plazo. El Ibuprofeno es voluminoso y se mete en el canal de la COX-1 de forma reversible. Si tomas Ibuprofeno antes, cuando llega el AAS no puede entrar a acetilar la enzima. Luego el Ibuprofeno se suelta, la plaqueta vuelve a funcionar, y el paciente puede infartarse. Regla: Tomar AAS al menos 2 horas antes de cualquier AINE."
    },
    {
        "familia": "AINEs",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente adulto mayor hipertenso y depresivo, en tratamiento con AAS 100 mg/día y Sertralina 50 mg/día. Llega al CESFAM por múltiples equimosis (moretones) y sangrado gingival. ¿Cuál es la justificación fisiopatológica de esta interacción?",
        "opciones": [
            "La Sertralina inhibe el CYP2C9, duplicando los niveles plasmáticos de AAS.",
            "Los ISRS agotan la serotonina almacenada en las plaquetas (necesaria para la agregación inicial), generando un sinergismo hemorrágico peligroso con el AAS.",
            "La combinación provoca una trombocitopenia autoinmune fulminante.",
            "El AAS desplaza a la Sertralina de la albúmina, induciendo un síndrome serotoninérgico que daña los capilares."
        ],
        "respuesta": "Los ISRS agotan la serotonina almacenada en las plaquetas (necesaria para la agregación inicial), generando un sinergismo hemorrágico peligroso con el AAS.",
        "feedback": "Las plaquetas no solo usan Tromboxano, también necesitan liberar Serotonina (captada del plasma) para llamar a otras plaquetas. Los ISRS (Sertralina, Fluoxetina) bloquean el transportador SERT, dejando a las plaquetas sin serotonina. Si además bloqueas el tromboxano con AAS, el riesgo de sangrado gastrointestinal se multiplica por 3."
    },
    {
        "familia": "AINEs",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: ¿Por qué está contraindicado administrar dosis bajas de AAS (100 mg) en un paciente con gota no controlada que usa Probenecid o Losartán por su efecto uricosúrico?",
        "opciones": [
            "Porque el AAS bloquea la xantina oxidasa, acumulando precursores tóxicos.",
            "Porque a dosis bajas, el AAS compite con el ácido úrico en los transportadores OAT (túbulo proximal), disminuyendo la secreción de uratos y exacerbando la hiperuricemia.",
            "Porque el AAS disuelve bruscamente los tofos gotosos, causando nefropatía por uratos.",
            "Porque la combinación genera falla hepática fulminante por necrosis centrolobulillar."
        ],
        "respuesta": "Porque a dosis bajas, el AAS compite con el ácido úrico en los transportadores OAT (túbulo proximal), disminuyendo la secreción de uratos y exacerbando la hiperuricemia.",
        "feedback": "Paradoja de dosis del AAS: A dosis muy altas (>3g) bota ácido úrico (uricosúrico). Pero a las dosis bajas que usamos en cardiología (100mg), el AAS y el ácido úrico compiten por la misma puerta de salida en el riñón. El AAS gana, y el ácido úrico se queda en la sangre, precipitando crisis de gota."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "AINEs",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Llega al SAPU un adolescente de 15 años en paro respiratorio por broncoespasmo severo minutos después de tomar AAS 500 mg para la cefalea. Refiere historia de poliposis nasal. ¿Qué mecanismo inmunológico o bioquímico explica la 'Triada de Samter' (o Enfermedad Respiratoria Exacerbada por Aspirina)?",
        "opciones": [
            "Reacción anafiláctica clásica mediada por desgranulación masiva de IgE frente al radical salicilo.",
            "Al bloquear la COX-1, el ácido araquidónico se desvía masivamente hacia la vía de la lipooxigenasa (LOX), generando una sobreproducción explosiva de leucotrienos broncoconstrictores.",
            "Toxicidad directa del AAS sobre los receptores beta-2 adrenérgicos del músculo liso bronquial.",
            "Acidosis metabólica aguda que fuerza una hiperventilación compensatoria, colapsando la vía aérea."
        ],
        "respuesta": "Al bloquear la COX-1, el ácido araquidónico se desvía masivamente hacia la vía de la lipooxigenasa (LOX), generando una sobreproducción explosiva de leucotrienos broncoconstrictores.",
        "feedback": "La intolerancia a la Aspirina (Asma, pólipos nasales y sensibilidad al AAS = Tríada de Samter) NO es una alergia. Es un desvío de tráfico. Tienes Ácido Araquidónico que puede ir por la COX (a hacer prostaglandinas) o por la LOX (a hacer leucotrienos). Al tapar la COX con AAS, todo el ácido se va a la LOX. Los leucotrienos son 1000 veces más broncoconstrictores que la histamina."
    },
    {
        "familia": "AINEs",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: El uso de AAS está formalmente contraindicado en niños y adolescentes (menores de 16 años) que cursan cuadros febriles virales (Influenza, Varicela). ¿Cuál es la RAM letal asociada a esta práctica?",
        "opciones": [
            "Síndrome de Kawasaki (vasculitis de arterias coronarias).",
            "Síndrome de Reye (daño mitocondrial masivo que genera encefalopatía aguda y esteatosis hepática microvesicular).",
            "Aplasia medular irreversible idiopática.",
            "Cierre prematuro de los cartílagos de crecimiento epifisiarios."
        ],
        "respuesta": "Síndrome de Reye (daño mitocondrial masivo que genera encefalopatía aguda y esteatosis hepática microvesicular).",
        "feedback": "Manejo básico de mostrador: NUNCA dar AAS a un niño con fiebre viral (para eso hay Paracetamol). El AAS en presencia de ciertos virus altera la beta-oxidación de grasas en las mitocondrias, causando acumulación de amonio cerebral (encefalopatía rápida, coma) y destrucción hepática. Mortalidad del 30%."
    },
    {
        "familia": "AINEs",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: Paciente psiquiátrico llega al servicio de urgencias por intento de autólisis con 40 comprimidos de AAS 500 mg. Presenta hiperventilación severa, tinnitus (zumbido en oídos) y confusión. ¿Cuál es la alteración ácido-base dual clásica en la intoxicación por salicilatos?",
        "opciones": [
            "Alcalosis metabólica primaria seguida de acidosis respiratoria por fatiga diafragmática.",
            "Acidosis láctica pura por inhibición de la glucólisis anaerobia.",
            "Alcalosis respiratoria primaria (por estimulación directa del centro bulbar) seguida de acidosis metabólica (por acumulación de ácidos orgánicos y salicilatos).",
            "Acidosis hiperclorémica aguda sin anión gap."
        ],
        "respuesta": "Alcalosis respiratoria primaria (por estimulación directa del centro bulbar) seguida de acidosis metabólica (por acumulación de ácidos orgánicos y salicilatos).",
        "feedback": "El salicilismo es un cuadro complejo. Primero, el AAS entra al cerebro y estimula el centro respiratorio: el paciente hiperventila y bota mucho CO2 (Alcalosis Respiratoria). Horas después, el fármaco desacopla la fosforilación oxidativa mitocondrial, el cuerpo empieza a producir ácido láctico y cetonas, sumado a que el propio ácido salicílico es un ácido, cayendo en una Acidosis Metabólica severa (Anión Gap elevado)."
    },

    # --- CATEGORÍA: 🏥 Caso Clínico ---
    {
        "familia": "AINEs",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Paciente de 65 años, sano, sin factores de riesgo cardiovascular evidentes, solicita al QF comprar 'Aspirina infantil' (100 mg) para tomarla diariamente porque vio en la tele que 'previene infartos' (Prevención Primaria). Según las guías clínicas actuales (ej. USPSTF, ACC/AHA), ¿qué conducta debes tomar?",
        "opciones": [
            "Desaconsejar el uso rutinario, ya que en pacientes mayores de 60 años sin enfermedad cardiovascular establecida, el riesgo de sangrado digestivo/intracraneal supera el beneficio de prevenir un primer evento.",
            "Recomendar su uso, pero sugerir que la tome con leche para evitar úlceras.",
            "Recomendar su uso solo si lo asocia a Omeprazol de por vida.",
            "Vender el producto indicando que la dosis de prevención primaria es en realidad 500 mg cada 48 horas."
        ],
        "respuesta": "Desaconsejar el uso rutinario, ya que en pacientes mayores de 60 años sin enfermedad cardiovascular establecida, el riesgo de sangrado digestivo/intracraneal supera el beneficio de prevenir un primer evento.",
        "feedback": "Paradigma cambiado. Hace 10 años, a todo viejo se le daba AAS preventivo. Hoy, múltiples estudios (ASPREE, ARRIVE) demostraron que dar AAS a gente sana mayor de 60 años causa más muertes por hemorragia cerebral o gástrica que los infartos que previene. Solo se justifica en prevención SECUNDARIA (ya tuvo el infarto) o riesgo cardiovascular altísimo comprobado."
    },
    {
        "familia": "AINEs",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Paciente con stent coronario medicado asiste al consultorio dental para una extracción de 2 piezas. El dentista le indica suspender su terapia dual (AAS 100 mg + Clopidogrel 75 mg) por 7 días antes de la cirugía para evitar sangrado. ¿Cuál es el rol del QF en este escenario?",
        "opciones": [
            "Validar la indicación del dentista; el riesgo de hemorragia alveolar post-extracción es inmanejable.",
            "Recomendar bajar la dosis de AAS a 50 mg diarios pero suspender el Clopidogrel.",
            "Intervenir urgentemente con el cardiólogo: suspender la terapia antiagregante en paciente con stent reciente tiene un riesgo altísimo de trombosis aguda del stent e IAM fulminante. Las extracciones menores no requieren suspensión.",
            "Sugerir rotar el AAS por Paracetamol 1g, manteniendo el efecto antitrombótico intacto."
        ],
        "respuesta": "Intervenir urgentemente con el cardiólogo: suspender la terapia antiagregante en paciente con stent reciente tiene un riesgo altísimo de trombosis aguda del stent e IAM fulminante. Las extracciones menores no requieren suspensión.",
        "feedback": "Error fatal recurrente. Un stent coronario (malla de metal en el corazón) es altamente trombogénico los primeros meses. Si quitas la Aspirina/Clopidogrel, la sangre coagula sobre el metal, tapa la arteria y el paciente muere de un IAM fulminante. Para una simple extracción dental, es preferible usar medidas hemostáticas locales (ácido tranexámico tópico, sutura) que arriesgar el corazón."
    },
    {
        "familia": "AINEs",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Paciente cursando cuadro de gota aguda e hipertenso, tiene dolor articular EVA 9/10 en el dedo del pie. Según el arsenal disponible en la farmacia comunitaria, ¿por qué NO debes recomendar el AAS 500 mg para el manejo de la inflamación gotosa?",
        "opciones": [
            "Porque el AAS destruye los cristales de ácido úrico muy rápido, generando émbolos de uratos que pueden tapar las arterias pulmonares.",
            "Porque a dosis analgésicas el AAS inhibe la excreción tubular de ácido úrico, exacerbando la hiperuricemia y prolongando el ataque de gota.",
            "Porque el AAS interactúa letalmente con el líquido sinovial inflamado, causando artritis séptica.",
            "Porque los pacientes con gota carecen genéticamente de la enzima COX-1."
        ],
        "respuesta": "Porque a dosis analgésicas el AAS inhibe la excreción tubular de ácido úrico, exacerbando la hiperuricemia y prolongando el ataque de gota.",
        "feedback": "Regla clínica básica: AAS y Gota son enemigos. El AAS altera el transporte renal de aniones orgánicos. Dosis bajas y medias (hasta 2 gramos) bloquean la secreción tubular de ácido úrico. El paciente tomará AAS, quizás le quite un poco el dolor inicial, pero el ácido úrico en sangre subirá, empeorando el cuadro subyacente de forma severa. Aquí se prefiere Indometacina, Naproxeno o Colchicina."
    },

    # ==========================================
    # LOTE 4: VANCOMICINA (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "Antimicrobianos",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: En un paciente crítico en la UCI del HCHM con bacteriemia por SAMR, ¿cuál es el mecanismo de acción específico de la Vancomicina a nivel molecular?",
        "opciones": [
            "Se une a las PBP (Penicillin-Binding Proteins) inactivando la transpeptidación de la pared celular.",
            "Se une irreversiblemente a la subunidad ribosomal 50S, bloqueando la translocación peptídica.",
            "Inhibe la ADN girasa bacteriana, impidiendo el superenrollamiento del ADN.",
            "Se une con alta afinidad a los residuos terminales D-alanil-D-alanina de los precursores del peptidoglicano, bloqueando estéricamente la transglicosilación."
        ],
        "respuesta": "Se une con alta afinidad a los residuos terminales D-alanil-D-alanina de los precursores del peptidoglicano, bloqueando estéricamente la transglicosilación.",
        "feedback": "Fisiopatología pura. A diferencia de los betalactámicos que actúan sobre la enzima (PBP), la Vancomicina actúa sobre el 'ladrillo' de construcción. Al pegarse a la cola D-Ala-D-Ala, hace un bloqueo estérico gigante que impide que las enzimas bacterianas puedan cruzar los polímeros para formar la pared celular, causando lisis."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: El índice Farmacocinético/Farmacodinámico (PK/PD) es vital en infectología. Para asegurar la eficacia bactericida de la Vancomicina frente a SAMR, ¿qué parámetro se debe maximizar según las guías clínicas actuales?",
        "opciones": [
            "Tiempo sobre la CIM (T > CIM) mayor al 40% del intervalo posológico.",
            "Relación Área Bajo la Curva / Concentración Inhibitoria Mínima (AUC/CIM) ≥ 400.",
            "Concentración máxima (Cmax / CIM) > 10.",
            "Concentración en el valle (Cmin) absolutamente por sobre 25 mcg/mL en todos los casos."
        ],
        "respuesta": "Relación Área Bajo la Curva / Concentración Inhibitoria Mínima (AUC/CIM) ≥ 400.",
        "feedback": "¡Cambio de paradigma en los últimos años! Ya no nos guiamos solo por el 'valle' (trough). La Vancomicina es de eficacia dependiente de la exposición total. El objetivo de oro para curar infecciones invasivas por SAMR y minimizar la nefrotoxicidad es lograr un AUC24/CIM entre 400 y 600."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: Tienes un urocultivo que aísla Enterococcus faecium Resistente a Vancomicina (ERV). ¿Qué modificación genética hizo esta bacteria para anular el mecanismo de acción de tu fármaco?",
        "opciones": [
            "Producción de betalactamasas de espectro extendido (BLEE) que hidrolizan la molécula.",
            "Mutación del gen mecA que altera el sitio de unión en las PBP2a.",
            "Alteración del precursor de la pared celular: cambia la terminación D-Ala-D-Ala por D-Ala-D-Lactato (genes VanA o VanB).",
            "Sobreexpresión de bombas de eflujo inespecíficas tipo MexAB-OprM."
        ],
        "respuesta": "Alteración del precursor de la pared celular: cambia la terminación D-Ala-D-Ala por D-Ala-D-Lactato (genes VanA o VanB).",
        "feedback": "Inteligencia bacteriana brígida. Como la Vancomicina está diseñada para pegarse exclusivamente a la secuencia D-Alanina-D-Alanina, el Enterococo (gracias al plásmido VanA) cambia el último eslabón por D-Lactato. La Vancomicina pierde toda su afinidad de unión y la bacteria sigue construyendo su pared como si nada."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "Antimicrobianos",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: Ingresa a Urgencias un paciente en shock séptico con foco pulmonar severo, obeso (120 kg, IMC 35). ¿Cómo calculas la dosis de carga inicial de Vancomicina para asegurar niveles terapéuticos rápidos?",
        "opciones": [
            "25 a 30 mg/kg utilizando el Peso Corporal Ideal (PCI) para evitar toxicidad.",
            "15 mg/kg utilizando el Peso Ajustado.",
            "20 a 30 mg/kg utilizando el Peso Corporal Real (Actual), con un tope habitual de 3000 mg.",
            "No se utiliza dosis de carga en pacientes obesos debido a la acumulación en el tejido adiposo."
        ],
        "respuesta": "20 a 30 mg/kg utilizando el Peso Corporal Real (Actual), con un tope habitual de 3000 mg.",
        "feedback": "Manejo crítico de Vd (Volumen de Distribución). La dosis de carga siempre se calcula con el PESO REAL, incluso en obesos, porque la Vancomicina es un fármaco hidrofílico que también penetra en el aumento de líquido extracelular y volumen sanguíneo del obeso. Usar el peso ideal dejaría al paciente subdosificado en pleno shock séptico."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: El médico de la UTI te pide calcular la pauta de mantención para un paciente anciano con ClCr de 25 mL/min. Sabiendo la cinética del fármaco, ¿qué parámetro se debe modificar prioritariamente respecto a una pauta normal?",
        "opciones": [
            "Aumentar significativamente la dosis por ampolla para compensar la pobre llegada al riñón.",
            "Aumentar el intervalo de dosificación (ej. cada 24 o 48 hrs) debido a la prolongación extrema de su vida media plasmática.",
            "Cambiar la vía de administración a infusión continua obligatoriamente.",
            "Mantener la pauta cada 12 hrs pero asociarla a Furosemida para forzar su excreción."
        ],
        "respuesta": "Aumentar el intervalo de dosificación (ej. cada 24 o 48 hrs) debido a la prolongación extrema de su vida media plasmática.",
        "feedback": "La depuración de Vancomicina es >90% por filtración glomerular renal sin metabolismo hepático previo. En falla renal (ClCr bajo), el fármaco no sale del cuerpo y su vida media puede pasar de 6 a más de 100 horas. Si das la dosis cada 12 horas, lo intoxicas. Se debe espaciar el intervalo."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Para monitorizar la terapia (TDM), se solicita un nivel de 'Valle' (Cmin) de Vancomicina plasmática. ¿En qué momento exacto debe la enfermera extraer la muestra de sangre para que el valor sea clínicamente interpretable?",
        "opciones": [
            "A las 2 horas de finalizada la primera infusión (fase de distribución).",
            "Justo en el punto medio del intervalo (ej. a las 6 horas si la pauta es cada 12 hrs).",
            "No más de 30 minutos ANTES de la administración de la 4ta o 5ta dosis, para asegurar el Estado Estacionario (Steady State).",
            "Inmediatamente después de terminar la dosis de carga."
        ],
        "respuesta": "No más de 30 minutos ANTES de la administración de la 4ta o 5ta dosis, para asegurar el Estado Estacionario (Steady State).",
        "feedback": "Concepto clave de farmacocinética clínica. Tomar niveles antes de la 3ra o 4ta dosis no sirve porque el fármaco aún está acumulándose. El Steady State se alcanza recién a las 4 vidas medias. El 'valle' refleja la concentración más baja del fármaco en el cuerpo, por lo que debe medirse justo antes de que caiga la siguiente gota de la nueva dosis."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "Antimicrobianos",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Una práctica común en la UCI es la cobertura empírica amplia combinando Vancomicina con Piperacilina/Tazobactam. ¿Cuál es el riesgo farmacodinámico principal de esta dupla que requiere monitoreo estricto?",
        "opciones": [
            "Antagonismo antibacteriano a nivel de las PBP, anulando el efecto de la Vancomicina.",
            "Sinergismo tóxico que multiplica exponencialmente el riesgo de Injuria Renal Aguda (AKIN/LRA).",
            "Interacción del citocromo CYP3A4, disminuyendo los niveles plasmáticos de Tazobactam.",
            "Inducción de arritmias ventriculares letales por prolongación del segmento QT."
        ],
        "respuesta": "Sinergismo tóxico que multiplica exponencialmente el riesgo de Injuria Renal Aguda (AKIN/LRA).",
        "feedback": "Red flag hospitalaria absoluta. Múltiples estudios han demostrado que juntar Vanco + Pip/Tazo aumenta la nefrotoxicidad aguda de un 5% (Vanco sola) a un 25-30% cuando están juntas. Si se prescribe esta dupla, la monitorización diaria de creatinina sérica y diuresis es obligatoria."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Durante el paso de visita, notas que el paciente recibe Vancomicina en Y junto con Cefepime a través del mismo lumen del catéter venoso central. ¿Qué recomendación farmacéutica inmediata debes hacer?",
        "opciones": [
            "Ninguna, ambas moléculas son hidrofílicas y sinérgicas, mejorando la penetración tisular.",
            "Solicitar la administración por lúmenes separados o lavar exhaustivamente la vía, ya que presentan incompatibilidad física y riesgo de precipitación en la vía venosa.",
            "Aumentar la velocidad de infusión para que se mezclen por menos tiempo en la tubería.",
            "Rotar el Cefepime a Ceftriaxona para mantener la estabilidad de la mezcla."
        ],
        "respuesta": "Solicitar la administración por lúmenes separados o lavar exhaustivamente la vía, ya que presentan incompatibilidad física y riesgo de precipitación en la vía venosa.",
        "feedback": "Problema clásico de enfermería que el QF debe detectar. La Vancomicina es muy ácida (pH ~3-5). Al mezclarse en la vía Y (Y-site) con betalactámicos como Cefepime (o drogas alcalinas), ocurre un cambio brusco de pH y precipita (formando 'nubes' o cristales blancos en la vía), bloqueando el catéter y perdiendo eficacia."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: Paciente en ventilación mecánica recibe infusión continua de un bloqueador neuromuscular (Vecuronio) y se le inicia Vancomicina empírica de alto goteo. ¿Qué interacción clínica puede ocurrir?",
        "opciones": [
            "La Vancomicina induce un bloqueo neuromuscular profundo y prolongado, dificultando el destete del ventilador.",
            "La Vancomicina inactiva al Vecuronio, causando que el paciente despierte y compita con el ventilador.",
            "La combinación genera hipertermia maligna mediada por calcio intracelular.",
            "Ocurre una reacción cruzada que precipita ambos fármacos en el alvéolo pulmonar."
        ],
        "respuesta": "La Vancomicina induce un bloqueo neuromuscular profundo y prolongado, dificultando el destete del ventilador.",
        "feedback": "Al igual que los aminoglucósidos, la Vancomicina a altas dosis tiene una actividad secundaria inhibidora sobre la liberación de acetilcolina en la placa motora. Esto potencia y alarga los efectos de los bloqueadores neuromusculares no despolarizantes, retrasando la extubación del paciente crítico si no se ajusta la sedación."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "Antimicrobianos",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Inician primera dosis de Vancomicina de 1 gramo a pasar en 20 minutos. A los 15 minutos, el paciente cursa con eritema masivo en cara, cuello y torso superior, prurito intenso e hipotensión severa. ¿Cuál es la fisiopatología del cuadro y la conducta QF adecuada?",
        "opciones": [
            "Es un shock anafiláctico mediado por IgE (alergia real). Suspender de por vida y registrar RAM.",
            "Es el 'Síndrome de Hombre Rojo', causado por degranulación directa de mastocitos e histamina por infusión rápida. Se debe detener, dar antihistamínicos y reiniciar la infusión más lento (mínimo 60-120 min).",
            "Toxicidad directa miocárdica por la rápida acumulación. Administrar adrenalina intracardíaca.",
            "Cristalización aguda en capilares dérmicos. Hidratar con suero salino al 0.9%."
        ],
        "respuesta": "Es el 'Síndrome de Hombre Rojo', causado por degranulación directa de mastocitos e histamina por infusión rápida. Se debe detener, dar antihistamínicos y reiniciar la infusión más lento (mínimo 60-120 min).",
        "feedback": "Fallo garrafal de administración. La Vancomicina NO debe pasarse rápido (regla QF: nunca más de 10-15 mg/min). Si entra de golpe, revienta los mastocitos liberando histamina masivamente. Parece anafilaxia, pero NO es alergia. Se maneja cortando la bomba, dando Clorfenamina y reiniciando a la mitad de la velocidad."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: Paciente con neumonía por SAMR recibe terapia con niveles valle persistentemente elevados (35 mcg/mL). Comienza con sedimento urinario activo (cilindros granulosos marrones) y alza de creatinina. ¿Qué patrón de daño renal genera la Vancomicina?",
        "opciones": [
            "Nefritis intersticial aguda alérgica, dependiente de inmunidad celular.",
            "Necrosis tubular aguda (NTA) por estrés oxidativo y acumulación directa del fármaco en las células del túbulo proximal.",
            "Glomerulonefritis post-infecciosa secundaria a complejos inmunes circulantes.",
            "Cristaluria obstructiva a nivel de la pelvis renal."
        ],
        "respuesta": "Necrosis tubular aguda (NTA) por estrés oxidativo y acumulación directa del fármaco en las células del túbulo proximal.",
        "feedback": "La nefrotoxicidad por Vancomicina es dosis/valle dependiente. El fármaco se filtra y al pasar por el túbulo proximal, entra a las células epiteliales causando un caos oxidativo mitocondrial, llevando a Necrosis Tubular Aguda. Por eso vemos cilindros granulosos ('muddy brown casts') en la orina."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚠️️ RAMs",
        "pregunta": "Variación 3: Aunque es menos común que con la Amikacina, el uso crónico o con valles excesivamente altos de Vancomicina puede causar una RAM neurológica irreversible. ¿De qué toxidad estamos hablando?",
        "opciones": [
            "Ototoxicidad, caracterizada por tinnitus y pérdida de la audición neurosensorial de altas frecuencias (daño al octavo par craneal).",
            "Neuropatía periférica severa (síndrome de guante y calcetín).",
            "Mielopatía transversa aguda inflamatoria.",
            "Encefalopatía espongiforme subaguda."
        ],
        "respuesta": "Ototoxicidad, caracterizada por tinnitus y pérdida de la audición neurosensorial de altas frecuencias (daño al octavo par craneal).",
        "feedback": "El octavo par craneal (nervio vestibulococlear) es frágil frente a ciertos antibióticos (Aminoglucósidos y Vancomicina). Aunque con Vanco la ototoxicidad es rara en monoterapia, si los niveles valle están altísimos (>30-40) por tiempo prolongado o se suma otro nefrotóxico/ototóxico, el daño a las células ciliadas del oído interno es inminente y muchas veces permanente."
    },

    # --- CATEGORÍA: CASO CLÍNICO ---
    {
        "familia": "Antimicrobianos",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Paciente politraumatizado joven en la UTI (22 años, sano previo). Está séptico. Su clearance de creatinina (ClCr) calculado por CKD-EPI está en 160 mL/min (Aclaramiento Renal Aumentado - ARC). A pesar de recibir Vancomicina 1g cada 12 hrs, los niveles valle son indetectables (<5 mcg/mL). ¿Qué decisión tomas?",
        "opciones": [
            "Considerar falla hepática oculta y cambiar a Daptomicina.",
            "Mantener la dosis, ya que en ARC el fármaco es indetectable en plasma pero se concentra masivamente en el sitio de infección.",
            "Aumentar drásticamente la dosis y frecuencia (ej. cada 8 hrs) o cambiar a una infusión continua, porque el riñón hiperactivo está 'barriendo' el fármaco.",
            "Suspender porque la bacteria ha desarrollado resistencia enzimática que destruye la droga en el plasma."
        ],
        "respuesta": "Aumentar drásticamente la dosis y frecuencia (ej. cada 8 hrs) o cambiar a una infusión continua, porque el riñón hiperactivo está 'barriendo' el fármaco.",
        "feedback": "El ARC (Augmented Renal Clearance) es el terror de los intensivistas en pacientes jóvenes, quemados o traumatizados. El riñón funciona 'al 150%' y filtra la Vancomicina más rápido de lo que entra. La única forma de alcanzar la meta de AUC >400 es achicar el intervalo (cada 8 o 6 hrs) o poner el antibiótico en bomba de infusión continua."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Paciente con endocarditis por SAMR en terapia con Vancomicina. El laboratorio reporta la CIM (Concentración Inhibitoria Mínima) de la cepa para Vancomicina en 2.0 mcg/mL. Sabiendo que la meta es un AUC/CIM > 400, ¿cuál es tu recomendación de infectología?",
        "opciones": [
            "Aumentar la dosis de Vancomicina a 4 gramos diarios para superar la barrera metabólica.",
            "Mantener el tratamiento normal, ya que 2.0 está dentro del rango sensible (S) según CLSI.",
            "Rotar a terapia alternativa (ej. Daptomicina o Linezolid), porque alcanzar un AUC de 800 (para superar la meta) requiere dosis tóxicas de Vancomicina.",
            "Asociar Rifampicina para sensibilizar al microorganismo y bajar la CIM a 1.0."
        ],
        "respuesta": "Rotar a terapia alternativa (ej. Daptomicina o Linezolid), porque alcanzar un AUC de 800 (para superar la meta) requiere dosis tóxicas de Vancomicina.",
        "feedback": "Matemática farmacológica pura. Si el objetivo es AUC/CIM = 400, y la CIM es 1, necesitas un AUC de 400. Pero si la CIM sube a 2, necesitas forzar el AUC de la Vancomicina a 800 para que funcione. Un AUC de 800 destruirá los riñones del paciente. La recomendación mundial frente a CIM = 2 (fenómeno MIC creep) es buscar alternativas."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Médica tratante te consulta: Tiene un paciente con diarrea grave por Clostridioides difficile. Le prescribió Vancomicina 125mg vía oral cada 6 horas. A las 48 horas, te pide medir 'niveles plasmáticos' de Vancomicina para ver si está absorbiendo bien. ¿Qué le contestas como QF?",
        "opciones": [
            "Que la solicitud es correcta y la muestra debe tomarse inmediatamente en el próximo valle.",
            "Que no es necesario, porque la Vancomicina vía oral NO se absorbe a nivel intestinal y su efecto es puramente local (tópico) en el lumen del colon; los niveles plasmáticos serán cero.",
            "Que la dosis es insuficiente, y se debe medir el nivel en las heces, no en el plasma.",
            "Que es mejor administrarla vía endovenosa para erradicar el C. difficile desde la submucosa."
        ],
        "respuesta": "Que no es necesario, porque la Vancomicina vía oral NO se absorbe a nivel intestinal y su efecto es puramente local (tópico) en el lumen del colon; los niveles plasmáticos serán cero.",
        "feedback": "Error de concepto médico frecuente. La Vancomicina es una molécula gigantesca y súper hidrofílica, por lo que su biodisponibilidad oral es 0%. Solo se usa por boca para barrer al C. difficile que está literalmente en la luz del colon, actuando como un 'jabón'. Darla por vena no sirve para esta infección intestinal, y pedir niveles en sangre tras darla oral no tiene lógica."
    },
# ==========================================
    # LOTE 5: METFORMINA (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "Endocrinología",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: A nivel hepático, la Metformina inhibe una enzima mitocondrial clave (mGPD), lo que altera el estado redox de la célula. ¿Cuál es el impacto final de esta inhibición sobre el metabolismo de la glucosa?",
        "opciones": [
            "Estimula la glucogenólisis, liberando reservas de glucógeno para evitar hipoglicemias nocturnas.",
            "Impide la conversión de lactato y glicerol en glucosa, bloqueando potentemente la gluconeogénesis hepática.",
            "Aumenta la actividad de la enzima DPP-4, prolongando la vida media de las incretinas endógenas.",
            "Bloquea la entrada de fructosa a la vía glucolítica mediante la inhibición de la fosfofructocinasa-1 (PFK-1)."
        ],
        "respuesta": "Impide la conversión de lactato y glicerol en glucosa, bloqueando potentemente la gluconeogénesis hepática.",
        "feedback": "Fisiología pura, loco. El hígado de un diabético produce glucosa de forma descontrolada a partir de precursores como el lactato (ciclo de Cori). La Metformina entra a la mitocondria, bloquea la glicerofosfato deshidrogenasa (mGPD) y corta de raíz esta fábrica de glucosa. Por eso baja la glicemia de ayuno."
    },
    {
        "familia": "Endocrinología",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: ¿Por qué la Metformina en monoterapia NO produce hipoglicemia en el paciente con DM2, a diferencia de medicamentos como la Glibenclamida (Sulfonilureas)?",
        "opciones": [
            "Porque la Metformina es un eu-glicemiante que no estimula la secreción directa de insulina desde las células beta pancreáticas.",
            "Porque su vida media es extremadamente corta y no alcanza a suprimir el glucagón circulante.",
            "Porque activa simultáneamente los receptores alfa-2 adrenérgicos, liberando catecolaminas compensatorias.",
            "Porque se inactiva rápidamente si la glicemia plasmática cae por debajo de 70 mg/dL."
        ],
        "respuesta": "Porque la Metformina es un eu-glicemiante que no estimula la secreción directa de insulina desde las células beta pancreáticas.",
        "feedback": "La Metformina es segura porque es un 'sensibilizador'. Abre las puertas de la célula (GLUT4) y le dice al hígado que deje de fabricar azúcar, pero NUNCA obliga al páncreas a exprimir insulina a la fuerza. Sin ese peak artificial de insulina, es casi imposible que el paciente haga una hipoglicemia severa."
    },
    {
        "familia": "Endocrinología",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: La Metformina también ejerce su acción farmacológica mediante la activación intracelular de la AMPK. ¿Qué efecto metabólico sistémico resulta de la activación persistente de esta cinasa?",
        "opciones": [
            "Cambia el metabolismo hacia la lipogénesis, provocando aumento de peso sostenido.",
            "Induce un estado de 'falsa inanición' celular, promoviendo la oxidación de ácidos grasos y la captación muscular de glucosa.",
            "Estimula la hiperplasia de islotes pancreáticos, revirtiendo el daño celular de la DM2.",
            "Inhibe los transportadores SGLT2 en el túbulo proximal renal, induciendo glucosuria."
        ],
        "respuesta": "Induce un estado de 'falsa inanición' celular, promoviendo la oxidación de ácidos grasos y la captación muscular de glucosa.",
        "feedback": "La AMPK es el 'sensor de energía' de la célula. Cuando se activa (por ejercicio o Metformina), la célula cree que se quedó sin energía (alto nivel de AMP). En respuesta, apaga procesos que gastan energía (como crear grasa o colesterol) y enciende procesos que la generan (quemar ácidos grasos y chupar glucosa de la sangre)."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "Endocrinología",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: Paciente de 68 años con DM2 presenta una Tasa de Filtración Glomerular (CKD-EPI) de 40 mL/min/1.73m2. Estaba en tratamiento con Metformina 850 mg cada 12 horas. ¿Qué ajuste posológico es obligatorio según la evidencia clínica y MINSAL?",
        "opciones": [
            "Mantener la dosis; la Metformina solo requiere ajuste si la VFG cae por debajo de 15 mL/min (Etapa 5).",
            "Suspender inmediatamente y rotar a Insulina, ya que la Metformina es altamente nefrotóxica.",
            "Reducir la dosis a un máximo de 1000 mg diarios y monitorizar la función renal cada 3-6 meses.",
            "Cambiar a una presentación de liberación prolongada (XR) para evitar el paso por la vasculatura renal."
        ],
        "respuesta": "Reducir la dosis a un máximo de 1000 mg diarios y monitorizar la función renal cada 3-6 meses.",
        "feedback": "Regla clínica inquebrantable: VFG > 45 (dosis plena, máximo 2000-2500 mg/día). VFG entre 30 y 45 (bajar la dosis a la mitad, máximo 1000 mg/día). VFG < 30 (SUSPENSIÓN ABSOLUTA). El paciente está en 40, no se suspende, se ajusta para evitar que la droga se acumule y genere acidosis láctica."
    },
    {
        "familia": "Endocrinología",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente debuta con DM2 y se le inicia Metformina 850 mg/día en el CESFAM. A los 3 días vuelve quejándose de diarrea acuosa explosiva y náuseas. Sabiendo que esto es dosis-dependiente, ¿cuál debió ser el enfoque de dosificación inicial por parte del médico/QF?",
        "opciones": [
            "Titulación ('Start low, go slow'): Iniciar con 500 mg una vez al día con la comida principal, y subir gradualmente cada 1-2 semanas.",
            "Carga rápida: Dar 2000 mg el primer día para saturar los receptores gástricos y luego bajar a 850 mg.",
            "Asociar obligatoriamente Loperamida al inicio del tratamiento para bloquear la motilidad alterada.",
            "Administrar la pastilla exclusivamente en ayunas estrictas para evitar el contacto con el quimo alimentario."
        ],
        "respuesta": "Titulación ('Start low, go slow'): Iniciar con 500 mg una vez al día con la comida principal, y subir gradualmente cada 1-2 semanas.",
        "feedback": "El abandono del tratamiento por RAMs gastrointestinales es altísimo (hasta 30%). La Metformina irrita la mucosa, altera las sales biliares y cambia el microbioma. Para evitarlo, siempre se inicia a dosis bajas y NUNCA con el estómago vacío. Se toma durante o justo después de las comidas."
    },
    {
        "familia": "Endocrinología",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Desde el punto de vista farmacocinético, ¿qué porcentaje de la dosis oral de Metformina sufre metabolismo de primer paso o biotransformación en el hígado mediante el sistema CYP450?",
        "opciones": [
            "Alrededor del 90%, convirtiéndose en metabolitos inactivos.",
            "Aproximadamente 50%, sujeto a polimorfismos del CYP2C9.",
            "0%. La Metformina no se une a proteínas plasmáticas y no sufre metabolismo hepático; se excreta totalmente inalterada por la orina.",
            "100%. Es un profármaco que requiere activación hepática para funcionar celularmente."
        ],
        "respuesta": "0%. La Metformina no se une a proteínas plasmáticas y no sufre metabolismo hepático; se excreta totalmente inalterada por la orina.",
        "feedback": "La Metformina es una molécula súper particular. Es hidrofílica, no se une a la albúmina, ignora al hígado (no usa citocromos) y sale por la orina exactamente igual que como entró por la boca. Por eso las interacciones hepáticas son nulas, pero el estado del riñón lo es todo."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "Endocrinología",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Paciente en tratamiento crónico con Metformina acude al hospital para una Tomografía Computarizada (TAC) con medio de contraste yodado endovenoso. ¿Cuál es el protocolo de seguridad obligatorio que debes verificar?",
        "opciones": [
            "Aumentar la dosis de Metformina al doble porque el contraste eleva transitoriamente la glicemia basal.",
            "Suspender la Metformina al momento del procedimiento y reiniciarla a las 48 hrs, solo tras comprobar que la función renal no se deterioró.",
            "Administrar N-acetilcisteína oral para quelar el yodo y evitar que la Metformina precipite en la sangre.",
            "Ninguna, no existe interacción farmacocinética entre compuestos yodados y biguanidas."
        ],
        "respuesta": "Suspender la Metformina al momento del procedimiento y reiniciarla a las 48 hrs, solo tras comprobar que la función renal no se deterioró.",
        "feedback": "Protocolo crítico. El contraste yodado NO interactúa directamente con la Metformina. El problema es que el contraste es nefrotóxico y puede causar Insuficiencia Renal Aguda. Si el riñón falla y el paciente sigue tomando Metformina, esta no se excreta, se acumula a niveles tóxicos y desencadena una acidosis láctica letal."
    },
    {
        "familia": "Endocrinología",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Fármacos como la Cimetidina o el Dolutegravir (antirretroviral) pueden aumentar los niveles plasmáticos de Metformina hasta en un 40% aumentando el riesgo de toxicidad. ¿Cuál es el mecanismo de esta interacción?",
        "opciones": [
            "Inhiben competitivamente los transportadores de cationes orgánicos (OCT2) y MATE1 en el túbulo renal proximal, disminuyendo la secreción tubular de Metformina.",
            "Compiten por los sitios de unión a proteínas plasmáticas, desplazando a la Metformina a su fracción libre.",
            "Activan la circulación enterohepática, forzando la reabsorción continua de Metformina en el íleon terminal.",
            "Bloquean la bomba de protones, alterando el pH gástrico y duplicando la absorción del comprimido."
        ],
        "respuesta": "Inhiben competitivamente los transportadores de cationes orgánicos (OCT2) y MATE1 en el túbulo renal proximal, disminuyendo la secreción tubular de Metformina.",
        "feedback": "Farmacocinética de alta escuela. Ya que la Metformina no se metaboliza, su única vía de escape es que el túbulo proximal del riñón la 'bombee' activamente hacia la orina usando el transportador OCT2. Si das Dolutegravir o Cimetidina, tapas ese transportador. La Metformina se queda atrapada en la sangre."
    },
    {
        "familia": "Endocrinología",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: Un paciente con DM2, bebedor crónico pesado (alcoholismo), está tomando Metformina 1000 mg cada 12 hrs. Llega a la urgencia estuporoso y con respiración de Kussmaul. ¿Por qué el alcohol y la Metformina son una mezcla potencialmente letal?",
        "opciones": [
            "El alcohol bloquea los receptores glutamatérgicos, induciendo un coma hipoglicémico que la Metformina vuelve irreversible.",
            "El alcohol incrementa el ratio NADH/NAD+, lo que desvía el metabolismo del piruvato hacia lactato. Sumado al bloqueo mitocondrial de la Metformina, precipitan una Acidosis Láctica fulminante.",
            "El etanol disuelve rápidamente la matriz del comprimido, generando una sobredosis por 'dose dumping'.",
            "El alcohol inactiva la insulina endógena, provocando una cetoacidosis diabética resistente."
        ],
        "respuesta": "El alcohol incrementa el ratio NADH/NAD+, lo que desvía el metabolismo del piruvato hacia lactato. Sumado al bloqueo mitocondrial de la Metformina, precipitan una Acidosis Láctica fulminante.",
        "feedback": "Sinergia destructiva. Procesar grandes cantidades de alcohol en el hígado altera brutalmente el equilibrio redox celular, favoreciendo que todo el piruvato se transforme en ácido láctico. Si además tienes Metformina, que bloquea el consumo de lactato en el hígado (gluconeogénesis), el ácido láctico se acumula en la sangre hasta causar colapso hemodinámico."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "Endocrinología",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: La guía ADA/MINSAL recomienda medir anualmente los niveles de cierta vitamina en pacientes con uso crónico de Metformina (especialmente si cursan con neuropatía que podría confundirse con neuropatía diabética). ¿De qué deficiencia vitamínica estamos hablando?",
        "opciones": [
            "Vitamina D (Colecalciferol), por alteración de la hidroxilación renal.",
            "Vitamina B12 (Cianocobalamina), por interferencia en su absorción dependiente de calcio a nivel del íleon terminal.",
            "Vitamina B9 (Ácido fólico), por competencia con la enzima dihidrofolato reductasa.",
            "Vitamina K, por erradicación de la flora bacteriana intestinal productora."
        ],
        "respuesta": "Vitamina B12 (Cianocobalamina), por interferencia en su absorción dependiente de calcio a nivel del íleon terminal.",
        "feedback": "Cerca del 10-30% de los pacientes que usan Metformina por varios años desarrollan déficit de B12. La droga interfiere en la unión celular dependiente de calcio del complejo factor intrínseco-B12 en el intestino. Esto causa anemia megaloblástica y neuropatía periférica, que muchas veces se confunde con el avance de la propia diabetes. A veces requiere suplementación."
    },
    {
        "familia": "Endocrinología",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: La Acidosis Láctica es la RAM más temida de las biguanidas. Clínicamente, ¿cuáles son los síntomas prodrómicos inespecíficos que un paciente en la farmacia podría referir antes del colapso respiratorio?",
        "opciones": [
            "Visión borrosa repentina, polidipsia extrema y aliento con olor a manzanas (cetónico).",
            "Mialgias profundas (dolor muscular inusual), somnolencia excesiva, disnea progresiva y malestar abdominal inexplicable.",
            "Ictericia conjuntival, coluria y dolor punzante en el hipocondrio derecho.",
            "Temblores finos, sudoración fría profusa y palpitaciones taquicárdicas."
        ],
        "respuesta": "Mialgias profundas (dolor muscular inusual), somnolencia excesiva, disnea progresiva y malestar abdominal inexplicable.",
        "feedback": "La acidosis láctica es traicionera. Empieza como si fuera una gripe fuerte post-ejercicio: le duelen los músculos (mialgias por acúmulo de ácido), empieza a respirar más rápido para botar CO2 (disnea) y le duele el estómago. Si un anciano renal toma Metformina y llega quejándose de esto, derivación urgente a Urgencias."
    },
    {
        "familia": "Endocrinología",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: ¿Cuál es el mecanismo fisiopatológico principal detrás de las intensas RAMs gastrointestinales (diarrea, flatulencia) que produce la Metformina, descartando la vía del ácido láctico?",
        "opciones": [
            "Inhibición de la secreción de ácido clorhídrico, provocando aclorhidria secundaria.",
            "Al disminuir la absorción intestinal de glucosa y alterar la recaptación de sales biliares, se genera un efecto osmótico severo y fermentación bacteriana en el colon.",
            "Inducción de espasmos musculares directos en los esfínteres pilórico y de Oddi.",
            "Destrucción irreversible de las vellosidades duodenales tipo enfermedad celíaca."
        ],
        "respuesta": "Al disminuir la absorción intestinal de glucosa y alterar la recaptación de sales biliares, se genera un efecto osmótico severo y fermentación bacteriana en el colon.",
        "feedback": "La Metformina aumenta la concentración de glucosa que se queda en la luz del intestino. Esa azúcar atrae agua (efecto osmótico) y llega al colon, donde las bacterias se hacen un festín fermentándola y creando gas (flatulencia/distensión). Además, interfiere con las sales biliares, lo que irrita la mucosa colónica acelerando el tránsito (diarrea)."
    },

    # --- CATEGORÍA: 🏥 Caso Clínico ---
    {
        "familia": "Endocrinología",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Llega una receta para una mujer de 24 años, delgada (IMC 22), con indicación de Metformina 850 mg. Al revisar su historial en el Rayén, no hay diagnóstico de diabetes ni prediabetes. ¿Cuál es el uso 'Off-Label' clásico y farmacológicamente fundamentado en este escenario?",
        "opciones": [
            "Manejo farmacológico del Síndrome de Intestino Irritable con predominio de constipación.",
            "Tratamiento del Síndrome de Ovario Poliquístico (SOP); la metformina reduce la hiperinsulinemia, lo que disminuye la producción de andrógenos ováricos y restaura la ovulación.",
            "Tratamiento adyuvante para el hipotiroidismo autoinmune (Hashimoto).",
            "Terapia supresora de la hormona del crecimiento para prevenir adenomas pituitarios."
        ],
        "respuesta": "Tratamiento del Síndrome de Ovario Poliquístico (SOP); la metformina reduce la hiperinsulinemia, lo que disminuye la producción de andrógenos ováricos y restaura la ovulación.",
        "feedback": "En el SOP, las mujeres (incluso delgadas) sufren de resistencia a la insulina en los tejidos periféricos. El páncreas bombea mucha insulina para compensar. Esa insulina en exceso golpea los ovarios (células de la teca) y los obliga a fabricar testosterona, causando acné, vello y anovulación. Al dar Metformina, la insulina baja y el ovario vuelve a la normalidad."
    },
    {
        "familia": "Endocrinología",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Paciente DM2 de 50 años ingresa a la UPC cursando un Shock Séptico grave por peritonitis. Su tratamiento ambulatorio incluía Metformina 1000 mg cada 12 horas. ¿Por qué el médico intensivista debe suspender INMEDIATAMENTE la Metformina?",
        "opciones": [
            "Porque la Metformina pierde eficacia antihipergilcémica en presencia de antibióticos de amplio espectro.",
            "Porque la sepsis genera hipoperfusión tisular masiva, forzando al cuerpo al metabolismo anaerobio (alta producción de lactato). La Metformina bloquearía la eliminación de este lactato, asegurando una acidosis mortal.",
            "Porque induce una caída abrupta de la presión arterial media al vasodilatar el lecho esplácnico.",
            "Porque la absorción enteral está detenida y podría causar íleo paralítico necrosante."
        ],
        "respuesta": "Porque la sepsis genera hipoperfusión tisular masiva, forzando al cuerpo al metabolismo anaerobio (alta producción de lactato). La Metformina bloquearía la eliminación de este lactato, asegurando una acidosis mortal.",
        "feedback": "Criterio de UCI absoluto. Ante cualquier cuadro que cause mala perfusión y falta de oxígeno (Infarto agudo, Shock séptico, Insuficiencia Cardíaca descompensada), las células producen ácido láctico masivamente. Mantener Metformina en ese estado es echarle bencina al fuego, ya que le quita al cuerpo su principal herramienta para barrer ese ácido (la gluconeogénesis)."
    },
    {
        "familia": "Endocrinología",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Según las guías de práctica clínica, ¿en qué situación un paciente recién diagnosticado con Diabetes Mellitus tipo 2 NO debería iniciar con monoterapia de Metformina, pasando directamente a la Insulinización de inicio?",
        "opciones": [
            "Cuando el paciente es adulto mayor de 65 años.",
            "Cuando presenta síntomas de catabolismo severo (baja de peso inexplicable, poliuria extrema) y una HbA1c > 10% o glicemia > 300 mg/dL al debut.",
            "Cuando el paciente presenta hipertensión arterial concomitante estadio 2.",
            "Cuando tiene un índice de masa corporal (IMC) mayor a 35 (Obesidad Grado II)."
        ],
        "respuesta": "Cuando presenta síntomas de catabolismo severo (baja de peso inexplicable, poliuria extrema) y una HbA1c > 10% o glicemia > 300 mg/dL al debut.",
        "feedback": "La Metformina es la reina, pero necesita tiempo para actuar. Si un paciente llega descompensado de forma brutal (adelgazando por estar quemando músculo/grasa porque la glucosa no entra a las células, y con HbA1c altísima), significa que hay 'glucotoxicidad'. El páncreas está paralizado. Tienes que rescatarlo rápido con Insulina basal, estabilizarlo y luego puedes titular con pastillas."
    },

    # ==========================================
    # LOTE 6: ATORVASTATINA (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️️ Mecanismo",
        "pregunta": "Variación 1: La Atorvastatina es un inhibidor competitivo de la HMG-CoA reductasa. Sin embargo, este bloqueo enzimático NO es la razón principal por la que bajan los niveles de colesterol en la sangre. ¿Cuál es el verdadero mecanismo final que limpia el plasma?",
        "opciones": [
            "La enzima bloqueada actúa como un transportador inverso, excretando colesterol hacia la bilis.",
            "La caída del colesterol intracelular en el hepatocito activa la proteína SREBP, lo que induce una sobreexpresión masiva de receptores LDL en la superficie del hígado, 'chupando' el LDL circulante.",
            "La Atorvastatina se une directamente a las partículas de LDL circulantes, marcándolas para su destrucción por los macrófagos esplénicos.",
            "El bloqueo mitocondrial fuerza al cuerpo a oxidar el colesterol plasmático para generar ATP."
        ],
        "respuesta": "La caída del colesterol intracelular en el hepatocito activa la proteína SREBP, lo que induce una sobreexpresión masiva de receptores LDL en la superficie del hígado, 'chupando' el LDL circulante.",
        "feedback": "Fisiopatología molecular clave. La estatina frena la 'fábrica' de colesterol del hígado. El hígado, desesperado por colesterol para funcionar, activa factores de transcripción (SREBP) que fabrican millones de receptores LDL. Estos receptores se ponen en la membrana y atrapan el colesterol que anda en la sangre. Ese es el efecto hipotrigliceremiante real."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: El uso de Atorvastatina post-Infarto Agudo al Miocardio (IAM) es obligatorio, independientemente de si el paciente tiene el colesterol normal. ¿Qué concepto farmacodinámico justifica esta práctica?",
        "opciones": [
            "Efectos pleiotrópicos: Disminuye la inflamación vascular, mejora la función endotelial (óxido nítrico) y estabiliza el core lipídico de la placa de ateroma para que no se rompa.",
            "Efecto cronotrópico negativo: Reduce el consumo de oxígeno del miocardio al disminuir la frecuencia cardíaca.",
            "Inhibición de la cascada de coagulación mediada por el factor Xa, previniendo nuevos trombos.",
            "Aumento drástico de la fracción de eyección del ventrículo izquierdo por optimización mitocondrial."
        ],
        "respuesta": "Efectos pleiotrópicos: Disminuye la inflamación vascular, mejora la función endotelial (óxido nítrico) y estabiliza el core lipídico de la placa de ateroma para que no se rompa.",
        "feedback": "Un QF Élite sabe que las estatinas no son solo para 'bajar la grasa'. Los efectos pleiotrópicos (más allá del LDL) salvan vidas. Al bloquear la síntesis de mevalonato, también bloquean la síntesis de isoprenoides. Esto 'apaga' la inflamación de la arteria y endurece la placa de ateroma para evitar que un pedazo se desprenda y cause un segundo infarto."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: ¿En qué paso exacto de la cascada de síntesis de esteroles interviene la Atorvastatina?",
        "opciones": [
            "Inhibe la conversión de Escualeno a Lanosterol.",
            "Inhibe la conversión de 3-hidroxi-3-metilglutaril-coenzima A (HMG-CoA) a Mevalonato.",
            "Bloquea la enzima Colesterol Esterasa a nivel intestinal.",
            "Inhibe la conversión de Acetil-CoA a Acetoacetil-CoA."
        ],
        "respuesta": "Inhibe la conversión de 3-hidroxi-3-metilglutaril-coenzima A (HMG-CoA) a Mevalonato.",
        "feedback": "Pura bioquímica clínica. La conversión de HMG-CoA a Mevalonato es el paso limitante (el 'cuello de botella') de toda la síntesis de colesterol. Al trancar la puerta ahí, se corta el suministro de toda la cadena posterior hacia el colesterol."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: En APS es común ver que los pacientes toman Simvastatina estrictamente en la noche. Sin embargo, al rotarlos a Atorvastatina, el QF les indica que pueden tomarla a cualquier hora del día. ¿Por qué?",
        "opciones": [
            "Porque la Atorvastatina no causa insomnio, que es la principal RAM nocturna de la Simvastatina.",
            "Porque la síntesis de colesterol ya no es un proceso de predominio nocturno en pacientes tratados crónicamente.",
            "Porque la Atorvastatina tiene una vida media larga (aprox. 14 horas), asegurando un bloqueo enzimático sostenido durante las 24 horas, incluyendo el peak nocturno.",
            "Porque la Atorvastatina requiere los picos matutinos de cortisol para absorberse en el duodeno."
        ],
        "respuesta": "Porque la Atorvastatina tiene una vida media larga (aprox. 14 horas), asegurando un bloqueo enzimático sostenido durante las 24 horas, incluyendo el peak nocturno.",
        "feedback": "El hígado fabrica la mayor parte de nuestro colesterol mientras dormimos. La Simvastatina dura apenas 2-3 horas en la sangre; si la tomas en la mañana, en la noche no hace efecto. La Atorvastatina (y Rosuvastatina) duran más de 14 horas, así que da lo mismo si te la tomas al desayuno, igual te cubrirá la noche."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente hipertenso severo y con Insuficiencia Renal Crónica Etapa 4 (VFG 20 mL/min). Requiere inicio de Atorvastatina por alto riesgo CV. ¿Qué ajuste de dosis se debe realizar según su filtración glomerular?",
        "opciones": [
            "Reducir la dosis a un máximo de 10 mg diarios por riesgo de acumulación tóxica.",
            "Ninguno. La Atorvastatina se elimina casi exclusivamente por vía hepato-biliar en las heces, no requiere ajuste en falla renal.",
            "Aumentar el intervalo de administración a días alternos (Lunes-Miércoles-Viernes).",
            "Contraindicación absoluta; se debe utilizar Ezetimiba en monoterapia."
        ],
        "respuesta": "Ninguno. La Atorvastatina se elimina casi exclusivamente por vía hepato-biliar en las heces, no requiere ajuste en falla renal.",
        "feedback": "Un golazo terapéutico de la Atorvastatina. Menos del 2% del fármaco sale por la orina. Todo el resto se metaboliza en el hígado y se va por la bilis a las fecas. Por lo tanto, puedes tener un paciente en diálisis y le puedes dar sus 40 mg u 80 mg sin miedo a intoxicarlo por falla renal."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Las guías del Colegio Americano de Cardiología (ACC/AHA) dividen a las estatinas por 'Intensidad'. Si un médico te pide prescribir una 'Estatina de Alta Intensidad' para reducir el LDL en MÁS de un 50%, ¿cuál es la dosis correcta de Atorvastatina?",
        "opciones": [
            "10 a 20 mg al día.",
            "40 a 80 mg al día.",
            "Solo 80 mg, combinada obligatoriamente con Fibratos.",
            "Cualquier dosis siempre que sea administrada endovenosa."
        ],
        "respuesta": "40 a 80 mg al día.",
        "feedback": "Clasificación clínica mundial. Alta intensidad (baja el LDL >50%): Atorva 40-80mg o Rosuva 20-40mg. Intensidad Moderada (baja el LDL 30-50%): Atorva 10-20mg, Rosuva 5-10mg, o Simva 20-40mg. Paciente infartado = siempre Alta Intensidad."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Paciente en tratamiento con Atorvastatina 40mg adquiere una neumonía atípica y le prescriben Claritromicina por 7 días. A los 5 días llega a urgencias sin poder caminar por dolor muscular severo. ¿Cuál es el mecanismo de esta interacción letal?",
        "opciones": [
            "La Claritromicina es un potente inhibidor del citocromo CYP3A4. Como la Atorvastatina se metaboliza por esta isoenzima, sus niveles plasmáticos se disparan, causando miotoxicidad masiva.",
            "La Claritromicina induce al CYP3A4, transformando a la Atorvastatina en un metabolito rabdomiolítico.",
            "Ambos fármacos compiten por el calcio intracelular, provocando tetania muscular.",
            "Sinergismo a nivel de la placa motora, bloqueando los receptores de acetilcolina."
        ],
        "respuesta": "La Claritromicina es un potente inhibidor del citocromo CYP3A4. Como la Atorvastatina se metaboliza por esta isoenzima, sus niveles plasmáticos se disparan, causando miotoxicidad masiva.",
        "feedback": "Interacción de libro. Atorvastatina, Simvastatina y Lovastatina son sustratos exclusivos del CYP3A4. Si le das al paciente un inhibidor fuerte de esta enzima (Claritromicina, Itraconazol, Jugo de Pomelo), la estatina no se destruye, se acumula en la sangre a niveles 5 o 10 veces mayores, y destruye el músculo esquelético."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente con Dislipidemia Mixta de alto riesgo cardiovascular. El médico decide asociar Atorvastatina con Gemfibrozilo. Como QF Élite, tú vetas esta receta inmediatamente. ¿Por qué el Gemfibrozilo está proscrito junto a la Atorvastatina y qué alternativa farmacológica de adición es la más respaldada en APS?",
        "opciones": [
            "Porque el Gemfibrozilo inhibe la glucuronidación de la estatina (UGT1A1) y bloquea el transportador hepático OATP1B1, multiplicando el riesgo de rabdomiólisis letal. La alternativa más segura y con evidencia de reducción de mortalidad es asociar Ezetimiba.",
            "Porque el Gemfibrozilo induce enzimas hepáticas que anulan el efecto de la estatina, haciéndola inútil. Se debe usar Niacina.",
            "Porque ambos fármacos causan litiasis biliar aguda en menos de 48 horas. Se debe usar Omega 3 en altas dosis.",
            "Porque la mezcla bloquea la síntesis de Coenzima Q10 en el miocardio, induciendo paro cardíaco. Se debe rotar a Fenofibrato."
        ],
        "respuesta": "Porque el Gemfibrozilo inhibe la glucuronidación de la estatina (UGT1A1) y bloquea el transportador hepático OATP1B1, multiplicando el riesgo de rabdomiólisis letal. La alternativa más segura y con evidencia de reducción de mortalidad es asociar Ezetimiba.",
        "feedback": "Red Flag farmacológica mundial. El Gemfibrozilo le corta TODAS las vías de escape a la estatina: bloquea el transportador (OATP1B1) para que entre al hígado y bloquea las enzimas que la destruyen. La estatina se acumula en la sangre y revienta el músculo. En la APS moderna, la mejor estrategia para potenciar la baja de lípidos y reducir el riesgo cardiovascular sin este peligro es combinar la estatina con Ezetimiba (inhibidor de absorción de colesterol)."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: ¿Qué consejo dietético obligatorio debes darle a un paciente que inicia Atorvastatina respecto a ciertas frutas, y cuál es el mecanismo subyacente?",
        "opciones": [
            "Evitar vegetales de hoja verde oscuro, ya que su vitamina K antagoniza la estabilización de placa.",
            "Evitar los lácteos, ya que el calcio quela la molécula de estatina en el intestino.",
            "Evitar consumir Jugo de Pomelo (Grapefruit) en grandes cantidades, ya que contiene furanocumarinas que inhiben irreversiblemente el CYP3A4 intestinal, aumentando la absorción y toxicidad de la droga.",
            "Aumentar el consumo de jugo de naranja, ya que la vitamina C es necesaria para el efecto pleiotrópico."
        ],
        "respuesta": "Evitar consumir Jugo de Pomelo (Grapefruit) en grandes cantidades, ya que contiene furanocumarinas que inhiben irreversiblemente el CYP3A4 intestinal, aumentando la absorción y toxicidad de la droga.",
        "feedback": "El jugo de pomelo no es un mito. Las furanocumarinas que contiene destruyen literalmente el CYP3A4 de las paredes del intestino. Normalmente, el 70% de la Atorvastatina se destruye antes de entrar al cuerpo gracias a este CYP intestinal. Si te tomas un litro de pomelo, entra el 100% de la pastilla de golpe. Riesgo de miopatía altísimo."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Paciente de 60 años en terapia con Atorvastatina 40mg consulta por dolor muscular difuso y debilidad en los muslos (Mialgia). ¿Qué examen de laboratorio es fundamental pedir para diferenciar una mialgia benigna de una Miopatía grave / Rabdomiólisis?",
        "opciones": [
            "Creatina Cinasa (CK o CPK) total. Si está elevada más de 10 veces el límite superior normal, es urgencia médica.",
            "Troponina T ultrasensible, para descartar isquemia del músculo estriado.",
            "Electromiografía (EMG) de extremidades inferiores.",
            "Niveles de Ácido Láctico venoso."
        ],
        "respuesta": "Creatina Cinasa (CK o CPK) total. Si está elevada más de 10 veces el límite superior normal, es urgencia médica.",
        "feedback": "SAMS (Statin-Associated Muscle Symptoms). Si al paciente le duelen los músculos pero la CK está normal, es una mialgia molesta pero sin destrucción muscular. Si el músculo se está rompiendo (miopatía o rabdomiólisis), la enzima que vive adentro del músculo (CK) se derrama a la sangre. Una CK altísima obliga a suspender el fármaco y evaluar daño renal por mioglobinuria."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: El uso prolongado de estatinas potentes como Atorvastatina 80mg se ha asociado a un ligero incremento en la incidencia de una enfermedad metabólica. ¿Cuál es esta patología y cuál es la recomendación clínica frente al riesgo?",
        "opciones": [
            "Hipotiroidismo inducido; se debe suspender la estatina y rotar a Ezetimiba.",
            "Diabetes Mellitus tipo 2 de nueva aparición; pero los beneficios cardiovasculares (prevención de infartos) superan con creces este riesgo, por lo que no se debe suspender, solo vigilar la glicemia.",
            "Hiperuricemia severa y crisis de gota; se debe coadministrar Alopurinol.",
            "Insuficiencia suprarrenal aguda por falta de colesterol para sintetizar cortisol."
        ],
        "respuesta": "Diabetes Mellitus tipo 2 de nueva aparición; pero los beneficios cardiovasculares (prevención de infartos) superan con creces este riesgo, por lo que no se debe suspender, solo vigilar la glicemia.",
        "feedback": "Las estatinas de alta potencia pueden aumentar levemente la resistencia a la insulina y subir un poco la HbA1c (efecto diabetogénico). Sin embargo, la FDA y el MINSAL son claros: por cada nuevo caso de diabetes que genera la estatina, previene de 5 a 9 infartos letales o accidentes cerebrovasculares. El beneficio gana por goleada."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: Previo al inicio de terapia con Atorvastatina, y luego a las 8-12 semanas, la guía clínica exige el monitoreo de un perfil de sangre específico para evaluar la principal RAM silenciosa. ¿Cuál es?",
        "opciones": [
            "Perfil tiroideo (TSH y T4 libre).",
            "Perfil Hepático (específicamente transaminasas ALT/AST), por el riesgo de hepatotoxicidad subclínica.",
            "Hemograma completo con recuento de plaquetas por riesgo de anemia aplásica.",
            "Niveles plasmáticos de Coenzima Q10 sérica."
        ],
        "respuesta": "Perfil Hepático (específicamente transaminasas ALT/AST), por el riesgo de hepatotoxicidad subclínica.",
        "feedback": "El hígado es la zona cero donde actúa la Atorvastatina. Cerca de un 1-2% de los pacientes presenta una elevación de las transaminasas (ALT/AST). Si la elevación supera 3 veces el límite superior normal (ej. >100 U/L), se debe considerar bajar la dosis o suspender transitoriamente para evitar un daño hepático inducido por drogas (DILI)."
    },

    # --- CATEGORÍA: 🏥 Caso Clínico ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Mujer de 35 años, dislipidémica severa familiar. Actualmente usa Atorvastatina 40mg. Acude a la farmacia contando que está planificando un embarazo. ¿Cuál es la indicación absoluta respecto a su terapia hipolipemiante?",
        "opciones": [
            "Bajar la dosis a 10 mg diarios durante el primer trimestre.",
            "Rotar a Pravastatina, que es la única estatina aprobada por la FDA para el embarazo.",
            "Suspender inmediatamente la Atorvastatina (Categoría X). El colesterol es esencial para la embriogénesis y síntesis de membranas celulares del feto.",
            "Asociar Ácido Fólico en altas dosis para prevenir los defectos del tubo neural causados por el fármaco."
        ],
        "respuesta": "Suspender inmediatamente la Atorvastatina (Categoría X). El colesterol es esencial para la embriogénesis y síntesis de membranas celulares del feto.",
        "feedback": "Regla de oro: ESTATINAS = TERATÓGENAS. Un feto en formación es una máquina de crear células nuevas, y cada célula necesita una membrana hecha de colesterol. Si le bloqueas el colesterol a la madre, destruyes el desarrollo neurológico y celular del feto. Las mujeres fértiles deben suspenderlas 1 a 2 meses antes de intentar concebir."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Llega un paciente post-IAM a control. Está con Atorvastatina 80mg y dieta estricta, pero su LDL se estancó en 95 mg/dL (meta post-infarto es < 55 mg/dL). El médico te pide sugerencias de adición farmacológica. Sabiendo que doblar la estatina no sirve por la 'Regla de los 6', ¿qué le recomiendas?",
        "opciones": [
            "Agregar Ezetimiba 10mg, ya que inhibe el transportador NPC1L1 en el ribete en cepillo intestinal, bloqueando la absorción del colesterol biliar y dietético, con un efecto sinérgico brillante.",
            "Agregar Colestiramina para precipitar la Atorvastatina y aumentar su vida media.",
            "Agregar Niacina a altas dosis para aumentar el HDL, ignorando el nivel de LDL.",
            "Cambiar la Atorvastatina por Gemfibrozilo."
        ],
        "respuesta": "Agregar Ezetimiba 10mg, ya que inhibe el transportador NPC1L1 en el ribete en cepillo intestinal, bloqueando la absorción del colesterol biliar y dietético, con un efecto sinérgico brillante.",
        "feedback": "La 'Regla del 6' dice que si duplicas la dosis de una estatina (ej. de 40 a 80), el LDL solo baja un patético 6% extra. Para llegar a metas difíciles, debes atacar por dos frentes: Atorvastatina frena la SÍNTESIS en el hígado, y Ezetimiba frena la ABSORCIÓN en el intestino. Esta dupla (aprobada por el estudio IMPROVE-IT) es la mejor arma en APS."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Paciente añoso inicia Atorvastatina 20mg y a las dos semanas presenta miopatía grave e inexplicable sin usar antibióticos ni otros fármacos. Al indagar en su historia clínica, notas que no se toma exámenes hace 5 años y reporta mucho frío crónico, constipación y bradicardia. ¿Qué patología de base NO diagnosticada aumenta drásticamente el riesgo de miopatía por estatinas?",
        "opciones": [
            "Diabetes tipo 1 autoinmune.",
            "Hipotiroidismo no tratado.",
            "Hiperplasia prostática benigna.",
            "Anemia perniciosa severa."
        ],
        "respuesta": "Hipotiroidismo no tratado.",
        "feedback": "El truco clínico que separa a los pro del resto. El hipotiroidismo no diagnosticado disminuye la depuración de las estatinas y altera la arquitectura del músculo esquelético. Iniciar estatinas en un paciente hipotiroideo no tratado es casi garantía de mialgias severas o miopatía. Siempre se debe pedir una TSH si hay sospecha antes de culpar al fármaco al 100%."
    },

    # ==========================================
    # LOTE 7: AMLODIPINO (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: A diferencia del Verapamilo (que es un calcioantagonista no dihidropiridínico), ¿por qué el Amlodipino es seguro de administrar en pacientes que sufren bloqueos auriculoventriculares (AV) de segundo grado?",
        "opciones": [
            "Porque el Amlodipino tiene alta selectividad por los canales de calcio del músculo liso vascular y afinidad casi nula por los canales del tejido de conducción cardíaco (nodo sinusal/AV).",
            "Porque el Amlodipino bloquea canales de sodio accesorios que compensan el retraso del nodo AV.",
            "Porque estimula los receptores adrenérgicos beta-1, contrarrestando el efecto depresor del calcio.",
            "Porque su vida media es tan larga que el corazón logra adaptarse y regenerar sus potenciales de acción."
        ],
        "respuesta": "Porque el Amlodipino tiene alta selectividad por los canales de calcio del músculo liso vascular y afinidad casi nula por los canales del tejido de conducción cardíaco (nodo sinusal/AV).",
        "feedback": "Farmacodinamia pura. Las 'dipinas' (Amlodipino, Nifedipino) van directo a las cañerías (arterias) y las dilatan; no tocan el cableado eléctrico del corazón. Por el contrario, Verapamilo y Diltiazem son depresores cardíacos y frenan el nodo AV. Dar Verapamilo a alguien con bloqueo AV es matarlo; darle Amlodipino es seguro."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: El Amlodipino es un vasodilatador potente, pero es asimétrico. ¿A qué sector del árbol vascular afecta de forma exclusiva, desencadenando su principal efecto adverso mecánico?",
        "opciones": [
            "Es un vasodilatador venoso potente, lo que reduce la precarga cardíaca.",
            "Dilata exclusivamente la arteriola pre-capilar (esfínter), sin afectar el lecho venoso post-capilar.",
            "Dilata arterias y venas por igual (vasodilatador balanceado), similar al Nitroprusiato.",
            "Genera vasoconstricción capilar paradójica en las extremidades inferiores."
        ],
        "respuesta": "Dilata exclusivamente la arteriola pre-capilar (esfínter), sin afectar el lecho venoso post-capilar.",
        "feedback": "¡La clave del edema! El Amlodipino abre la llave de entrada (arteriola) pero la llave de salida (vénula) sigue normal. Esto genera un aumento masivo de presión hidrostática dentro del capilar, empujando el agua hacia afuera de los vasos sanguíneos y causando el clásico edema de tobillos."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: ¿Qué ventaja farmacocinética intrínseca tiene el Amlodipino que evita el fenómeno de 'taquicardia refleja' que sí produce el Nifedipino de liberación rápida?",
        "opciones": [
            "Posee actividad simpaticolítica secundaria a nivel del bulbo raquídeo.",
            "Se une lentamente a los receptores y tiene una vida media larguísima (35-50 hrs), logrando una caída de presión arterial gradual y sostenida que no activa los barorreceptores.",
            "Su metabolito activo bloquea la liberación de noradrenalina desde las terminaciones nerviosas.",
            "Requiere activación por la enzima convertidora de angiotensina, lo que modula su velocidad de acción."
        ],
        "respuesta": "Se une lentamente a los receptores y tiene una vida media larguísima (35-50 hrs), logrando una caída de presión arterial gradual y sostenida que no activa los barorreceptores.",
        "feedback": "Si le bajas la presión a alguien de un golpe (como pasaba con el Nifedipino sublingual antiguo), el cerebro entra en pánico y manda adrenalina para subirla, causando taquicardia. El Amlodipino es tan lento en absorberse y dura tanto tiempo, que el cuerpo ni se entera del cambio, evitando la respuesta refleja del sistema simpático."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: Paciente adulto mayor de 75 años requiere iniciar Amlodipino. ¿Cuál es la conducta de dosificación inicial recomendada para evitar RAMs hemodinámicas y cuál es su metabolismo hepático?",
        "opciones": [
            "Iniciar con 10 mg/día, ya que su excreción renal está disminuida por la edad.",
            "Iniciar con 2.5 mg a 5 mg al día. El fármaco tiene metabolismo extenso por CYP3A4, el cual suele estar reducido en adultos mayores.",
            "Iniciar con 10 mg cada 48 horas para evitar el metabolismo de primer paso.",
            "La edad no influye en la dosis porque el Amlodipino se excreta 100% inalterado por las heces."
        ],
        "respuesta": "Iniciar con 2.5 mg a 5 mg al día. El fármaco tiene metabolismo extenso por CYP3A4, el cual suele estar reducido en adultos mayores.",
        "feedback": "El Amlodipino pasa casi completamente por el hígado (CYP3A4). En adultos mayores o pacientes con falla hepática, el hígado es más lento, por lo que la vida media del fármaco se puede alargar hasta 60 horas. Si partes con 10 mg de golpe, el abuelo se puede ir al piso por hipotensión. Start low, go slow."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente hipertenso severo olvida tomar su comprimido de Amlodipino 10mg en la mañana y se acuerda a las 8 PM. Te llama a la farmacia preguntando si debe tomarlo a esa hora o saltarse la dosis. ¿Qué le indicas basado en la cinética del fármaco?",
        "opciones": [
            "Que no lo tome y espere al día siguiente, ya que si lo toma de noche causará insomnio severo.",
            "Que lo tome de inmediato, ya que su vida media es corta y perderá la protección nocturna.",
            "Que puede tomarlo sin problemas. Al tener una vida media de más de 35 horas, la hora exacta de la toma no afecta significativamente los niveles plasmáticos en estado estacionario.",
            "Que tome media dosis (5mg) porque la absorción intestinal es el doble durante la noche."
        ],
        "respuesta": "Que puede tomarlo sin problemas. Al tener una vida media de más de 35 horas, la hora exacta de la toma no afecta significativamente los niveles plasmáticos en estado estacionario.",
        "feedback": "La gran ventaja del Amlodipino es su 'efecto perdonador'. Al durar casi dos días en el plasma, un retraso de 10 o 12 horas en una toma puntual no genera caídas bruscas de la concentración ni alzas peligrosas de presión. Puede tomarlo y al día siguiente volver a su horario habitual."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Un paciente con Enfermedad Renal Crónica terminal (en hemodiálisis) requiere control estricto de PA. El nefrólogo indica Amlodipino 10 mg/día. ¿Qué ajuste dialítico o de dosis necesita este fármaco?",
        "opciones": [
            "Debe administrarse una dosis suplementaria post-diálisis porque la máquina lo extrae de la sangre.",
            "Ninguno. Tiene alta unión a proteínas (>93%) y amplio volumen de distribución, por lo que no es dializable ni requiere ajuste por VFG.",
            "Reducir la dosis a 2.5 mg/día debido a que sus metabolitos tóxicos se acumulan en el riñón fallido.",
            "Está contraindicado en hemodiálisis por riesgo de calcifilaxis."
        ],
        "respuesta": "Ninguno. Tiene alta unión a proteínas (>93%) y amplio volumen de distribución, por lo que no es dializable ni requiere ajuste por VFG.",
        "feedback": "Fármaco amigable con el riñón. Como casi todo se destruye en el hígado y lo que viaja por la sangre va súper pegado a las proteínas (como si llevara cinturón de seguridad), el filtro de la diálisis no logra sacarlo del cuerpo. Tampoco se acumula si el riñón falla. Dosis normal."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Paciente diabético toma Simvastatina 40 mg en la noche. El cardiólogo le agrega Amlodipino 10 mg. Según las alertas de la FDA y MINSAL, ¿qué intervención farmacéutica es imperativa?",
        "opciones": [
            "Ninguna, son fármacos de primera línea y totalmente seguros en conjunto.",
            "Sugerir bajar la dosis de Simvastatina a un MÁXIMO de 20 mg/día o rotar a Atorvastatina, ya que el Amlodipino inhibe parcialmente el CYP3A4, duplicando el riesgo de miopatía por Simvastatina.",
            "Separar la toma de ambos fármacos por 12 horas para evitar que precipiten en el estómago.",
            "Suspender Amlodipino, ya que la Simvastatina anula su efecto hipotensor."
        ],
        "respuesta": "Sugerir bajar la dosis de Simvastatina a un MÁXIMO de 20 mg/día o rotar a Atorvastatina, ya que el Amlodipino inhibe parcialmente el CYP3A4, duplicando el riesgo de miopatía por Simvastatina.",
        "feedback": "Una clásica interacción de receta. El Amlodipino no solo se metaboliza por el CYP3A4, sino que también es un inhibidor débil de este. La Simvastatina es exquisitamente sensible a esto. Si los juntas a dosis plenas, la Simvastatina se acumula y el paciente debuta con rabdomiólisis. La regla es: máximo 20mg de Simvastatina si usa Amlodipino."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente en tratamiento para disfunción eréctil compra Sildenafil (Viagra) en tu farmacia. En su ficha figura que usa Amlodipino 10 mg diarios. ¿Qué consejo de seguridad debes darle de forma proactiva?",
        "opciones": [
            "Que la mezcla causará priapismo irreversible por sinergismo de calcio.",
            "Que ambos son vasodilatadores. Aunque no están contraindicados absolutamente (como con los nitratos), la coadministración puede causar hipotensión ortostática severa y mareos bruscos.",
            "Que el Sildenafil acelera el metabolismo del Amlodipino, causando picos de hipertensión de rebote.",
            "Que debe tomar el Sildenafil sublingual para evitar la interacción hepática."
        ],
        "respuesta": "Que ambos son vasodilatadores. Aunque no están contraindicados absolutamente (como con los nitratos), la coadministración puede causar hipotensión ortostática severa y mareos bruscos.",
        "feedback": "Interacción dinámica. Amlodipino relaja las arterias. Sildenafil inhibe la PDE-5 y relaja el músculo liso (mediado por óxido nítrico). Juntarlos no es muerte segura como con los nitratos (Nitroglicerina), pero la suma de ambos efectos hipotensores puede hacer que el paciente se desmaye al pararse (síncope ortostático)."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: ¿Por qué la combinación de Amlodipino y Clopidogrel es objeto de debate en pacientes cardiópatas, aunque se usen juntos frecuentemente?",
        "opciones": [
            "Porque el Amlodipino es un profármaco que requiere CYP2C19, enzima que el Clopidogrel bloquea.",
            "Porque compiten por el citocromo CYP3A4 hepático. El Clopidogrel requiere esta enzima para transformarse parcialmente en su metabolito activo, por lo que el Amlodipino podría reducir su efecto antiplaquetario.",
            "Porque ambos reducen drásticamente los niveles de calcio plaquetario, causando hemorragias letales.",
            "Porque el Clopidogrel induce falla hepática aguda si se junta con calcioantagonistas."
        ],
        "respuesta": "Porque compiten por el citocromo CYP3A4 hepático. El Clopidogrel requiere esta enzima para transformarse parcialmente en su metabolito activo, por lo que el Amlodipino podría reducir su efecto antiplaquetario.",
        "feedback": "Polifarmacia cardíaca fina. El Clopidogrel es un profármaco que necesita de los CYP hepáticos (principalmente 2C19, pero también 3A4) para activarse y proteger contra los trombos. Si el Amlodipino ocupa y bloquea levemente el 3A4, teóricamente reduce la cantidad de Clopidogrel activo. Aunque en la práctica clínica se usan, requiere vigilancia de eventos isquémicos."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Paciente mujer de 60 años, tras 3 meses de Amlodipino 10 mg, acude quejándose de tobillos hinchados (edema maleolar). Según el mecanismo fisiopatológico del fármaco, ¿cuál es el manejo farmacológico MÁS efectivo para resolver este edema?",
        "opciones": [
            "Agregar Furosemida 40 mg, ya que el edema se debe a retención hidrosalina y sobrecarga de volumen renal.",
            "Suspender el Amlodipino o asociarlo a un IECA o ARA II (ej. Enalapril/Losartán), ya que estos relajan la vénula post-capilar, igualando las presiones y drenando el edema.",
            "Recetar medias de compresión y mantener la dosis, el edema desaparecerá solo al sexto mes.",
            "Reducir el consumo de sodio en la dieta a cero."
        ],
        "respuesta": "Suspender el Amlodipino o asociarlo a un IECA o ARA II (ej. Enalapril/Losartán), ya que estos relajan la vénula post-capilar, igualando las presiones y drenando el edema.",
        "feedback": "Errores de manual: Dar diuréticos para el edema por Amlodipino. ¡El paciente no está reteniendo agua por el riñón! El edema es puramente mecánico (presión capilar alta porque la arteria está dilatada y la vena apretada). Si le sumas un IECA/ARA II (que dilatan las venas), alivias la presión del capilar y el líquido vuelve a entrar a la circulación."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: El uso crónico de calcioantagonistas dihidropiridínicos (como el Amlodipino) se asocia a una RAM odontológica poco común pero muy molesta que dificulta la masticación. ¿Cuál es?",
        "opciones": [
            "Pérdida acelerada del esmalte dental (caries rampantes).",
            "Hiperplasia gingival (agrandamiento y sangrado de las encías).",
            "Necrosis del maxilar inferior.",
            "Xerostomía absoluta (ausencia total de saliva)."
        ],
        "respuesta": "Hiperplasia gingival (agrandamiento y sangrado de las encías).",
        "feedback": "Al igual que la Fenitoína o la Ciclosporina, el Amlodipino altera el metabolismo del colágeno en los fibroblastos de las encías, causando hiperplasia (las encías crecen y cubren los dientes). Ocurre especialmente en pacientes con mala higiene oral. Muchas veces requiere cirugía periodontal y rotar el fármaco."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: Al iniciar Amlodipino, algunos pacientes reportan cefalea pulsátil, rubor facial (flushing) y palpitaciones leves en la primera semana. ¿Cómo explicas clínicamente estos síntomas?",
        "opciones": [
            "Es una reacción alérgica mediada por histamina tipo I.",
            "Son consecuencia directa de la potente vasodilatación arterial en los lechos craneales y faciales. Suelen tolerarse y disminuir con el tiempo.",
            "Indican una crisis hipertensiva de rebote y exigen hospitalización.",
            "Es un signo de toxicidad hepática incipiente."
        ],
        "respuesta": "Son consecuencia directa de la potente vasodilatación arterial en los lechos craneales y faciales. Suelen tolerarse y disminuir con el tiempo.",
        "feedback": "Las tuberías se abren de golpe. Más flujo de sangre a la cara = rubor. Más flujo a las meninges = dolor de cabeza pulsátil. Es el precio fisiológico de la vasodilatación y es completamente benigno. El QF debe calmar al paciente, explicarle que el cuerpo se adaptará en un par de semanas y que no debe botar las pastillas."
    },

    # --- CATEGORÍA: 🏥 Caso Clínico ---
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Paciente de raza negra (afrodescendiente) recién diagnosticado con HTA estadio 1. Según las guías internacionales (JNC 8 / AHA), ¿por qué el médico prescribe Amlodipino como primera línea en vez de Enalapril?",
        "opciones": [
            "Porque los afrodescendientes tienen genéticamente una 'hipertensión de renina baja'. El sistema renina-angiotensina no es su motor principal, por lo que IECAs/ARA II son menos efectivos; responden mejor a diuréticos tiazídicos o calcioantagonistas.",
            "Porque los pacientes de raza negra tienen alergia genética demostrada a los IECAs.",
            "Porque el Amlodipino induce la excreción de melanina que disminuye la resistencia vascular.",
            "Porque los afrodescendientes hipermetabolizan el Enalapril, destruyéndolo antes de actuar."
        ],
        "respuesta": "Porque los afrodescendientes tienen genéticamente una 'hipertensión de renina baja'. El sistema renina-angiotensina no es su motor principal, por lo que IECAs/ARA II son menos efectivos; responden mejor a diuréticos tiazídicos o calcioantagonistas.",
        "feedback": "Pura medicina basada en la evidencia. La población de raza negra tiende a retener sal y a tener bajos niveles de renina plasmática. Darles un bloqueador de renina (IECA/ARA II) como primera pastilla no sirve de mucho y, además, tienen hasta 4 veces más riesgo de angioedema con los IECAs. Amlodipino o Clortalidona son los reyes aquí."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Paciente hipertenso acude a la urgencia rural por cuadro de dolor torácico opresivo de esfuerzo (Angina Estable). Toma Amlodipino 10 mg. El médico de turno le receta adicionalmente Propranolol 40mg. ¿Qué lógica clínica fundamenta esta combinación para la angina?",
        "opciones": [
            "Sinergismo vasodilatador: ambos relajan el músculo liso coronario, destapando arterias ocluidas al 100%.",
            "Manejo complementario: Amlodipino dilata las coronarias (aumenta aporte de O2) y Propranolol frena el corazón (disminuye consumo de O2), equilibrando la balanza isquémica.",
            "Ambos fármacos disuelven químicamente la placa de ateroma, revirtiendo la enfermedad coronaria.",
            "No hay lógica, es una contraindicación letal por riesgo de paro sinusal inmediato."
        ],
        "respuesta": "Manejo complementario: Amlodipino dilata las coronarias (aumenta aporte de O2) y Propranolol frena el corazón (disminuye consumo de O2), equilibrando la balanza isquémica.",
        "feedback": "La angina es un problema de oferta y demanda. El corazón pide mucha sangre (ejercicio) pero las coronarias tapadas no la entregan (oferta). El Amlodipino mejora la oferta dilatando las coronarias, pero no relaja al corazón. El Betabloqueador (Propranolol, Atenolol) hace que el corazón lata más lento y más suave (baja la demanda de oxígeno). Juntos son el combo perfecto."
    },
    {
        "familia": "Cardiovasculares",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Llega un caso complejo: Mujer de 30 años, sin factores de riesgo cardiovascular, embarazada de 24 semanas. En el control detectan PA de 160/100 mmHg. Sabiendo que los IECAs y ARA II (Enalapril/Losartán) son teratogénicos, ¿cuál es el rol del Amlodipino o fármacos similares en este escenario?",
        "opciones": [
            "Están contraindicados. Se debe tratar exclusivamente con dieta sin sodio.",
            "El Amlodipino se puede usar, pero el fármaco de elección (dihidropiridina preferida) en el embarazo es el Nifedipino de acción prolongada, el cual es seguro y efectivo para la HTA gestacional.",
            "Se debe usar siempre junto a Estatinas para evitar preeclampsia.",
            "Generan malformaciones óseas fetales al bloquear el calcio, por lo que están estrictamente prohibidos."
        ],
        "respuesta": "El Amlodipino se puede usar, pero el fármaco de elección (dihidropiridina preferida) en el embarazo es el Nifedipino de acción prolongada, el cual es seguro y efectivo para la HTA gestacional.",
        "feedback": "Manejo crítico de embarazo. IECAs/ARA II destrozan los riñones del feto. Para la presión alta en embarazadas nos quedan pocas opciones seguras: Metildopa, Labetalol o Calcioantagonistas. De estos últimos, la estrella mundial es el Nifedipino de liberación prolongada (Retard/GITS), pero el Amlodipino también es una alternativa aceptada y segura si el primero no está disponible."
    },

    # ==========================================
    # LOTE 8: OMEPRAZOL (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "Gastroenterología",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: El Omeprazol es un profármaco inactivo al momento de absorberse. ¿Qué condición biofísica exacta debe ocurrir dentro de la célula parietal gástrica para que logre inhibir la bomba de protones?",
        "opciones": [
            "Requiere unirse a los receptores histaminérgicos H2 para sufrir un cambio conformacional.",
            "Requiere entrar a los canalículos secretores altamente ácidos (pH < 2), donde se protona y se convierte en una sulfenamida activa que forma enlaces disulfuro irreversibles con la enzima H+/K+ ATPasa.",
            "Requiere ser fosforilado por cinasas intracelulares mediadas por gastrina.",
            "Requiere unirse a la bomba solo cuando esta se encuentra en estado inactivo o de reposo nocturno."
        ],
        "respuesta": "Requiere entrar a los canalículos secretores altamente ácidos (pH < 2), donde se protona y se convierte en una sulfenamida activa que forma enlaces disulfuro irreversibles con la enzima H+/K+ ATPasa.",
        "feedback": "Fisiopatología molecular fina. El Omeprazol viaja por la sangre inactivo. Al entrar a la célula parietal y acercarse al canalículo (donde se bota el ácido), el pH ácido extremo lo 'activa' de golpe. Al activarse, se pega como cemento (enlace covalente) a la bomba. Por eso la célula parietal debe estar fabricando ácido en ese momento para que el fármaco funcione."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: Sabiendo que el Omeprazol tiene una vida media plasmática muy corta (1 a 2 horas), ¿cómo es posible que logre inhibir la secreción ácida gástrica durante 24 a 48 horas con una sola toma?",
        "opciones": [
            "Porque su unión a las proteínas plasmáticas es del 99%, liberándose lentamente a lo largo del día.",
            "Porque forma un enlace covalente irreversible con la H+/K+ ATPasa. La secreción de ácido solo se reanuda cuando la célula parietal sintetiza nuevas bombas desde cero.",
            "Porque experimenta una intensa circulación enterohepática, reciclándose continuamente.",
            "Porque altera el ADN de la célula parietal, apagando el gen de la bomba por días."
        ],
        "respuesta": "Porque forma un enlace covalente irreversible con la H+/K+ ATPasa. La secreción de ácido solo se reanuda cuando la célula parietal sintetiza nuevas bombas desde cero.",
        "feedback": "El fármaco desaparece de la sangre en 2 horas, pero el efecto dura días. ¿Por qué? Porque el enlace que hace con la bomba de ácido es irreversible. Destruye la bomba. El estómago solo volverá a producir ácido cuando sus células gasten energía y tiempo (18-24 horas) en construir e insertar bombas nuevas en la membrana apical."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: ¿Por qué las cápsulas de Omeprazol de la APS vienen formuladas obligatoriamente con gránulos de cubierta entérica?",
        "opciones": [
            "Para evitar que el Omeprazol irrite directamente la mucosa gástrica y cause úlceras de contacto.",
            "Porque si el Omeprazol inactivo entra en contacto con el ácido del estómago antes de ser absorbido, se protona prematuramente en el lumen gástrico, se degrada y pierde su capacidad de absorberse hacia la sangre.",
            "Para asegurar que se libere exclusivamente en el colon, donde se ejerce su acción sistémica.",
            "Para prolongar su vida media plasmática a más de 12 horas (efecto retard)."
        ],
        "respuesta": "Porque si el Omeprazol inactivo entra en contacto con el ácido del estómago antes de ser absorbido, se protona prematuramente en el lumen gástrico, se degrada y pierde su capacidad de absorberse hacia la sangre.",
        "feedback": "Paradoja farmacéutica: El Omeprazol necesita ácido para funcionar (adentro de la célula parietal), pero el ácido lo destruye si lo toca antes de tiempo (en el lumen del estómago). La cápsula debe resistir el ácido, viajar al intestino (donde el pH es neutro), disolverse ahí, absorberse a la sangre, y llegar a la célula parietal POR DETRÁS (vía circulación sistémica)."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "Gastroenterología",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: Indicación QF de mostrador: Un paciente toma su Omeprazol justo DESPUÉS de un desayuno abundante. Tú le adviertes que esto reducirá drásticamente la eficacia del tratamiento. ¿Cuál es el fundamento farmacodinámico?",
        "opciones": [
            "La comida alcaliniza el estómago, anulando la cubierta entérica de la cápsula.",
            "Las grasas del desayuno se unen al fármaco formando complejos insolubles insolubles.",
            "Las bombas de protones son reclutadas a la membrana por el estímulo de la comida. Si tomas el fármaco después, las bombas ya hicieron su trabajo y volvieron al estado de reposo, donde el Omeprazol no puede activarse ni unirse a ellas.",
            "El metabolismo hepático de primer paso se acelera masivamente en presencia de glucosa."
        ],
        "respuesta": "Las bombas de protones son reclutadas a la membrana por el estímulo de la comida. Si tomas el fármaco después, las bombas ya hicieron su trabajo y volvieron al estado de reposo, donde el Omeprazol no puede activarse ni unirse a ellas.",
        "feedback": "Regla de oro de los IBP: 30 a 60 minutos ANTES de la comida principal. El Omeprazol necesita que la célula parietal esté trabajando al máximo para destruirla (bombas activas). Si comes primero, las bombas tiran ácido y se guardan. Cuando el Omeprazol llega a la célula 1 hora después, las bombas están inactivas y la droga pasa de largo."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente en la UCI HCHM cursando sangrado digestivo alto (Úlcera péptica sangrante activa). ¿Cuál es la posología intravenosa del Omeprazol recomendada por las guías para inducir la hemostasia gástrica?",
        "opciones": [
            "Bolo inicial de 80 mg IV, seguido de una infusión continua de 8 mg/hora por 72 horas.",
            "20 mg IV diarios, en bolo, igual que la dosis de mantención oral.",
            "Bolo único de 200 mg IV y rotar inmediatamente a vía oral para evitar taquifilaxia.",
            "40 mg IV cada 12 horas de forma estricta."
        ],
        "respuesta": "Bolo inicial de 80 mg IV, seguido de una infusión continua de 8 mg/hora por 72 horas.",
        "feedback": "En una úlcera sangrante, las plaquetas y los coágulos se disuelven si el pH gástrico cae por debajo de 6 (el ácido destruye la cicatrización). Para asegurar un pH > 6 constante y permitir que la úlcera cicatrice, no sirve dar bolos intermitentes. Se necesita el bloqueo total de bombas con un bolo gigante (80mg) y un goteo continuo (8mg/h) por 3 días."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Paciente con ERGE crónico lleva tomando Omeprazol 40 mg diarios por 3 años. Decide suspenderlo bruscamente por su cuenta. A los tres días regresa con acidez refractaria, peor que antes de iniciar el tratamiento. ¿Qué fenómeno explica esto y cómo debió suspenderse?",
        "opciones": [
            "Síndrome de abstinencia serotoninérgica gástrica; requiere reemplazo con cinitaprida.",
            "Hipersecreción ácida de rebote. El bloqueo crónico induce hipergastrinemia e hiperplasia de células parietales. Se debe hacer un 'tapering' (reducción gradual de la dosis) a lo largo de 4-6 semanas.",
            "Reactiva la infección latente por H. pylori, generando úlceras fulminantes inmediatas.",
            "El cuerpo desarrolla anticuerpos anti-bomba de protones que inflaman la mucosa irreversiblemente."
        ],
        "respuesta": "Hipersecreción ácida de rebote. El bloqueo crónico induce hipergastrinemia e hiperplasia de células parietales. Se debe hacer un 'tapering' (reducción gradual de la dosis) a lo largo de 4-6 semanas.",
        "feedback": "Si le tapas la boca de ácido al estómago por años, el cuerpo detecta que falta ácido y libera cantidades industriales de la hormona Gastrina para compensar. La Gastrina hace que las células parietales se multipliquen (hiperplasia). Si quitas el Omeprazol de golpe, tienes un ejército extra de células tirando ácido a destajo. Hay que quitarlo bajando la dosis lentamente (tapering)."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "Gastroenterología",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Paciente post-IAM con stent coronario, en terapia dual con Ácido Acetilsalicílico y Clopidogrel. El médico general le agrega Omeprazol para 'proteger el estómago'. Según alertas internacionales (FDA/EMA), ¿qué interacción crítica ocurrirá?",
        "opciones": [
            "El Omeprazol potencia el sangrado al destruir la barrera de moco gástrico en presencia de Clopidogrel.",
            "El Omeprazol es un inhibidor fuerte del CYP2C19. El Clopidogrel es un profármaco que necesita esta enzima para activarse. La mezcla deja al paciente sin efecto antiplaquetario, riesgo altísimo de trombosis del stent.",
            "El Clopidogrel bloquea las bombas de protones de forma alostérica, causando toxicidad cruzada renal.",
            "Ambos fármacos compiten por el transportador P-gp a nivel renal, causando falla multiorgánica."
        ],
        "respuesta": "El Omeprazol es un inhibidor fuerte del CYP2C19. El Clopidogrel es un profármaco que necesita esta enzima para activarse. La mezcla deja al paciente sin efecto antiplaquetario, riesgo altísimo de trombosis del stent.",
        "feedback": "La interacción estrella en farmacia clínica cardiovascular. Si un paciente tiene un stent y toma Clopidogrel, y tú le das Omeprazol, le bloqueas la enzima (CYP2C19) que activa el Clopidogrel. El stent se puede tapar y el paciente se infarta de nuevo. Si un cardiópata necesita obligatoriamente un IBP, el indicado es el Pantoprazol, que tiene mínima interferencia con esta enzima."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente VIH positivo en terapia con Atazanavir (inhibidor de proteasa) inicia automedicación con Omeprazol 20 mg diarios porque sufre de pirosis. ¿Qué interacción farmacocinética (pH dependiente) se producirá?",
        "opciones": [
            "El Atazanavir necesita un ambiente altamente ácido para disolverse y absorberse. El Omeprazol sube el pH gástrico, anulando la absorción del antirretroviral, lo que lleva a falla terapéutica y resistencia viral.",
            "El aumento de pH gástrico induce la precipitación de cristales de Atazanavir en los riñones, causando urolitiasis.",
            "El Omeprazol inactiva los transportadores de membrana del VIH, actuando como sinergista antiviral.",
            "Se acelera el tránsito intestinal, causando diarrea severa y pérdida del medicamento por lavado mecánico."
        ],
        "respuesta": "El Atazanavir necesita un ambiente altamente ácido para disolverse y absorberse. El Omeprazol sube el pH gástrico, anulando la absorción del antirretroviral, lo que lleva a falla terapéutica y resistencia viral.",
        "feedback": "Al alterar la fisiología gástrica natural (subir el pH de 2 a 5 o 6), el Omeprazol arruina la absorción de fármacos que son bases débiles y que requieren ácido para disolverse, como los antifúngicos (Ketoconazol, Itraconazol), antirretrovirales (Atazanavir), y sales de Hierro. Un error de prescripción aquí puede costar el control inmunológico del VIH."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: ¿Por qué la coadministración de Omeprazol crónico con suplementos de Carbonato de Calcio en mujeres postmenopáusicas (en APS) resulta en una polifarmacia ineficaz y riesgosa?",
        "opciones": [
            "Porque el Omeprazol actúa como un quelante luminal de cationes divalentes, formando sales insolubles.",
            "Porque el Carbonato de Calcio requiere ácido gástrico para disociarse y liberar el ion calcio (Ca2+) para su absorción. Sin ácido, el calcio pasa de largo y aumenta el riesgo de osteoporosis y fracturas.",
            "Porque el calcio inactiva la bomba H+/K+ ATPasa de forma competitiva, anulando el efecto del Omeprazol.",
            "Porque el Omeprazol acelera la excreción renal de calcio al bloquear la activación de vitamina D."
        ],
        "respuesta": "Porque el Carbonato de Calcio requiere ácido gástrico para disociarse y liberar el ion calcio (Ca2+) para su absorción. Sin ácido, el calcio pasa de largo y aumenta el riesgo de osteoporosis y fracturas.",
        "feedback": "El Carbonato de Calcio (la sal más barata y usada en la red de salud pública) es como una piedra; necesita ácido de estómago para romperse y liberar el calcio libre que se absorbe en el intestino. Si la abuelita toma Omeprazol crónico, no hay ácido, no hay absorción de calcio, y el hueso se descalcifica. La solución es rotar a Citrato de Calcio, que se absorbe independiente del pH."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "Gastroenterología",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Paciente de 70 años lleva 2 semanas con Omeprazol endovenoso en medicina interna. Inicia con diarrea acuosa severa (muy fétida) y leucocitosis. ¿Qué RAM infecciosa, advertida por alertas sanitarias, está directamente ligada al uso hospitalario de IBPs?",
        "opciones": [
            "Infección por Clostridioides difficile. El ácido gástrico es una barrera bactericida; al anularlo, las esporas ingresan viables al colon y colonizan oportunistamente.",
            "Sobrecrecimiento del Helicobacter pylori por adaptación aberrante al pH alcalino.",
            "Translocación bacteriana de E. coli desde el lumen intestinal hacia la sangre (Sepsis endógena).",
            "Amebiasis intestinal fulminante mediada por trofozoítos resistentes."
        ],
        "respuesta": "Infección por Clostridioides difficile. El ácido gástrico es una barrera bactericida; al anularlo, las esporas ingresan viables al colon y colonizan oportunistamente.",
        "feedback": "El estómago es como una piscina de ácido que esteriliza todo lo que comemos, tragamos o respiramos hacia la vía digestiva. Si apagas el ácido con Omeprazol, las bacterias patógenas y esporas (como C. difficile) pasan intactas hacia el intestino. Los IBP son un factor de riesgo gigantesco para diarreas intrahospitalarias severas."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: Paciente que consume Omeprazol por más de tres años llega a la urgencia con espasmos musculares (tetania), fasciculaciones y un electrocardiograma con arritmias ventriculares. Al revisar sus laboratorios, el Calcio y el Potasio están bajos. ¿Qué alteración electrolítica primaria, inducida crónicamente por el IBP, justifica este caos?",
        "opciones": [
            "Hiponatremia severa por dilución.",
            "Hipomagnesemia severa.",
            "Hipocloremia alcalótica.",
            "Hipofosfatemia severa."
        ],
        "respuesta": "Hipomagnesemia severa.",
        "feedback": "Alerta de farmacovigilancia seria (FDA). El uso crónico de IBP altera los canales TRPM6/7 en el intestino, bloqueando la absorción activa de Magnesio. El magnesio es clave para que funcionen las glándulas paratiroides (que regulan el calcio) y las bombas de la membrana (que regulan el potasio). Si cae el magnesio, caen el calcio y el potasio en cadena, causando un caos arrítmico y neuromuscular."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: ¿Qué hallazgo histológico es común (y generalmente benigno) en biopsias gástricas de pacientes con uso ininterrumpido de Omeprazol por más de 5 años, secundario a la hipergastrinemia crónica?",
        "opciones": [
            "Adenocarcinoma gástrico de tipo difuso (células en anillo de sello).",
            "Pólipos de glándulas fúndicas.",
            "Metaplasia intestinal de la mucosa gástrica (Esófago de Barrett intragástrico).",
            "Necrosis coagulativa y atrofia de las células principales."
        ],
        "respuesta": "Pólipos de glándulas fúndicas.",
        "feedback": "La Gastrina (que se dispara porque el estómago no detecta ácido) actúa como un factor de crecimiento celular (trófico) sobre la mucosa gástrica del fondo. Después de años de uso continuo de IBP, aparecen pequeños pólipos benignos en el estómago. Rara vez malignizan, pero en la endoscopia son el sello visual del abuso crónico de Omeprazol."
    },

    # --- CATEGORÍA: 🏥 Caso Clínico ---
    {
        "familia": "Gastroenterología",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: La guía MINSAL para erradicación de Helicobacter pylori exige un esquema triconjugado (Ej: Claritromicina + Amoxicilina + Omeprazol) por 14 días. ¿Cuál es el rol FARMACOCINÉTICO exacto del Omeprazol dentro de este esquema antimicrobiano?",
        "opciones": [
            "Tiene efecto antibacteriano directo y destructivo contra las paredes del H. pylori.",
            "Al subir el pH gástrico > 6, previene la degradación en ácido de la Amoxicilina y la Claritromicina, aumentando su biodisponibilidad y vida media en el lumen estomacal.",
            "Inhibir competitivamente la enzima ureasa del Helicobacter pylori para asfixiar químicamente a la bacteria.",
            "Estimular la secreción de moco gástrico rico en bicarbonato que atrapa a la bacteria facilitando la fagocitosis de macrófagos."
        ],
        "respuesta": "Al subir el pH gástrico > 6, previene la degradación en ácido de la Amoxicilina y la Claritromicina, aumentando su biodisponibilidad y vida media en el lumen estomacal.",
        "feedback": "Los antibióticos como la Amoxicilina y los macrólidos son moléculas inestables que se destruyen en ambientes muy ácidos. Además, el H. pylori entra en fase de replicación activa (se vuelve vulnerable a los ATB) cuando el pH sube. El Omeprazol no mata a la bacteria por sí solo, pero pavimenta el terreno (sube el pH) para que los antibióticos sobrevivan en el estómago y logren penetrar el moco."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Paciente de 45 años, sano, sin patologías críticas, está ingresado en cama de medicina básica por neumonía comunitaria. En su indicación médica aparece Omeprazol 20 mg/día como 'protector gástrico profiláctico'. Como QF clínico evaluador, ¿qué acción farmacoterapéutica corresponde?",
        "opciones": [
            "Validar la receta inmediatamente. Todo paciente hospitalizado por más de 48 horas requiere un IBP para profilaxis de úlcera por estrés.",
            "Recomendar la desprescripción (suspensión). La profilaxis de úlcera por estrés solo está indicada en UCI bajo criterios de alto riesgo (ej. ventilación mecánica >48h, coagulopatía). En sala básica genera riesgos innecesarios (Neumonía, C. difficile).",
            "Sugerir doblar la dosis a 40 mg porque los antibióticos utilizados para neumonía causan úlceras perforantes graves.",
            "Sugerir el cambio por Sucralfato, que es el protector universal aprobado para todo paciente hospitalizado."
        ],
        "respuesta": "Recomendar la desprescripción (suspensión). La profilaxis de úlcera por estrés solo está indicada en UCI bajo criterios de alto riesgo (ej. ventilación mecánica >48h, coagulopatía). En sala básica genera riesgos innecesarios (Neumonía, C. difficile).",
        "feedback": "La pandemia silenciosa de los hospitales chilenos: el 'protector gástrico' por si acaso. El Omeprazol no es inocuo. Darlo en una sala de baja complejidad aumenta el riesgo de que el paciente haga una neumonía aspirativa (al quitar el ácido bactericida del estómago) o se infecte con C. difficile. Si el paciente no está intubado, no tiene falla de coagulación o no está gran quemado, NO requiere IBP profiláctico."
    },
    {
        "familia": "Gastroenterología",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Paciente adulto mayor en CESFAM que lleva 6 años usando Omeprazol porque 'toma muchas pastillas para el corazón y le arde la guata'. Según los criterios de Beers y la evidencia clínica de desprescripción, además del riesgo de caídas, ¿cuál es el peligro óseo a largo plazo de mantener esta prescripción injustificada?",
        "opciones": [
            "Aumento del riesgo de fracturas de cadera y columna, ya que la aclorhidria crónica impide la absorción de calcio dietético y altera la homeostasis del recambio óseo.",
            "Desarrollo precoz de osteoartritis inflamatoria por acumulación de la molécula intacta en el líquido sinovial.",
            "Fusión de las vértebras cervicales (espondilosis) inducida por hipermagnesemia de rebote.",
            "Gota poliarticular aguda debido a la inhibición de la secreción tubular de ácido úrico en el túbulo proximal."
        ],
        "respuesta": "Aumento del riesgo de fracturas de cadera y columna, ya que la aclorhidria crónica impide la absorción de calcio dietético y altera la homeostasis del recambio óseo.",
        "feedback": "Un estómago sin ácido es un estómago que no puede extraer el calcio de los alimentos (lácteos, verduras, carne). En adultos mayores, mantener Omeprazol de forma injustificada por 6 años es condenarlos a tener huesos porosos. Las guías exigen reevaluar a todo paciente con IBP crónico y tratar de hacer un tapering si no hay indicación dura (como Esófago de Barrett o uso crónico de corticoides+AINEs)."
    },
# ==========================================
    # LOTE: AMOXICILINA / ÁC. CLAVULÁNICO (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "Antimicrobianos",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: En la asociación de Amoxicilina con Ácido Clavulánico, ¿cuál es el rol farmacodinámico exacto del Ácido Clavulánico contra bacterias como H. influenzae o M. catarrhalis?",
        "opciones": [
            "Inhibe la subunidad 50S del ribosoma bacteriano, aportando un efecto bacteriostático adicional.",
            "Posee actividad bactericida intrínseca al inhibir las PBP2a, expandiendo el espectro hacia el SAMR.",
            "Es un inhibidor suicida. No mata a la bacteria, sino que se une irreversiblemente al sitio activo de las enzimas betalactamasas, impidiendo que estas hidrolicen el anillo betalactámico de la Amoxicilina.",
            "Altera la permeabilidad de la membrana externa, permitiendo que la Amoxicilina ingrese masivamente por las porinas."
        ],
        "respuesta": "Es un inhibidor suicida. No mata a la bacteria, sino que se une irreversiblemente al sitio activo de las enzimas betalactamasas, impidiendo que estas hidrolicen el anillo betalactámico de la Amoxicilina.",
        "feedback": "El Ácido Clavulánico es el 'guardaespaldas' de la Amoxicilina. Por sí solo tiene cero poder antibiótico. Su estructura molecular engaña a las enzimas bacterianas (betalactamasas) que buscan destruir la amoxicilina. La enzima ataca al clavulánico y quedan fusionados para siempre, dejando a la amoxicilina libre para destruir la pared celular."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: Sabiendo que el Ácido Clavulánico inactiva betalactamasas, ¿por qué la mezcla Amoxi/Clav es inútil frente a un 'Streptococcus pneumoniae' resistente a penicilina (PRSP)?",
        "opciones": [
            "Porque el Neumococo produce un tipo especial de betalactamasa (Metalo-betalactamasa tipo VIM) que el clavulánico no puede bloquear.",
            "Porque el mecanismo de resistencia del Neumococo NO es producir enzimas betalactamasas, sino que muta la estructura de sus PBP (proteínas de unión a penicilina), impidiendo que la amoxicilina se una a ellas.",
            "Porque el Neumococo es una bacteria intracelular obligada, y la molécula combinada es demasiado grande para atravesar los macrófagos.",
            "Porque el Neumococo inactiva directamente al ácido clavulánico mediante bombas de eflujo activo."
        ],
        "respuesta": "Porque el mecanismo de resistencia del Neumococo NO es producir enzimas betalactamasas, sino que muta la estructura de sus PBP (proteínas de unión a penicilina), impidiendo que la amoxicilina se una a ellas.",
        "feedback": "Trampa clásica de infectología. El Neumococo NUNCA produce betalactamasas. Se vuelve resistente modificando sus PBP (la cerradura donde entra la amoxicilina). Como no hay enzimas que bloquear, el clavulánico aquí no sirve para absolutamente nada. Para matar a un neumococo resistente, solo se debe subir enormemente la dosis de amoxicilina pura (ej. 90-100 mg/kg/día)."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: ¿Qué clase específica de betalactamasas, según la clasificación de Ambler, es inhibida eficientemente por el Ácido Clavulánico?",
        "opciones": [
            "Clase B (Metalo-betalactamasas dependientes de Zinc).",
            "Clase C (Cefalosporinasas tipo AmpC, inducibles cromosómicamente).",
            "Clase A (Betalactamasas de espectro extendido - BLEE y penicilinasas clásicas como TEM-1 o SHV-1).",
            "Todas las clases de betalactamasas por igual."
        ],
        "respuesta": "Clase A (Betalactamasas de espectro extendido - BLEE y penicilinasas clásicas como TEM-1 o SHV-1).",
        "feedback": "El clavulánico es bueno, pero no es Dios. Inhibe excelente las enzimas Clase A (las más comunes en E. coli y Klebsiella ambulatorias). Sin embargo, es completamente inútil contra las enzimas AmpC (Clase C) de la familia SPACE (Serratia, Pseudomonas, Acinetobacter, Citrobacter, Enterobacter) y las temidas carbapenemasas (Clase B)."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "Antimicrobianos",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: En APS existen presentaciones de 500/125 mg y 875/125 mg. ¿Por qué al subir la dosis de amoxicilina (de 500 a 875) el laboratorio mantiene estática la dosis de clavulánico (125 mg) en vez de aumentarla proporcionalmente?",
        "opciones": [
            "Porque el ácido clavulánico inhibe su propia absorción a dosis mayores a 150 mg.",
            "Porque un aumento en la dosis de ácido clavulánico por encima de 125 mg por toma dispara drásticamente la toxicidad gastrointestinal (diarrea severa y dismotilidad).",
            "Porque a dosis mayores, el clavulánico cristaliza en los túbulos renales.",
            "Porque la legislación chilena (ISP) prohíbe dosis de inhibidores de betalactamasas mayores a 125 mg en atención ambulatoria."
        ],
        "respuesta": "Porque un aumento en la dosis de ácido clavulánico por encima de 125 mg por toma dispara drásticamente la toxicidad gastrointestinal (diarrea severa y dismotilidad).",
        "feedback": "Manejo galénico crítico. El Ácido Clavulánico es un potente estimulador de la motilidad intestinal. Si le das a un adulto dos pastillas de 500/125 mg juntas (para llegar a 1g de amoxi), le estás metiendo 250 mg de clavulánico de golpe: diarrea explosiva garantizada. Por eso se creó la pastilla de 875/125, para dar más amoxicilina sin reventar el estómago."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente adulto mayor con falla renal crónica (ClCr = 20 mL/min) acude al CESFAM con una exacerbación infecciosa de EPOC. Según las guías farmacocinéticas, ¿qué ajuste es obligatorio si se indica Amoxicilina/Ácido Clavulánico?",
        "opciones": [
            "Usar la presentación 875/125 mg cada 24 horas.",
            "Usar la presentación 500/125 mg cada 12 o 24 horas, y está CONTRAINDICADA la presentación de 875/125 mg porque el clavulánico se acumula a niveles tóxicos.",
            "No requiere ajuste porque ambos se excretan principalmente por la bilis.",
            "Disminuir la dosis de Amoxicilina pero agregar Probenecid para forzar su excreción renal."
        ],
        "respuesta": "Usar la presentación 500/125 mg cada 12 o 24 horas, y está CONTRAINDICADA la presentación de 875/125 mg porque el clavulánico se acumula a niveles tóxicos.",
        "feedback": "Ojo con el riñón. El clavulánico depende críticamente de la filtración glomerular. Si el riñón funciona a menos de 30 mL/min, el fármaco de 875/125 mg (que se da cada 12h) está estrictamente contraindicado por riesgo de toxicidad y neurotoxicidad. Se debe usar solo la dosis de 500/125mg separando el intervalo a 12 o 24 horas."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Como betalactámico, la eficacia de la Amoxicilina depende del tiempo sobre la CIM (T > CIM). Sabiendo esto, ¿por qué la pauta de 875/125 mg se administra cada 12 horas y no cada 8 horas como la amoxicilina pura de 500mg?",
        "opciones": [
            "Porque el clavulánico tiene una vida media de 24 horas y protege a la amoxicilina todo el día.",
            "Para mejorar la adherencia del paciente, asumiendo un leve riesgo de fracaso terapéutico.",
            "Porque la dosis de 875 mg alcanza concentraciones plasmáticas tan altas que logra mantener los niveles por encima de la CIM bacteriana durante al menos el 40-50% del intervalo de 12 horas.",
            "Porque a dosis de 875 mg el fármaco cambia a un perfil de cinética concentración-dependiente."
        ],
        "respuesta": "Porque la dosis de 875 mg alcanza concentraciones plasmáticas tan altas que logra mantener los niveles por encima de la CIM bacteriana durante al menos el 40-50% del intervalo de 12 horas.",
        "feedback": "Cálculo PK/PD puro. Los betalactámicos necesitan estar por encima de la CIM de la bacteria al menos el 40-50% del tiempo entre tomas. Al inyectar 875 mg (una curva altísima), la droga tarda mucho más tiempo en caer por debajo de la línea crítica (CIM), lo que nos permite separar las tomas a cada 12 horas sin perder eficacia bactericida."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "Antimicrobianos",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Paciente de APS con Fibrilación Auricular, anticoagulado crónicamente con Acenocumarol (Neosintrom), con INR estable en 2.5. Acude al dentista y le recetan Amoxi/Clav por 7 días por un absceso dental. ¿Qué interacción clínica puede resultar en una hemorragia letal?",
        "opciones": [
            "La amoxicilina desplaza al Acenocumarol de la albúmina sérica, liberando un 90% de fracción libre tóxica.",
            "El antibiótico destruye la flora intestinal bacteriana normal, disminuyendo drásticamente la síntesis endógena de Vitamina K. Esto potencia el efecto del anticoagulante y dispara el INR.",
            "El ácido clavulánico inhibe la enzima CYP2C9, bloqueando el metabolismo del Acenocumarol.",
            "Se produce una inhibición directa de la agregación plaquetaria por el anillo betalactámico."
        ],
        "respuesta": "El antibiótico destruye la flora intestinal bacteriana normal, disminuyendo drásticamente la síntesis endógena de Vitamina K. Esto potencia el efecto del anticoagulante y dispara el INR.",
        "feedback": "Interacción de libro de infectología y cardiología. Los pacientes anticoagulados con antagonistas de la vitamina K dependen, en parte, de la vitamina K que fabrican las bacterias buenas del intestino. La dupla Amoxi/Clav hace un 'bombardeo' y barre con esta flora. El paciente se queda sin vitamina K, el anticoagulante actúa sin freno, el INR vuela por encima de 6 y el paciente puede sufrir hemorragia cerebral."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente con Artritis Reumatoide en tratamiento con Metotrexato oral (inmunosupresor). Inicia Amoxi/Clav por una infección respiratoria. A los 5 días presenta mucositis severa, úlceras orales y pancitopenia. ¿Cuál es el mecanismo de esta interacción?",
        "opciones": [
            "La amoxicilina inhibe la enzima dihidrofolato reductasa hepática de forma sinérgica al Metotrexato.",
            "Ambos fármacos compiten agresivamente por la secreción tubular renal pasiva. La amoxicilina satura los transportadores OAT, impidiendo la salida del Metotrexato, el cual se acumula a niveles tóxicos.",
            "El clavulánico cambia el pH de la orina, induciendo la cristalización del Metotrexato en la pelvis renal.",
            "Se activa una reacción autoinmune tipo III por depósito de complejos de penicilina-metotrexato en las mucosas."
        ],
        "respuesta": "Ambos fármacos compiten agresivamente por la secreción tubular renal pasiva. La amoxicilina satura los transportadores OAT, impidiendo la salida del Metotrexato, el cual se acumula a niveles tóxicos.",
        "feedback": "Peligro en Reumatología. El Metotrexato (MTX) se elimina por la orina a través de unas 'puertas' llamadas transportadores OAT (aniones orgánicos). La Amoxicilina usa exactamente las mismas puertas. Cuando llegan juntos, la Amoxicilina acapara los transportadores y el MTX se queda en la sangre. Como el MTX es altamente citotóxico, destruye la médula ósea y las mucosas en cuestión de días."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: Un paciente cursando crisis de Gota es tratado con Alopurinol en el policlínico. Una semana después, se le prescribe Amoxi/Clav por una otitis. ¿Qué RAM dermatológica tiene un riesgo altísimo de aparecer con esta combinación?",
        "opciones": [
            "Síndrome de Stevens-Johnson inmediato mediado por IgE.",
            "Exantema maculopapular difuso y pruriginoso (Erupción cutánea), cuya incidencia se multiplica casi al 20% cuando se asocian estos dos fármacos.",
            "Fotosensibilidad severa con ampollas tras la exposición solar leve.",
            "Necrosis epidérmica tóxica puramente desencadenada por el ácido clavulánico."
        ],
        "respuesta": "Exantema maculopapular difuso y pruriginoso (Erupción cutánea), cuya incidencia se multiplica casi al 20% cuando se asocian estos dos fármacos.",
        "feedback": "Interacción idiosincrática histórica. Dar Amoxicilina a alguien que está tomando Alopurinol dispara la incidencia de rash (erupción de manchas rojas) en todo el cuerpo. No es una alergia real a la penicilina (mediada por IgE), sino un rash maculopapular secundario a la combinación química, pero obliga a suspender el tratamiento por la molestia clínica y el diagnóstico confuso."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "Antimicrobianos",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: La RAM más común y que causa mayor abandono del tratamiento con Amoxi/Clav es la diarrea. ¿Cuál es la fisiopatología principal de esta RAM en los primeros 3 días de uso, diferenciándola de una infección por C. difficile?",
        "opciones": [
            "Inflamación directa de la mucosa gástrica por el pH ácido de la amoxicilina.",
            "Bloqueo de la reabsorción de sales biliares en el íleon terminal.",
            "Efecto procinético directo del Ácido Clavulánico sobre el intestino delgado y alteración inmediata del microbioma osmótico, resultando en deposiciones blandas sin sangre ni leucocitos.",
            "Invasión de Candida albicans en el ciego en las primeras 24 horas."
        ],
        "respuesta": "Efecto procinético directo del Ácido Clavulánico sobre el intestino delgado y alteración inmediata del microbioma osmótico, resultando en deposiciones blandas sin sangre ni leucocitos.",
        "feedback": "El clavulánico es una molécula súper irritante para las tripas. Acelera el tránsito intestinal por sí mismo. Sumado a que la amoxicilina mata algunas bacterias buenas (causando mala absorción osmótica), el resultado es diarrea casi segura. Si la diarrea aparece al inicio, sin fiebre ni sangre, es RAM de la pastilla. Si aparece a la semana, con fiebre y olor pútrido, cuidado con C. difficile."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: Un hombre de 65 años termina un curso de 10 días de Amoxi/Clav por una sinusitis. Dos semanas DESPUÉS de terminar el fármaco, acude con ictericia (piel amarilla), coluria y picazón severa. ¿Cuál es la RAM idiosincrática característica del fármaco que explica este cuadro?",
        "opciones": [
            "Cirrosis fulminante por depósito de amoxicilina en los hepatocitos.",
            "Hepatitis Colestásica aguda. Es una toxicidad hepática directa o inmunológica ligada exclusivamente al Ácido Clavulánico, más frecuente en hombres mayores y que puede aparecer semanas después del tratamiento.",
            "Obstrucción biliar por cálculos de penicilina cristalizada.",
            "Necrosis hepática centrolobulillar dependiente del citocromo CYP3A4."
        ],
        "respuesta": "Hepatitis Colestásica aguda. Es una toxicidad hepática directa o inmunológica ligada exclusivamente al Ácido Clavulánico, más frecuente en hombres mayores y que puede aparecer semanas después del tratamiento.",
        "feedback": "RAM de farmacovigilancia. El Ácido Clavulánico tiene un potencial hepatotóxico raro pero grave. Causa inflamación de los conductos biliares (colestasis), lo que tapa la salida de bilirrubina (el paciente se pone amarillo). Lo más loco es que puede debutar hasta 6 semanas después de haber tomado la última pastilla. Por esto, los tratamientos largos (>14 días) son riesgosos en ancianos."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: Paciente refiere que 'de niño le salieron ronchas' con la Amoxicilina. Requiere profilaxis antibiótica, y el médico sugiere Cefadroxilo (una cefalosporina de 1ra generación). Como QF, ¿qué riesgo cruzado real existe entre la alergia a penicilinas y las cefalosporinas?",
        "opciones": [
            "100% de reactividad cruzada porque ambos poseen el mismo anillo betalactámico.",
            "Existe un riesgo de reactividad cruzada (aprox. 1-10%), principalmente si ambos fármacos comparten una cadena lateral R1 idéntica (ej. Amoxicilina y Cefadroxilo la comparten), aumentando el riesgo de anafilaxia.",
            "Cero riesgo, las cefalosporinas usan vías enzimáticas totalmente diferentes.",
            "Riesgo exclusivo de anemia hemolítica, pero no anafilaxia IgE."
        ],
        "respuesta": "Existe un riesgo de reactividad cruzada (aprox. 1-10%), principalmente si ambos fármacos comparten una cadena lateral R1 idéntica (ej. Amoxicilina y Cefadroxilo la comparten), aumentando el riesgo de anafilaxia.",
        "feedback": "Cuidado con la alergia cruzada. El cuerpo humano rara vez hace alergia al 'anillo betalactámico' central; casi siempre la alergia es a las cadenas laterales (R1) que cuelgan del anillo. Curiosamente, la Amoxicilina (penicilina) y el Cefadroxilo (cefalosporina) tienen exactamente la misma cadena R1. Si el paciente hizo anafilaxia a la amoxi, darle cefadroxilo es jugar a la ruleta rusa."
    },

    # --- CATEGORÍA: 🏥 Caso Clínico ---
    {
        "familia": "Antimicrobianos",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Llega a tu farmacia un paciente mordido por un perro callejero en la mano hace 12 horas. La herida está roja y caliente. El médico del SAPU le receta Amoxi/Clav 875/125 mg cada 12 horas por 7 días. ¿Cuál es el fundamento microbiológico de usar esta mezcla y no Cefalexina o Flucloxacilina?",
        "opciones": [
            "Porque la boca del perro transmite Clostridium tetani, que es resistente a penicilinas simples.",
            "Porque la principal bacteria de las mordeduras de perro/gato es Pasteurella multocida, que puede producir betalactamasas. Amoxi/Clav es la primera línea mundial porque cubre Pasteurella, Estafilococos y anaerobios de la boca del animal.",
            "Para evitar la rabia, ya que el clavulánico tiene acción antiviral profiláctica.",
            "Porque el fármaco penetra mejor en el tejido óseo en caso de mordeduras profundas."
        ],
        "respuesta": "Porque la principal bacteria de las mordeduras de perro/gato es Pasteurella multocida, que puede producir betalactamasas. Amoxi/Clav es la primera línea mundial porque cubre Pasteurella, Estafilococos y anaerobios de la boca del animal.",
        "feedback": "Las mordeduras (perro, gato o humano) son un caldo de cultivo asqueroso. Tienen bacterias aerobias y anaerobias. La Flucloxacilina cubre la piel (Staphylo), pero NO sirve para la clásica bacteria de boca de animal (Pasteurella) ni para los anaerobios. El Amoxi/Clavulánico barre con la flora de la boca del animal y la piel del paciente al mismo tiempo. Es la terapia empírica de oro."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Niño de 3 años con Otitis Media Aguda a repetición o fracaso a tratamiento previo. El pediatra indica Amoxi/Clavulánico en una dosis inusualmente alta de Amoxicilina (90 mg/kg/día) pero manteniendo la presentación de baja proporción de Clavulánico (ej. suspensión 7:1 o 14:1). ¿Por qué se hace esta matemática posológica?",
        "opciones": [
            "Para forzar la apertura de la barrera hematoencefálica y evitar meningitis.",
            "Porque el oído medio requiere dosis masivas de Amoxicilina para lograr concentraciones bactericidas contra el Neumococo Resistente (PRSP), pero si aumentamos el Clavulánico a la misma velocidad, le causaremos una diarrea severa e intratable al niño.",
            "Para compensar el rápido metabolismo de primer paso hepático que tienen los niños de 3 años.",
            "Porque a esa edad el ácido clavulánico causa cierre de los cartílagos epifisiarios (crecimiento)."
        ],
        "respuesta": "Porque el oído medio requiere dosis masivas de Amoxicilina para lograr concentraciones bactericidas contra el Neumococo Resistente (PRSP), pero si aumentamos el Clavulánico a la misma velocidad, le causaremos una diarrea severa e intratable al niño.",
        "feedback": "Manejo pediátrico de élite. El neumococo resistente te obliga a subir la amoxicilina al cielo (80-90 mg/kg). Pero si usas la suspensión común (donde Amoxi y Clavulánico van de la mano 4:1), le estarías dando dosis tóxicas de clavulánico al niño y lo matarías de diarrea. Por eso existen formulaciones 'altas en amoxi, bajas en clav' (proporción 7:1 o 14:1) para matar la bacteria sin romper el intestino."
    },
    {
        "familia": "Antimicrobianos",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Paciente joven acude al consultorio con dolor de garganta intenso, ganglios del cuello muy inflamados y fatiga extrema. El médico, creyendo que es Amigdalitis Bacteriana, le receta Amoxicilina. A los 3 días el paciente regresa con todo el cuerpo cubierto de un sarpullido rojo intenso (rash morbiliforme), pero jura no ser alérgico. ¿Qué error de diagnóstico y qué reacción cruzada ocurrieron?",
        "opciones": [
            "El paciente tenía Escarlatina, y el rash es producto de las toxinas del Estreptococo destruido.",
            "El paciente cursaba con Mononucleosis Infecciosa (Virus Epstein-Barr). Dar Amoxicilina (o derivados) a un paciente con esta infección viral desencadena un rash cutáneo masivo en más del 90% de los casos, que NO es alergia, sino una reacción linfocítica tóxica.",
            "El paciente desarrolló Síndrome de Stevens-Johnson por una amigdalitis resistente.",
            "Hubo interacción con paracetamol, generando fotosensibilidad."
        ],
        "respuesta": "El paciente cursaba con Mononucleosis Infecciosa (Virus Epstein-Barr). Dar Amoxicilina (o derivados) a un paciente con esta infección viral desencadena un rash cutáneo masivo en más del 90% de los casos, que NO es alergia, sino una reacción linfocítica tóxica.",
        "feedback": "Un clásico de urgencias ambulatorias. La 'Enfermedad del Beso' (Mononucleosis) produce placas de pus en las amígdalas idénticas a las de las bacterias. Si el médico se equivoca de diagnóstico y le dispara Amoxicilina a este virus, el sistema inmune colapsa y genera un sarpullido gigante (rash morbiliforme) en todo el cuerpo. No es alergia, es un error médico."
    },
# ==========================================
    # LOTE: TRAMADOL (15 VARIACIONES)
    # ==========================================
    
    # --- CATEGORÍA: ⚙️ Mecanismo ---
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 1: A diferencia de la morfina, que es un agonista opioide puro, el Tramadol posee un mecanismo de acción dual. ¿Cuáles son las dos vías farmacodinámicas mediante las cuales el Tramadol ejerce su efecto analgésico?",
        "opciones": [
            "Es agonista del receptor opioide Mu (μ) y a la vez inhibe la enzima ciclooxigenasa-2 (COX-2) en el asta dorsal de la médula.",
            "Es un agonista débil del receptor opioide Mu (μ) y también inhibe la recaptación sináptica de Serotonina y Noradrenalina (IRSN) en las vías descendentes del dolor.",
            "Es antagonista de los receptores NMDA y bloquea los canales de sodio voltaje dependientes tipo lidocaína.",
            "Estimula los receptores GABA-A induciendo sedación profunda y actúa como agonista parcial del receptor Kappa (κ)."
        ],
        "respuesta": "Es un agonista débil del receptor opioide Mu (μ) y también inhibe la recaptación sináptica de Serotonina y Noradrenalina (IRSN) en las vías descendentes del dolor.",
        "feedback": "El Tramadol es una molécula fascinante de doble filo. Su componente opioide es débil, pero su poder real radica en que se comporta casi igual que un antidepresivo dual (tipo Venlafaxina o Duloxetina). Al dejar más Serotonina y Noradrenalina libres en la médula, estas 'apagan' la señal de dolor que intenta subir al cerebro."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 2: El Tramadol comercializado (racémico) es una mezcla de dos enantiómeros (Isómero + y Isómero -). ¿Por qué es necesaria la combinación de ambos enantiómeros para lograr la analgesia total?",
        "opciones": [
            "Porque el isómero (+) estimula los receptores Mu, y el isómero (-) evita la depresión respiratoria.",
            "Porque el isómero (+) inhibe la recaptación de Serotonina, mientras que el isómero (-) inhibe la recaptación de Noradrenalina, logrando la sinergia analgésica.",
            "Porque un isómero es de liberación inmediata y el otro actúa como una matriz de liberación prolongada.",
            "Porque el isómero (+) cruza la barrera hematoencefálica y el isómero (-) actúa en el sistema nervioso periférico."
        ],
        "respuesta": "Porque el isómero (+) inhibe la recaptación de Serotonina, mientras que el isómero (-) inhibe la recaptación de Noradrenalina, logrando la sinergia analgésica.",
        "feedback": "Farmacología de ultra élite. El Tramadol es un espejo molecular. La forma (+) inhibe la recaptación de Serotonina y es el precursor del metabolito opioide. La forma (-) se encarga exclusivamente de inhibir la recaptación de Noradrenalina. Juntos, complementan la vía inhibidora del dolor. Si separas la molécula, pierde casi todo su efecto."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "⚙️ Mecanismo",
        "pregunta": "Variación 3: Un concepto crucial para el QF es que el Tramadol, en estricto rigor, es un PROFÁRMACO. ¿Qué enzima hepática y qué metabolito activo son responsables de la verdadera analgesia opioide del medicamento?",
        "opciones": [
            "El CYP3A4 desmetila el Tramadol transformándolo en N-desmetiltramadol, el cual tiene alta afinidad por el receptor Kappa.",
            "El CYP2D6 metaboliza el Tramadol formando O-desmetiltramadol (Metabolito M1), el cual tiene 200 veces más afinidad por el receptor Mu que el compuesto original.",
            "El CYP1A2 oxida la molécula formando Glucurónido de Tramadol, el cual cruza fácilmente al LCR.",
            "La enzima Glucuronosiltransferasa (UGT) lo conjuga con ácido glucurónico activando su efecto noradrenérgico."
        ],
        "respuesta": "El CYP2D6 metaboliza el Tramadol formando O-desmetiltramadol (Metabolito M1), el cual tiene 200 veces más afinidad por el receptor Mu que el compuesto original.",
        "feedback": "La trampa genética del Tramadol. La pastilla que el paciente se traga no quita el dolor opioide por sí sola. Tiene que viajar al hígado y ser procesada por el citocromo CYP2D6, quien le corta un pedazo (O-desmetilación) para crear el Metabolito M1. Este metabolito es la verdadera 'morfina' del fármaco. Si el paciente no tiene esta enzima o la tiene inhibida, el Tramadol no le quitará el dolor."
    },

    # --- CATEGORÍA: 💊 Dosis ---
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 1: Paciente adulto de 60 años con lumbago crónico severo. El médico le prescribe Tramadol en gotas (100 mg/mL). ¿Cuál es la dosis máxima diaria establecida por las guías clínicas para población adulta sin disfunción renal ni hepática?",
        "opciones": [
            "200 mg al día.",
            "300 mg al día.",
            "400 mg al día.",
            "600 mg al día."
        ],
        "respuesta": "400 mg al día.",
        "feedback": "El tope universal del Tramadol en adultos sanos es de 400 mg/día (usualmente repartido en 100 mg cada 6 horas). En adultos mayores de 75 años, el límite se baja a 300 mg/día. Si se supera este techo, no se gana más analgesia, pero el riesgo de convulsiones y síndrome serotoninérgico se dispara exponencialmente."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 2: Paciente de 70 años con Enfermedad Renal Crónica Etapa 4 (ClCr de 20 mL/min). Se le debe iniciar Tramadol por dolor osteoarticular. ¿Cuál es el ajuste posológico farmacocinético obligatorio en este caso?",
        "opciones": [
            "No requiere ajuste, el Tramadol es de excreción exclusivamente hepática y biliar.",
            "Aumentar el intervalo de dosificación a cada 12 horas, con una dosis máxima diaria que no supere los 200 mg.",
            "Se debe rotar obligatoriamente a Fentanilo en parche transdérmico, ya que el Tramadol está contraindicado en VFG < 30.",
            "Dar dosis plenas, pero asociar a naloxona oral para evitar constipación urémica."
        ],
        "respuesta": "Aumentar el intervalo de dosificación a cada 12 horas, con una dosis máxima diaria que no supere los 200 mg.",
        "feedback": "El metabolito M1 (el activo) se excreta por el riñón. Si el riñón no filtra bien (ClCr < 30 mL/min), el M1 se acumula a niveles tóxicos, causando profunda sedación y depresión respiratoria. La indicación clínica es alargar las tomas a 12 horas y nunca pasar de 200 mg al día."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "💊 Dosis",
        "pregunta": "Variación 3: Al iniciar terapia con Tramadol en APS, especialmente en adultos mayores, el QF debe instruir al paciente sobre la titulación lenta ('Start low, go slow'). ¿Cuál es la razón clínica principal para no iniciar con dosis plenas de 50 mg cada 8 horas desde el día uno?",
        "opciones": [
            "Para evitar la inducción de úlceras gástricas agudas mediadas por serotonina.",
            "Para mitigar el riesgo de náuseas severas, vómitos intratables y mareos vertiginosos que ocurren al estimular súbitamente la zona gatillo quimiorreceptora (CTZ) del bulbo raquídeo.",
            "Para prevenir la bradicardia sinusal y bloqueos AV de tercer grado.",
            "Para evitar el agotamiento de las reservas neuronales de noradrenalina y la consecuente depresión mayor."
        ],
        "respuesta": "Para mitigar el riesgo de náuseas severas, vómitos intratables y mareos vertiginosos que ocurren al estimular súbitamente la zona gatillo quimiorreceptora (CTZ) del bulbo raquídeo.",
        "feedback": "La razón #1 por la que los pacientes botan el Tramadol al segundo día es que 'los marea y los hace vomitar'. El Tramadol inunda de serotonina y estímulo opioide el centro del vómito en el cerebro. Si inicias con una gota (ej. 10 gotas o 25 mg cada 12h) y vas subiendo cada 3 días, el cerebro genera tolerancia a la náusea y el paciente logra adherirse a la terapia del dolor."
    },

    # --- CATEGORÍA: 🔄 Interacciones ---
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 1: Paciente de APS tratado crónicamente con Fluoxetina (20 mg/día) acude quejándose de que el Tramadol (50 mg c/8h) que le dio el médico por su ciática 'no le hace absolutamente nada para el dolor'. Como QF Élite, ¿qué explicación farmacocinética le das al médico tratante?",
        "opciones": [
            "La Fluoxetina es un inhibidor extremadamente potente del CYP2D6. Al bloquear esta enzima, impide que el Tramadol se convierta en su metabolito activo M1 (O-desmetiltramadol), dejándolo sin su principal efecto analgésico opioide.",
            "La Fluoxetina induce las enzimas hepáticas que destruyen el Tramadol, reduciendo su vida media a menos de 30 minutos.",
            "La Fluoxetina compite por el mismo receptor opioide Mu a nivel medular, actuando como antagonista competitivo irreversible.",
            "Ambos fármacos se quelan en el intestino, impidiendo su absorción conjunta."
        ],
        "respuesta": "La Fluoxetina es un inhibidor extremadamente potente del CYP2D6. Al bloquear esta enzima, impide que el Tramadol se convierta en su metabolito activo M1 (O-desmetiltramadol), dejándolo sin su principal efecto analgésico opioide.",
        "feedback": "Interacción maestra. El Tramadol necesita al CYP2D6 para transformarse en 'M1' y quitar el dolor. Fármacos como la Fluoxetina, Paroxetina o Bupropión son los destructores (inhibidores fuertes) de esa enzima. Si el paciente toma Fluoxetina, su hígado no puede activar el Tramadol. El paciente tragará pastillas pero seguirá con el mismo dolor."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 2: Paciente que utiliza Tramadol a altas dosis (300 mg/día) y Sertralina (100 mg/día) ingresa a urgencias con agitación psicomotora, sudoración profusa (diaforesis), taquicardia, temblores e hiperreflexia con clonus. ¿Cuál es el diagnóstico toxicológico y la interacción responsable?",
        "opciones": [
            "Síndrome Neuroléptico Maligno por bloqueo agudo de receptores dopaminérgicos D2.",
            "Síndrome Serotoninérgico. Tanto la Sertralina (ISRS) como el Tramadol inhiben la recaptación de serotonina, causando un exceso tóxico y potencialmente letal de este neurotransmisor en el SNC.",
            "Crisis Tirotóxica desencadenada por la estimulación simpática de la noradrenalina del Tramadol.",
            "Abstinencia opioide aguda precipitada por competencia a nivel de los receptores."
        ],
        "respuesta": "Síndrome Serotoninérgico. Tanto la Sertralina (ISRS) como el Tramadol inhiben la recaptación de serotonina, causando un exceso tóxico y potencialmente letal de este neurotransmisor en el SNC.",
        "feedback": "Una de las 'Red Flags' más peligrosas en la farmacia comunitaria. El Tramadol esconde un antidepresivo en su estructura. Si lo sumas a otro antidepresivo real (Sertralina, Fluoxetina, Venlafaxina), la médula espinal y el cerebro se inundan de Serotonina. El paciente se pone rígido, con temblores, fiebre y puede morir de colapso cardiovascular. Hay que evitar esta mezcla a toda costa."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "🔄 Interacciones",
        "pregunta": "Variación 3: Un paciente anticoagulado con Warfarina (Acenocumarol) inicia terapia con Tramadol por un esguince severo. A los pocos días, sufre una hemorragia nasal masiva y su INR se eleva a 6.0. ¿Cuál es la precaución descrita al combinar estos dos fármacos?",
        "opciones": [
            "El Tramadol destruye la vitamina K a nivel intestinal por inhibición de la flora.",
            "El Tramadol es un inhibidor directo de la trombina, actuando como un anticoagulante endovenoso.",
            "Aunque el mecanismo exacto es desconocido, está documentado que el Tramadol puede potenciar el efecto de los antagonistas de la Vitamina K, prolongando el tiempo de protrombina y el INR, exigiendo monitoreo estricto.",
            "El Tramadol induce trombocitopenia autoinmune fulminante en menos de 24 horas."
        ],
        "respuesta": "Aunque el mecanismo exacto es desconocido, está documentado que el Tramadol puede potenciar el efecto de los antagonistas de la Vitamina K, prolongando el tiempo de protrombina y el INR, exigiendo monitoreo estricto.",
        "feedback": "Un clásico dolor de cabeza para los QF de policlínico TACO. Nadie sabe con 100% de certeza por qué ocurre (se sospecha competencia por citocromos como el CYP2C9), pero es un hecho empírico: dar Tramadol a alguien que usa Warfarina/Acenocumarol hace que la sangre se 'licúe' aún más. Siempre que se asocie, el QF debe citar al paciente para un control de INR a los 3-4 días."
    },

    # --- CATEGORÍA: ⚠️ RAMs ---
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 1: Paciente epiléptico controlado hace años con Levetiracetam sufre un accidente y el médico de urgencias le indica Tramadol endovenoso rápido. El paciente convulsiona en la camilla. ¿Cuál es el mecanismo fisiopatológico por el cual el Tramadol induce esta RAM grave?",
        "opciones": [
            "Porque el Tramadol bloquea los receptores GABA-A de forma competitiva con el Levetiracetam.",
            "El Tramadol y su metabolito inhiben la recaptación de monoaminas, disminuyendo drásticamente el umbral convulsivo, especialmente en pacientes predispuestos o a dosis altas (>400 mg).",
            "Porque induce la inflamación directa de las meninges, causando irritación cortical focal.",
            "Porque disminuye drásticamente el flujo sanguíneo cerebral al causar vasoconstricción severa."
        ],
        "respuesta": "El Tramadol y su metabolito inhiben la recaptación de monoaminas, disminuyendo drásticamente el umbral convulsivo, especialmente en pacientes predispuestos o a dosis altas (>400 mg).",
        "feedback": "Trampa mortal del Tramadol: Bajar el umbral convulsivo. En un cerebro normal es difícil que pase a dosis clínicas, pero si el paciente ya tiene epilepsia, o si se pasó de los 400 mg/día, o si está usando fármacos que también bajen el umbral (como antipsicóticos o antidepresivos), el Tramadol es un gatillo directo para desencadenar una crisis tónico-clónica."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 2: Se ha emitido una alerta internacional sobre el uso de Tramadol y una RAM metabólica rara pero letal, especialmente en ancianos y pacientes diabéticos. De hecho, supera al resto de los opioides en este riesgo. ¿Cuál es esta RAM?",
        "opciones": [
            "Hipoglicemia severa, que puede llevar a coma o muerte, mediada posiblemente por mecanismos autonómicos y serotoninérgicos aún no bien definidos.",
            "Cetoacidosis diabética euglicémica por inhibición de los receptores GLUT-4.",
            "Hipercalcemia aguda por lisis ósea acelerada.",
            "Insuficiencia suprarrenal primaria por infarto de la glándula."
        ],
        "respuesta": "Hipoglicemia severa, que puede llevar a coma o muerte, mediada posiblemente por mecanismos autonómicos y serotoninérgicos aún no bien definidos.",
        "feedback": "Alerta roja de farmacovigilancia reciente. Investigaciones (y alertas de la FDA/EMA) descubrieron que los pacientes mayores que inician Tramadol tienen 3 veces más riesgo de caer al hospital por Hipoglicemia severa (azúcar por el piso) que si tomaran morfina o codeína. Se cree que el exceso de serotonina en el cerebro estimula una hiper-respuesta metabólica."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "⚠️ RAMs",
        "pregunta": "Variación 3: Al suspender un tratamiento prolongado con Tramadol a altas dosis, el paciente no solo experimentará el clásico síndrome de abstinencia opioide (diarrea, midriasis, piloerección). ¿Qué otros síntomas 'atípicos' sufrirá debido al componente no opioide del fármaco?",
        "opciones": [
            "Hiperplasia prostática aguda y retención urinaria severa.",
            "Síntomas de discontinuación de antidepresivos (ISRS): ataques de pánico, ansiedad extrema, parestesias ('corrientes eléctricas' en la cabeza), alucinaciones y parestesias severas.",
            "Anemia hemolítica fulminante y sangrado gingival profundo.",
            "Bradicardia extrema e hipotermia refractaria."
        ],
        "respuesta": "Síntomas de discontinuación de antidepresivos (ISRS): ataques de pánico, ansiedad extrema, parestesias ('corrientes eléctricas' en la cabeza), alucinaciones y parestesias severas.",
        "feedback": "Quitar el Tramadol de golpe es un infierno doble para el paciente. No solo sufre el dolor de dejar la morfina (dolor de huesos, diarrea, sudor frío), sino que también sufre el síndrome de abstinencia de la serotonina (como si dejaras la Venlafaxina o Paroxetina de golpe). El cerebro se queda sin serotonina y el paciente sufre de 'Brain Zaps' (cortocircuitos en la cabeza), ataques de pánico y depresión profunda. Se debe retirar muy gradualmente (tapering)."
    },

    # --- CATEGORÍA: 🏥 Caso Clínico ---
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 1: Acude un paciente con la receta de su hijo de 8 años. El dentista le recetó Tramadol en gotas para el dolor post-extracción dental. Según las directrices actuales de la FDA, la EMA y el MINSAL sobre opioides y pediatría, ¿cuál debe ser la intervención del QF?",
        "opciones": [
            "Dispensar normalmente, ya que el Tramadol en gotas está formulado específicamente para población pediátrica.",
            "Rechazar la receta. El Tramadol está estrictamente CONTRAINDICADO en menores de 12 años (y en menores de 18 años tras amigdalectomía/adenoidectomía) por el riesgo letal de depresión respiratoria severa en niños ultra-metabolizadores del CYP2D6.",
            "Llamar al médico para que asocie un antiemético como Ondansetrón obligatoriamente.",
            "Ajustar la dosis a la mitad del peso corporal ideal para evitar convulsiones."
        ],
        "respuesta": "Rechazar la receta. El Tramadol está estrictamente CONTRAINDICADO en menores de 12 años (y en menores de 18 años tras amigdalectomía/adenoidectomía) por el riesgo letal de depresión respiratoria severa en niños ultra-metabolizadores del CYP2D6.",
        "feedback": "Regla vital de pediatría. Algunos niños tienen una genética especial (Ultra-metabolizadores CYP2D6). Si a esos niños les das una gota de Tramadol, su hígado la transforma en 1000 gotas del metabolito activo (M1) en segundos. El niño sufre una sobredosis masiva de opioide endógeno, deja de respirar y muere mientras duerme. La Codeína y el Tramadol están prohibidos en niños menores de 12 años mundialmente."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 2: Paciente adicto a la heroína en proceso de rehabilitación, en tratamiento con Naltrexona (antagonista puro de receptores Mu), llega a urgencias con una fractura expuesta. El traumatólogo le indica Tramadol endovenoso. Como QF clínico de la UPC, ¿qué adviertes sobre esta indicación?",
        "opciones": [
            "Que la combinación generará un sinergismo que inducirá coma profundo.",
            "Que la Naltrexona bloquea todos los receptores opioides Mu de la médula. Por lo tanto, el metabolito activo del Tramadol rebotará y el paciente NO experimentará ninguna analgesia opioide, sintiendo todo el dolor de la fractura.",
            "Que la interacción precipitará cristales insolubles en la vía venosa periférica.",
            "Que el Tramadol inducirá el metabolismo hepático de la Naltrexona, eliminándola del cuerpo."
        ],
        "respuesta": "Que la Naltrexona bloquea todos los receptores opioides Mu de la médula. Por lo tanto, el metabolito activo del Tramadol rebotará y el paciente NO experimentará ninguna analgesia opioide, sintiendo todo el dolor de la fractura.",
        "feedback": "Farmacodinamia pura de receptores. La Naltrexona es un 'escudo' impenetrable que cubre los receptores de morfina en el cerebro para que el adicto no sienta placer si recae. Si le inyectas Tramadol a este paciente, el fármaco viajará al cerebro, encontrará todos los receptores bloqueados y rebotará. El paciente aullará de dolor. En estos pacientes se usan anestésicos locales, bloqueos regionales o ketamina."
    },
    {
        "familia": "Sistema Nervioso Central (SNC)",
        "categoria": "🏥 Caso Clínico",
        "pregunta": "Variación 3: Un paciente de fenotipo caucásico europeo presenta polimorfismo genético documentado como 'Metabolizador Lento del CYP2D6' (PM - Poor Metabolizer). Si el médico le prescribe Tramadol por dolor neuropático, ¿cuál será el resultado clínico esperado?",
        "opciones": [
            "Analgesia tóxica inmediata con depresión respiratoria severa en la primera dosis.",
            "Falla terapéutica analgésica. Al carecer de la enzima funcional, el hígado no puede convertir el Tramadol inactivo en su metabolito analgésico M1 (O-desmetiltramadol). El paciente solo sentirá efectos adversos noradrenérgicos (insomnio, sudor, taquicardia) pero el dolor continuará intacto.",
            "El riñón excretará el fármaco de inmediato, produciendo hematuria.",
            "Desarrollará tolerancia opioide en menos de 24 horas requiriendo rotación a metadona."
        ],
        "respuesta": "Falla terapéutica analgésica. Al carecer de la enzima funcional, el hígado no puede convertir el Tramadol inactivo en su metabolito analgésico M1 (O-desmetiltramadol). El paciente solo sentirá efectos adversos noradrenérgicos (insomnio, sudor, taquicardia) pero el dolor continuará intacto.",
        "feedback": "Farmacogenética de vanguardia. Cerca del 10% de los caucásicos son metabolizadores lentos (CYP2D6 deficiente). Son 'fábricas estropeadas'. Si toman Tramadol, el hígado no puede cortarlo para hacer la forma activa. El paciente jura que la pastilla es falsa porque el dolor no se va, pero se llena de náuseas y sudor frío por el componente serotoninérgico que sí queda activo circulando. Se debe rotar a morfina o buprenorfina."
    },
]