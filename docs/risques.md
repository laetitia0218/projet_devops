# T1 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Analyse des risques

## 1. Contexte

Notre entreprise est une start-up qui met en relation des producteurs, des restaurants et des particuliers. Elle repart sur un dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t GitHub public aprÃƒÆ’Ã‚Â¨s plusieurs pratiques risquÃƒÆ’Ã‚Â©es : push directs sur `main`, dÃƒÆ’Ã‚Â©ploiements automatiques sans tests, images Docker identifiÃƒÆ’Ã‚Â©es uniquement par `latest`, secrets dans un fichier `.env` versionnÃƒÆ’Ã‚Â© et migrations PostgreSQL exÃƒÆ’Ã‚Â©cutÃƒÆ’Ã‚Â©es manuellement.

Lors de l'incident d'aoÃƒÆ’Ã‚Â»t, une mise en production effectuÃƒÆ’Ã‚Â©e un vendredi ÃƒÆ’Ã‚Â  19 h a bloquÃƒÆ’Ã‚Â© les commandes pendant **14 heures**. L'ÃƒÆ’Ã‚Â©quipe ne savait pas quelle version ÃƒÆ’Ã‚Â©tait dÃƒÆ’Ã‚Â©ployÃƒÆ’Ã‚Â©e.

**Carte contexte :** l'ÃƒÆ’Ã‚Â©quipe compte **2 dÃƒÆ’Ã‚Â©veloppeurs permanents et 2 alternants**, prÃƒÆ’Ã‚Â©sents en entreprise **2 semaines sur 4**. Pendant leurs semaines de formation, seuls les 2 permanents assurent la continuitÃƒÆ’Ã‚Â©. Le scÃƒÆ’Ã‚Â©nario mentionne ÃƒÆ’Ã‚Â©galement une lead dev prÃƒÆ’Ã‚Â©occupÃƒÆ’Ã‚Â©e par la lenteur des revues, un Product Owner qui souhaite livrer rapidement, une CEO qui refuse une nouvelle panne majeure et un freelance ponctuel qui ne veut pas attendre les relectures.

## 2. Identification des 5 risques

### R1 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Absence des alternants et perte de connaissances

- **Origine :** carte contexte (2 alternants absents 2 semaines sur 4) et crainte de ralentissement exprimÃƒÆ’Ã‚Â©e par la lead dev.
- **CatÃƒÆ’Ã‚Â©gorie :** Organisation.
- **ScÃƒÆ’Ã‚Â©nario concret :** un alternant commence une fonctionnalitÃƒÆ’Ã‚Â© puis repart en formation sans expliquer son travail. Les permanents ne savent pas la terminer. Si deux approbations ÃƒÆ’Ã‚Â©taient exigÃƒÆ’Ã‚Â©es par Pull Request, les deux personnes prÃƒÆ’Ã‚Â©sentes certaines semaines pourraient difficilement faire avancer les changements.
- **GravitÃƒÆ’Ã‚Â© : 4/5 (ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â©e).** Le risque ralentit les livraisons et peut retarder une correction urgente.
- **Mesure dans le futur socle :** dÃƒÆ’Ã‚Â©couper les travaux en petites issues GitHub, ouvrir une *Draft Pull Request* pour le travail inachevÃƒÆ’Ã‚Â© et prÃƒÆ’Ã‚Â©voir une passation avant le dÃƒÆ’Ã‚Â©part en formation. Exiger **une approbation par PR**, donnÃƒÆ’Ã‚Â©e par une personne disponible et compÃƒÆ’Ã‚Â©tente sur le changement. Les deux permanents se relisent mutuellement pendant les semaines d'absence des alternants. Documenter les procÃƒÆ’Ã‚Â©dures dans `CONTRIBUTING.md`.

### R2 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modification de `main` sans relecture

