# Deployment (Projektserver)

Mini-PC Intel N100, 16 GB RAM, 1 TB SSD, Ubuntu Server, Docker Compose (HLD 1.3, 2.7).

- `docker-compose.yml` – Inferenzdienst (+ später Tunnel, optional Kontodienst)
- `.env.example` – Vorlage für `deploy/.env` (nie committen)
- Modellregister: `/srv/macrolog/registry/<semver>/` (read-only in den Container gemountet)
- Protokolle: `/srv/macrolog/logs` (tägliche Rotation, Löschung nach 90 Tagen)

Härtung laut HLD 7: SSH nur mit Schlüssel, Firewall ohne offene Eingangsports,
unattended-upgrades, Container als Nicht-Root mit read-only Dateisystem und Ressourcenlimits.
