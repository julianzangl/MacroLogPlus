/**
 * Display derivation (SRS 4.2.1, S-01): round only for display –
 * energy to 10 kcal, macronutrients and mass to 1 g. Confidence level as text + symbol,
 * never colour only (SRS 4.2.3).
 */
import type { ConfidenceLevel } from '../services/api/types';

export function roundEnergy(_kcal: number): number {
  // TODO: implement
  throw new Error('not implemented');
}

export function roundGrams(_g: number): number {
  // TODO: implement
  throw new Error('not implemented');
}

export interface ConfidenceDisplay {
  label: string;
  symbol: string;
  accessibilityLabel: string;
}

export function confidenceDisplay(_level: ConfidenceLevel): ConfidenceDisplay {
  // TODO: implement (FR-08)
  throw new Error('not implemented');
}
