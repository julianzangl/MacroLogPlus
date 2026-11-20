# API-Vertrag App ↔ Inferenzdienst (HLD 5.2, 5.3)

Alle Endpunkte unter `/v1`, Header `X-API-Key` erforderlich.

| Endpunkt | Anfrage | Antwort |
|---|---|---|
| `POST /v1/estimate` | roher Body, `image/jpeg`, ≤ 10 MB | 200: [`estimate-response.example.json`](estimate-response.example.json) |
| `GET /v1/health` | – | 200 `{status: "ok", model_version}`; 503 während des Ladens |
| `GET /v1/model` | – | 200: Version, Variante, Trainingsdatum, Validierungs-MAE, Abdeckung, Modellkarte (Kurzfassung) |

Fehler: einheitliches Format [`error-response.example.json`](error-response.example.json)
mit Codes 400, 401, 413, 415, 429, 503.

**Single Source of Truth:** Pydantic-Modelle in `service/src/macrolog_service/schemas.py`
(OpenAPI unter `/docs` des laufenden Dienstes). Die TypeScript-Typen in
`app/src/services/api/types.ts` müssen bei jeder Änderung mitgezogen werden.
Änderungen am Antwortschema = MAJOR-Version des Modells bzw. neuer API-Pfad.
