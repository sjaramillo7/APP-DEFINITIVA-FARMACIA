# ==========================================
# ARCHIVO: vademecum.py
# BASE DE DATOS TEÓRICA - QF ÉLITE RED PÚBLICA
# ==========================================

datos_vademecum = [
    {
        "familia": "Cardiovasculares",
        "nombre": "Enalapril (Comprimido 10mg / 20mg)",
        "mecanismo": "Inhibidor de la Enzima Convertidora de Angiotensina (IECA). Previene la conversión de Angiotensina I en Angiotensina II, disminuyendo la resistencia vascular periférica y la secreción de aldosterona. Impide la degradación de bradicininas.",
        "uso": "Hipertensión arterial, insuficiencia cardíaca con FEVI reducida, nefroprotección en diabetes (frena microalbuminuria).",
        "cinetica": "Profármaco (Enalaprilato). Eliminación 100% renal (exige ajuste de dosis o intervalo si ClCr < 30 mL/min).",
        "interacciones": "Contraindicado con ARA II. Riesgo de hiperkalemia letal con Espironolactona o AINEs (triple whammy). RAM clásica: Tos seca y Angioedema por bradicininas."
    },
    {
        "familia": "Cardiovasculares",
        "nombre": "Losartán (Comprimido 50mg)",
        "mecanismo": "Antagonista de Receptores de Angiotensina II (ARA II). Bloquea selectivamente el receptor AT1, anulando la vasoconstricción y secreción de aldosterona, dejando libre el AT2 (vasodilatador).",
        "uso": "HTA, nefropatía diabética, alternativa a IECAs por tos seca. Posee leve efecto uricosúrico (ideal en hipertensos con gota).",
        "cinetica": "Metabolismo hepático CYP2C9 y CYP3A4 a su metabolito activo E-3174. No requiere ajuste inicial estricto en falla renal.",
        "interacciones": "Sinergismo tóxico con AINEs (falla renal). Aumenta riesgo de toxicidad por Litio al forzar su reabsorción proximal. Teratogénico (falla renal fetal)."
    },
    {
        "familia": "AINEs",
        "nombre": "Ácido Acetilsalicílico (Comprimido 100mg, 500mg)",
        "mecanismo": "Inhibición IRREVERSIBLE de la enzima ciclooxigenasa (COX-1) mediante acetilación. En plaquetas, bloquea la síntesis de Tromboxano A2 por toda la vida útil de la plaqueta (7-10 días).",
        "uso": "Prevención secundaria cardiovascular (100mg), Síndrome Coronario Agudo (300-500mg masticado), Profilaxis preeclampsia. Uso analgésico obsoleto por RAMs.",
        "cinetica": "Sufre intenso metabolismo de primer paso. A dosis de 100mg acetila plaquetas en la vena porta antes de llegar al hígado. Excreción renal.",
        "interacciones": "Ibuprofeno causa impedimento estérico (tomar AAS 2h antes). Aumenta riesgo de sangrado con ISRS. Contraindicado en asma con pólipos (Tríada de Samter) y en niños con fiebre viral (Sd. de Reye)."
    },
    {
        "familia": "Antimicrobianos",
        "nombre": "Vancomicina (Frasco ampolla 500mg, 1g)",
        "mecanismo": "Glucopéptido bactericida. Se une estéricamente a los precursores D-Ala-D-Ala de la pared celular bacteriana (peptidoglicano), impidiendo la transglicosilación. Espectro exclusivo Gram positivos.",
        "uso": "Infecciones graves por S. aureus meticilino resistente (SAMR), Enterococo sensible. Vía oral EXCLUSIVA para C. difficile en lumen colónico.",
        "cinetica": "Excreción >90% renal inalterada. Cinética compleja dependiente del Área Bajo la Curva (AUC/CIM >400). Requiere medir niveles valle antes de la 4ta dosis.",
        "interacciones": "Nefrotoxicidad severa potenciada si se asocia a Piperacilina/Tazobactam o Aminoglucósidos. Incompatible en vía Y con Cefepime (precipita). RAM: Síndrome de Hombre Rojo por infusión rápida."
    },
    {
        "familia": "Endocrinología / Antidiabéticos",
        "nombre": "Metformina (Comprimido 500mg, 850mg, 1000mg)",
        "mecanismo": "Biguanida. Bloquea la enzima mGPD mitocondrial y activa la AMPK hepática. Suprime potentemente la gluconeogénesis hepática (bloquea ciclo de lactato) y mejora la captación muscular de glucosa.",
        "uso": "Primera línea en DM2. Off-label en Síndrome de Ovario Poliquístico (SOP) y resistencia a insulina.",
        "cinetica": "Hidrofílica extrema. Cero unión a proteínas, Cero metabolismo hepático. Se secreta inalterada al 100% por transportador OCT2 renal.",
        "interacciones": "Contraindicada si VFG < 30. Suspender en uso de contraste yodado intravenoso (riesgo de falla renal y acidosis láctica). RAMs: Diarrea explosiva (osmótica) y déficit de Vitamina B12."
    },
    {
        "familia": "Cardiovasculares",
        "nombre": "Atorvastatina (Comprimido 10mg, 20mg, 40mg)",
        "mecanismo": "Inhibidor competitivo de HMG-CoA reductasa. Al bajar el colesterol intracelular, el hígado sobreexpresa receptores LDL, barriendo el colesterol plasmático. Posee efectos pleiotrópicos estabilizadores de placa.",
        "uso": "Dislipidemia, prevención primaria y secundaria de infartos (dosis altas 40-80mg).",
        "cinetica": "Metabolismo exclusivo por CYP3A4. Larga vida media (14 hrs) permite dosificación diurna o nocturna. Excreción biliar (no requiere ajuste renal).",
        "interacciones": "Contraindicada con Gemfibrozilo (usar Fenofibrato) y Jugo de Pomelo. Macrólidos (Claritromicina) disparan sus niveles causando Rabdomiólisis. RAM: Elevación de transaminasas y Mialgias."
    },
    {
        "familia": "Cardiovasculares",
        "nombre": "Amlodipino (Comprimido 5mg, 10mg)",
        "mecanismo": "Calcioantagonista dihidropiridínico. Bloquea canales de calcio voltaje-dependientes tipo L en el músculo liso vascular coronario y periférico, causando vasodilatación arterial pura (no afecta venas).",
        "uso": "Hipertensión arterial (ideal en afrodescendientes y ancianos), Angina de pecho estable y vasoespástica (Prinzmetal).",
        "cinetica": "Metabolismo hepático extenso (CYP3A4). Vida media larguísima (35-50 horas), lo que evita la taquicardia refleja aguda de otros de su clase (Nifedipino).",
        "interacciones": "La FDA advierte que Amlodipino aumenta los niveles de Simvastatina (no usar más de 20mg/día de Simvastatina juntos). RAM clásica: Edema periférico maleolar refractario a diuréticos."
    },
    {
        "familia": "Gastroenterología",
        "nombre": "Omeprazol (Cápsula 20mg, Frasco ampolla 40mg)",
        "mecanismo": "Inhibidor de la Bomba de Protones (IBP). Profármaco que requiere ambiente ácido para activarse (sulfenamida). Se une de forma irreversible (enlace disulfuro) a la enzima H+/K+ ATPasa en el canalículo de la célula parietal, bloqueando el paso final de la secreción ácida.",
        "uso": "ERGE, Úlcera Péptica, Erradicación H. pylori (coadyuvante pH-dependiente), Profilaxis de úlcera por estrés (solo en UCI).",
        "cinetica": "Requiere administración 30 a 60 minutos ANTES de la comida principal. Cápsula con cubierta entérica obligatoria. Metabolismo hepático potente (sustrato e inhibidor del CYP2C19).",
        "interacciones": "Inhibe la activación del Clopidogrel (CYP2C19). Al subir el pH gástrico, anula la absorción de fármacos dependientes de ácido (Ketoconazol, Atazanavir, Carbonato de Calcio, Hierro). RAMs crónicas: Hipomagnesemia, déficit de B12 y riesgo de infección por C. difficile."
    }
{
        "familia": "Antimicrobianos",
        "nombre": "Amoxicilina / Ácido Clavulánico (Comp. 500/125mg, 875/125mg)",
        "mecanismo": "Asociación sinérgica. La Amoxicilina inhibe las PBP (frena síntesis de pared celular). El Ácido Clavulánico es un inhibidor 'suicida' de betalactamasas; se sacrifica uniéndose irreversiblemente a la enzima bacteriana, protegiendo a la Amoxicilina de la destrucción.",
        "uso": "Otitis media aguda resistente, sinusitis bacteriana, mordeduras (animal/humano), exacerbación de EPOC y pie diabético (fase inicial APS).",
        "cinetica": "Cinética tiempo-dependiente (T > CIM). Ambos se absorben bien vía oral. El clavulánico tiene intensa excreción hepato-renal y su acúmulo causa toxicidad gastrointestinal.",
        "interacciones": "Acenocumarol/Warfarina (destruye flora productora de Vitamina K, disparando el INR y riesgo de sangrado). Metotrexato (compite en secreción tubular, causando toxicidad). RAM: Diarrea severa (efecto directo del clavulánico) y Hepatitis colestásica idiosincrática."
    },
{
        "familia": "Sistema Nervioso Central (SNC)",
        "nombre": "Tramadol (Cápsula 50mg, Gotas 100mg/mL)",
        "mecanismo": "Analgésico central de acción dual. 1) Agonista débil del receptor opioide Mu (μ). 2) Inhibidor de la recaptación de Serotonina y Noradrenalina (IRSN) en las vías descendentes del dolor en la médula espinal.",
        "uso": "Dolor moderado a severo (Escalón 2 de la OMS). Dolor neuropático y osteoarticular resistente a AINEs.",
        "cinetica": "Es un PROFÁRMACO. Requiere metabolismo hepático por el citocromo CYP2D6 para convertirse en O-desmetiltramadol (Metabolito M1), el cual es 6 veces más potente en el receptor opioide.",
        "interacciones": "Contraindicado con ISRS (Sertralina, Fluoxetina) por riesgo mortal de Síndrome Serotoninérgico. Fármacos inhibidores del CYP2D6 (Bupropión, Fluoxetina) bloquean su conversión al metabolito activo, dejando al paciente sin analgesia. Baja el umbral convulsivo."
    },
]