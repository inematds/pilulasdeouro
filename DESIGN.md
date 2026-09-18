---
name: Pílulas de Ouro
description: Sistema INEMA v2 para leitura, prática e entregas verificáveis.
colors:
  primary: "hsl(48 96% 53%)"
  primary-ink: "hsl(48 96% 53%)"
  on-primary: "#111827"
  accent-2: "hsl(199 92% 60%)"
  bg: "#111827"
  surface: "#1f2937"
  surface-2: "#374151"
  text: "#e6e6e6"
  text-muted: "#a8a8b3"
  border: "#374151"
  border-strong: "#4b5563"
  track-emerald: "#6ee7b7"
  track-blue: "#93c5fd"
  track-purple: "#d8b4fe"
  track-amber: "#fcd34d"
  light-bg: "#ffffff"
  light-surface: "#f8fafc"
  light-surface-2: "#f3f4f6"
  light-text: "#1a1a1a"
  light-muted: "#555f6e"
  light-border: "#e2e8f0"
  light-border-strong: "#718096"
  light-primary-ink: "#92400e"
  light-on-primary: "#1a1a1a"
  light-track-emerald: "#047857"
  light-track-blue: "#1d4ed8"
  light-track-purple: "#7c3aed"
  light-track-amber: "#92400e"
  sepia-bg: "#fbf0d9"
  sepia-surface: "#f4e8ce"
  sepia-surface-2: "#ecdfbf"
  sepia-text: "#5f4b32"
  sepia-muted: "#705c42"
  sepia-border: "#e0d2b0"
  sepia-border-strong: "#8b765c"
  sepia-primary-ink: "#7c4a12"
  sepia-on-primary: "#3b2c18"
  contrast-bg: "#0a0e14"
  contrast-surface: "#131a24"
  contrast-surface-2: "#1e2733"
  contrast-text: "#f5f7fa"
  contrast-muted: "#c7ced6"
  contrast-border: "#3a4658"
  contrast-border-strong: "#8e99a8"
  contrast-on-primary: "#0a0e14"
typography:
  display:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "clamp(3rem, 5vw, 4.6rem)"
    fontWeight: 800
    lineHeight: 1.03
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1.65rem"
    fontWeight: 700
    lineHeight: 1.22
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "0.83rem"
    fontWeight: 600
    lineHeight: 1.35
rounded:
  sm: "0.5rem"
  control: "9px"
  md: "0.75rem"
  panel: "14px"
  hero: "16px"
  pill: "9999px"
spacing:
  sm: "0.5rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
  section: "3.5rem"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.control}"
    padding: "0.7rem 1rem"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    padding: "0.7rem 1rem"
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.panel}"
    padding: "1.6rem"
---

# Design System: Pílulas de Ouro

## Overview

**Direção escolhida: INEMA v2 dark âmbar.** A interface combina fundo azul-acinzentado escuro, marca âmbar, Inter local e diagramas SVG geométricos. O objetivo visual é sustentar leitura e prática: títulos claros, explicações com medida confortável e controles de aprendizagem próximos do conteúdo.

Quatro cores identificam Fundamentos, Conhecimento, Produção e Entrega. A estrutura atual contém quatro trilhas, doze módulos e setenta e dois tópicos. Esses números descrevem o curso; a linguagem visual permanece reutilizável em novas páginas.

Características: superfícies sólidas; hierarquia por tipografia e espaçamento; diagramas explicativos; temas de leitura; estados acompanhados de texto. Documento extraído de `assets/learn.css`, `assets/site.css`, `assets/fonts.css` e do contrato visual em `index.html`. O sidecar `.impeccable/design.json` reúne extensões e exemplos.

## Colors

### Primary

O âmbar marca a identidade e a ação principal. **Regra de tinta e preenchimento:** `--primary` serve ao preenchimento, `--primary-ink` ao texto âmbar e `--on-primary` ao texto sobre botões preenchidos. A tinta escurece em claro e sépia; não aplicar o amarelo de preenchimento diretamente sobre esses fundos. O botão principal da página usa atualmente o texto escuro do tema padrão de forma literal; os controles da camada de aprendizagem usam `--on-primary`.

### Secondary

O ciano `accent-2` identifica INEMA.CLUB e o foco de teclado. Os tons das quatro trilhas seguem a ordem emerald, blue, purple e amber. Números, títulos auxiliares e links dão redundância à cor. O token `--track` identifica a trilha; `--accent` e `--accent-text` pertencem aos controles de aprendizagem e às preferências. Não são intercambiáveis: o acento pessoal não renomeia a trilha.

### Neutral

Fundo, superfície, superfície secundária, texto e bordas formam camadas sólidas. Os tokens sem prefixo no frontmatter representam o dark padrão. As famílias `light-*`, `sepia-*` e `contrast-*` registram os valores efetivos após a cascata de `site.css`, inclusive texto secundário e bordas reforçadas.

Claro retira a classe `dark`; sépia e contraste acrescentam seus atributos de tema. Foco é uma preferência de apresentação: reduz elementos laterais, sem criar outra paleta. Novos componentes devem consumir variáveis semânticas, preservando todos esses modos.

## Typography

Inter é servida localmente, em pesos 400, 500, 600, 700 e 800, com `font-display: swap`. Display e corpo compartilham a família; hierarquia vem de tamanho, peso e ritmo. O hero usa display, títulos de página usam `clamp(2rem, 4vw, 3.3rem)` e títulos de tópico usam 1.6rem. O corpo geral tem entrelinha 1.65; a prosa tem 1.7 e medida padrão de 68ch.

