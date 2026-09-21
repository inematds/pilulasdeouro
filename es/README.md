# Pílulas de Ouro — IA en proyectos prácticos

Curso en portugués en formato INEMA v2: **4 trilhas, 12 módulos, 72 tópicos y 12 prácticas**. Incluye ejemplos, ejercicios con verificación, dos proyectos de cierre, progreso de lectura, dudas, resaltados, anotaciones y exportación del recorrido.

[Abrir el curso](https://inematds.github.io/pilulasdeouro/) · [Materiales del alumno](https://inematds.github.io/pilulasdeouro/materiais/) · [Plan de proyectos](PLANO-PROJETOS.md)

## Estudiar

Empieza por los fundamentos o elige una trilha en el índice. Marca los tópicos leídos y selecciona fragmentos para resaltar/anotar. El progreso queda en el navegador: usa **Mi recorrido → Exportar** para guardar una copia o cambiar de dispositivo. Sin JavaScript, el contenido permanece disponible para la lectura.

La estimación de siete horas incluye las prácticas; ajusta el ritmo a tu experiencia. Los ejemplos usan datos ficticios. Las herramientas externas pueden requerir instalación o su propia cuenta.

## Editar y ejecutar

Requiere Python 3. El contenido editorial está en `conteudo/curso.json`; las páginas se generan, sin dependencias de build externas.

```bash
python3 scripts/gerar_curso.py
python3 scripts/verificar_curso.py
python3 -m http.server 8766
```

Abre `http://localhost:8766`. Edita textos en el JSON, estructura en el generador y presentación/interacciones en `assets/`. Regenera las páginas antes de commitar.

- `curso/`: índices de las cuatro trilhas y módulos completos.
- `materiais/`: fichas prácticas, CSV ficticio y curso en Markdown.
- `assets/`: fuentes locales, estilos y aprendizaje.
- `PLANO-PROJETOS.md`: portafolio de 12 proyectos propuestos; implementaciones futuras.
- `PRODUCT.md` y `DESIGN.md`: decisiones de producto e interfaz.

## Publicación y privacidad

GitHub Pages publica la raíz de la branch `main` de este repositorio. El curso y sus materiales editoriales quedan versionados aquí. Los materiales privados de preparación en `down/`, los medios, las transcripciones y las herramientas de recopilación se excluyen por `.gitignore` y no forman parte de la publicación.

La licencia de la fuente Inter acompaña a los archivos en `assets/inter-LICENSE.txt`.
