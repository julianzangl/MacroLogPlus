/**
 * API contract v1 (ADR 0001) – friendly aliases over the generated OpenAPI types.
 *
 * Never define API shapes by hand. To change the contract: edit
 * service/src/macrolog_service/schemas.py, run
 * `uv run python -m macrolog_service.openapi_export` and then `npm run gen:api`.
 *
 * Rules: the server only sends codes (confidence, warnings, problems) – all user-facing
 * German texts live in the app. Ignore unknown fields and warning codes (tolerant reader).
 */
import type { components } from './schema.gen';

type Schemas = components['schemas'];

export type EstimateResponse = Schemas['EstimateResponse'];
export type HealthResponse = Schemas['HealthResponse'];
export type ModelInfoResponse = Schemas['ModelInfoResponse'];
export type Problem = Schemas['Problem'];
export type ProblemCode = Problem['code'];

export type Interval = Schemas['Interval'];
export type FactorRange = Schemas['FactorRange'];
export type Variant = Schemas['ModelRef']['variant'];
export type ConfidenceLevel = EstimateResponse['confidence_level'];
export type WarningCode = EstimateResponse['warnings'][number];

export type Target = keyof Schemas['Estimate'];
export type TotalTarget = keyof Schemas['PerGram'];

export const API_KEY_HEADER = 'X-API-Key';
export const REQUEST_ID_HEADER = 'X-Request-ID';
export const PROBLEM_MEDIA_TYPE = 'application/problem+json';
