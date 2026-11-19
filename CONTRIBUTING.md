# Guide de contribution (CONTRIBUTING.md)

Bienvenue sur le projet ! Ce document définit nos règles de travail communes.
Dans notre équipe (2 développeurs permanents, 2 alternants présents 2 semaines sur 4, et un développeur freelance ponctuel), ces règles nous permettent de livrer rapidement sans revivre l'incident d'août (14h de panne un vendredi soir).

Chaque règle est directement liée aux risques identifiés dans notre analyse [`docs/risques.md`](docs/risques.md).

---

## 1. Relecture de code (Code Review)

* **Règle :** **1 seule approbation obligatoire** par Pull Request pour pouvoir fusionner sur `main`.
* **Justification :** Nous sommes 4 dans l'équipe, mais les 2 alternants sont absents 2 semaines sur 4 en formation (**R1**). Exiger 2 relecteurs bloquerait le travail quand seuls les 2 permanents sont là. 1 relecteur suffit pour détecter les erreurs sans ralentir (**R2**).
* **Qui relit qui ?**
  * Un alternant est relu par un permanent (effet formateur).
  * Les 2 permanents se relisent mutuellement quand les alternants sont en cours (**R1**).
  * Les contributions du freelance sont relues par la lead dev ou un permanent (**R2**).
* **Que faire si le seul relecteur compétent est absent ?**
  * **Cas normal :** La PR est réattribuée au permanent disponible. On privilégie une courte session de relecture à deux (binômage) si le sujet est pointu. On n'attend pas passivement (**R1**, **R2**).
  * **Règle absolue :** On ne contourne **JAMAIS** l'obligation de relecture sur `main` (**R2**).
  * **En cas d'urgence en production (incident) :** On ne pousse pas un correctif à l'aveugle. On applique d'abord la procédure de **retour arrière (rollback en < 5 minutes)** pour restaurer le service (**R5**). Ensuite, le correctif est rédigé et relu dès qu'un permanent est joignable.

---

## 2. Nommage des branches et messages de commit

### A. Branches
Toute modification se fait sur une branche dédiée créée depuis `main` à jour.

Format : `<type>/<description-courte>`

* `feat/nom-fonctionnalite` : nouvelle fonctionnalité (ex: `feat/gestion-stock`, `feat/route-produits`)
* `fix/description-bug` : correction d'un bug (ex: `fix/calcul-total`)
* `hotfix/nom-urgence` : correctif critique en production (ex: `hotfix/blocage-commandes`)
* `docs/sujet` : documentation (ex: `docs/t3-regles-gestion`)
* `test/sujet` : ajout ou mise à jour de tests
* `ci/sujet` : modification des pipelines GitHub Actions

