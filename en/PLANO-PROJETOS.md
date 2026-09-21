# Project plan — Pílulas de Ouro

Date: 18/09/2026. A portfolio of practical projects to turn AI tasks into verifiable deliverables. The proposals below have not been implemented yet.

## Goal and execution rule

Turn the pills into small, useful, demonstrable tools for the INEMA ecosystem. Start with a problem, an input, an output, and an acceptance criterion per project. Work limit: only one MVP in development at a time. Only start the next one after demonstrating the result and recording the limitations.

Before implementing an integration, check the current documentation, the requirements, and how the selected tools work.

## Portfolio and priority

Estimates in days of focused work for prototypes, not including waiting for services or external approvals. These are planning estimates.

| Order | Proposed project | Course module | MVP result | Effort | Depends on |
|---|---|---|---|---|---|
| 1 | Encargo Fechado | 01 | Request becomes a verifiable card + task table | 1 day | — |
| 2 | Skill Check INEMA | 08 | Inspection report with evidence and review of false positives | 2–3 days | 1 |
| 3 | Docs for AI | 05 | Documents become Markdown with conversion report | 2–3 days | 1, 2 |
| 4 | Project Map | 07 | Architecture and sequence diagrams traceable to code | 2 days | 1, 2 |
| 5 | Segunda Opinião | 06 | Diff review with reproduction of the issues found | 2–3 days | 1 |
| 6 | Oficina Visual | 04 | Visual improvements with before/after comparison | 2–3 days | 1, 2 |
| 7 | Estúdio de Prompts Visuais | 02 | Prompt catalog and generation with traceability | 2–3 days | 1, 2 |
| 8 | Dossiê de Pesquisa | 03 | Sources become a report, questions, and a presentation | 3–4 days | 3 |
| 9 | Perfis de Modelos | 09 | Isolated executions per provider, returning to the original profile | 2–3 days | 1, 5 |
| 10 | Auditor GEO INEMA | 10 | Site audit with verifiable tasks | 3–4 days | 1, 2 |
| 11 | Kit de Entrega de Projetos | 01 + 04 + 06 + 07 + 10 | Documentation package, review, and evidence for a deliverable | 3–5 days | 4, 5, 6, 10 |
| 12 | Biblioteca Viva de Conhecimento | 03 + 05 + 07 | Updateable document base with sources and dossiers | 4–6 days | 3, 4, 8 |

## 1. Encargo Fechado

**Problem:** vague requests expand scope and make deliverables hard to verify.

**MVP:** receive a request in text and produce `encargo.md` with objective, scope, exclusions, inputs, expected output, and verification; convert requests into a table with owner, task, deadline, and pending items. Missing dates remain “pending”.

**Steps:** write a scope card in Portuguese; create three fictitious requests and the expected table; define the output format; add Markdown/CSV export; record an example execution.

**Acceptance:** the three requests generate three lines; no data is invented; the request without a date keeps the pending status; the file can be reopened and compared to the expected result. Outside the MVP: calendar, notifications, and integration with external managers.

## 2. Skill Check INEMA

**Problem:** installing skills without knowing dependencies, permissions, or commands that execute.

**MVP:** analyze a local folder without executing it and output a JSON + Markdown report with file, line, evidence, severity, justification, and a reviewable decision. Separate confirmed findings from suspicions and false positives.

**Steps:** check the chosen tool; define rules for executing shell, network, reading credentials, and destructive commands; create benign and suspicious fixtures; add a human triage log.

**Acceptance:** detect known test cases, point to locally discoverable evidence, and allow justifying false positives; no installation or execution of code during inspection. Explicit limitation: lack of findings is not proof of security.

## 3. Docs for AI

**Problem:** documents in different formats arrive disorganized and hard to consult.

**MVP:** input folder with DOCX, XLSX, PPTX, and PDF containing text; Markdown output per document, auxiliary files, and a manifest with hash, tool, status, and warnings. Prioritize an existing converter after verification, without rewriting parsers.

**Steps:** assemble four small documents with the expected outcome; test the chosen converter; preserve tables and titles; identify duplicates by hash; register unsupported files. OCR of scans is left for a second version.

**Acceptance:** four converted formats with verified titles and tables; a corrupted file produces a visible error without ending the batch; re-executing does not create duplicates; each output points to its origin.

## 4. Project Map

**Problem:** architecture and flows stay in the mind of the person who developed it.

**MVP:** generate an architecture diagram and a sequence diagram for a local project, with an editable source and an exported image. Each component and connection must have evidence in a file/configuration or explicit hypothesis markup.

**Steps:** pick a small project; gather inputs, services, and persistence; generate the two diagrams; verify the connections; include light/dark theme and export.

**Acceptance:** no invented services; diagram legible as an image; editable source enables regeneration; the flow matches a demonstrated execution. Outside the MVP: real-time monitoring.

## 5. Segunda Opinião

**Problem:** the same session that writes code can repeat mistakes or ignore concurrency and export failures.

**MVP:** review a Git diff in an isolated environment, producing prioritized findings with location, reproduction scenario, and the smallest proposed correction. Adopt the available integration after checking documentation and authentication.

**Steps:** define input (base and commit); prepare examples with duplication via retry, non-atomic change, and export without filtering; review; reproduce the findings; fix and repeat only the relevant checks.

