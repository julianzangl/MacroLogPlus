import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

/**
 * Foto aufnehmen
 * FR-03, FR-11: overlay frame (1:1), tilt hint from 10°, gallery picker.
 */
export default function CameraScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Foto aufnehmen</Text>
      <Text>TODO</Text>
      <Link href="/capture/result" style={styles.link}>
        Weiter (Platzhalter)
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, gap: 12 },
  title: { fontSize: 22, fontWeight: '600' },
  link: { fontSize: 16, paddingVertical: 8 },
});
