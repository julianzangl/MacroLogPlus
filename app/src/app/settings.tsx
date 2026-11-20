import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

/**
 * Einstellungen
 * FR-07: consent, delete all local data.
 */
export default function SettingsScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Einstellungen</Text>
      <Text>TODO</Text>
      <Link href="/about-ai" style={styles.link}>
        Über die KI-Schätzung
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
  link: { fontSize: 16, paddingVertical: 8 },
});
