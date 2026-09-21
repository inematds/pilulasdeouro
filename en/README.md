# Pílulas de Ouro — AI in practical projects

Course in Portuguese in INEMA v2 format: **4 tracks, 12 modules, 72 topics, and 12 practices**. Includes examples, exercises with checking, two final projects, reading progress, questions, highlights, notes, and export of your journey.

[Open the course](https://inematds.github.io/pilulasdeouro/) · [Student materials](https://inematds.github.io/pilulasdeouro/materiais/) · [Project plan](PLANO-PROJETOS.md)

## Study

Start with the fundamentals or choose a track from the index. Mark topics as read and select excerpts to highlight/note. Progress is stored in the browser: use **My learning journey → Export** to save a copy or switch devices. Without JavaScript, the content remains available for reading.

The estimate of seven hours includes the practices; adjust the pace to your experience. The examples use fictitious data. External tools may require installation or their own account.

## Edit and run

Requires Python 3. The editorial content is in `conteudo/curso.json`; the pages are generated with no external build dependencies.

```bash
python3 scripts/gerar_curso.py
python3 scripts/verificar_curso.py
python3 -m http.server 8766
```

Open `http://localhost:8766`. Edit the texts in JSON, keep the structure in the generator, and the presentation/interactions in `assets/`. Rebuild the pages before committing.

- `curso/`: indexes of the four tracks and complete modules.
- `materiais/`: practice flashcards, fictitious CSV, and a course in Markdown.
- `assets/`: local sources, styles, and learning.
- `PLANO-PROJETOS.md`: portfolio of 12 proposed projects; future implementations.
- `PRODUCT.md` and `DESIGN.md`: product and interface decisions.

## Publishing and privacy

GitHub Pages publishes the root of the branch `main` from this repository. The course and its editorial materials are versioned here. Private prep materials in `down/`, media, transcripts, and data-collection tools are excluded by `.gitignore` and are not part of the publication.

The Inter source license comes with the files in `assets/inter-LICENSE.txt`.
