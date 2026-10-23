# Vault modelo

Copie esta pasta, abra no Obsidian ("Abrir pasta como vault") e comece pelo `00-Inbox`.

- `00-Inbox/` captura rápida
- `10-Journal/` uma nota por dia
- `20-Projects/` com prazo e fim
- `30-Areas/` Personal · Spiritual · Professional
- `40-Sources/` notas de livros e aulas
- `50-Permanent-Notes/` suas ideias, em frases completas
- `90-Templates/` Configurar em *Configurações → Templates* (ou plugin Templates) apontando para esta pasta

Notas diárias e templates já vêm configurados em `.obsidian/` (pasta `10-Journal`, formato `YYYY/YYYY-MM-DD`, template `Journal`).
Isso cria uma subpasta por ano (`10-Journal/2026/2026-10-23.md`). Não crie pasta por mês.

## Git e `.obsidian/`

O `.gitignore` versiona as configurações e a lista de plugins e temas, mas **não** o código deles: dos plugins ficam só `manifest.json` e `data.json`; `workspace.json` e caches são ignorados. Depois de clonar, o Obsidian pede para reativar os plugins da lista.

Limite: 7 pastas, 3 propriedades, 3 templates em uso (ver `method/sustainability.md`).

## Templates: comece só com 3

- **Essenciais:** `Journal`, `Source-note`, `Permanent-note`.
- **Opcionais** (adicione depois de 2–3 semanas): `Reading-session`, `Weekly-review`.
