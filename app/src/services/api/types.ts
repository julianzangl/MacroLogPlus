/**
 * API contract of the inference service (HLD 5.2, SRS 2.3.5).
 * Must stay in sync with service/src/macrolog_service/schemas.py and
 * docs/api/estimate-response.example.json.
 */

export type Variant = 'A' | 'B' | 'C';
export type ConfidenceLevel = 'hoch' | 'mittel' | 'niedrig';

export type TotalTarget = 'energy_kcal' | 'fat_g' | 'carbs_g' | 'protein_g';
export type Target = TotalTarget | 'mass_g';

export interface Interval {
  value: number;
  lower: number;
  upper: number;
}

export interface FactorRange {
  lower: number;
  upper: number;
}

export type EstimateWarning = 'unusual_image' | 'too_dark' | 'blurry' | 'implausible_values';

export interface EstimateResponse {
  request_id: string;
  model: { version: string; variant: Variant };
  coverage: number;
  estimate: Record<Target, Interval>;
  per_gram: Record<TotalTarget, number>;
  known_mass_factors: Record<TotalTarget, FactorRange>;
  confidence_level: ConfidenceLevel;
  warnings: EstimateWarning[];
}

export interface HealthResponse {
  status: 'ok' | 'loading';
  model_version: string | null;
}

export interface ModelInfoResponse {
  version: string;
  variant: Variant;
  trained_at: string;
  validation_mae: Record<Target, number>;
  coverage: number;
  model_card_summary: string;
}

export interface ErrorResponse {
  error: { code: number; message: string; request_id: string };
}
