/** Input validation (M-01, SRS 4.2.4): nutrients numeric and ≥ 0, mass > 0 g. */

export type ValidationResult = { ok: true; value: number } | { ok: false; message: string };

export function parseNutrientValue(_input: string): ValidationResult {
  // TODO: implement – accept German decimal comma ("12,5")
  throw new Error('not implemented');
}

export function parseMass(_input: string): ValidationResult {
  // TODO: implement
  throw new Error('not implemented');
}
