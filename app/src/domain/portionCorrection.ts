/**
 * Portion correction with a known mass (S-02, FR-09, HLD 3.8 step 4).
 * total = mass × per_gram, range = total × known_mass_factors (computed locally, no second request).
 * TS-04: 300 g × 2.0 kcal/g = 600 kcal, range ≈ 520–700 kcal (narrower than without known mass).
 */
import type { EstimateResponse, Interval, TotalTarget } from '../services/api/types';

export function correctForKnownMass(
  _estimate: EstimateResponse,
  _massG: number,
): Record<TotalTarget, Interval> {
  // TODO: implement (FR-09, TS-04)
  throw new Error('not implemented');
}
