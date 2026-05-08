# Landing Page — Déploiement GitHub Pages

> URL finale visée : **https://lautre10mension.github.io** (compte dédié)
> ou : `https://<ton-pseudo-github>.github.io/lautre10mension/` si tu utilises ton compte perso

## Option A — Compte GitHub dédié (recommandé, URL propre)

1. Va sur https://github.com/signup
2. Crée un compte avec username = `lautre10mension`
   - Email : utilise un mail dédié si possible (Proton ou alias gmail+)
3. Une fois connecté, crée un repo public :
   - **Repository name** : `lautre10mension.github.io` (exactement ça, c'est magique)
   - Public ✅
   - **Add README** : non
4. En local, dans le dossier `landing/` :
   ```bash
   cd "C:/Users/rayan/BeatMarket/Lautre10Mension/landing"
   git init
   git add index.html avatar.png
   git commit -m "init landing page"
   git branch -M main
   git remote add origin https://github.com/lautre10mension/lautre10mension.github.io.git
   git push -u origin main
   ```
5. Attends 30-60 sec → la page est live sur **https://lautre10mension.github.io**

## Option B — Compte GitHub perso (URL avec sous-dossier)

1. Crée un repo public `lautre10mension` sur ton compte
2. Push le contenu du dossier `landing/` (mêmes commandes que ci-dessus, juste le remote change)
3. Va dans **Settings → Pages**
4. Source : Deploy from branch → `main` / `(root)` → Save
5. URL : `https://<ton-pseudo>.github.io/lautre10mension/`

## Après publication

- [ ] Copier l'URL finale (lautre10mension.github.io)
- [ ] Update bio **Insta** (le seul lien autorisé, c'est CRITIQUE)
- [ ] Update bio **SoundCloud** (lien externe)
- [ ] Update "À propos" **YouTube**
- [ ] Update bio **TikTok**

## Pour modifier la page plus tard

Édite `index.html` localement, puis :
```bash
cd "C:/Users/rayan/BeatMarket/Lautre10Mension/landing"
git add -A
git commit -m "update landing"
git push
```
30-60 sec plus tard la nouvelle version est live.
