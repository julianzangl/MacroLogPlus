import { StyleSheet, Text, View } from 'react-native';

/**
 * Über die KI-Schätzung
 * SRS 4.2.6: purpose, limits, capture tips, data basis, model version, average error (GET /v1/model).
 */
export default function AboutAiScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Über die KI-Schätzung</Text>
      <Text>TODO</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
});
