import { StyleSheet, Text, View } from 'react-native';

/**
 * Ergebnis prüfen
 * M-04, FR-04, FR-08–FR-10: value, range as number + band, explanation, confidence, portion correction, accept (FR-06).
 */
export default function ResultScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Ergebnis prüfen</Text>
      <Text>TODO</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
});