Preferências de prosa oferecem medida de 60, 68 ou 75ch, entrelinha compacta ou confortável e escala relativa da fonte. A escolha de fonte afeta a prosa; o chrome mantém Inter. A opção de leitura declara Atkinson Hyperlegible e cai para Inter quando ela não está disponível; apenas Inter tem arquivos locais registrados. Código usa `ui-monospace, SFMono-Regular, Consolas, monospace`, tamanho 0.82rem e entrelinha 1.7.

## Layout

O contêiner central mede no máximo 1160px, com margem lateral total de 3rem no desktop e 2rem no mobile. O hero usa duas colunas proporcionais (1.15:1); páginas de módulo usam índice lateral de 210px e área flexível, separados por 3rem. O mapa de módulos tem três colunas. A lista de trilhas é organizada em linhas com número, título, descrição e acesso.

Em 1050px o índice passa a 170px e detalhes da navegação encolhem. Em 720px o conteúdo principal vira uma coluna, a navegação de trilhas forma grade de duas colunas e as estatísticas ficam em duas colunas. A camada de aprendizagem tem também ajustes próprios em 1024px para seu índice e 640px para o painel de jornada. O índice efetivo da página usa o comportamento de `site.css`.

A prosa limita somente a leitura; tabelas, código e figuras podem aproveitar a largura da área. Diagramas têm versões verticais no mobile; o diagrama do hero usa a versão vertical em todos os tamanhos. Navegação fixa e âncoras mantêm compensação de altura. Foco esconde o índice lateral e centraliza o módulo em até 900px.

## Elevation & Depth

A profundidade vem sobretudo de superfícies e bordas, sem sombra nos cartões comuns. Sombras ficam em popovers, painel de jornada e avisos temporários. O popover da página usa `0 12px 32px #0003`; a jornada usa `-12px 0 40px hsl(220 40% 4% / 0.3)`. O preview tem backdrop escuro e conteúdo contido em diálogo.

Mudanças de estado são discretas: cor, borda e sublinhado. A camada de aprendizagem tem durações de 120, 180 e 320ms com curva `cubic-bezier(0.4, 0, 0.2, 1)`. Movimento reduzido desativa animações, transições e rolagem suave.

## Shapes

Cantos suaves organizam superfícies de estudo: painéis usam raio de 14px, diagramas e cartões compactos 12px, hero 16px. Controles usam 8–9px; etiquetas e alguns controles de estado são pílulas. Números de tópico e etapas são circulares. A marca é um símbolo hexagonal em SVG. Bordas finas separam linhas e áreas de leitura sem criar caixas em torno de cada parágrafo.

## Components

**Botões.** Ações alinhadas ao início, ícone opcional e rótulo explícito. O botão principal usa âmbar, o secundário superfície neutra; ambos têm padding de 0.7rem por 1rem e altura mínima de 44px. Hover altera preenchimento ou brilho. Foco de teclado tem contorno ciano de 3px; os controles da página usam afastamento de 4px, a camada de aprendizagem usa 2px.

**Navegação.** Marca à esquerda, acesso INEMA.CLUB em ciano, quatro trilhas e aparência. Links ativos combinam superfície secundária e cor da trilha. No mobile os rótulos completos continuam visíveis numa grade. Breadcrumbs e índice situam o leitor; links permitem retorno e avanço entre módulos.

**Painéis e cartões.** Superfície sólida, borda sutil e espaçamento interno de 1.4–1.6rem. Cartões de módulo agrupam introdução, tópicos expansíveis e ações. Sem JavaScript, explicações permanecem visíveis. Cards do mapa reforçam a borda com a cor da trilha no hover.

**Diagramas.** SVG com blocos, setas, rótulos e legenda explica relações do conteúdo. A composição pode mudar no mobile para preservar a leitura. Ilustração deve transmitir um conceito; não é textura de fundo.

**Leitura e prática.** Comparações lado a lado, passos numerados, caixas de prompt com cópia, tabelas, prática e respostas em `details` atendem funções distintas. Comparações se empilham no mobile. Cor de acerto/erro acompanha texto explicativo; checagem não bloqueia o estudo.

**Controles de aprendizagem.** Marcar lido e dúvida usam estado pressionado, texto e cor. Barras mostram progresso numérico junto à representação visual. A jornada abre à direita, ocupa até 30rem no desktop e toda a largura em telas estreitas. Filtros são chips; exportação e importação ficam no rodapé. O seletor nativo de cor das marcações herda superfície e texto; não existe campo de busca desenhado no curso.

**Aparência.** Popover com grupos de botões para temas e preferências. A escolha atual usa borda âmbar e tinta âmbar, com estado acessível. Preferências acompanham a leitura sem substituir a identidade das trilhas.

## Do's and Don'ts

- **Do** manter dark âmbar, Inter local, quatro cores de trilha e diagramas SVG como vocabulário comum.
- **Do** usar `primary-ink` para texto e `on-primary` sobre preenchimentos principais.
- **Do** conferir claro, sépia, contraste, teclado e mobile após mudanças de componente.
- **Do** combinar cor com rótulo, número, borda ou estado textual.
- **Do** preservar texto acessível sem JavaScript e respeitar movimento reduzido.
- **Don't** transformar a preferência de acento em mudança da identificação das trilhas.
- **Don't** fixar cores claras de texto sobre superfícies claras ou sépia.
- **Don't** aplicar limite de medida da prosa a tabelas e diagramas inteiros.
- **Don't** acrescentar animação decorativa ou dependência de fonte remota para reproduzir este sistema.
