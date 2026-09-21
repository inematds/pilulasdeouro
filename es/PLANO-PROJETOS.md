# Plano de projetos — Pílulas de Ouro

Fecha: 18/09/2026. Portafolio de proyectos prácticos para transformar tareas con IA en entregas verificables. Las propuestas de abajo aún no se han implementado.

## Objetivo y regla de ejecución

Transformar las pílulas en herramientas pequeñas, útiles y demostrables para el ecosistema INEMA. Empezar con un problema, una entrada, una salida y un criterio de aceptación por proyecto. Límite de trabajo: un MVP en desarrollo por vez. Solo iniciar el siguiente después de demostrar el resultado y registrar las limitaciones.

Antes de implementar una integración, revisar la documentación actual, los requisitos y el funcionamiento de las herramientas elegidas.

## Portafolio y prioridad

Estimaciones en días de trabajo concentrado para prototipos, sin incluir espera por servicios o aprobaciones externas. Son estimaciones de planificación.

| Orden | Proyecto propuesto | Módulo del curso | Resultado del MVP | Esfuerzo | Depende de |
|---|---|---|---|---|---|
| 1 | Encargo Cerrado | 01 | El pedido se convierte en ficha verificable + tabla de tareas | 1 día | — |
| 2 | Skill Check INEMA | 08 | Informe de inspección con evidencias y revisión de falsos positivos | 2–3 días | 1 |
| 3 | Docs para IA | 05 | Los documentos se vuelven Markdown con informe de conversión | 2–3 días | 1, 2 |
| 4 | Mapa del Proyecto | 07 | Diagramas de arquitectura y secuencia rastreables al código | 2 días | 1, 2 |
| 5 | Segunda Opinión | 06 | Revisión de diff con reproducción de los problemas encontrados | 2–3 días | 1 |
| 6 | Oficina Visual | 04 | Mejoras visuales con comparación antes/después | 2–3 días | 1, 2 |
| 7 | Estudio de Prompts Visuales | 02 | Catálogo de prompts y generación con rastreabilidad | 2–3 días | 1, 2 |
| 8 | Dossier de Investigación | 03 | Las fuentes se vuelven informe, preguntas y presentación | 3–4 días | 3 |
| 9 | Perfiles de Modelos | 09 | Ejecuciones aisladas por proveedor, con retorno al perfil original | 2–3 días | 1, 5 |
| 10 | Auditor GEO INEMA | 10 | Auditoría de sitio con tareas verificables | 3–4 días | 1, 2 |
| 11 | Kit de Entrega de Proyectos | 01 + 04 + 06 + 07 + 10 | Paquete de documentación, revisión y evidencias de una entrega | 3–5 días | 4, 5, 6, 10 |
| 12 | Biblioteca Viva de Conocimiento | 03 + 05 + 07 | Base documental actualizable con fuentes y dossiers | 4–6 días | 3, 4, 8 |

## 1. Encargo Cerrado

**Problema:** pedidos vagos generan expansión del alcance y entregas difíciles de comprobar.

**MVP:** recibir un pedido en texto y producir `encargo.md` con objetivo, alcance, exclusiones, entradas, salida esperada y verificación; convertir solicitudes en una tabla con responsable, tarea, plazo y pendientes. Las fechas ausentes permanecen como “pendiente”.

**Etapas:** redactar una ficha de alcance en portugués; crear tres pedidos ficticios y la tabla esperada; definir el formato de salida; agregar exportación Markdown/CSV; registrar una ejecución de ejemplo.

**Aceptación:** las tres solicitudes generan tres líneas; ningún dato se inventa; la solicitud sin fecha conserva el estado de pendiente; el archivo se puede reabrir y comparar con el resultado esperado. Fuera del MVP: calendario, notificaciones e integración con gestores externos.

## 2. Skill Check INEMA

**Problema:** instalar skills sin conocer dependencias, permisos o comandos que ejecutan.

**MVP:** analizar una carpeta local sin ejecutarla y emitir un informe JSON + Markdown con archivo, línea, evidencia, gravedad, justificación y decisión revisable. Separar hallazgos confirmados de sospechas y falsos positivos.

**Etapas:** verificar la herramienta elegida; definir reglas para ejecución de shell, red, lectura de credenciales y comandos destructivos; crear fixtures benignas y sospechosas; agregar registro de triaje humano.

**Aceptación:** detectar casos de prueba conocidos, señalar evidencia localizable y permitir justificar falsos positivos; ninguna instalación o ejecución de código durante la inspección. Limitación explícita: la ausencia de hallazgos no es prueba de seguridad.

