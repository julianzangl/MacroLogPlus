# ADR 0001 – API-Vertrag v1 zwischen App und Inferenzdienst

- **Status:** vorgeschlagen (wird mit dem Merge von PR „Closes #2“ angenommen)
- **Datum:** 20.11.2026
- **Beteiligte:** julianzangl, Fsylkaj
- **Bezug:** Issue #2, SRS 2.3.5, HLD 5.2, 5.3, 7, FR-13, FR-14

## Kontext

App und Inferenzdienst werden parallel entwickelt (SRS 1.1.2). Der Entwurf aus HLD 5.2/5.3 legt
Endpunkte, Antwortfelder und Statuscodes fest, lässt aber einige Punkte offen: Format der Fehler und
Warnungen, wer die Texte formuliert, Absicherung von `/v1/health`, Felder von `/v1/model` und wie
Server- und App-Typen synchron bleiben. Dieses ADR entscheidet diese Punkte nach aktuellem Stand der
Technik und begründet die Stellen, an denen vom Beispiel im HLD abgewichen wird.

## Entscheidungen

### 1. Eine Quelle für den Vertrag: OpenAPI 3.1 aus Pydantic, App-Typen generiert

- Die Pydantic-Modelle in `service/src/macrolog_service/schemas.py` sind die einzige Quelle.
- FastAPI erzeugt daraus OpenAPI 3.1; der Export liegt versioniert in `docs/api/openapi.json`
  (`uv run python -m macrolog_service.openapi_export`).
- Die App generiert ihre Typen daraus mit `openapi-typescript`
  (`npm run gen:api` → `app/src/services/api/schema.gen.ts`); `types.ts` gibt nur sprechende Aliase weiter.
- Die CI bricht ab, wenn `openapi.json` oder `schema.gen.ts` nicht zum Code passen, und prüft die
  Beispiel-JSONs in `docs/api/` gegen die Modelle (Contract-Test).

*Begründung:* Handgepflegte Typen auf zwei Seiten driften auseinander. Ein maschinenlesbarer Vertrag
mit generierten Client-Typen ist heute der Standard (Contract-first/Code-first mit OpenAPI) und macht
Vertragsbrüche zu CI-Fehlern statt zu Laufzeitfehlern in der App.

### 2. Maschinencodes vom Server, alle Texte in der App

- Der Dienst liefert nur stabile, englische Codes in `snake_case` (Fehler, Warnungen, Konfidenz).
- Alle Texte für Nutzer:innen formuliert und übersetzt die App.
- Freitext vom Server (`detail`) ist nur für Entwickler:innen und wird nie angezeigt.

*Begründung:* Die Formulierung der KI-Ausgabe ist Teil der UX (SRS 4.2.1: deutsch, ohne
KI-Fachbegriffe; BA Sylkaj: Verständlichkeit, Vertrauen). Sie muss ohne Server-Deployment änderbar und in
Usability-Tests variierbar sein. Getrennte Codes und Texte sind gängige Praxis für lokalisierbare APIs.

### 3. Konfidenzstufe als `high | medium | low` (Abweichung vom HLD-Beispiel)

Das HLD-Beispiel verwendet `"mittel"`. Konsequent zu Entscheidung 2 werden auch die Konfidenzstufen als
sprachneutrale Codes übertragen; die App zeigt „hoch/mittel/niedrig“ (Text + Symbol, S-01, FR-08).

### 4. Warnungen als Code-Liste, App ignoriert unbekannte Codes

`warnings: WarningCode[]` mit

| Code | Auslöser (HLD 3.8) |
|---|---|
| `unusual_image` | σ(x) über dem 95. Perzentil des Validierungsbestands |
| `low_light` | Helligkeit unter Grenzwert |
| `blurry` | Schärfemaß unter Grenzwert |
| `implausible_values` | z. B. Energiedichte > 9 kcal/g |

Die App muss unbekannte Codes still ignorieren (Tolerant Reader), damit neue Warnungen ohne
App-Update ergänzt werden können.

### 5. Fehler als Problem Details nach RFC 9457

Alle Fehler werden als `application/problem+json` (RFC 9457, Nachfolger von RFC 7807) ausgeliefert:

```json
{
  "type": "https://github.com/julianzangl/MacroLogPlus/blob/main/docs/api/problems.md#payload_too_large",
  "title": "Payload too large",
  "status": 413,
  "detail": "Upload exceeds 10 MB",
  "code": "payload_too_large",
  "request_id": "3f9c2a7e-1b2c-4d5e-8f90-123456789abc"
}
```

- `type` verweist auf die Beschreibung in [`problems.md`](../api/problems.md), `code` ist der
  kurze Schlüssel, nach dem die App verzweigt, `request_id` verknüpft die Meldung mit dem Protokoll.
- Codes: `invalid_image`, `invalid_image_dimensions` (400), `unauthorized` (401), `not_found` (404),
  `method_not_allowed` (405), `payload_too_large` (413), `unsupported_media_type` (415),
  `validation_error` (422), `rate_limited` (429), `internal_error` (500), `model_unavailable` (503).
- Nie Stacktraces oder interne Details (HLD 5.3, OWASP API8).

*Begründung:* RFC 9457 ist der IETF-Standard für Fehler in HTTP-APIs und wird von FastAPI, Spring,
ASP.NET usw. unterstützt. Die Anforderung aus HLD 5.3 („einheitliches JSON-Format mit Code, kurzer
Meldung und request_id“) bleibt erfüllt.

### 6. Request-ID und Header

- Der Dienst erzeugt für jede Anfrage eine UUIDv4 und liefert sie im Header `X-Request-ID` und in
  Schätzungen bzw. Fehlern mit. Vom Client gesendete IDs werden nicht übernommen.
- `429` und `503` senden `Retry-After` in Sekunden (RFC 9110 §10.2.3).
- Antworten auf `/v1/estimate` tragen `Cache-Control: no-store` (Ernährungsdaten gelten als sensibel,
  HLD 7).

### 7. Authentifizierung bleibt `X-API-Key` – auch für `/v1/health`

- Alle Endpunkte unter `/v1` verlangen den API-Schlüssel (FR-13, Muss-Kriterium M-08).
- Der Docker-Health-Check läuft im Container und liest den Schlüssel aus der Umgebungsvariable
  `API_KEYS`; ein ungeschützter Endpunkt ist dafür nicht nötig.
- `/v1/health` antwortet `200 {"status": "ok", ...}` bzw. `503 {"status": "loading", ...}` während
  Modell-Laden und Aufwärm-Inferenz; der Body bleibt in beiden Fällen ein `HealthResponse`.

*Begründung:* Ein öffentlicher Liveness-Endpunkt wäre in Kubernetes-Umgebungen üblich, widerspräche hier
aber FR-13 und brächte keinen Vorteil, weil der Check ohnehin im Container läuft.

### 8. Upload bleibt roher JPEG-Body mit festen Grenzen

- `POST /v1/estimate` mit `Content-Type: image/jpeg`, Body = JPEG-Bytes (kein Multipart, HLD 5.2).
- Grenzen: ≤ 10 MB (`413`), kürzere Kante ≥ 224 px, längere Kante ≤ 4.096 px (`400
  invalid_image_dimensions`), nicht dekodierbar → `400 invalid_image`, anderer Typ → `415`.
- Die App sendet laut HLD 4.2 ohnehin ≤ 1.280 px.

### 9. Zahlen ungerundet in Basiseinheiten

Alle Werte als JSON-Zahlen in g bzw. kcal, ungerundet. Gerundet wird nur in der App für die Anzeige
(SRS 4.2.1); die Portionskorrektur rechnet mit den vollen Werten von `per_gram` und
`known_mass_factors`. Das hält auch TS-08 (Toleranz 10⁻⁴) einfach.

### 10. `/v1/model` liefert alles für die Infoseite

```json
{
  "version": "1.0.0",
  "variant": "B",
  "trained_at": "2026-12-10",
  "dataset": { "name": "Nutrition5k", "license": "CC BY 4.0", "url": "...", "data_version": "a1b2c3d4" },
  "coverage": { "nominal": 0.8, "validation": 0.81 },
  "validation_mae": { "mass_g": 38.2, "energy_kcal": 92.5, "fat_g": 6.1, "carbs_g": 9.8, "protein_g": 7.4 },
  "validation_mae_percent": { "mass_g": 0.19, "energy_kcal": 0.36, "fat_g": 0.42, "carbs_g": 0.39, "protein_g": 0.37 },
  "model_card_summary": "…"
}
```

Die Infoseite (SRS 4.2.6) braucht Datengrundlage, Modellversion und durchschnittliche Abweichung.
`validation_mae_percent` ist ein Anteil (0,36 = 36 %), damit die App „im Schnitt etwa ±36 %“ formulieren
kann. `model_card_summary` ist der einzige Freitext und wird vom ML-Team auf Deutsch gepflegt.

### 11. Versionierung und Kompatibilität

- Pfadversion `/v1`. Innerhalb von v1 sind nur **additive** Änderungen erlaubt (neue optionale Felder,
  neue Warnungs-Codes). Clients ignorieren unbekannte Felder.
- Inkompatible Änderungen → `/v2` und neue MAJOR-Version des Modells (HLD 8.1).
- Änderungen am Vertrag nur gemeinsam und im selben PR für Dienst, App-Typen und Doku.

## Konsequenzen

- (+) Vertragsbrüche fallen in der CI auf, nicht erst auf dem Gerät.
- (+) Texte und Darstellung bleiben vollständig in der App und damit im Studiendesign steuerbar.
- (+) Fehlerbehandlung nach Standard; Werkzeuge und Bibliotheken verstehen das Format.
- (−) Ein zusätzlicher Generierungsschritt (`npm run gen:api`) nach Vertragsänderungen.
- (−) Kleine Abweichungen vom Beispiel im HLD (Konfidenz-Codes, Fehlerformat, erweitertes `/v1/model`) –
  im Abschlussbericht zu erwähnen.
