import { StyleSheet, Text, View } from 'react-native';

/**
 * Manuell erfassen
 * M-01, FR-01: name, kcal, fat, carbs, protein, date, time, meal.
 */
export default function ManualEntryScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Manuell erfassen</Text>
      <Text>TODO</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
});