## 3. Docs para IA

**Problema:** documentos de formatos distintos llegan desorganizados y difíciles de consultar.

**MVP:** carpeta de entrada con DOCX, XLSX, PPTX y PDF con texto; salida Markdown por documento, archivos auxiliares y manifiesto con hash, herramienta, estado y avisos. Priorizar un conversor existente tras verificar, sin reescribir parsers.

**Etapas:** montar cuatro documentos pequeños con resultado esperado; probar el conversor elegido; preservar tablas y títulos; identificar duplicados por hash; registrar archivos no soportados. OCR de escaneos queda para una segunda versión.

**Aceptación:** cuatro formatos convertidos con títulos y tablas verificados; un archivo corrupto genera un error visible sin cerrar el lote; reejecutar no crea duplicados; cada salida apunta a su origen.

## 4. Mapa del Proyecto

**Problema:** arquitectura y flujos quedan en la memoria de quien desarrolló.

**MVP:** generar un diagrama de arquitectura y uno de secuencia para un proyecto local, con fuente editable e imagen exportada. Cada componente y conexión necesita evidencia en archivo/configuración o marcado explícito de hipótesis.

**Etapas:** elegir un proyecto pequeño; levantar entradas, servicios y persistencia; generar los dos diagramas; verificar las ligas; incluir tema claro/oscuro y exportación.

**Aceptación:** ningún servicio inventado; diagrama legible en imagen; la fuente editable permite regeneración; el flujo corresponde a una ejecución demostrada. Fuera del MVP: monitoreo en tiempo real.

## 5. Segunda Opinión

**Problema:** la misma sesión que escribe código puede repetir errores o ignorar fallas de concurrencia y exportación.

**MVP:** revisión de un diff Git en un entorno aislado, produciendo hallazgos priorizados con localización, escenario de reproducción y menor corrección propuesta. Adoptar la integración disponible después de revisar la documentación y la autenticación.

**Etapas:** definir entrada (base y commit); preparar ejemplos con duplicación por retry, cambio no atómico y exportación sin filtro; revisar; reproducir los hallazgos; corregir y repetir solo las verificaciones pertinentes.

**Aceptación:** problemas sin evidencia se identifican como hipótesis; el caso de retry no duplica la operación después del fix; la exportación respeta el filtro esperado; cada conclusión informa qué se probó y qué no. Sin merge o publicación automática.

## 6. Oficina Visual

**Problema:** interfaces funcionales pueden tener jerarquía confusa e inconsistencias visuales.

**MVP:** aplicar una auditoría y un conjunto pequeño de mejoras a una página de demostración, usando la herramienta ya existente cuando sea compatible. Entregar capturas antes/después, diff y lista de decisiones.

**Etapas:** elegir página; registrar baseline; seleccionar tres problemas de jerarquía, legibilidad o interacción; comparar hasta tres propuestas; aplicar una; verificar en desktop y celular.

**Aceptación:** sin desplazamiento horizontal a 360 px; enfoque de teclado visible; textos y acciones legibles; los cambios en el código corresponden a la comparación visual. Fuera del MVP: crear un editor visual propio.

## 7. Estudio de Prompts Visuales

**Problema:** imágenes de una misma serie varían demasiado por falta de brief estructurado.

**MVP:** catálogo de diez briefs para portadas, infográficos e ilustraciones con campos de objetivo, composición, estilo, proporción, texto y restricciones. Guardar prompt, referencia de la receta y resultado de cada generación.

**Adaptación INEMA:** usar `flux2-klein` como estándar, según la preferencia del proyecto. Comparar otro modelo solo cuando el proyecto lo exija.

**Etapas:** verificar la licencia de las recetas; estructurar el catálogo; generar tres casos representativos; evaluar un caso simple y otro de composición difícil; ajustar solo los campos que fallaron.

**Aceptación:** briefs reproducibles e historial de generaciones; dimensiones correctas; tres resultados verificados visualmente contra el briefing; problemas de texto o composición registrados. Fuera del MVP: promesa de consistencia perfecta o generación en masa.

## 8. Dossier de Investigación

**Problema:** investigación, referencias y materiales de presentación se dispersan en herramientas distintas.

**MVP:** recibir tema + conjunto de documentos autorizado y producir un informe en portugués, diez preguntas con respuestas y una presentación, todos con fuentes identificables. Antes de integrar, confirmar qué CLI se utilizará y quién la mantiene; no asumir que sea oficial.

**Etapas:** revisar la integración y la sesión; importar tres documentos del proyecto Docs para IA; generar el dossier; revisar citas; exportar los tres entregables. Podcast y video quedan para una segunda etapa.

