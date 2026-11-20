import { StyleSheet, Text, View } from 'react-native';

/**
 * Meine Gerichte
 * M-02, FR-02, FR-12: list, create/edit/delete, favourites, recently used.
 */
export default function DishesScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Meine Gerichte</Text>
      <Text>TODO</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
});