**Acceptance:** issues without evidence are identified as hypotheses; the retry case does not duplicate the operation after the fix; export respects the expected filter; every conclusion states what was and was not tested. No merge or automatic publishing.

## 6. Oficina Visual

**Problem:** functional interfaces can have a confusing hierarchy and visual inconsistencies.

**MVP:** apply an audit and a small set of improvements to a demonstration page, using the already existing tool when compatible. Deliver before/after screenshots, a diff, and a list of decisions.

**Steps:** choose a page; record a baseline; select three hierarchy, readability, or interaction issues; compare up to three proposals; apply one; check desktop and mobile.

**Acceptance:** no horizontal scrolling at 360 px; visible keyboard focus; legible text and actions; code changes correspond to the visual comparison. Outside the MVP: create your own visual editor.

## 7. Estúdio de Prompts Visuais

**Problem:** images from the same series vary too much due to lack of structured briefing.

**MVP:** a catalog of ten briefs for covers, infographics, and illustrations with fields for objective, composition, style, proportion, text, and restrictions. Save the prompt, recipe reference, and the result of each generation.

**INEMA adaptation:** use `flux2-klein` as the standard, according to the project’s preference. Compare another model only when the project requires it.

**Steps:** verify license of the recipes; structure the catalog; generate three representative cases; evaluate one simple case and one difficult composition case; adjust only the fields that failed.

**Acceptance:** reproducible briefs and a generation history; correct dimensions; three results visually checked against the brief; text or composition problems recorded. Outside the MVP: a promise of perfect consistency or mass generation.

## 8. Dossiê de Pesquisa

**Problem:** research, references, and presentation materials get scattered across different tools.

**MVP:** receive a topic + an authorized set of documents and produce a report in Portuguese, ten questions with answers, and a presentation, all with identifiable sources. Before integrating, confirm which CLI will be used and who maintains it; do not assume it is official.

**Steps:** check the integration and session; import three project documents from Docs for AI; generate the dossier; review citations; export the three deliverables. Podcast and video are left for a second stage.

**Acceptance:** each core claim references a source; the three deliverables open locally; missing information is indicated; language is explicitly defined. Local files are only sent to an external service when that use is authorized.

## 9. Perfis de Modelos

**Problem:** changing settings by hand can delete adjustments or mix credentials.

**MVP:** validate provider profiles and run a test task in an isolated configuration, keeping the original profile recoverable. Create examples without credentials and confirm the current format before use.

**Steps:** inspect field names without displaying sensitive values; define a schema; validate a profile; load the key at runtime from locations already established by the user; test a small task; verify the return to the previous state.

**Acceptance:** no secrets in logs or Git; invalid JSON is rejected; authentication failure appears clearly; original configuration remains intact. Measure duration and consumption when the provider provides the data, without assuming savings without measuring consumption.

## 10. Auditor GEO INEMA

**Problem:** websites have structure and content that can make them harder for search engines and AI tools to read.

**MVP:** analyze five pages of an authorized site, collect evidence, and produce tasks about titles, main content, individual URLs, brand consistency, references, and discovery resources. If a score is used, it will have published criteria.

**Steps:** review the repository without automatically installing; choose a pilot site; produce a baseline; fix three issues; repeat the same collection and compare.

**Acceptance:** each finding points to a URL and evidence; important internal links work; fixes are demonstrable. Do not promise rankings, recommendations by models, or increased traffic from a score.

## 11. Kit de Entrega de Projetos

**Problem:** projects end without usage instructions, validation, and context for maintenance.

**MVP:** combine a scope card, diagrams, review report, execution instructions, and evidence in a `entrega/` folder for a pilot project.

**Steps:** define a common checklist; reuse outputs from projects 4–6 and 10; record commands that were actually executed; prepare continuity context.

**Acceptance:** someone else can execute the project by following the README; every pending item has an impact and a next step; local links work; the documented version matches the reviewed code.

## 12. Biblioteca Viva de Conhecimento

**Problem:** converted documents lose usefulness when there is no origin, update process, and organization.

**MVP:** index ten local documents by topic, version, origin, and hash; produce a dossier from a selection; identify changes without duplicating content.

**Steps:** define a catalog; import documents; generate a map of topics; integrate Dossiê de Pesquisa export; test updating two files.

**Acceptance:** ten locally discoverable items with origin; a search takes you to the correct file; updating changes only modified items; deleting the source is indicated as pending. Outside the MVP: a multi-user platform and unrestricted account synchronization.

## Suggested sequence

1. **Foundation:** complete Encargo Fechado; use your card to scope everything else. Then, Skill Check and Docs for AI.
2. **Delivery quality:** Project Map, Segunda Opinião, and Oficina Visual, applied to a single pilot.
3. **Production and research:** Estúdio de Prompts and Dossiê de Pesquisa.
4. **Integrations:** Perfis de Modelos and Auditor GEO after validating current services.
5. **Composition:** Kit de Entrega and Biblioteca Viva only after dependencies can run in isolation.

Complete portfolio: approximately 28–40 concentrated days, depending on the discovery of integrations. The first cycle should close only the three foundation projects (estimated 5–7 days), with a demonstration at the end of each one.

## Next concrete action

Start with **Encargo Fechado**: create three fictitious requests, define the expected output, and check the produced table. Initial delivery: scope card + Markdown/CSV table + verification log. This is the smallest demonstrable project in the set.