- **Origine :** ancienne pratique des push directs sur `main` ; inquiÃƒÆ’Ã‚Â©tude de la lead dev concernant les revues ; freelance souhaitant ÃƒÆ’Ã‚Â©viter l'attente.
- **CatÃƒÆ’Ã‚Â©gorie :** FiabilitÃƒÆ’Ã‚Â© et organisation.
- **ScÃƒÆ’Ã‚Â©nario concret :** pour livrer vite, un dÃƒÆ’Ã‚Â©veloppeur ou le freelance pousse un changement non relu sur `main`. Une rÃƒÆ’Ã‚Â©gression affectant les commandes est fusionnÃƒÆ’Ã‚Â©e puis livrÃƒÆ’Ã‚Â©e en production.
- **GravitÃƒÆ’Ã‚Â© : 5/5 (critique).** Une modification non vÃƒÆ’Ã‚Â©rifiÃƒÆ’Ã‚Â©e peut interrompre le service et entraÃƒÆ’Ã‚Â®ner des pertes commerciales.
- **Mesure dans le futur socle :** protÃƒÆ’Ã‚Â©ger `main` avec une rÃƒÆ’Ã‚Â¨gle GitHub imposant une Pull Request, **une approbation** et le succÃƒÆ’Ã‚Â¨s des contrÃƒÆ’Ã‚Â´les CI avant fusion. Appliquer la rÃƒÆ’Ã‚Â¨gle aux administrateurs lorsque la configuration du dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t le permet ; ne pas accorder de droits d'administration au freelance. Fixer un objectif interne de relecture sous **4 heures ouvrÃƒÆ’Ã‚Â©es**, avec rÃƒÆ’Ã‚Â©attribution si le relecteur est absent. Cet objectif relÃƒÆ’Ã‚Â¨ve de la discipline de l'ÃƒÆ’Ã‚Â©quipe, contrairement aux contrÃƒÆ’Ã‚Â´les imposÃƒÆ’Ã‚Â©s par GitHub.

### R3 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â DÃƒÆ’Ã‚Â©ploiement sans tests ni validation au mauvais moment

- **Origine :** dÃƒÆ’Ã‚Â©ploiement automatique par SSH ÃƒÆ’Ã‚Â  chaque push, tests insuffisants et incident d'aoÃƒÆ’Ã‚Â»t (vendredi 19 h, 14 heures de panne) ; exigence de fiabilitÃƒÆ’Ã‚Â© de la CEO.
- **CatÃƒÆ’Ã‚Â©gorie :** FiabilitÃƒÆ’Ã‚Â©.
- **ScÃƒÆ’Ã‚Â©nario concret :** une modification casse `POST /orders`. Le code est dÃƒÆ’Ã‚Â©ployÃƒÆ’Ã‚Â© automatiquement un vendredi soir sans tests ni vÃƒÆ’Ã‚Â©rification, empÃƒÆ’Ã‚Âªchant les clients de commander alors que peu de personnes sont disponibles pour intervenir.
- **GravitÃƒÆ’Ã‚Â© : 5/5 (critique).** Ce type d'incident s'est dÃƒÆ’Ã‚Â©jÃƒÆ’Ã‚Â  produit et a bloquÃƒÆ’Ã‚Â© l'activitÃƒÆ’Ã‚Â© pendant 14 heures.
- **Mesure dans le futur socle :** exÃƒÆ’Ã‚Â©cuter automatiquement les tests avec GitHub Actions sur les PR et bloquer la fusion en cas d'ÃƒÆ’Ã‚Â©chec. Tester la version sur un environnement de *staging* avec un *smoke test*, puis demander une approbation humaine avant le dÃƒÆ’Ã‚Â©ploiement en production. ÃƒÆ’Ã¢â‚¬Â°viter les dÃƒÆ’Ã‚Â©ploiements ordinaires du vendredi ÃƒÆ’Ã‚Â  14 h jusqu'au lundi ; autoriser un **hotfix critique** aprÃƒÆ’Ã‚Â¨s validation et avec une procÃƒÆ’Ã‚Â©dure de retour arriÃƒÆ’Ã‚Â¨re prÃƒÆ’Ã‚Âªte. La restriction horaire est une rÃƒÆ’Ã‚Â¨gle d'organisation ÃƒÆ’Ã‚Â  respecter et ÃƒÆ’Ã‚Â  documenter.

