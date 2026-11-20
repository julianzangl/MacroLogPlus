import { Stack } from 'expo-router';

export default function RootLayout() {
  // TODO: run DB migrations before rendering, consent gate before first photo estimate (FR-07)
  return (
    <Stack>
      <Stack.Screen name="index" options={{ title: 'Heute' }} />
      <Stack.Screen name="capture/index" options={{ title: 'Erfassen' }} />
      <Stack.Screen name="capture/manual" options={{ title: 'Manuell erfassen' }} />
      <Stack.Screen name="capture/camera" options={{ title: 'Foto aufnehmen', headerShown: false }} />
      <Stack.Screen name="capture/result" options={{ title: 'Ergebnis prüfen' }} />
      <Stack.Screen name="dishes/index" options={{ title: 'Meine Gerichte' }} />
      <Stack.Screen name="about-ai" options={{ title: 'Über die KI-Schätzung' }} />
      <Stack.Screen name="settings" options={{ title: 'Einstellungen' }} />
    </Stack>
  );
}
