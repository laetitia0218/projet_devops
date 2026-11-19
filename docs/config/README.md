# Configuration GitHub du DÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t

Ce dossier contient les ÃƒÆ’Ã‚Â©lÃƒÆ’Ã‚Â©ments de configuration GitHub traduisant les rÃƒÆ’Ã‚Â¨gles de gestion dÃƒÆ’Ã‚Â©finies dans le [`CONTRIBUTING.md`](../../CONTRIBUTING.md).

---

## 1. Protection de la branche `main` (Settings > Branches)

Pour empÃƒÆ’Ã‚Âªcher les pushs directs et forcer les tests et la relecture (**R2**, **R3**) :

* **Branch name pattern :** `main`
* **Options ÃƒÆ’Ã‚Â  activer :**
  1. `Require a pull request before merging`
     * `Require approvals : 1` (traite **R1** et **R2**)
     * `Dismiss stale pull request approvals when new commits are pushed` (optionnel mais conseillÃƒÆ’Ã‚Â©)
  2. `Require status checks to pass before merging`
     * `Require branches to be up to date before merging`
     * SÃƒÆ’Ã‚Â©lectionner le check de tests CI (dÃƒÆ’Ã‚Â¨s qu'il sera configurÃƒÆ’Ã‚Â© en T5) (traite **R3**)
  3. `Do not allow bypassing the above settings` (s'applique ÃƒÆ’Ã‚Â  tout le monde, mÃƒÆ’Ã‚Âªme aux administrateurs)
  4. `Require conversation resolution before merging` (permet de s'assurer que tous les retours de revue sont traitÃƒÆ’Ã‚Â©s)

*(DÃƒÆ’Ã‚Â©poser la capture d'ÃƒÆ’Ã‚Â©cran ici : `docs/config/branch-protection.png`)*

---

## 2. Environnements et Secrets (Settings > Environments & Secrets)

Pour protÃƒÆ’Ã‚Â©ger les accÃƒÆ’Ã‚Â¨s et sÃƒÆ’Ã‚Â©parer le dÃƒÆ’Ã‚Â©veloppement de la production (**R4**) :

* **Environnement `production` :**
  * `Deployment branches` : restreindre aux tags `v*` ou ÃƒÆ’Ã‚Â  la branche `main`.
  * `Required reviewers` : activer la validation manuelle avant dÃƒÆ’Ã‚Â©ploiement (1 approbateur permanent requis).
* **Secrets de dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t / d'environnement :**
  * DÃƒÆ’Ã‚Â©finir les secrets nÃƒÆ’Ã‚Â©cessaires pour le dÃƒÆ’Ã‚Â©ploiement (tokens GHCR, variables de production).
  * Les secrets ne sont visibles par aucun membre non-administrateur.

*(DÃƒÆ’Ã‚Â©poser la capture d'ÃƒÆ’Ã‚Â©cran ici : `docs/config/environment-protection.png`)*

---

## 3. Gestion des collaborateurs (Settings > Collaborators)

Pour encadrer le freelance et les alternants (**R1**, **R2**, **R4**) :

* **DÃƒÆ’Ã‚Â©veloppeurs permanents / Lead dev :** rÃƒÆ’Ã‚Â´le `Admin` ou `Maintain` (accÃƒÆ’Ã‚Â¨s aux secrets et configuration).
* **Alternants :** rÃƒÆ’Ã‚Â´le `Write` (crÃƒÆ’Ã‚Â©ation de branches, ouverture de PRs, pas d'accÃƒÆ’Ã‚Â¨s direct aux secrets de prod).
* **Freelance :** rÃƒÆ’Ã‚Â´le `Triage` ou `Write` restreint (interdiction de bypasser les rÃƒÆ’Ã‚Â¨gles, pas d'accÃƒÆ’Ã‚Â¨s aux secrets).

*(DÃƒÆ’Ã‚Â©poser la capture d'ÃƒÆ’Ã‚Â©cran ici : `docs/config/collaborators-roles.png`)*