### R4 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Exposition de secrets dans le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t public

- **Origine :** ancienne pratique de versionnement d'un fichier `.env` contenant des mots de passe et clÃƒÆ’Ã‚Â©s d'API ; dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t GitHub public.
- **CatÃƒÆ’Ã‚Â©gorie :** SÃƒÆ’Ã‚Â©curitÃƒÆ’Ã‚Â©.
- **ScÃƒÆ’Ã‚Â©nario concret :** un membre commite par erreur des identifiants PostgreSQL dans `.env`. Une personne extÃƒÆ’Ã‚Â©rieure rÃƒÆ’Ã‚Â©cupÃƒÆ’Ã‚Â¨re ces secrets et peut tenter d'accÃƒÆ’Ã‚Â©der aux services ou aux donnÃƒÆ’Ã‚Â©es de l'entreprise.
- **GravitÃƒÆ’Ã‚Â© : 5/5 (critique).** Une fuite peut compromettre des donnÃƒÆ’Ã‚Â©es et l'infrastructure, avec des consÃƒÆ’Ã‚Â©quences rÃƒÆ’Ã‚Â©glementaires possibles.
- **Mesure dans le futur socle :** exclure `.env` via `.gitignore` dÃƒÆ’Ã‚Â¨s le dÃƒÆ’Ã‚Â©part et fournir un `.env.example` sans secret rÃƒÆ’Ã‚Â©el. Stocker les secrets du pipeline dans **GitHub Actions Secrets / Environments** et les secrets du serveur dans une configuration sÃƒÆ’Ã‚Â©curisÃƒÆ’Ã‚Â©e hors Git. Ajouter un contrÃƒÆ’Ã‚Â´le de dÃƒÆ’Ã‚Â©tection des secrets dans la CI. En cas de fuite, **rÃƒÆ’Ã‚Â©voquer et renouveler immÃƒÆ’Ã‚Â©diatement** les identifiants, vÃƒÆ’Ã‚Â©rifier les accÃƒÆ’Ã‚Â¨s et traiter l'historique Git ; effacer un commit ne suffit pas ÃƒÆ’Ã‚Â  rendre un secret sÃƒÆ’Ã‚Â»r.

### R5 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Version inconnue, migrations non maÃƒÆ’Ã‚Â®trisÃƒÆ’Ã‚Â©es et rollback impossible

