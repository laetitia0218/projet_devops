# Guide de contribution (CONTRIBUTING.md)

Bienvenue sur le projet ! Ce document dÃƒÆ’Ã‚Â©finit nos rÃƒÆ’Ã‚Â¨gles de travail communes.
Dans notre ÃƒÆ’Ã‚Â©quipe (2 dÃƒÆ’Ã‚Â©veloppeurs permanents, 2 alternants prÃƒÆ’Ã‚Â©sents 2 semaines sur 4, et un dÃƒÆ’Ã‚Â©veloppeur freelance ponctuel), ces rÃƒÆ’Ã‚Â¨gles nous permettent de livrer rapidement sans revivre l'incident d'aoÃƒÆ’Ã‚Â»t (14h de panne un vendredi soir).

Chaque rÃƒÆ’Ã‚Â¨gle est directement liÃƒÆ’Ã‚Â©e aux risques identifiÃƒÆ’Ã‚Â©s dans notre analyse [`docs/risques.md`](docs/risques.md).

---

## 1. Relecture de code (Code Review)

* **RÃƒÆ’Ã‚Â¨gle :** **1 seule approbation obligatoire** par Pull Request pour pouvoir fusionner sur `main`.
* **Justification :** Nous sommes 4 dans l'ÃƒÆ’Ã‚Â©quipe, mais les 2 alternants sont absents 2 semaines sur 4 en formation (**R1**). Exiger 2 relecteurs bloquerait le travail quand seuls les 2 permanents sont lÃƒÆ’Ã‚Â . 1 relecteur suffit pour dÃƒÆ’Ã‚Â©tecter les erreurs sans ralentir (**R2**).
* **Qui relit qui ?**
  * Un alternant est relu par un permanent (effet formateur).
  * Les 2 permanents se relisent mutuellement quand les alternants sont en cours (**R1**).
  * Les contributions du freelance sont relues par la lead dev ou un permanent (**R2**).
* **Que faire si le seul relecteur compÃƒÆ’Ã‚Â©tent est absent ?**
  * **Cas normal :** La PR est rÃƒÆ’Ã‚Â©attribuÃƒÆ’Ã‚Â©e au permanent disponible. On privilÃƒÆ’Ã‚Â©gie une courte session de relecture ÃƒÆ’Ã‚Â  deux (binÃƒÆ’Ã‚Â´mage) si le sujet est pointu. On n'attend pas passivement (**R1**, **R2**).
  * **RÃƒÆ’Ã‚Â¨gle absolue :** On ne contourne **JAMAIS** l'obligation de relecture sur `main` (**R2**).
  * **En cas d'urgence en production (incident) :** On ne pousse pas un correctif ÃƒÆ’Ã‚Â  l'aveugle. On applique d'abord la procÃƒÆ’Ã‚Â©dure de **retour arriÃƒÆ’Ã‚Â¨re (rollback en < 5 minutes)** pour restaurer le service (**R5**). Ensuite, le correctif est rÃƒÆ’Ã‚Â©digÃƒÆ’Ã‚Â© et relu dÃƒÆ’Ã‚Â¨s qu'un permanent est joignable.

---

## 2. Nommage des branches et messages de commit

### A. Branches
Toute modification se fait sur une branche dÃƒÆ’Ã‚Â©diÃƒÆ’Ã‚Â©e crÃƒÆ’Ã‚Â©ÃƒÆ’Ã‚Â©e depuis `main` ÃƒÆ’Ã‚Â  jour.

Format : `<type>/<description-courte>`

* `feat/nom-fonctionnalite` : nouvelle fonctionnalitÃƒÆ’Ã‚Â© (ex: `feat/gestion-stock`, `feat/route-produits`)
* `fix/description-bug` : correction d'un bug (ex: `fix/calcul-total`)
* `hotfix/nom-urgence` : correctif critique en production (ex: `hotfix/blocage-commandes`)
* `docs/sujet` : documentation (ex: `docs/t3-regles-gestion`)
* `test/sujet` : ajout ou mise ÃƒÆ’Ã‚Â  jour de tests
* `ci/sujet` : modification des pipelines GitHub Actions

