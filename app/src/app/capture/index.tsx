import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

/**
 * Erfassen
 * Choose: photo, own dish, manual (SRS 4.2.5).
 */
export default function CaptureScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Erfassen</Text>
      <Text>TODO</Text>
      <Link href="/capture/camera" style={styles.link}>
        Foto aufnehmen
      </Link>
      <Link href="/capture/manual" style={styles.link}>
        Manuell erfassen
      </Link>
      <Link href="/dishes" style={styles.link}>
        Eigenes Gericht
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
  link: { fontSize: 16, paddingVertical: 8 },
});