- **Origine :** images Docker publiÃƒÆ’Ã‚Â©es avec `latest`, absence de traÃƒÆ’Ã‚Â§abilitÃƒÆ’Ã‚Â© de la version en production lors de l'incident d'aoÃƒÆ’Ã‚Â»t et migrations de base lancÃƒÆ’Ã‚Â©es manuellement Ãƒâ€šÃ‚Â« quand on y pense Ãƒâ€šÃ‚Â».
- **CatÃƒÆ’Ã‚Â©gorie :** FiabilitÃƒÆ’Ã‚Â© et exploitation.
- **ScÃƒÆ’Ã‚Â©nario concret :** une nouvelle version de l'API nÃƒÆ’Ã‚Â©cessite une colonne `stock`, mais la migration PostgreSQL est oubliÃƒÆ’Ã‚Â©e. Les commandes ÃƒÆ’Ã‚Â©chouent. L'ÃƒÆ’Ã‚Â©quipe ne connaÃƒÆ’Ã‚Â®t pas la version prÃƒÆ’Ã‚Â©cÃƒÆ’Ã‚Â©dente et une migration incompatible peut empÃƒÆ’Ã‚Âªcher de restaurer rapidement l'application.
- **GravitÃƒÆ’Ã‚Â© : 5/5 (critique).** La panne peut durer plusieurs heures et le retour arriÃƒÆ’Ã‚Â¨re peut ÃƒÆ’Ã‚Âªtre bloquÃƒÆ’Ã‚Â© par le schÃƒÆ’Ã‚Â©ma de la base.
- **Mesure dans le futur socle :** identifier chaque livraison par un **tag Git**, une image Docker versionnÃƒÆ’Ã‚Â©e publiÃƒÆ’Ã‚Â©e sur **GHCR** et un identifiant de commit ; exposer la version active sur `GET /health` pour la retrouver en moins de 10 secondes. Conserver la derniÃƒÆ’Ã‚Â¨re image connue comme stable et tester un **rollback applicatif en moins de 5 minutes**. Versionner les migrations, les exÃƒÆ’Ã‚Â©cuter dans une **ÃƒÆ’Ã‚Â©tape dÃƒÆ’Ã‚Â©diÃƒÆ’Ã‚Â©e et contrÃƒÆ’Ã‚Â´lÃƒÆ’Ã‚Â©e du pipeline**, les tester en staging et privilÃƒÆ’Ã‚Â©gier des changements de schÃƒÆ’Ã‚Â©ma rÃƒÆ’Ã‚Â©trocompatibles. Un rollback applicatif ne restaure pas automatiquement les donnÃƒÆ’Ã‚Â©es modifiÃƒÆ’Ã‚Â©es.

## 3. Matrice gravitÃƒÆ’Ã‚Â© ÃƒÆ’Ã¢â‚¬â€ effort

**ÃƒÆ’Ã¢â‚¬Â°chelle de gravitÃƒÆ’Ã‚Â© :** 1 = faible ; 2 = modÃƒÆ’Ã‚Â©rÃƒÆ’Ã‚Â©e ; 3 = importante ; 4 = ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â©e ; 5 = critique.

**ÃƒÆ’Ã¢â‚¬Â°chelle d'effort de traitement :** 1 = trÃƒÆ’Ã‚Â¨s faible ; 2 = faible ; 3 = moyen ; 4 = ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â© ; 5 = trÃƒÆ’Ã‚Â¨s ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â©.

| Risque | GravitÃƒÆ’Ã‚Â© | Effort | Justification du positionnement |
|---|---:|---:|---|
| **R1 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Absence des alternants** | **4/5** | **2/5** | La moitiÃƒÆ’Ã‚Â© de l'ÃƒÆ’Ã‚Â©quipe est absente deux semaines sur quatre : les blocages peuvent ÃƒÆ’Ã‚Âªtre importants. Les passations, petites PR et rÃƒÆ’Ã‚Â¨gles de relecture sont peu coÃƒÆ’Ã‚Â»teuses ÃƒÆ’Ã‚Â  instaurer. |
| **R2 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Push sur `main` sans relecture** | **5/5** | **1/5** | Une erreur peut casser les commandes. La protection de branche et l'exigence d'une approbation demandent principalement de la configuration GitHub. |
| **R3 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â DÃƒÆ’Ã‚Â©ploiement sans tests** | **5/5** | **3/5** | Le risque a dÃƒÆ’Ã‚Â©jÃƒÆ’Ã‚Â  causÃƒÆ’Ã‚Â© 14 heures d'arrÃƒÆ’Ã‚Âªt. ÃƒÆ’Ã¢â‚¬Â°crire les tests, configurer la CI, le staging et la validation de production demande un effort moyen. |
| **R4 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Fuite de secrets** | **5/5** | **2/5** | Une fuite dans un dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t public peut ÃƒÆ’Ã‚Âªtre grave. `.gitignore`, secrets hors Git et dÃƒÆ’Ã‚Â©tection automatisÃƒÆ’Ã‚Â©e sont relativement simples ÃƒÆ’Ã‚Â  mettre en place, mÃƒÆ’Ã‚Âªme si la gestion d'une fuite reste complexe. |
| **R5 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Version, migrations et rollback** | **5/5** | **4/5** | L'absence de version connue prolonge les pannes. La traÃƒÆ’Ã‚Â§abilitÃƒÆ’Ã‚Â© des images, les migrations compatibles et un rollback testÃƒÆ’Ã‚Â© en moins de 5 minutes nÃƒÆ’Ã‚Â©cessitent plusieurs mÃƒÆ’Ã‚Â©canismes coordonnÃƒÆ’Ã‚Â©s. |