* **Justification :** Permet à tout le monde (notamment aux alternants après 2 semaines d'absence ou au trinôme voisin qui relit nos PRs) de comprendre immédiatement la nature de la tâche (**R1**, **R2**).

### B. Messages de commit
Nous utilisons une convention simple et lisible (inspirée de Conventional Commits) :

Format : `<type>: <description courte au présent>`

* `feat: ajout de la route POST /orders`
* `fix: empeche la commande si stock insuffisant`
* `docs: mise a jour du CONTRIBUTING`
* `test: ajout test unitaire sur la route health`
* `ci: configuration du job de test`

* **Justification :** L'historique Git reste clair et permet de retrouver facilement quel commit a introduit un changement (**R5**).
* **Fusion sur `main` :** On utilise le mode **Squash and merge** sur GitHub. Cela rassemble tous les commits intermédiaires d'une PR en un seul commit propre sur `main`.

---

## 3. Definition of Done (DoD)

Une tâche ou une User Story est considérée comme **« Terminée » (Done)** uniquement si :

1. [ ] **Code fonctionnel :** Le code répond aux critères de la User Story, sans code mort ou inutile.
2. [ ] **Tests automatiques :** Au moins un test automatisé valide la fonctionnalité ou la correction (**R3**).
3. [ ] **Pipeline CI au vert :** Le pipeline GitHub Actions passe avec succès (tests + build Docker valides) (**R3**).
4. [ ] **Relecture approuvée :** La PR a reçu au moins **1 approbation** d'un collègue (**R2**).
5. [ ] **Sécurité vérifiée :** Aucun mot de passe, clé d'API ou secret n'est présent dans le code ou l'historique (**R4**).
6. [ ] **Documentation à jour :** Si l'API ou le comportement change, la documentation est ajustée.
7. [ ] **Fusion et nettoyage :** La PR est fusionnée sur `main` via *Squash and merge* et la branche de travail est supprimée.

> **Cas particulier des alternants :** Si une tâche n'est pas finie avant le départ en formation de 2 semaines, l'alternant doit ouvrir une **Draft PR** et rédiger une courte note de passation (ce qui est fait, ce qui reste à faire, comment tester) (**R1**).

---

## 4. Versionnage et visibilité en production (Règle des 10 secondes)

Pour éviter l'incident d'août où personne ne savait quelle version tournait en production (**R5**) :

* **Numérotation sémantique :** Chaque livraison officielle est étiquetée par un tag Git au format `vX.Y.Z` (ex: `v1.0.0`, `v1.0.1`).
* **Images Docker :** L'image Docker construite porte le tag de version exact (ex: `ghcr.io/organisation/api:v1.0.0`) ainsi que le hash du commit. On bannit l'utilisation du tag `latest` seul (**R5**).
* **Le test des 10 secondes :**
  L'API expose obligatoirement une route publique `GET /health`.
  Une simple requête permet de savoir immédiatement quelle version tourne :

  ```bash
  curl http://localhost:8000/health
  ```

  Réponse JSON attendue en moins de 10 secondes :
  ```json
  {
    "status": "ok",
    "version": "v1.0.0",
    "commit": "3852322",
    "database": "connected"
  }
  ```

---

## 5. Gestion des secrets

* **Où vivent les secrets ?**
  * **En local (développement) :** Dans un fichier `.env` non versionné, strictement ignoré par le `.gitignore`. Un fichier `.env.example` sans aucun secret réel est versionné pour guider l'installation (**R4**).
  * **Dans le pipeline CI/CD :** Dans les **GitHub Actions Secrets** (chiffrés et masqués dans les logs) (**R4**).
  * **En production :** Définis comme variables d'environnement sur le serveur de déploiement.
* **Qui y a accès ?**
  * Seuls les 2 développeurs permanents (administrateurs du dépôt) ont accès aux secrets de production (**R4**). Les alternants et le freelance travaillent avec des mocks ou des bases locales jetables.
* **Que fait-on si un secret fuite (ex: commité par erreur) ?**
  1. **Révocation immédiate (Priorité 1) :** On change immédiatement le mot de passe, le token ou la clé sur le service externe (PostgreSQL, hébergeur...). *Règle : Supprimer le commit ne rend pas un secret révoqué sûr* (**R4**).
  2. **Audit :** Vérifier les logs pour s'assurer qu'aucune action malveillante n'a eu lieu pendant l'exposition.
  3. **Mise à jour :** Renseigner le nouveau secret dans GitHub Secrets et sur le serveur de production.
  4. **Nettoyage Git :** Retirer le fichier de l'historique Git si nécessaire.
  5. **Traçabilité :** Rédiger un compte-rendu dans `docs/incidents.md`.

---

## 6. Cas du développeur freelance

* **Rappel :** Le freelance a déclaré : *« Je suis payé à l'heure, je n'ai pas le temps d'attendre qu'on me relise. »*
* **Notre décision :**
  * **Aucune exception aux règles de sécurité et de qualité :** Le freelance ne pousse **JAMAIS** directement sur `main` et n'a aucun droit d'administration sur le dépôt (**R2**, **R4**).
  * **Pour ne pas le bloquer dans sa facturation :**
    1. **Découpage fin :** Le freelance travaille sur des tâches courtes et indépendantes.
    2. **Travail en parallèle :** Dès qu'il ouvre une PR pour une tâche finie, il bascule sur une nouvelle branche et continue sa mission sans attendre que la première PR soit fusionnée.
    3. **Engagement de l'équipe :** Les développeurs permanents s'engagent à relire ses PRs sous un délai rapide (**objectif : moins de 4 heures ouvrées**) (**R2**).
    4. **Sécurité :** Le freelance n'a pas accès aux secrets de production (**R4**).

---

## 7. Récapitulatif : Imposé par GitHub vs Discipline de l'équipe

Pour l'oral et pour la clarté du TP, nous distinguons ce que l'outil technique bloque automatiquement de ce qui dépend de notre sérieux au quotidien :

| Règle | Imposé par GitHub (technique) | Discipline de l'équipe (humain) | Risque traité |
|---|:---:|:---:|---|
| **Interdiction de push direct sur `main`** | ✅ Branch protection | — | **R2** |
| **Au moins 1 approbation avant merge** | ✅ Require a pull request before merging (1 approval) | — | **R1, R2** |
| **Succès obligatoire des tests CI** | ✅ Require status checks to pass before merging | — | **R3** |
| **Respect du format des branches et commits** | ❌ (possible via bot lourd, mais trop complexe pour un TP) | ✅ Discipline lors de l'ouverture de la PR | **R1, R5** |
| **Objectif de relecture sous 4 heures** | ❌ GitHub ne peut pas forcer un humain à relire vite | ✅ Organisation interne de l'équipe | **R2** |
| **Interdiction de déployer le vendredi à 19h** | ❌ | ✅ Accord d'équipe (gel des mises en prod le vendredi après-midi) | **R3** |
| **Passation écrite avant le départ en formation** | ❌ | ✅ Remplissage obligatoire de la Draft PR par l'alternant | **R1** |
| **Pas de secrets commités dans le code** | ⚠️ GitHub Secret Scanning (alerte mais n'empêche pas toujours) | ✅ Vigilance, `.gitignore` et `.env.example` | **R4** |
| **Procédure de révocation en cas de fuite** | ❌ | ✅ Procédure d'urgence de l'équipe | **R4** |
