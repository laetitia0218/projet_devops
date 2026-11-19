# Configuration GitHub du Dépôt

Ce dossier contient les éléments de configuration GitHub traduisant les règles de gestion définies dans le [`CONTRIBUTING.md`](../../CONTRIBUTING.md).

---

## 1. Protection de la branche `main` (Settings > Branches)

Pour empêcher les pushs directs et forcer les tests et la relecture (**R2**, **R3**) :

* **Branch name pattern :** `main`
* **Options à activer :**
  1. `Require a pull request before merging`
     * `Require approvals : 1` (traite **R1** et **R2**)
     * `Dismiss stale pull request approvals when new commits are pushed` (optionnel mais conseillé)
  2. `Require status checks to pass before merging`
     * `Require branches to be up to date before merging`
     * Sélectionner le check de tests CI (dès qu'il sera configuré en T5) (traite **R3**)
  3. `Do not allow bypassing the above settings` (s'applique à tout le monde, même aux administrateurs)
  4. `Require conversation resolution before merging` (permet de s'assurer que tous les retours de revue sont traités)

*(Déposer la capture d'écran ici : `docs/config/branch-protection.png`)*

---

## 2. Environnements et Secrets (Settings > Environments & Secrets)

Pour protéger les accès et séparer le développement de la production (**R4**) :

* **Environnement `production` :**
  * `Deployment branches` : restreindre aux tags `v*` ou à la branche `main`.
  * `Required reviewers` : activer la validation manuelle avant déploiement (1 approbateur permanent requis).
* **Secrets de dépôt / d'environnement :**
  * Définir les secrets nécessaires pour le déploiement (tokens GHCR, variables de production).
  * Les secrets ne sont visibles par aucun membre non-administrateur.

*(Déposer la capture d'écran ici : `docs/config/environment-protection.png`)*

---

## 3. Gestion des collaborateurs (Settings > Collaborators)

Pour encadrer le freelance et les alternants (**R1**, **R2**, **R4**) :

* **Développeurs permanents / Lead dev :** rôle `Admin` ou `Maintain` (accès aux secrets et configuration).
* **Alternants :** rôle `Write` (création de branches, ouverture de PRs, pas d'accès direct aux secrets de prod).
* **Freelance :** rôle `Triage` ou `Write` restreint (interdiction de bypasser les règles, pas d'accès aux secrets).

*(Déposer la capture d'écran ici : `docs/config/collaborators-roles.png`)*
