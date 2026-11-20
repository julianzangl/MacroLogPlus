/**
 * HTTP client for the inference service (HLD 4.2 steps 3 + 7, HLD 5.3, ADR 0001).
 *
 * - POST /v1/estimate with the raw JPEG body (not multipart), header X-API-Key
 * - timeout 15 s, then a user-facing error with a one-tap switch to manual entry (TS-05)
 * - errors arrive as RFC 9457 problem details (application/problem+json); branch on `code`,
 *   never show `detail`. Unknown codes → treat like 'internal_error' (tolerant reader).
 * - 429/503 carry Retry-After (seconds); every response carries X-Request-ID
 */
import type {
  EstimateResponse,
  HealthResponse,
  ModelInfoResponse,
  ProblemCode,
} from './types';

export const REQUEST_TIMEOUT_MS = 15_000;

/** Client-side failures plus the server's problem codes. German texts are mapped in the UI. */
export type EstimateErrorKind = 'offline' | 'timeout' | 'invalid_response' | ProblemCode;

export class EstimateError extends Error {
  constructor(
    public readonly kind: EstimateErrorKind,
    public readonly status?: number,
    public readonly requestId?: string,
    public readonly retryAfterS?: number,
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
  throw new EstimateError('internal_error');
}

export async function health(_config = apiConfigFromEnv()): Promise<HealthResponse> {
  // TODO: implement GET /v1/health
  throw new EstimateError('internal_error');
}

export async function modelInfo(_config = apiConfigFromEnv()): Promise<ModelInfoResponse> {
  // TODO: implement GET /v1/model (used by the "Über die KI-Schätzung" page)
  throw new EstimateError('internal_error');
}
