import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'be.gauthierdoumont.duocompta',
  appName: 'DuoCompta',
  webDir: 'www',
  android: {
    allowMixedContent: true,
    webContentsDebuggingEnabled: false,
    backgroundColor: '#0e0f14'
  },
  server: {
    // Utilise les fichiers locaux (pas de serveur distant)
    // Pour activer le rechargement live en dev : hostname: 'localhost'
    androidScheme: 'https'
  },
  plugins: {
    // Preferences remplace localStorage pour le stockage natif Android
    // (compatible avec le DB.get/set/del de DuoCompta)
    Preferences: {
      group: 'DuoComptaStorage'
    }
  }
};

export default config;
