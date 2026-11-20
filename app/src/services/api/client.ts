/**
 * HTTP client for the inference service (HLD 4.2 steps 3 + 7, HLD 5.3).
 *
 * - POST /v1/estimate with the raw JPEG body (not multipart), header X-API-Key
 * - timeout 15 s, then a user-facing error with a one-tap switch to manual entry (TS-05)
 * - maps HTTP status codes (400/401/413/415/429/503) to German messages
 */
import type { EstimateResponse, HealthResponse, ModelInfoResponse } from './types';

export const REQUEST_TIMEOUT_MS = 15_000;

export type EstimateErrorKind =
  | 'offline'
  | 'timeout'
  | 'bad_image'
  | 'unauthorized'
  | 'too_large'
  | 'rate_limited'
  | 'unavailable'
  | 'unknown';

export class EstimateError extends Error {
  constructor(
    public readonly kind: EstimateErrorKind,
    public readonly status?: number,
  ) {
    super(kind);
  }
}

export interface ApiConfig {
  baseUrl: string;
  apiKey: string;
  mock: boolean;
}

export function apiConfigFromEnv(): ApiConfig {
  return {
    baseUrl: process.env.EXPO_PUBLIC_API_BASE_URL ?? '',
    apiKey: process.env.EXPO_PUBLIC_API_KEY ?? '',
    mock: process.env.EXPO_PUBLIC_API_MOCK === '1',
  };
}

export async function estimate(_jpegUri: string, _config = apiConfigFromEnv()): Promise<EstimateResponse> {
  // TODO: implement (FR-03, TS-05) – mock mode returns MOCK_ESTIMATE
  throw new EstimateError('unknown');
}

export async function health(_config = apiConfigFromEnv()): Promise<HealthResponse> {
  // TODO: implement GET /v1/health
  throw new EstimateError('unknown');
}

export async function modelInfo(_config = apiConfigFromEnv()): Promise<ModelInfoResponse> {
  // TODO: implement GET /v1/model (used by the "Über die KI-Schätzung" page)
  throw new EstimateError('unknown');
}