* **Justification :** Permet ÃƒÆ’Ã‚Â  tout le monde (notamment aux alternants aprÃƒÆ’Ã‚Â¨s 2 semaines d'absence ou au trinÃƒÆ’Ã‚Â´me voisin qui relit nos PRs) de comprendre immÃƒÆ’Ã‚Â©diatement la nature de la tÃƒÆ’Ã‚Â¢che (**R1**, **R2**).

### B. Messages de commit
Nous utilisons une convention simple et lisible (inspirÃƒÆ’Ã‚Â©e de Conventional Commits) :

Format : `<type>: <description courte au prÃƒÆ’Ã‚Â©sent>`

* `feat: ajout de la route POST /orders`
* `fix: empeche la commande si stock insuffisant`
* `docs: mise a jour du CONTRIBUTING`
* `test: ajout test unitaire sur la route health`
* `ci: configuration du job de test`

* **Justification :** L'historique Git reste clair et permet de retrouver facilement quel commit a introduit un changement (**R5**).
* **Fusion sur `main` :** On utilise le mode **Squash and merge** sur GitHub. Cela rassemble tous les commits intermÃƒÆ’Ã‚Â©diaires d'une PR en un seul commit propre sur `main`.

---

## 3. Definition of Done (DoD)

Une tÃƒÆ’Ã‚Â¢che ou une User Story est considÃƒÆ’Ã‚Â©rÃƒÆ’Ã‚Â©e comme **Ãƒâ€šÃ‚Â« TerminÃƒÆ’Ã‚Â©e Ãƒâ€šÃ‚Â» (Done)** uniquement si :

1. [ ] **Code fonctionnel :** Le code rÃƒÆ’Ã‚Â©pond aux critÃƒÆ’Ã‚Â¨res de la User Story, sans code mort ou inutile.
2. [ ] **Tests automatiques :** Au moins un test automatisÃƒÆ’Ã‚Â© valide la fonctionnalitÃƒÆ’Ã‚Â© ou la correction (**R3**).
3. [ ] **Pipeline CI au vert :** Le pipeline GitHub Actions passe avec succÃƒÆ’Ã‚Â¨s (tests + build Docker valides) (**R3**).
4. [ ] **Relecture approuvÃƒÆ’Ã‚Â©e :** La PR a reÃƒÆ’Ã‚Â§u au moins **1 approbation** d'un collÃƒÆ’Ã‚Â¨gue (**R2**).
5. [ ] **SÃƒÆ’Ã‚Â©curitÃƒÆ’Ã‚Â© vÃƒÆ’Ã‚Â©rifiÃƒÆ’Ã‚Â©e :** Aucun mot de passe, clÃƒÆ’Ã‚Â© d'API ou secret n'est prÃƒÆ’Ã‚Â©sent dans le code ou l'historique (**R4**).
6. [ ] **Documentation ÃƒÆ’Ã‚Â  jour :** Si l'API ou le comportement change, la documentation est ajustÃƒÆ’Ã‚Â©e.
7. [ ] **Fusion et nettoyage :** La PR est fusionnÃƒÆ’Ã‚Â©e sur `main` via *Squash and merge* et la branche de travail est supprimÃƒÆ’Ã‚Â©e.

> **Cas particulier des alternants :** Si une tÃƒÆ’Ã‚Â¢che n'est pas finie avant le dÃƒÆ’Ã‚Â©part en formation de 2 semaines, l'alternant doit ouvrir une **Draft PR** et rÃƒÆ’Ã‚Â©diger une courte note de passation (ce qui est fait, ce qui reste ÃƒÆ’Ã‚Â  faire, comment tester) (**R1**).

---

## 4. Versionnage et visibilitÃƒÆ’Ã‚Â© en production (RÃƒÆ’Ã‚Â¨gle des 10 secondes)

Pour ÃƒÆ’Ã‚Â©viter l'incident d'aoÃƒÆ’Ã‚Â»t oÃƒÆ’Ã‚Â¹ personne ne savait quelle version tournait en production (**R5**) :

* **NumÃƒÆ’Ã‚Â©rotation sÃƒÆ’Ã‚Â©mantique :** Chaque livraison officielle est ÃƒÆ’Ã‚Â©tiquetÃƒÆ’Ã‚Â©e par un tag Git au format `vX.Y.Z` (ex: `v1.0.0`, `v1.0.1`).
* **Images Docker :** L'image Docker construite porte le tag de version exact (ex: `ghcr.io/organisation/api:v1.0.0`) ainsi que le hash du commit. On bannit l'utilisation du tag `latest` seul (**R5**).
* **Le test des 10 secondes :**
  L'API expose obligatoirement une route publique `GET /health`.
  Une simple requÃƒÆ’Ã‚Âªte permet de savoir immÃƒÆ’Ã‚Â©diatement quelle version tourne :

  ```bash
  curl http://localhost:8000/health
  ```

  RÃƒÆ’Ã‚Â©ponse JSON attendue en moins de 10 secondes :
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

* **OÃƒÆ’Ã‚Â¹ vivent les secrets ?**
  * **En local (dÃƒÆ’Ã‚Â©veloppement) :** Dans un fichier `.env` non versionnÃƒÆ’Ã‚Â©, strictement ignorÃƒÆ’Ã‚Â© par le `.gitignore`. Un fichier `.env.example` sans aucun secret rÃƒÆ’Ã‚Â©el est versionnÃƒÆ’Ã‚Â© pour guider l'installation (**R4**).
  * **Dans le pipeline CI/CD :** Dans les **GitHub Actions Secrets** (chiffrÃƒÆ’Ã‚Â©s et masquÃƒÆ’Ã‚Â©s dans les logs) (**R4**).
  * **En production :** DÃƒÆ’Ã‚Â©finis comme variables d'environnement sur le serveur de dÃƒÆ’Ã‚Â©ploiement.
* **Qui y a accÃƒÆ’Ã‚Â¨s ?**
  * Seuls les 2 dÃƒÆ’Ã‚Â©veloppeurs permanents (administrateurs du dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t) ont accÃƒÆ’Ã‚Â¨s aux secrets de production (**R4**). Les alternants et le freelance travaillent avec des mocks ou des bases locales jetables.
* **Que fait-on si un secret fuite (ex: commitÃƒÆ’Ã‚Â© par erreur) ?**
  1. **RÃƒÆ’Ã‚Â©vocation immÃƒÆ’Ã‚Â©diate (PrioritÃƒÆ’Ã‚Â© 1) :** On change immÃƒÆ’Ã‚Â©diatement le mot de passe, le token ou la clÃƒÆ’Ã‚Â© sur le service externe (PostgreSQL, hÃƒÆ’Ã‚Â©bergeur...). *RÃƒÆ’Ã‚Â¨gle : Supprimer le commit ne rend pas un secret rÃƒÆ’Ã‚Â©voquÃƒÆ’Ã‚Â© sÃƒÆ’Ã‚Â»r* (**R4**).
  2. **Audit :** VÃƒÆ’Ã‚Â©rifier les logs pour s'assurer qu'aucune action malveillante n'a eu lieu pendant l'exposition.
  3. **Mise ÃƒÆ’Ã‚Â  jour :** Renseigner le nouveau secret dans GitHub Secrets et sur le serveur de production.
  4. **Nettoyage Git :** Retirer le fichier de l'historique Git si nÃƒÆ’Ã‚Â©cessaire.
  5. **TraÃƒÆ’Ã‚Â§abilitÃƒÆ’Ã‚Â© :** RÃƒÆ’Ã‚Â©diger un compte-rendu dans `docs/incidents.md`.

---

## 6. Cas du dÃƒÆ’Ã‚Â©veloppeur freelance

* **Rappel :** Le freelance a dÃƒÆ’Ã‚Â©clarÃƒÆ’Ã‚Â© : *Ãƒâ€šÃ‚Â« Je suis payÃƒÆ’Ã‚Â© ÃƒÆ’Ã‚Â  l'heure, je n'ai pas le temps d'attendre qu'on me relise. Ãƒâ€šÃ‚Â»*
* **Notre dÃƒÆ’Ã‚Â©cision :**
  * **Aucune exception aux rÃƒÆ’Ã‚Â¨gles de sÃƒÆ’Ã‚Â©curitÃƒÆ’Ã‚Â© et de qualitÃƒÆ’Ã‚Â© :** Le freelance ne pousse **JAMAIS** directement sur `main` et n'a aucun droit d'administration sur le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t (**R2**, **R4**).
  * **Pour ne pas le bloquer dans sa facturation :**
    1. **DÃƒÆ’Ã‚Â©coupage fin :** Le freelance travaille sur des tÃƒÆ’Ã‚Â¢ches courtes et indÃƒÆ’Ã‚Â©pendantes.
    2. **Travail en parallÃƒÆ’Ã‚Â¨le :** DÃƒÆ’Ã‚Â¨s qu'il ouvre une PR pour une tÃƒÆ’Ã‚Â¢che finie, il bascule sur une nouvelle branche et continue sa mission sans attendre que la premiÃƒÆ’Ã‚Â¨re PR soit fusionnÃƒÆ’Ã‚Â©e.
    3. **Engagement de l'ÃƒÆ’Ã‚Â©quipe :** Les dÃƒÆ’Ã‚Â©veloppeurs permanents s'engagent ÃƒÆ’Ã‚Â  relire ses PRs sous un dÃƒÆ’Ã‚Â©lai rapide (**objectif : moins de 4 heures ouvrÃƒÆ’Ã‚Â©es**) (**R2**).
    4. **SÃƒÆ’Ã‚Â©curitÃƒÆ’Ã‚Â© :** Le freelance n'a pas accÃƒÆ’Ã‚Â¨s aux secrets de production (**R4**).

---

## 7. RÃƒÆ’Ã‚Â©capitulatif : ImposÃƒÆ’Ã‚Â© par GitHub vs Discipline de l'ÃƒÆ’Ã‚Â©quipe

Pour l'oral et pour la clartÃƒÆ’Ã‚Â© du TP, nous distinguons ce que l'outil technique bloque automatiquement de ce qui dÃƒÆ’Ã‚Â©pend de notre sÃƒÆ’Ã‚Â©rieux au quotidien :

| RÃƒÆ’Ã‚Â¨gle | ImposÃƒÆ’Ã‚Â© par GitHub (technique) | Discipline de l'ÃƒÆ’Ã‚Â©quipe (humain) | Risque traitÃƒÆ’Ã‚Â© |
|---|:---:|:---:|---|
| **Interdiction de push direct sur `main`** | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Branch protection | ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â | **R2** |
| **Au moins 1 approbation avant merge** | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Require a pull request before merging (1 approval) | ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â | **R1, R2** |
| **SuccÃƒÆ’Ã‚Â¨s obligatoire des tests CI** | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Require status checks to pass before merging | ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â | **R3** |
| **Respect du format des branches et commits** | ÃƒÂ¢Ã‚ÂÃ…â€™ (possible via bot lourd, mais trop complexe pour un TP) | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Discipline lors de l'ouverture de la PR | **R1, R5** |
| **Objectif de relecture sous 4 heures** | ÃƒÂ¢Ã‚ÂÃ…â€™ GitHub ne peut pas forcer un humain ÃƒÆ’Ã‚Â  relire vite | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Organisation interne de l'ÃƒÆ’Ã‚Â©quipe | **R2** |
| **Interdiction de dÃƒÆ’Ã‚Â©ployer le vendredi ÃƒÆ’Ã‚Â  19h** | ÃƒÂ¢Ã‚ÂÃ…â€™ | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Accord d'ÃƒÆ’Ã‚Â©quipe (gel des mises en prod le vendredi aprÃƒÆ’Ã‚Â¨s-midi) | **R3** |
| **Passation ÃƒÆ’Ã‚Â©crite avant le dÃƒÆ’Ã‚Â©part en formation** | ÃƒÂ¢Ã‚ÂÃ…â€™ | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Remplissage obligatoire de la Draft PR par l'alternant | **R1** |
| **Pas de secrets commitÃƒÆ’Ã‚Â©s dans le code** | ÃƒÂ¢Ã…Â¡Ã‚Â ÃƒÂ¯Ã‚Â¸Ã‚Â GitHub Secret Scanning (alerte mais n'empÃƒÆ’Ã‚Âªche pas toujours) | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Vigilance, `.gitignore` et `.env.example` | **R4** |
| **ProcÃƒÆ’Ã‚Â©dure de rÃƒÆ’Ã‚Â©vocation en cas de fuite** | ÃƒÂ¢Ã‚ÂÃ…â€™ | ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ ProcÃƒÆ’Ã‚Â©dure d'urgence de l'ÃƒÆ’Ã‚Â©quipe | **R4** |
