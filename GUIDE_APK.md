# DuoCompta — Guide de compilation APK
## Par Gauthier Doumont

---

## CE QU'IL TE FAUT SUR TON PC (Windows/Mac/Linux)

| Outil | Lien | Pourquoi |
|-------|------|----------|
| Node.js 18+ | https://nodejs.org | Pour Capacitor |
| Android Studio | https://developer.android.com/studio | Pour compiler l'APK |
| JDK 17+ | Inclus avec Android Studio | Java |

---

## ETAPE 1 — Installer Android Studio

1. Télécharge Android Studio sur https://developer.android.com/studio
2. Lance l'installeur, accepte tout par défaut
3. Au premier lancement, laisse-le télécharger le SDK Android (ça prend 10-20 min)
4. Dans Android Studio → SDK Manager → vérifie que **Android 14 (API 34)** est coché

---

## ETAPE 2 — Préparer le projet Capacitor

Ouvre un terminal (PowerShell sur Windows, Terminal sur Mac) et tape :

```bash
# Va dans le dossier du projet (là où tu as décompressé le zip)
cd duocompta-apk

# Installe les dépendances
npm install

# Initialise Capacitor (si premier lancement)
npx cap init DuoCompta be.gauthierdoumont.duocompta --web-dir www

# Ajoute la plateforme Android
npx cap add android

# Synchronise les fichiers web vers Android
npx cap sync android
```

---

## ETAPE 3 — Configurer Android (sécurité réseau)

Après `npx cap add android`, copie le fichier `network_security_config.xml` vers :
```
android/app/src/main/res/xml/network_security_config.xml
```
(Crée le dossier `xml` s'il n'existe pas)

Puis ouvre `android/app/src/main/AndroidManifest.xml` et ajoute dans la balise `<application>` :
```xml
android:networkSecurityConfig="@xml/network_security_config"
android:usesCleartextTraffic="false"
```

---

## ETAPE 4 — Compiler l'APK

### Option A — Via Android Studio (recommandé)
```bash
npx cap open android
```
Android Studio s'ouvre. Attends que Gradle se synchronise, puis :
- **Build** → **Build Bundle(s) / APK(s)** → **Build APK(s)**
- L'APK sera dans `android/app/build/outputs/apk/debug/app-debug.apk`

### Option B — Via ligne de commande
```bash
cd android
./gradlew assembleDebug
# L'APK est dans android/app/build/outputs/apk/debug/
```

---

## ETAPE 5 — Installer sur ta tablette

### Méthode 1 — Via câble USB (la plus simple)
1. Sur ta tablette Android : **Paramètres** → **À propos de la tablette** → appuie 7 fois sur **Numéro de build** → le mode développeur s'active
2. **Paramètres** → **Options développeur** → active **Débogage USB**
3. Branche la tablette au PC avec un câble USB
4. Dans Android Studio : en haut, sélectionne ta tablette dans la liste des appareils
5. Clique le bouton **▶ Run** — l'appli s'installe automatiquement

### Méthode 2 — Via fichier APK (sans Android Studio)
1. Copie `app-debug.apk` sur ta tablette (clé USB, email, Google Drive...)
2. Sur la tablette : **Paramètres** → **Sécurité** → active **Sources inconnues** (ou "Installer des applis inconnues")
3. Ouvre le fichier APK avec le gestionnaire de fichiers → Installer

---

## ETAPE 6 — Vérifier que tout fonctionne

Lance DuoCompta sur ta tablette :
- Connecte-toi avec ta clé Groq
- Crée un dossier, importe un PDF
- Lance les flashcards

Si l'IA ne répond pas, vérifie que la tablette a du wifi.

---

## METTRE A JOUR L'APK PLUS TARD

Quand tu modifies index.html :
```bash
# Copier le nouvel index.html dans www/
cp nouveau_index.html www/index.html

# Resynchroniser
npx cap sync android

# Recompiler
cd android && ./gradlew assembleDebug
```

---

## SI CA NE MARCHE PAS

### Erreur "JAVA_HOME not set"
Ajoute Java au PATH. Sous Windows :
- Panneau de configuration → Système → Variables d'environnement
- Ajoute `JAVA_HOME` = chemin vers ton JDK (ex: `C:\Program Files\Android\Android Studio\jbr`)

### Erreur "SDK not found"
Dans Android Studio → SDK Manager → copie le chemin du SDK
Ajoute `local.properties` dans le dossier `android/` :
```
sdk.dir=/chemin/vers/android/sdk
```

### L'appli plante au lancement
Ouvre Android Studio → **Logcat** → filtre par "DuoCompta" pour voir l'erreur

---

## STRUCTURE DES FICHIERS

```
duocompta-apk/
├── www/                    ← Tes fichiers web
│   ├── index.html          ← L'application complète
│   ├── manifest.json       ← Config PWA
│   └── sw.js               ← Service worker
├── package.json            ← Dépendances Node
├── capacitor.config.ts     ← Config Capacitor
├── network_security_config.xml ← Config réseau Android
└── GUIDE_APK.md            ← Ce fichier
```

---

## POUR ALLER PLUS LOIN (optionnel)

### Icône personnalisée
Remplace les fichiers dans `android/app/src/main/res/mipmap-*/`
Utilise https://easyappicon.com pour générer toutes les tailles

### Splash screen
```bash
npm install @capacitor/splash-screen
npx cap sync android
```

### Publier sur le Play Store
1. **Build** → **Generate Signed Bundle/APK** → **APK**
2. Crée une clé de signature (garde-la précieusement !)
3. Va sur https://play.google.com/console
4. Crée une nouvelle application → upload l'APK signé

---

*DuoCompta — Développé par Gauthier Doumont*
*Guide rédigé avec Claude — Anthropic*
