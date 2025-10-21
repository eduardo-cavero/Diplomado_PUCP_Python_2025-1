import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Análisis de Temperatura en el Perú a nivel distrital en 2024", layout="wide")

st.title("Análisis de Temperatura Mínima en Perú — 2024")
st.markdown("""
Este dashboard muestra el análisis de temperaturas a nivel distrital en Perú,
identificando zonas críticas para intervenciones de política pública en tres ámbitos.
""")

# Ruta base 
BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "notebook"

## Tabs 

tab1, tab2 = st.tabs(['Descripción de la Temperatura en el Perú a nivel distrital en 2024', 'Propuestas de política pública'])

## Contenido de tab1

with tab1:
    
    st.subheader('Descripción de los datos a nivel distrital')

    # columnas 

    a, b, c = st.columns(3, border= True)

    with a:    
        st.subheader("Listado de los 15 distritos más cálidos en el Perú")

        st.image(str(OUTPUT_DIR / 'distritos_mas_calidos.png'), width= 500)

    with b: 
        st.subheader('Listado de los 15 distritos más frios en el Perú')

        st.image(str(OUTPUT_DIR / 'distritos_mas_frios.png'), width= 500)
    
    with c: 
        
        st.subheader('Mapa de los distritos más fríos y cálidos en el Perú')
        
        st.image(str(OUTPUT_DIR / 'map_tmin.png'), width= 500)
                                        
with tab2:

    st.title('Propuestas de política pública')

    st.markdown(
"""
# Propuesta 1: Programa Integral de Prevención y Atención de Neumonía en la Sierra Sur

Una propuesta desde el Sector Salud a cargo de MINSA sería la implementación de un "Programa Integral de Prevención y Atención de Neumonía en la Sierra Sur", que incluya:

1.	Fortalecimiento de la infraestructura sanitaria: Mejorar y equipar los centros de salud locales para garantizar atención oportuna y de calidad.
2.	Campañas de sensibilización y educación comunitaria: Informar a la población sobre medidas preventivas, como el uso adecuado de ropa de abrigo y la ventilación de viviendas.
3.	Ampliación de la cobertura de vacunación: Asegurar que niños y adultos mayores reciban las vacunas contra la influenza y el neumococo, con especial énfasis en las zonas rurales.
4.	Monitoreo y vigilancia epidemiológica: Establecer sistemas de alerta temprana para detectar brotes y responder rápidamente.

Dicha estrategia debe ser implementada en colaboración con gobiernos locales, organizaciones comunitarias y las unidades ejecutoras el Ministerio de Salud, adaptándose a las particularidades culturales y geográficas de cada distrito. La inversión en estas medidas fortalecería el sistema de salud en la región, mejorando la calidad de vida de sus habitantes.
"""
        )

    st.markdown(
"""
# Propuesta 2: Programa Nacional de Resiliencia Agropecuaria ante el Friaje

El Ministerio de Desarrollo Agrario y Riego (Midagri), a través del programa Agro Rural, tendría que REPOTENCIAR el "Plan Multisectorial ante Heladas y Friaje 2025–2027", con una inversión de S/ 94 millones para beneficiar a más de 54,900 familias productoras en 15 regiones del país: Las acciones a implementar incluyen la entrega de 18,012 kits veterinarios, 3,500 kits de aplicación foliar, 860 kits de conservación de forraje, 18,500 kits de semillas de pastos cultivados, 3,227 cobertizos para ganado y 3,102 fitotoldos para cultivos en zonas altoandinas.

Para fortalecer esta estrategia, se propone la implementación de un "Programa Nacional de Resiliencia Agropecuaria ante el Friaje", que contemple:

1.	Fortalecimiento de infraestructura rural: Construcción y mantenimiento de cobertizos, fitotoldos y sistemas de riego en zonas vulnerables.
2.	Capacitación y asistencia técnica: Entrenamiento en prácticas agrícolas y ganaderas resilientes al clima, incluyendo el uso de cultivos resistentes al frío y manejo adecuado del ganado.
3.	Acceso a financiamiento y seguros agrícolas: Facilitar créditos blandos y seguros que permitan a los productores recuperarse rápidamente tras eventos climáticos extremos.
4.	Monitoreo y alerta temprana: Implementación de sistemas de información climática y redes de alerta para anticipar eventos de friaje y coordinar respuestas oportunas.
"""
)
    
    st.markdown(
""" 
# Propuesta 3: Programa focalizado contra los 
friajes en la Sierra Sur

Se identifica, basado en el “Plan de Preparación ante Emergencias y Desastres del sector Educación 
2024-2026” del Ministerio de Educación, que el escenario de riesgo por friajes muestra un total de 933 
LL. EE. en nivel de riesgo muy alto; 6044 en alto; 5569 en medio y 30 en bajo. Respecto a la cantidad de 
estudiantes, 82 467 están expuestos a nivel de riesgo muy alto; 619 830 a alto; 558 273 a medio y 1525 a 
bajo. En cuanto a la cantidad de docentes, 5252 están expuestos a nivel de riesgo muy alto; 36 421 a 
alto; 32 103 a medio y 105 a bajo.

Este sector considera como unidad de análisis a la institución educativa, por ello su análisis puede ser 
georreferenciado. Considerando ello, se propone una intervención de “Programa focalizado contra los 
friajes en la Sierra Sur”.

Población Objetivo: Comunidad Educativa (estudiantes, docentes, personal administrativo y padres de 
familia) de las IIEE identificadas en las jurisdicciones de los 15 distritos más fríos del Perú.

Objetivo específico: La prevención de la ocurrencia de riesgos asociados a los friajes y fríos extremos 
en la comunidad educativa y la educación ante ellos.

Costo estimado: S/ 312 985 821.00 en un periodo multianual de 3 años sujeto a los créditos aprobados en 
cada Ley de Presupuesto. (Basado en “Plan de Preparación ante Emergencias y Desastres del sector 
Educación 2024-2026”).

KPIs para el “Programa focalizado contra los friajes en la Sierra Sur” en el sector Educación
1.	Porcentaje de Instituciones Educativas (IIEE) con infraestructura adaptada para afrontar friajes y 
fríos extremos
Al menos el 80 por ciento de las 9,546 IIEE en niveles de riesgo muy alto y alto cuenten con mejoras en 
infraestructura (aislamiento térmico, sistemas de calefacción seguros, ventilación adecuada) al finalizar 
el tercer año del programa.

2.	Porcentaje de la comunidad educativa capacitada en prevención y manejo de riesgos por friajes
Capacitar al 90 por ciento de estudiantes, docentes, personal administrativo y padres de familia en las 15 
jurisdicciones focalizadas, mediante talleres, simulacros y materiales educativos, antes de concluir el 
periodo de implementación.
Medición: Registro de asistencia y encuestas de conocimiento previas y posteriores a las capacitaciones.
3.	Reducción del número de ausencias escolares relacionadas con enfermedades o condiciones provocadas 
por los friajes
Meta: Disminuir en un 50 por ciento las ausencias por enfermedades respiratorias y afecciones vinculadas al friaje 
en las IIEE de riesgo muy alto y alto durante los tres años del programa.
Medición: Reportes mensuales de ausentismo escolar y consultas médicas registradas en las escuelas.
"""
)