```mermaid
quadrantChart
    title GravitÃƒÆ’Ã‚Â© ÃƒÆ’Ã¢â‚¬â€ effort
    x-axis Effort faible --> Effort ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â©
    y-axis GravitÃƒÆ’Ã‚Â© faible --> GravitÃƒÆ’Ã‚Â© ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â©e
    quadrant-1 Chantiers structurants
    quadrant-2 PrioritÃƒÆ’Ã‚Â© immÃƒÆ’Ã‚Â©diate
    quadrant-3 Gains rapides
    quadrant-4 ÃƒÆ’Ã¢â€šÂ¬ planifier
    R2: [0.10, 0.95]
    R4: [0.30, 0.92]
    R1: [0.30, 0.72]
    R3: [0.60, 0.94]
    R5: [0.82, 0.90]
```

La matrice met en ÃƒÆ’Ã‚Â©vidence deux **gains rapides critiques** (R2 et R4), deux **chantiers structurants critiques** (R3 et R5) et un **risque organisationnel ÃƒÆ’Ã‚Â©levÃƒÆ’Ã‚Â©** ÃƒÆ’Ã‚Â  traiter dÃƒÆ’Ã‚Â¨s le dÃƒÆ’Ã‚Â©but (R1).

## 4. Priorisation

1. **R2 et R4 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â SÃƒÆ’Ã‚Â©curiser immÃƒÆ’Ã‚Â©diatement le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t :** protÃƒÆ’Ã‚Â©ger `main` et empÃƒÆ’Ã‚Âªcher la publication de secrets.
2. **R1 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Assurer la continuitÃƒÆ’Ã‚Â© du travail :** mettre en place les passations et une relecture rÃƒÆ’Ã‚Â©alisable avec seulement deux permanents prÃƒÆ’Ã‚Â©sents.
3. **R3 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Fiabiliser les livraisons :** ajouter les tests, le staging et l'approbation de production.
4. **R5 ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â PrÃƒÆ’Ã‚Â©parer la reprise aprÃƒÆ’Ã‚Â¨s incident :** tracer les versions, contrÃƒÆ’Ã‚Â´ler les migrations et dÃƒÆ’Ã‚Â©montrer un rollback en moins de 5 minutes.

## 5. Conclusion

Ces cinq risques dÃƒÆ’Ã‚Â©coulent des pratiques historiques de l'entreprise, de l'incident d'aoÃƒÆ’Ã‚Â»t, des attentes des parties prenantes et de notre carte contexte. Notre futur socle DevOps reposera sur des Pull Requests contrÃƒÆ’Ã‚Â´lÃƒÆ’Ã‚Â©es, des tests automatisÃƒÆ’Ã‚Â©s, une gestion sÃƒÆ’Ã‚Â©curisÃƒÆ’Ã‚Â©e des secrets, une traÃƒÆ’Ã‚Â§abilitÃƒÆ’Ã‚Â© des versions et des procÃƒÆ’Ã‚Â©dures de passation et de rollback. Chaque rÃƒÆ’Ã‚Â¨gle sera reprise et justifiÃƒÆ’Ã‚Â©e dans les documents de stratÃƒÆ’Ã‚Â©gie de branches, de contribution et de pipeline.
