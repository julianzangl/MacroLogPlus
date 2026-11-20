/** Domain types of the app (HLD 4.3). Pure TypeScript – no UI, no network, no storage. */

export type MealCategory = 'breakfast' | 'lunch' | 'dinner' | 'snack';

export interface Nutrients {
  energyKcal: number;
  fatG: number;
  carbsG: number;
  proteinG: number;
}

export type EntrySource = 'manual' | 'dish' | 'ai_estimate';

export interface DiaryEntry extends Nutrients {
  id: number;
  name: string;
  eatenAt: string; // ISO 8601
  meal: MealCategory;
  source: EntrySource;
  dishId?: number;
  estimateId?: number;
}

export type DishBasis = 'per_portion' | 'per_100g';

export interface Dish extends Nutrients {
  id: number;
  name: string;
  basis: DishBasis;
  favorite: boolean;
  lastUsedAt?: string;
}
