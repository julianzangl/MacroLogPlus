/**
 * Design tokens from the Figma prototype. Text/controls need a contrast ratio
 * of at least 4.5:1 (WCAG 2.1, SRS 4.2.3).
 */
export const colors = {
  background: '#FFFFFF',
  text: '#111111',
  primary: '#1B5E20',
  // TODO: take over palette from Figma
} as const;

export const spacing = { xs: 4, sm: 8, md: 16, lg: 24, xl: 32 } as const;
