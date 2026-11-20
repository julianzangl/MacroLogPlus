# Fehlertypen der API (RFC 9457)

Alle Fehler werden als `application/problem+json` ausgeliefert. Die App verzweigt nach `code`;
`detail` ist nur für Entwickler:innen. Hintergrund: [ADR 0001](../adr/0001-api-vertrag-v1.md).

| Code | Status | Bedeutung | Verhalten der App (HLD 5.3) |
|---|---|---|---|
| `invalid_image` | 400 | Bild nicht dekodierbar | Hinweis, Foto erneut aufnehmen oder manuell erfassen |
| `invalid_image_dimensions` | 400 | Kürzere Kante < 224 px oder längere Kante > 4.096 px | wie `invalid_image` |
| `unauthorized` | 401 | API-Schlüssel fehlt oder ist ungültig (TS-06) | Hinweis auf Konfigurationsfehler, manuelle Erfassung |
| `not_found` | 404 | Pfad existiert nicht | Konfigurationsfehler |
| `method_not_allowed` | 405 | falsche HTTP-Methode | Konfigurationsfehler |
| `payload_too_large` | 413 | Datei größer als 10 MB (TS-06) | Bild stärker verkleinern und erneut senden |
| `unsupported_media_type` | 415 | Inhaltstyp ist nicht `image/jpeg` | wie `invalid_image` |
| `validation_error` | 422 | Anfrage formal ungültig | Konfigurationsfehler |
| `rate_limited` | 429 | Ratenbegrenzung überschritten, `Retry-After` beachten | später erneut versuchen |
| `internal_error` | 500 | unerwarteter Fehler im Dienst | später erneut versuchen, manuelle Erfassung |
| `model_unavailable` | 503 | Modell nicht geladen oder Dienst startet, `Retry-After` beachten | später erneut versuchen, manuelle Erfassung |

### invalid_image

Der Body ließ sich nicht als JPEG dekodieren.

### invalid_image_dimensions

Das Bild ist zu klein für die Vorverarbeitung (kürzere Kante < 224 px) oder größer als erlaubt
(längere Kante > 4.096 px).

### unauthorized

Header `X-API-Key` fehlt oder enthält keinen gültigen Schlüssel. Es wird bewusst nicht unterschieden,
welcher der beiden Fälle vorliegt.

### not_found

Der angefragte Pfad existiert nicht.

### method_not_allowed

Der Pfad existiert, unterstützt die HTTP-Methode aber nicht.

### payload_too_large

Der Body ist größer als 10 MB.

### unsupported_media_type

`Content-Type` ist nicht `image/jpeg`.

### validation_error

Die Anfrage ist formal ungültig (z. B. falsche Header).

### rate_limited

Zu viele Anfragen mit diesem Schlüssel. Der Header `Retry-After` nennt die Wartezeit in Sekunden.

### internal_error

Unerwarteter Fehler. Details stehen nur im Protokoll des Dienstes (über `request_id` auffindbar).

### model_unavailable

Das Modell wird gerade geladen oder ist nicht verfügbar. Der Header `Retry-After` nennt die Wartezeit in
Sekunden.
