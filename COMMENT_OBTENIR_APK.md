# Comment obtenir ton APK DuoCompta

## ETAPE 1 — Mettre les fichiers sur GitHub

Tu as déjà un repo GitHub (Duocompta). Il faut y ajouter ces nouveaux fichiers :

```
.github/
  workflows/
    build-apk.yml        ← Le fichier magique qui compile l'APK
www/
  index.html             ← Ton application
  manifest.json
  sw.js
package.json
capacitor.config.ts
network_security_config.xml
.gitignore
```

**Comment uploader :**
1. Va sur github.com/gauthierdoumont/Duocompta
2. Clique "Add file" → "Upload files"
3. Glisse TOUS ces fichiers (en respectant les dossiers)
4. Clique "Commit changes"

---

## ETAPE 2 — GitHub compile automatiquement

Dès que tu ajoutes le fichier `.github/workflows/build-apk.yml`, GitHub lance la compilation.

Va dans l'onglet **Actions** de ton repo :
- Tu verras "Build DuoCompta APK" en cours (cercle jaune ⏳)
- Ça prend environ **5-10 minutes**
- Quand c'est vert ✅ → l'APK est prêt

---

## ETAPE 3 — Télécharger l'APK

1. Clique sur le workflow vert ✅ "Build DuoCompta APK"
2. En bas de la page → section **Artifacts**
3. Clique **DuoCompta-APK** → téléchargement d'un ZIP
4. Décompresse le ZIP → tu as **app-debug.apk**

---

## ETAPE 4 — Installer sur ta tablette

### Option A — Via câble USB + Android Studio (si tu l'as)
- Branche ta tablette, active le débogage USB
- Glisse l'APK sur la tablette via le câble

### Option B — Via le cloud (sans câble, le plus simple)
1. Envoie `app-debug.apk` sur ton Google Drive ou par email à toi-même
2. Sur ta tablette, ouvre le fichier APK
3. Si Android demande : **Paramètres** → **Sécurité** → active **"Sources inconnues"** ou **"Installer des applications inconnues"**
4. Confirme l'installation → DuoCompta apparaît sur ton écran d'accueil !

---

## Mettre à jour l'APK

À chaque fois que tu modifies index.html et que tu le pousses sur GitHub :
→ GitHub recompile automatiquement un nouvel APK
→ Tu le télécharges et réinstalles sur la tablette

---

## Si le workflow échoue (croix rouge ✗)

1. Clique sur le workflow rouge
2. Clique sur "build" pour voir les logs
3. Copie le message d'erreur et envoie-le moi, je règle ça

---

*DuoCompta — Gauthier Doumont*
