# ADR 0001 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â StratÃƒÆ’Ã‚Â©gie de branches : GitHub Flow avec livraison par tag

- **Statut :** acceptÃƒÆ’Ã‚Â©
- **Date :** 19/11/2026
- **DÃƒÆ’Ã‚Â©cideurs :** l'ÃƒÆ’Ã‚Â©quipe DevOps, pour l'ÃƒÆ’Ã‚Â©quipe de dÃƒÆ’Ã‚Â©veloppement (2 permanents, 2 alternants, freelance ponctuel)

## 1. Contexte

- **Carte contexte :** 2 dÃƒÆ’Ã‚Â©veloppeurs permanents et 2 alternants prÃƒÆ’Ã‚Â©sents **2 semaines sur 4**. Certaines semaines, **seuls les 2 permanents sont lÃƒÆ’Ã‚Â ** (R1).
- **Anciennes pratiques :** tout le monde poussait directement sur `main`, et chaque push ÃƒÆ’Ã‚Â©tait dÃƒÆ’Ã‚Â©ployÃƒÆ’Ã‚Â© sans tests (R2, R3).
- **Incident d'aoÃƒÆ’Ã‚Â»t :** dÃƒÆ’Ã‚Â©ploiement un vendredi ÃƒÆ’Ã‚Â  19 h, 14 h de panne, version en production inconnue (R3, R5).
- **Parties prenantes :** le Product Owner veut livrer vite ; la lead dev craint que les revues ralentissent tout ; le freelance ne veut pas attendre ; la CEO ne veut plus de panne (R2, R3).

