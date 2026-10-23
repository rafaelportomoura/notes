# Um vault ou vários?

## Recomendação

**Um vault só**, organizado por pastas e ligações. Separe um segundo vault **apenas** se houver uma razão rígida (veja abaixo).

## Por que um só

- **O valor do Obsidian está nos links.** Uma ideia da vida espiritual (ex.: "atenção plena") pode se ligar a uma de trabalho (foco) e a uma do diário. Em vaults separados, esses links não existem.
- **Busca única.** Uma pesquisa encontra tudo.
- **Menos atrito = mais constância.** Para quem procrastina, "em qual vault eu escrevo isso?" já é um motivo para não escrever.
- **Uma rotina de revisão** em vez de três.

## Quando separar

| Situação | Ação |
|---|---|
| Notas de trabalho com dados da empresa, clientes ou segredo | Vault separado (ou fora do seu sync pessoal). Segue as regras da empresa. |
| Você precisa compartilhar um vault com outras pessoas | Vault separado |
| Diário íntimo que você quer criptografar | Vault separado ou pasta criptografada |

Fora isso, use **pastas** e **propriedades/tags** para separar contextos.

## Estrutura sugerida (já em `template-vault/`)

```
00-Inbox/             captura rápida, esvaziar toda semana
10-Journal/            uma nota por dia
20-Projects/          o que tem prazo e fim (ex.: "Estudar Liber O")
30-Areas/             o que dura (Personal, Spiritual, Professional)
40-Sources/            notas de literatura (livros, artigos, aulas)
50-Permanent-Notes/ ideias suas, em frases completas, ligadas entre si
90-Templates/
```

Base: método PARA (Projetos, Áreas, Recursos, Arquivo) misturado com Zettelkasten. Não use mais que isso no começo.

## Propriedades mínimas (frontmatter)

```yaml
type: source | permanent | journal | project
area: personal | spiritual | professional
status: inbox | reading | done
```

## Regra de ouro

A organização é para **encontrar depois**, não para ficar bonita. Se você gasta mais tempo organizando do que lendo e anotando, volte ao mínimo.
