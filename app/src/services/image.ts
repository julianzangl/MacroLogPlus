/**
 * Image preparation before upload (HLD 4.2 step 2, S-04).
 * Resize to max. 1280 px edge length and re-encode as JPEG via expo-image-manipulator,
 * which drops all metadata incl. EXIF/location. The actual model preprocessing
 * (crop, 224 px, normalisation) happens only on the server in macrolog_core.
 */
export const MAX_EDGE_PX = 1280;
export const JPEG_QUALITY = 0.85;

export async function prepareForUpload(_uri: string): Promise<string> {
  // TODO: implement (FR-11)
  throw new Error('not implemented');
}
