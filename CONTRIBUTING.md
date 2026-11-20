# Mitarbeit an MacroLog+

Gilt für beide Teammitglieder (`julianzangl`, `Fsylkaj`). Grundlage: SRS 4.7.2, HLD 8.1 und 8.5.

## Lokale Umgebung

```bash
# Python (core, ml, service) – braucht uv, Python 3.12 wird automatisch installiert
uv sync
uv run ruff check . && uv run ruff format --check .
uv run pytest

# App – braucht Node.js 22
cd app
npm ci
cp .env.example .env.local      # EXPO_PUBLIC_API_MOCK=1 → ohne Server entwickeln
npm run check                   # ESLint + tsc + Jest
npm start                       # w = Web, i = iOS-Simulator, a = Android
```

Kamera, SQLite und Sensoren laufen nur in einem Development Build (`npx expo run:ios|android`),
nicht im Web.

## Ablauf je Issue

1. Issue im [Projekt-Board](https://github.com/users/julianzangl/projects/3) von **Ready** nach
   **In progress** ziehen und dir zuweisen.
2. Branch von `main` anlegen:

   | Präfix | Wofür | Beispiel |
   |---|---|---|
   | `feat/` | neue Funktion | `feat/30-nutrition-logic` |
   | `fix/` | Fehlerbehebung | `fix/41-consent-not-saved` |
   | `chore/` | Setup, Tooling, Abhängigkeiten | `chore/1-repo-setup` |
   | `docs/` | nur Dokumentation | `docs/49-report-outline` |
   | `exp/` | ML-Experiment ohne Merge-Absicht | `exp/pilot-variant-b` |

   Schema: `<präfix>/<issue-nr>-<kurzbeschreibung>` (Englisch, Kleinbuchstaben, Bindestriche).
3. Commits nach [Conventional Commits](https://www.conventionalcommits.org/de/v1.0.0/):

   ```
   <typ>(<bereich>): <kurze Beschreibung im Imperativ>
   ```

   - Typen: `feat`, `fix`, `test`, `refactor`, `docs`, `chore`, `ci`, `perf`
   - Bereiche: `app`, `core`, `ml`, `service`, `deploy`, `ci`, `docs`
   - Beispiele: `feat(app): add daily totals`, `test(ml): cover test lock (TS-07)`,
     `fix(service): return 413 for oversized uploads`
   - Englisch, Betreffzeile ≤ 72 Zeichen, Begründung bei Bedarf im Body.
4. Pull Request gegen `main` öffnen (Vorlage wird automatisch geladen):
   - `Closes #<nr>` und Bezug auf Anforderungen (FR-xx, S-xx, TS-xx, HLD-Abschnitt)
   - die jeweils andere Person als Reviewer anfordern
5. Merge erst, wenn **CI grün** und **1 Approval** vorhanden ist (Branch-Schutz erzwingt beides).
   Bevorzugt *Squash and merge*, damit `main` je Issue einen sauberen Commit hat.
6. Das Board verschiebt geschlossene Issues und gemergte PRs automatisch nach **Done**.

## Review

- Reviewt wird jeweils von der anderen Person, auch über die Bereichsgrenze hinweg – so kennt jede
  Person die Schnittstellen, die ihre Arbeit betreffen.
- Forschungsrelevante Entscheidungen (Evaluationsprotokoll, Darstellungsvarianten, Studiendesign)
  trifft die verantwortliche Person; im Review wird nachgefragt, nicht überstimmt.
- Änderungen am API-Vertrag nur gemeinsam und im selben PR: `service/src/macrolog_service/schemas.py`,
  `app/src/services/api/types.ts` und `docs/api/`.

## Board

| Spalte | Bedeutung |
|---|---|
| Backlog | geplant, noch nicht dran |
| Ready | als Nächstes zu tun, Abhängigkeiten erfüllt |
| In progress | jemand arbeitet daran (Branch existiert) |
| Done | gemergt bzw. geschlossen |

## Was nie ins Repository gehört

- Secrets (`.env`, API-Keys) – nur Umgebungsvariablen bzw. GitHub-/EAS-Secrets
- Nutrition5k-Rohdaten, eigene Fotos, Modellgewichte (`*.pt`), Laufverzeichnisse
- Projektdokumente als PDF (das Repository ist öffentlich)

## Tags und Versionen

- `freeze-vX.Y` – Konfigurations-Freeze der ML-Pipeline; erst danach wird der Testbestand ausgewertet
- Modellversionen im Register nach Semantic Versioning: MAJOR = geändertes Ausgabeschema,
  MINOR = neues Training, PATCH = nur neue Kalibrierung
- Container-Images in GHCR mit dem Git-Commit als Tag
