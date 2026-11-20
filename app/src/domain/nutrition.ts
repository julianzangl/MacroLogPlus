/**
 * Nutrition calculations (M-02, M-05, HLD 2.2 "Anwendungslogik").
 * Test cases: TS-01 (daily sum), TS-02 (portion factor 1.5 × 400 kcal = 600 kcal).
 */
import type { DiaryEntry, Dish, Nutrients } from './types';

/** Nutrients of a dish logged with a portion factor (basis per_portion). */
export function scaleByPortion(_dish: Dish, _factor: number): Nutrients {
  // TODO: implement (FR-02, TS-02)
  throw new Error('not implemented');
}

/** Nutrients of a dish logged with a gram amount (basis per_100g). */
export function scaleByGrams(_dish: Dish, _grams: number): Nutrients {
  // TODO: implement (FR-02)
  throw new Error('not implemented');
}

/** Daily totals – computed on demand, never stored (HLD 4.3). */
export function dailyTotals(_entries: DiaryEntry[]): Nutrients {
  // TODO: implement (FR-05, TS-01)
  throw new Error('not implemented');
}
