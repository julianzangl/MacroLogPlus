/**
 * Local SQLite database (expo-sqlite), offline-first (M-09, HLD 4.3).
 *
 * Four tables (HLD Abb. 6):
 *  - entries    diary entries with final values; optional FK to dishes or estimates
 *  - dishes     own dishes (per portion / per 100 g), favourite flag, last used
 *  - estimates  original AI estimate (unchanged!), model version, request_id, corrected mass
 *  - settings   key/value (consent given, API config, display variant, …)
 *
 * Daily totals are computed on demand and never stored.
 */
export const DATABASE_NAME = 'macrolog.db';

export async function migrate(): Promise<void> {
  // TODO: implement schema + versioned migrations (PRAGMA user_version)
  throw new Error('not implemented');
}

/** "Alle lokalen Daten löschen" (FR-07). */
export async function deleteAllLocalData(): Promise<void> {
  // TODO: implement
  throw new Error('not implemented');
}