**Aceptación:** cada afirmación central referencia una fuente; los tres entregables se abren localmente; la información ausente se señala; el idioma se define explícitamente. Los archivos locales solo se envían a un servicio externo cuando ese uso esté autorizado.

## 9. Perfiles de Modelos

**Problema:** cambiar configuraciones a mano puede borrar ajustes o mezclar credenciales.

**MVP:** validar perfiles de proveedores y ejecutar una tarea de prueba en una configuración aislada, manteniendo el perfil original recuperable. Crear ejemplos sin credenciales y verificar el formato actual antes de usar.

**Etapas:** inspeccionar nombres de campos sin mostrar valores sensibles; definir esquema; validar perfil; cargar la clave en runtime de los locales ya establecidos por el usuario; probar una tarea pequeña; verificar retorno al estado anterior.

**Aceptación:** ningún secreto en logs o Git; JSON inválido se rechaza; el fallo de autenticación aparece claramente; la configuración original permanece íntegra. Medir duración y consumo cuando el proveedor proporcione los datos, sin asumir ahorros sin medir el consumo.

## 10. Auditor GEO INEMA

**Problema:** los sitios tienen estructura y contenido que pueden dificultar la lectura para buscadores y herramientas de IA.

**MVP:** analizar cinco páginas de un sitio autorizado, recolectar evidencias y producir tareas sobre títulos, contenido principal, URLs individuales, consistencia de la marca, referencias y recursos de descubrimiento. El score, si se usa, tendrá criterios publicados.

**Etapas:** revisar el repositorio sin instalar automáticamente; elegir un sitio piloto; producir baseline; corregir tres problemas; repetir la misma recolección y comparar.

**Aceptación:** cada hallazgo apunta a URL y evidencia; los enlaces internos importantes funcionan; las correcciones son demostrables. No prometer posicionamiento, recomendación por modelos o aumento de tráfico a partir de un score.

## 11. Kit de Entrega de Proyectos

**Problema:** los proyectos terminan sin instrucciones de uso, validación y contexto para mantenimiento.

**MVP:** combinar ficha de alcance, diagramas, informe de revisión, instrucciones de ejecución y evidencias en una carpeta `entrega/` de un proyecto piloto.

**Etapas:** definir checklist común; reutilizar las salidas de los proyectos 4–6 y 10; registrar comandos que realmente se ejecutaron; preparar contexto de continuidad.

**Aceptación:** otra persona puede ejecutar el proyecto siguiendo el README; toda pendiente tiene impacto y próximo paso; los enlaces locales funcionan; la versión documentada corresponde al código revisado.

## 12. Biblioteca Viva de Conocimiento

**Problema:** los documentos convertidos pierden utilidad cuando no hay origen, actualización y organización.

**MVP:** indexar diez documentos locales por tema, versión, origen y hash; producir un dossier a partir de una selección; identificar cambios sin duplicar contenido.

**Etapas:** definir catálogo; importar documentos; generar un mapa de temas; integrar la exportación del Dossier de Investigación; probar la actualización de dos archivos.

**Aceptación:** diez ítems localizables con origen; la consulta lleva al archivo correcto; la actualización altera solo los ítems modificados; la eliminación de la fuente se indica como pendiente. Fuera del MVP: plataforma multiusuario y sincronización irrestricta de cuentas.

## Secuencia sugerida

1. **Fundación:** cerrar Encargo Cerrado; usar tu ficha para delimitar todo lo demás. Luego, Skill Check y Docs para IA.
2. **Calidad de entrega:** Mapa del Proyecto, Segunda Opinión y Oficina Visual, aplicados a un único piloto.
3. **Producción e investigación:** Estudio de Prompts y Dossier de Investigación.
4. **Integraciones:** Perfiles de Modelos y Auditor GEO después de validar los servicios actuales.
5. **Composición:** Kit de Entrega y Biblioteca Viva solo después de que sus dependencias funcionen de forma aislada.

Portafolio completo: aproximadamente 28–40 días concentrados, sujeto al descubrimiento de las integraciones. El primer ciclo debe cerrar solo los tres proyectos de fundación (5–7 días estimados), con demostración al final de cada uno.

## Próxima acción concreta

Empezar por el **Encargo Cerrado**: crear tres pedidos ficticios, definir la salida esperada y comprobar la tabla producida. Entrega inicial: ficha de alcance + tabla Markdown/CSV + registro de la verificación. Este es el proyecto más pequeño y demostrable del conjunto.