Il nous faut donc une stratÃƒÆ’Ã‚Â©gie **simple** (des alternants dÃƒÆ’Ã‚Â©butants doivent pouvoir la suivre), **rapide** (livrer souvent) et **contrÃƒÆ’Ã‚Â´lÃƒÆ’Ã‚Â©e** (plus rien n'arrive en production sans relecture ni tests).

## 2. Options ÃƒÆ’Ã‚Â©tudiÃƒÆ’Ã‚Â©es

| Option | Principe | Pour | Contre, dans **notre** contexte |
|---|---|---|---|
| **GitFlow** | branches `main`, `develop`, `feature/*`, `release/*`, `hotfix/*` | cadre trÃƒÆ’Ã‚Â¨s structurÃƒÆ’Ã‚Â© | trop de branches longues pour 4 personnes dont 2 absentes la moitiÃƒÆ’Ã‚Â© du temps : conflits, fusions oubliÃƒÆ’Ã‚Â©es entre `develop` et `main`, livraisons lentes (contraire au souhait du PO) |
| **Trunk-based** | intÃƒÆ’Ã‚Â©grations trÃƒÆ’Ã‚Â¨s frÃƒÆ’Ã‚Â©quentes sur `main`, avec ou sans PR, et branches trÃƒÆ’Ã‚Â¨s courtes | favorise une intÃƒÆ’Ã‚Â©gration rapide | notre ÃƒÆ’Ã‚Â©quipe prÃƒÆ’Ã‚Â©fÃƒÆ’Ã‚Â¨re formaliser systÃƒÆ’Ã‚Â©matiquement les PR et les revues pour accompagner les alternants et sÃƒÆ’Ã‚Â©curiser les changements, compte tenu du faible historique de tests (R1, R2, R3) |
| **GitHub Flow** | une seule branche permanente `main`, des branches courtes, une PR relue pour chaque changement | simple, un seul circuit ÃƒÆ’Ã‚Â  apprendre, la PR sert de relecture **et** de formation | `main` doit toujours rester dans un ÃƒÆ’Ã‚Â©tat dÃƒÆ’Ã‚Â©ployable |

## 3. DÃƒÆ’Ã‚Â©cision

Nous choisissons **GitHub Flow**, avec une variante : **fusionner sur `main` ne dÃƒÆ’Ã‚Â©clenche pas la mise en production.** La mise en production se fait uniquement quand on crÃƒÆ’Ã‚Â©e un **tag de version** (`v1.0.0`, `v1.1.0`ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦).

### Quelles branches ?

| Branche | DurÃƒÆ’Ã‚Â©e de vie | Qui la crÃƒÆ’Ã‚Â©e | Comment elle est fusionnÃƒÆ’Ã‚Â©e |
|---|---|---|---|
| `main` | permanente, **protÃƒÆ’Ã‚Â©gÃƒÆ’Ã‚Â©e** | ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â | uniquement via une pull request : 1 approbation + tests verts. Personne ne pousse directement dessus, administrateurs compris |
| `feat/ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦` (fonctionnalitÃƒÆ’Ã‚Â©), `fix/ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦` (bug), `docs/ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦`, `test/ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦`, `ci/ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦` | **objectif : 2 jours, sauf justification** | n'importe quel membre | par son auteur, aprÃƒÆ’Ã‚Â¨s approbation |
| `hotfix/ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦` (correctif urgent) | quelques heures | n'importe quel membre | idem, avec relecture prioritaire |

### Qui fait quoi ?

- **Tout le monde** (permanents, alternants, freelance) travaille sur une branche et ouvre une pull request. **Aucune exception**, pas mÃƒÆ’Ã‚Âªme pour le freelance pressÃƒÆ’Ã‚Â© (R2).
- **Relecture :** 1 approbation suffit. Le code d'un alternant est relu par un permanent ; pendant les semaines d'ÃƒÆ’Ã‚Â©cole, les 2 permanents se relisent mutuellement (R1, R2).
- **Mise en production :** une personne crÃƒÆ’Ã‚Â©e le tag de version ; une **autre** personne approuve le dÃƒÆ’Ã‚Â©ploiement en production (R3).

### Comment ?

1. Partir de `main` ÃƒÆ’Ã‚Â  jour et crÃƒÆ’Ã‚Â©er sa branche : `feat/US-42-stock`.
2. Faire des petits changements ; ouvrir la pull request tÃƒÆ’Ã‚Â´t (en **Draft** si ce n'est pas fini).
3. Les tests automatiques tournent ; un collÃƒÆ’Ã‚Â¨gue relit et approuve.
4. Fusion sur `main` (*Squash and merge* : 1 PR = 1 commit propre).
5. Quand on veut livrer : tag `vX.Y.Z` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ staging ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ test ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ approbation ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ production. **Jamais du vendredi 14 h au lundi** (R3).

### Pourquoi ces choix ?

- **Branches courtes (objectif : 2 jours) :** cela limite les conflits et facilite les revues. Une tÃƒÆ’Ã‚Â¢che plus longue est possible si elle est justifiÃƒÆ’Ã‚Â©e et suivie. Avant de repartir 2 semaines en formation, un alternant fusionne son travail terminÃƒÆ’Ã‚Â© ou transmet sa branche ÃƒÆ’Ã‚Â  un permanent avec une note de passation dans la Draft PR (R1).
- **Livrer par tag, et non ÃƒÆ’Ã‚Â  chaque fusion :** on peut fusionner le mardi et livrer le mercredi matin, quand quelqu'un est disponible pour surveiller. Chaque version porte un numÃƒÆ’Ã‚Â©ro, ce qui permet de savoir ce qui tourne en production et de revenir ÃƒÆ’Ã‚Â  la version prÃƒÆ’Ã‚Â©cÃƒÆ’Ã‚Â©dente (R3, R5).
- **Un seul circuit :** facile ÃƒÆ’Ã‚Â  apprendre pour des dÃƒÆ’Ã‚Â©butants (R1).

## 4. Correctif urgent (hotfix)

**Exemple :** en production, `POST /orders` renvoie une erreur et plus personne ne peut commander.

**ÃƒÆ’Ã¢â‚¬Â°tape 0 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â d'abord arrÃƒÆ’Ã‚Âªter la panne :** on revient ÃƒÆ’Ã‚Â  la version prÃƒÆ’Ã‚Â©cÃƒÆ’Ã‚Â©dente avec la procÃƒÆ’Ã‚Â©dure de retour arriÃƒÆ’Ã‚Â¨re (moins de 5 minutes, R5). On corrige ensuite au calme.

**ArrivÃƒÆ’Ã‚Â©e du correctif en production :**
1. CrÃƒÆ’Ã‚Â©er une branche depuis `main` : `hotfix/commande-bloquee`.
2. Corriger le bug et ajouter un test qui le reproduit.
3. Ouvrir une PR intitulÃƒÆ’Ã‚Â©e `fix: ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦`, avec l'ÃƒÆ’Ã‚Â©tiquette `hotfix`. Elle est relue **en prioritÃƒÆ’Ã‚Â© (objectif : dans l'heure)** par un relecteur disponible et compÃƒÆ’Ã‚Â©tent, diffÃƒÆ’Ã‚Â©rent de l'auteur (R1, R2).
4. Si aucun relecteur compÃƒÆ’Ã‚Â©tent n'est disponible, **on ne contourne pas l'approbation prÃƒÆ’Ã‚Â©alable**. On privilÃƒÆ’Ã‚Â©gie le rollback pour rÃƒÆ’Ã‚Â©tablir le service, puis on attend la revue avant de fusionner et dÃƒÆ’Ã‚Â©ployer le correctif. L'incident est documentÃƒÆ’Ã‚Â© dans `docs/incidents.md` (R2, R5).
5. AprÃƒÆ’Ã‚Â¨s approbation et CI verte, fusion sur `main` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ crÃƒÆ’Ã‚Â©ation d'un **nouveau tag en incrÃƒÆ’Ã‚Â©mentant le numÃƒÆ’Ã‚Â©ro de patch** (par exemple `v1.1.0` ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ `v1.1.1`) ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ build de l'image GHCR ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ staging ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ smoke test ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ approbation humaine ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ production. Le gel du vendredi ne s'applique pas ÃƒÆ’Ã‚Â  un hotfix critique, mais l'exception est documentÃƒÆ’Ã‚Â©e (R3, R5).

**Retour dans le travail en cours :**
- Le correctif est dans `main` : il constitue la rÃƒÆ’Ã‚Â©fÃƒÆ’Ã‚Â©rence commune, mais les branches dÃƒÆ’Ã‚Â©jÃƒÆ’Ã‚Â  ouvertes doivent ÃƒÆ’Ã‚Âªtre mises ÃƒÆ’Ã‚Â  jour pour le rÃƒÆ’Ã‚Â©cupÃƒÆ’Ã‚Â©rer.
- Chaque personne qui a une branche en cours la met ÃƒÆ’Ã‚Â  jour depuis `main` (bouton **Ãƒâ€šÃ‚Â« Update branch Ãƒâ€šÃ‚Â»** sur la PR, ou les commandes ci-dessous). Les tests sont relancÃƒÆ’Ã‚Â©s pour vÃƒÆ’Ã‚Â©rifier que la correction reste prÃƒÆ’Ã‚Â©sente (R3).

  ```bash
  git switch feat/US-42-stock
  git fetch origin
  git merge origin/main
  ```

**Cas rare :** si `main` contient dÃƒÆ’Ã‚Â©jÃƒÆ’Ã‚Â  des changements non encore livrÃƒÆ’Ã‚Â©s et qu'il faut corriger uniquement la version dÃƒÆ’Ã‚Â©ployÃƒÆ’Ã‚Â©e, la branche `hotfix/ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦` part du **tag en production** (ex. `v1.1.0`). AprÃƒÆ’Ã‚Â¨s correction, revue et tests, on crÃƒÆ’Ã‚Â©e un nouveau tag de patch **annotÃƒÆ’Ã‚Â© avec la mention `[hotfix]`** sur cette branche pour livrer uniquement le correctif (le pipeline refuse tout tag hors `main` sans cette mention). Le hotfix est ensuite **rÃƒÆ’Ã‚Â©intÃƒÆ’Ã‚Â©grÃƒÆ’Ã‚Â© dans `main` par une PR**, puis dans les branches de travail en cours. Ce cas est un signal d'alerte (voir section 6, R5).

## 5. ConsÃƒÆ’Ã‚Â©quences

- (+) Un seul circuit, simple pour les alternants ; la PR sert aussi de formation (R1).
- (+) On peut livrer souvent, comme le veut le PO, mais avec des contrÃƒÆ’Ã‚Â´les, comme l'exige la CEO (R2, R3).
- (+) Chaque version en production est identifiÃƒÆ’Ã‚Â©e et peut ÃƒÆ’Ã‚Âªtre annulÃƒÆ’Ã‚Â©e (R5).
- (ÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢) `main` doit toujours ÃƒÆ’Ã‚Âªtre livrable : pas de travail ÃƒÆ’Ã‚Â  moitiÃƒÆ’Ã‚Â© fini fusionnÃƒÆ’Ã‚Â©, et des migrations de base qui ajoutent sans supprimer (R5).
- (ÃƒÂ¢Ã‹â€ Ã¢â‚¬â„¢) Tout dÃƒÆ’Ã‚Â©pend de relectures rapides : objectif de **4 heures ouvrÃƒÆ’Ã‚Â©es** maximum (R2). Cette rÃƒÆ’Ã‚Â¨gle repose sur la discipline de l'ÃƒÆ’Ã‚Â©quipe, GitHub ne peut pas l'imposer.

## 6. Signaux que ce choix ne fonctionne plus

On rÃƒÆ’Ã‚Â©examine cette dÃƒÆ’Ã‚Â©cision si, sur un mois :

| Signal | Ce qu'il rÃƒÆ’Ã‚Â©vÃƒÆ’Ã‚Â¨le |
|---|---|
| une PR attend en moyenne **plus d'1 jour** avant d'ÃƒÆ’Ã‚Âªtre fusionnÃƒÆ’Ã‚Â©e | les relectures sont trop lentes (R2) : la stratÃƒÆ’Ã‚Â©gie freine au lieu d'aider |
| des branches vivent **plus de 5 jours**, ou les conflits sont frÃƒÆ’Ã‚Â©quents | les tÃƒÆ’Ã‚Â¢ches sont trop grosses, ou les absences des alternants sont mal gÃƒÆ’Ã‚Â©rÃƒÆ’Ã‚Â©es (R1) |
| **plus d'un hotfix** a dÃƒÆ’Ã‚Â» partir d'un tag au lieu de `main` | `main` n'est pas rÃƒÆ’Ã‚Â©ellement livrable |
| les tests de `main` sont cassÃƒÆ’Ã‚Â©s **plus de 2 fois** | la relecture et les tests ne jouent pas leur rÃƒÆ’Ã‚Â´le (R3) |
| la protection de `main` est dÃƒÆ’Ã‚Â©sactivÃƒÆ’Ã‚Â©e, mÃƒÆ’Ã‚Âªme une fois, Ãƒâ€šÃ‚Â« pour aller plus vite Ãƒâ€šÃ‚Â» | la rÃƒÆ’Ã‚Â¨gle est contournÃƒÆ’Ã‚Â©e : il faut l'adapter plutÃƒÆ’Ã‚Â´t que l'ignorer (R2) |
| l'ÃƒÆ’Ã‚Â©quipe dÃƒÆ’Ã‚Â©passe **8 ÃƒÆ’Ã‚Â  10 personnes**, ou doit maintenir plusieurs versions en mÃƒÆ’Ã‚Âªme temps | GitHub Flow devient trop lÃƒÆ’Ã‚Â©ger ; envisager des branches `release/*` |
