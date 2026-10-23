# notes

Este repositório **é o vault do Obsidian** (abra a pasta raiz com "Abrir pasta como vault").
Ele também guarda o projeto para aprender a ler, anotar e lembrar: tudo o que é método e decisão fica em `99-SYSTEM/`.

> Objetivo: uma prática de estudo **fácil de manter**, que **não vire peso**, com notas que dá para consultar depois.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `00-Inbox/` | captura rápida; esvaziar toda semana |
| `10-Journal/` | uma nota por dia (`YYYY/YYYY-MM-DD`) |
| `20-Projects/` | o que tem prazo e fim |
| `30-Areas/` | o que dura: Personal · Spiritual · Professional |
| `40-Sources/` | notas de livros, artigos e aulas |
| `50-Permanent-Notes/` | suas ideias, em frases completas, ligadas entre si |
| `90-Templates/` | `Journal`, `Source-note`, `Permanent-note` (essenciais); `Reading-session`, `Weekly-review` (opcionais) |
| `99-SYSTEM/` | método, decisões e plano de 30 dias (ver abaixo) |

Limite: 8 pastas na raiz, 3 propriedades (`type`, `area`, `status`) e 3 templates em uso (ver `99-SYSTEM/method/sustainability.md`).

## Começando

1. Leia `99-SYSTEM/decisions/one-vault-or-many.md` (5 min).
2. Leia primeiro `99-SYSTEM/method/sustainability.md` (a regra que protege o resto), depois os outros guias de `99-SYSTEM/method/` (um por dia, ~10 min cada).
3. Siga `99-SYSTEM/plan-30-days.md`. É curto de propósito.

## `99-SYSTEM/`

| Arquivo | Conteúdo |
|---|---|
| `decisions/one-vault-or-many.md` | Um vault só; quando separar |
| `method/reading.md` | Leitura ativa em 3 passadas |
| `method/note-taking.md` | Do rascunho à nota permanente |
| `method/remembering.md` | Recuperação ativa e repetição espaçada |
| `method/routine.md` | Sessão mínima, antiprocrastinação, revisão semanal |
| `method/sustainability.md` | Modos pleno/leve/manutenção, pausa sem culpa, teste dos 3 meses |
| `plan-30-days.md` | Prática guiada |
| `glossary.md` | Termos do sistema |

## Configuração do Obsidian e Git

- Notas diárias e templates já vêm configurados em `.obsidian/` (pasta `10-Journal`, formato `YYYY/YYYY-MM-DD`, template `Journal`). Isso cria uma subpasta por ano; não crie pasta por mês.
- O `.gitignore` versiona as configurações e a lista de plugins e temas, mas **não** o código deles: dos plugins ficam só `manifest.json` e `data.json`; `workspace.json` e caches são ignorados. Depois de clonar, o Obsidian pede para reativar os plugins da lista.
- `.claude/`, `CLAUDE.md` e este `README.md` são do projeto e do agente; o Obsidian ignora pastas ocultas.

## Regra única

Se um passo do método tomar mais de 15 minutos por dia, ele é complexo demais. **Simplifique antes de abandonar.**
