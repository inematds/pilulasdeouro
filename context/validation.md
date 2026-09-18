# Verificação — 18/09/2026

- Estrutura: 18 páginas, 12 módulos, 72 tópicos; um h1 por página; IDs únicos; manifesto consistente; links e âncoras locais existentes.
- Navegador Chromium: todas as páginas carregadas sem erro JavaScript; progresso total 72; leitura persiste entre páginas; dúvidas e checagens registradas.
- Exportação/importação: round-trip preserva campos extras; curso diferente e notas malformadas rejeitados sem alterar progresso.
- Grifos: criados por Range, restaurados após navegação; notas de outro módulo não se tornam órfãs.
- Jornada/aparência: abrem por clique, fecham por Escape; tema muda; retomada localiza o módulo; preview abre e fecha.
- Fallback: conteúdo de tópicos visível sem JavaScript; storage bloqueado mantém leitura e progresso efêmero.
- Responsivo: índices e módulo em 360 px sem overflow; capturas desktop e mobile revisadas. Claro/sépia capturados após estabilização.
- Revisão independente: dois problemas de contraste corrigidos e classificados como resolvidos.
- Portal: 7 testes aprovados e build Next.js concluído.
- Base de conteúdo: 41 testes aprovados; novo curso classificado nos filtros.

Capturas e scripts temporários de navegador permanecem na pasta local de trabalho. O validador público de links pode ser repetido com `python3 scripts/verificar_curso.py`.
