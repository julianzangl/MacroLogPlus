import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

/**
 * Tagesübersicht
 * M-05, FR-05: daily totals, entries by meal, AI entries marked. Quick capture (S-05).
 */
export default function DailyOverviewScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Tagesübersicht</Text>
      <Text>TODO</Text>
      <Link href="/capture" style={styles.link}>
        Erfassen
      </Link>
      <Link href="/dishes" style={styles.link}>
        Meine Gerichte
      </Link>
      <Link href="/settings" style={styles.link}>
        Einstellungen
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
  link: { fontSize: 16, paddingVertical: 8 },
});
