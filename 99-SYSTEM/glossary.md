# Glossário

Termos do sistema, em ordem alfabética dentro de cada grupo. Nomes de pastas, arquivos e propriedades ficam em inglês; a explicação, em português.

## Vault e organização

| Termo | Significado |
|---|---|
| **Vault** | A pasta que o Obsidian abre. Aqui, é a raiz deste repositório. Um só, para tudo (ver `decisions/one-vault-or-many.md`). |
| **Inbox** (`00-Inbox/`) | Captura rápida, sem formatar. Esvaziada na revisão semanal: apagar, virar tarefa ou virar nota. |
| **Journal** (`10-Journal/`) | Uma nota por dia, em `YYYY/YYYY-MM-DD`. Só a linha "1 linha" é obrigatória. |
| **Project** (`20-Projects/`) | Algo com prazo e fim (ex.: estudar um livro). Quando acaba, sai do caminho. |
| **Area** (`30-Areas/`) | Algo que dura e não "termina": `Personal`, `Spiritual`, `Professional`. |
| **Sources** (`40-Sources/`) | Notas de livros, artigos e aulas. Uma nota por fonte. |
| **Permanent notes** (`50-Permanent-Notes/`) | Suas ideias, em frases completas, ligadas entre si. É o coração do vault. |
| **Templates** (`90-Templates/`) | Modelos de nota. Essenciais: `Journal`, `Source-note`, `Permanent-note`. |
| **99-SYSTEM** | Método, decisões, plano e este glossário. É o "manual" do vault, fora do fluxo diário. |
| **PARA** | Método de pastas: Projects, Areas, Resources, Archive. Aqui, adaptado e simplificado. |
| **Zettelkasten** | Método de notas pequenas e ligadas entre si, uma ideia por nota. |
| **MOC** (Map of Content) | Nota-índice de um assunto. Só se cria quando passa de ~10 notas sobre ele. |
| **Wikilink** | Link `[[nota]]`. Quanto mais ligações, mais útil o vault. |
| **Backlink** | Lista de notas que apontam para a nota atual. |
| **Frontmatter / propriedades** | Bloco `---` no topo da nota. Só 3 propriedades: `type`, `area`, `status`. |
| **`.obsidian/`** | Configurações do Obsidian. Versionadas, exceto código de plugins e estado volátil. |

## Ler, anotar e lembrar

| Termo | Significado |
|---|---|
| **Passada** | Cada leitura de um texto. São 3: *mapa*, *leitura* e *fechar* (ver `method/reading.md`). |
| **SQ3R** | Survey, Question, Read, Recite, Review. A base das passadas, em versão enxuta. |
| **Nota de fonte** (literature note) | Resumo e ideias de uma fonte, com suas palavras e a referência. |
| **Nota permanente** | Uma ideia, em frase completa, entendível sem abrir a fonte, com 2+ links. |
| **Captura** | Anotar rápido no Inbox, sem processar. |
| **Cornell** | Formato de anotação de aulas: pistas à esquerda, notas à direita, resumo embaixo. |
| **Recuperação ativa** (retrieval practice) | Tentar lembrar *sem olhar* e depois conferir. Funciona mais que reler. |
| **Repetição espaçada** | Revisar em intervalos crescentes (1 dia, 3 dias, 1 semana, 1 mês). |
| **Anki** | Programa de flashcards com repetição espaçada. Uma pergunta por cartão. |
| **Técnica de Feynman** | Explicar o conceito de forma simples; onde travar é a lacuna. |
| **Intercalar** | Alternar temas em vez de estudar um só por horas. |

## Rotina e sustentabilidade

| Termo | Significado |
|---|---|
| **Sessão mínima viável** | A versão pequena da prática (≈10 min). No pior dia, esse é o padrão. |
| **Modo pleno** | Semana tranquila: sessão de 25–45 min, nota de fonte e 1 permanente. |
| **Modo leve** | Semana normal (padrão): 10–15 min, ler e escrever 3 linhas. |
| **Modo manutenção** | Semana corrida ou de crise: 5 min, abrir a nota do dia e escrever 1 linha. |
| **Dias em 7** | Medida de constância (ex.: 4 em 7 é ótimo), no lugar de "dias seguidos". |
| **Pausa sem culpa** | Até 7 dias parados sem se punir; na volta, só o mínimo. |
| **Revisão semanal** | 20–30 min fixos: esvaziar o Inbox, escolher notas para virar permanentes, ver o que travou, definir 1 prioridade e o modo da próxima semana. |
| **Revisão mensal** | 1 h: ver o que cresceu, cortar o que não é usado. Único momento de mudar o método. |
| **Teste dos 3 meses** | Três perguntas que dizem se o sistema é sustentável (ver `method/sustainability.md`). |
| **Teto de complexidade** | 8 pastas na raiz, 3 propriedades, 3 templates em uso. Para adicionar algo, remova outra coisa. |
| **Colecionismo** | Juntar fontes e notas sem processar. Antídotos: 1 fonte por vez, regra 3 por 1. |

## Lições dos agentes (`.claude/lessons/`)

| Termo | Significado |
|---|---|
| **Lesson** | Aprendizado de um agente, em um arquivo curto, com corpo imutável. |
| **Nó** (node) | Pasta com um `SUMMARY.md` limitado, lições soltas e nós filhos. |
| **`nodes/`** | Contêiner de todos os tópicos de lições (sem resumo próprio). |
| **`SUMMARY.md`** | Resumo consolidado de um nó. O da raiz é carregado em toda sessão. |
| **Inbox de lições** (`_inbox/`) | Onde nascem as lições novas, antes de serem roteadas a um tópico. |
| **Tópico** | O caminho do nó em relação a `nodes/` (ex.: `tooling/obsidian`). |
| **Cap (teto)** | Limite de tamanho: 40 linhas / 3000 bytes por resumo, 12 filhos, 8 lições soltas por nó. |
| **Route** | Mover uma lição do inbox para o tópico certo e atualizar o resumo. |
| **Fold** | Agrupar lições soltas em subpastas e condensar seus resumos para cima. |
| **Split** | Dividir um nó com filhos demais, agrupando-os sob um novo nó. |
| **Superseded** | Lição substituída por outra mais nova. Continua no repositório. |
| **Imutabilidade** | O corpo de uma lição nunca é editado; só `hits`, `status` e `superseded_by`. |
| **Skill `lessons`** | Instruções e script (`lessons.py check`/`new`) para capturar e consolidar lições. |
