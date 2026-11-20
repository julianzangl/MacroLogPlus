# MacroLog+

KI-gestütztes Ernährungstracking: Energie (kcal) und Makronährstoffe (Fett, Kohlenhydrate, Protein)
manuell, über eigene Gerichte oder per Foto erfassen. Die Fotoschätzung nutzt ein ResNet-50, trainiert
auf Nutrition5k, und liefert jede Schätzung mit 80-%-Unsicherheitsbereich, Konfidenzstufe und kurzer
Erklärung.

Wahlfachprojekt 2, Hochschule Campus Wien (CSDC VZ27) – Florian Sylkaj, Julian Zangl.

## Repository

```
app/       Mobile App (Expo, React Native, TypeScript)
core/      macrolog_core – gemeinsamer Inferenzkern (Vorverarbeitung, Modell, Kalibrierung)
ml/        macrolog_ml – ML-Pipeline (Daten, Training A/B/C, Evaluation, Kalibrierung, Release)
service/   macrolog_service – Inferenzdienst (FastAPI, Docker)
deploy/    Docker Compose für den Projektserver
docs/      Architektur und API-Vertrag
```

Details: [docs/architecture.md](docs/architecture.md) · API: [docs/api/](docs/api/README.md)

## Schnellstart

### Python (core, ml, service)

Voraussetzung: [uv](https://docs.astral.sh/uv/). Python 3.12 wird automatisch installiert.

```bash
uv sync                         # alle Pakete + Dev-Tools
uv run ruff check . && uv run ruff format --check .
uv run pytest
uv run uvicorn macrolog_service.main:app --reload   # Dienst lokal auf :8000
uv run macrolog-ml --help                            # Pipeline-CLI
```

Auf Linux (CI, Docker, Projektserver) werden die CPU-Wheels von PyTorch verwendet, auf macOS die
Standard-Wheels mit MPS. In Google Colab: `pip install -e core -e ml` (nutzt das vorinstallierte
CUDA-PyTorch).

### App

Voraussetzung: Node.js 22.

```bash
cd app
npm ci
cp .env.example .env.local      # EXPO_PUBLIC_API_MOCK=1 → Beispielantwort ohne Server
npm start
npm run check                   # ESLint + tsc + Jest
```

Kamera, SQLite und Sensoren brauchen einen Development Build (`npx expo run:ios|android` oder EAS).

## Arbeitsweise

- Änderungen über Pull Requests mit Review; CI muss grün sein.
- Konfigurations-Freeze per Git-Tag `freeze-vX.Y`; erst danach wird der Testbestand ausgewertet.
- Modelle nach Semantic Versioning im Modellregister, nie überschreiben.
- Secrets nur in Umgebungsvariablen bzw. GitHub-/EAS-Secrets – nie im Repository.
- Rohdaten (Nutrition5k) liegen nie im Repository, nur Manifest, Ausschluss- und Splitlisten.

## Daten

Nutrition5k (Thames et al., 2021), CC BY 4.0 – https://github.com/google-research-datasets/Nutrition5k
