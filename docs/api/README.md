# API-Vertrag v1 – App ↔ Inferenzdienst

Entscheidungen und Begründungen: [ADR 0001](../adr/0001-api-vertrag-v1.md).

- **Maschinenlesbar:** [`openapi.json`](openapi.json) (OpenAPI 3.1, aus dem Code exportiert)
- **Quelle:** Pydantic-Modelle in `service/src/macrolog_service/schemas.py`
- **App-Typen:** generiert nach `app/src/services/api/schema.gen.ts` (`npm run gen:api`)

## Endpunkte

Alle unter `/v1`, Header `X-API-Key` erforderlich (FR-13). Jede Antwort trägt `X-Request-ID`.

| Endpunkt | Anfrage | Antwort |
|---|---|---|
| `POST /v1/estimate` | roher Body, `Content-Type: image/jpeg`, ≤ 10 MB, Kanten 224–4.096 px | 200: [`estimate-response.example.json`](estimate-response.example.json) |
| `GET /v1/health` | – | 200 `ok` / 503 `loading`: [`health-response.example.json`](health-response.example.json) |
| `GET /v1/model` | – | 200: [`model-info-response.example.json`](model-info-response.example.json) |

Fehler: `application/problem+json` nach RFC 9457 – [`error-response.example.json`](error-response.example.json),
alle Codes in [`problems.md`](problems.md).

## Regeln

- Server liefert Codes (`high|medium|low`, Warnungs- und Fehlercodes), **alle Texte macht die App**.
- Werte ungerundet in g bzw. kcal; gerundet wird nur in der Anzeige.
- Unbekannte Felder und Warnungs-Codes ignorieren (Tolerant Reader).
- Innerhalb von v1 nur additive Änderungen; Bruch → `/v2`.

## Vertrag ändern

1. `schemas.py` (und ggf. `routes.py`) anpassen
2. `uv run python -m macrolog_service.openapi_export` → aktualisiert `docs/api/openapi.json`
3. `cd app && npm run gen:api` → aktualisiert `schema.gen.ts`
4. Beispiel-JSONs in `docs/api/` anpassen (werden in der CI gegen die Modelle geprüft)
5. Ein gemeinsamer PR, Review durch die andere Person
