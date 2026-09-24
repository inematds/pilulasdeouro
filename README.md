# Pílulas de Ouro — IA em projetos práticos

Curso em português no formato INEMA v2: **4 trilhas, 12 módulos, 72 tópicos e 12 práticas**. Inclui exemplos, exercícios com conferência, dois projetos de conclusão, progresso de leitura, dúvidas, grifos, anotações e exportação da jornada.

[Abrir o curso](https://inematds.github.io/pilulasdeouro/) · [Materiais do aluno](https://inematds.github.io/pilulasdeouro/materiais/) · [Plano de projetos](PLANO-PROJETOS.md)

## Estudar

Comece pelos fundamentos ou escolha uma trilha no índice. Marque os tópicos lidos e selecione trechos para grifar/anotar. O progresso fica no navegador: use **Minha jornada → Exportar** para guardar uma cópia ou mudar de dispositivo. Sem JavaScript, o conteúdo permanece disponível para leitura.

A estimativa de sete horas inclui as práticas; adapte o ritmo à sua experiência. Os exemplos usam dados fictícios. As ferramentas externas podem exigir instalação ou conta própria.

## Editar e executar

Requer Python 3. O conteúdo editorial está em `conteudo/curso.json`; as páginas são geradas, sem dependências de build externas.

```bash
python3 scripts/gerar_curso.py
python3 scripts/verificar_curso.py
python3 -m http.server 8766
```

Abra `http://localhost:8766`. Edite textos no JSON, estrutura no gerador e apresentação/interações em `assets/`. Regere as páginas antes de commitar.

- `curso/`: índices das quatro trilhas e módulos completos.
- `materiais/`: fichas práticas, CSV fictício e curso em Markdown.
- `assets/`: fontes locais, estilos e aprendizagem.
- `PLANO-PROJETOS.md`: portfólio de 12 projetos propostos; implementações futuras.
- `PRODUCT.md` e `DESIGN.md`: decisões de produto e interface.

## Publicação e privacidade

GitHub Pages publica a raiz da branch `main` deste repositório. O curso e seus materiais editoriais ficam versionados aqui. Materiais privados de preparação em `down/`, mídias, transcrições e ferramentas de coleta são excluídos pelo `.gitignore` e não fazem parte da publicação.

A licença da fonte Inter acompanha os arquivos em `assets/inter-LICENSE.txt`.

<!-- inema-backlink:v1 -->
## Mais no INEMA.CLUB

- [Ficha completa deste curso](https://www.inema.club/cursos/275-pilulas-de-ouro-ia-em-projetos-praticos/)
- [Guia: como aprender inteligência artificial](https://www.inema.club/aprender-inteligencia-artificial/)
- [Todos os cursos](https://www.inema.club/cursos/)
<!-- /inema-backlink:v1 -->
