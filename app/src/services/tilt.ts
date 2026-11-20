/**
 * Tilt measurement for the capture aid (FR-03, S-04): show a hint as soon as the
 * phone deviates more than 10° from horizontal (top-down shot). Uses expo-sensors.
 */
export const TILT_WARNING_DEG = 10;

/** Angle between device z-axis and gravity in degrees (0 = flat, camera facing down). */
export function tiltFromAcceleration(_x: number, _y: number, _z: number): number {
  // TODO: implement
  throw new Error('not implemented');
}
