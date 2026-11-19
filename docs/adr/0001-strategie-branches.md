# ADR 0001 — Stratégie de branches : GitHub Flow avec livraison par tag

- **Statut :** accepté
- **Date :** 19/11/2026
- **Décideurs :** l'équipe DevOps, pour l'équipe de développement (2 permanents, 2 alternants, freelance ponctuel)

## 1. Contexte

- **Carte contexte :** 2 développeurs permanents et 2 alternants présents **2 semaines sur 4**. Certaines semaines, **seuls les 2 permanents sont là** (R1).
- **Anciennes pratiques :** tout le monde poussait directement sur `main`, et chaque push était déployé sans tests (R2, R3).
- **Incident d'août :** déploiement un vendredi à 19 h, 14 h de panne, version en production inconnue (R3, R5).
- **Parties prenantes :** le Product Owner veut livrer vite ; la lead dev craint que les revues ralentissent tout ; le freelance ne veut pas attendre ; la CEO ne veut plus de panne (R2, R3).

Il nous faut donc une stratégie **simple** (des alternants débutants doivent pouvoir la suivre), **rapide** (livrer souvent) et **contrôlée** (plus rien n'arrive en production sans relecture ni tests).

## 2. Options étudiées

| Option | Principe | Pour | Contre, dans **notre** contexte |
|---|---|---|---|
| **GitFlow** | branches `main`, `develop`, `feature/*`, `release/*`, `hotfix/*` | cadre très structuré | trop de branches longues pour 4 personnes dont 2 absentes la moitié du temps : conflits, fusions oubliées entre `develop` et `main`, livraisons lentes (contraire au souhait du PO) |
| **Trunk-based** | intégrations très fréquentes sur `main`, avec ou sans PR, et branches très courtes | favorise une intégration rapide | notre équipe préfère formaliser systématiquement les PR et les revues pour accompagner les alternants et sécuriser les changements, compte tenu du faible historique de tests (R1, R2, R3) |
| **GitHub Flow** | une seule branche permanente `main`, des branches courtes, une PR relue pour chaque changement | simple, un seul circuit à apprendre, la PR sert de relecture **et** de formation | `main` doit toujours rester dans un état déployable |

## 3. Décision

Nous choisissons **GitHub Flow**, avec une variante : **fusionner sur `main` ne déclenche pas la mise en production.** La mise en production se fait uniquement quand on crée un **tag de version** (`v1.0.0`, `v1.1.0`…).

### Quelles branches ?

| Branche | Durée de vie | Qui la crée | Comment elle est fusionnée |
|---|---|---|---|
| `main` | permanente, **protégée** | — | uniquement via une pull request : 1 approbation + tests verts. Personne ne pousse directement dessus, administrateurs compris |
| `feat/…` (fonctionnalité), `fix/…` (bug), `docs/…`, `test/…`, `ci/…` | **objectif : 2 jours, sauf justification** | n'importe quel membre | par son auteur, après approbation |
| `hotfix/…` (correctif urgent) | quelques heures | n'importe quel membre | idem, avec relecture prioritaire |

### Qui fait quoi ?

- **Tout le monde** (permanents, alternants, freelance) travaille sur une branche et ouvre une pull request. **Aucune exception**, pas même pour le freelance pressé (R2).
- **Relecture :** 1 approbation suffit. Le code d'un alternant est relu par un permanent ; pendant les semaines d'école, les 2 permanents se relisent mutuellement (R1, R2).
- **Mise en production :** une personne crée le tag de version ; une **autre** personne approuve le déploiement en production (R3).

### Comment ?

1. Partir de `main` à jour et créer sa branche : `feat/US-42-stock`.
2. Faire des petits changements ; ouvrir la pull request tôt (en **Draft** si ce n'est pas fini).
3. Les tests automatiques tournent ; un collègue relit et approuve.
4. Fusion sur `main` (*Squash and merge* : 1 PR = 1 commit propre).
5. Quand on veut livrer : tag `vX.Y.Z` → staging → test → approbation → production. **Jamais du vendredi 14 h au lundi** (R3).

### Pourquoi ces choix ?

- **Branches courtes (objectif : 2 jours) :** cela limite les conflits et facilite les revues. Une tâche plus longue est possible si elle est justifiée et suivie. Avant de repartir 2 semaines en formation, un alternant fusionne son travail terminé ou transmet sa branche à un permanent avec une note de passation dans la Draft PR (R1).
- **Livrer par tag, et non à chaque fusion :** on peut fusionner le mardi et livrer le mercredi matin, quand quelqu'un est disponible pour surveiller. Chaque version porte un numéro, ce qui permet de savoir ce qui tourne en production et de revenir à la version précédente (R3, R5).
- **Un seul circuit :** facile à apprendre pour des débutants (R1).

## 4. Correctif urgent (hotfix)

**Exemple :** en production, `POST /orders` renvoie une erreur et plus personne ne peut commander.

**Étape 0 — d'abord arrêter la panne :** on revient à la version précédente avec la procédure de retour arrière (moins de 5 minutes, R5). On corrige ensuite au calme.

**Arrivée du correctif en production :**
1. Créer une branche depuis `main` : `hotfix/commande-bloquee`.
2. Corriger le bug et ajouter un test qui le reproduit.
3. Ouvrir une PR intitulée `fix: …`, avec l'étiquette `hotfix`. Elle est relue **en priorité (objectif : dans l'heure)** par un relecteur disponible et compétent, différent de l'auteur (R1, R2).
4. Si aucun relecteur compétent n'est disponible, **on ne contourne pas l'approbation préalable**. On privilégie le rollback pour rétablir le service, puis on attend la revue avant de fusionner et déployer le correctif. L'incident est documenté dans `docs/incidents.md` (R2, R5).
5. Après approbation et CI verte, fusion sur `main` → création d'un **nouveau tag en incrémentant le numéro de patch** (par exemple `v1.1.0` → `v1.1.1`) → build de l'image GHCR → staging → smoke test → approbation humaine → production. Le gel du vendredi ne s'applique pas à un hotfix critique, mais l'exception est documentée (R3, R5).

**Retour dans le travail en cours :**
- Le correctif est dans `main` : il constitue la référence commune, mais les branches déjà ouvertes doivent être mises à jour pour le récupérer.
- Chaque personne qui a une branche en cours la met à jour depuis `main` (bouton **« Update branch »** sur la PR, ou les commandes ci-dessous). Les tests sont relancés pour vérifier que la correction reste présente (R3).

  ```bash
  git switch feat/US-42-stock
  git fetch origin
  git merge origin/main
  ```

**Cas rare :** si `main` contient déjà des changements non encore livrés et qu'il faut corriger uniquement la version déployée, la branche `hotfix/…` part du **tag en production** (ex. `v1.1.0`). Après correction, revue et tests, on crée un nouveau tag de patch **annoté avec la mention `[hotfix]`** sur cette branche pour livrer uniquement le correctif (le pipeline refuse tout tag hors `main` sans cette mention). Le hotfix est ensuite **réintégré dans `main` par une PR**, puis dans les branches de travail en cours. Ce cas est un signal d'alerte (voir section 6, R5).

## 5. Conséquences

- (+) Un seul circuit, simple pour les alternants ; la PR sert aussi de formation (R1).
- (+) On peut livrer souvent, comme le veut le PO, mais avec des contrôles, comme l'exige la CEO (R2, R3).
- (+) Chaque version en production est identifiée et peut être annulée (R5).
- (−) `main` doit toujours être livrable : pas de travail à moitié fini fusionné, et des migrations de base qui ajoutent sans supprimer (R5).
- (−) Tout dépend de relectures rapides : objectif de **4 heures ouvrées** maximum (R2). Cette règle repose sur la discipline de l'équipe, GitHub ne peut pas l'imposer.

## 6. Signaux que ce choix ne fonctionne plus

On réexamine cette décision si, sur un mois :

| Signal | Ce qu'il révèle |
|---|---|
| une PR attend en moyenne **plus d'1 jour** avant d'être fusionnée | les relectures sont trop lentes (R2) : la stratégie freine au lieu d'aider |
| des branches vivent **plus de 5 jours**, ou les conflits sont fréquents | les tâches sont trop grosses, ou les absences des alternants sont mal gérées (R1) |
| **plus d'un hotfix** a dû partir d'un tag au lieu de `main` | `main` n'est pas réellement livrable |
| les tests de `main` sont cassés **plus de 2 fois** | la relecture et les tests ne jouent pas leur rôle (R3) |
| la protection de `main` est désactivée, même une fois, « pour aller plus vite » | la règle est contournée : il faut l'adapter plutôt que l'ignorer (R2) |
| l'équipe dépasse **8 à 10 personnes**, ou doit maintenir plusieurs versions en même temps | GitHub Flow devient trop léger ; envisager des branches `release/*` |
