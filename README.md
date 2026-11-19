# Projet DevOps ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Start-up Producteurs & Consommateurs

## ÃƒÂ°Ã…Â¸Ã¢â‚¬Å“Ã¢â‚¬Â¡ Carte Contexte tirÃƒÆ’Ã‚Â©e
* **Composition de l'ÃƒÆ’Ã‚Â©quipe :** 2 dÃƒÆ’Ã‚Â©veloppeurs permanents + 2 alternants (prÃƒÆ’Ã‚Â©sents 2 semaines sur 4).
* **Contrainte d'effectif :** Les semaines de formation, seuls les 2 permanents assurent la production et les revues.
* **Parties prenantes :**
  * **La CEO :** Exige zÃƒÆ’Ã‚Â©ro panne majeure (plus jamais un incident comme celui d'aoÃƒÆ’Ã‚Â»t avec 14h de coupure).
  * **Le Product Owner :** Veut des livraisons rapides et frÃƒÆ’Ã‚Â©quentes pour satisfaire les restaurateurs.
  * **La Lead Dev :** S'inquiÃƒÆ’Ã‚Â¨te du temps passÃƒÆ’Ã‚Â© en relecture de code dans une petite ÃƒÆ’Ã‚Â©quipe.
  * **Le DÃƒÆ’Ã‚Â©veloppeur Freelance :** PayÃƒÆ’Ã‚Â© ÃƒÆ’Ã‚Â  l'heure, refuse d'attendre passivement les revues de code.

---

## ÃƒÂ°Ã…Â¸Ã…Â¡Ã¢â€šÂ¬ DÃƒÆ’Ã‚Â©marrage rapide en local

```bash
# Cloner le dÃƒÆ’Ã‚Â©pÃƒÆ’Ã‚Â´t
git clone https://github.com/laetitia0218/projet_devops.git
cd projet_devops

# Lancer la stack (API + Base de donnÃƒÆ’Ã‚Â©es PostgreSQL)
docker-compose up --build
```

L'API est accessible sur `http://localhost:8000` (route de santÃƒÆ’Ã‚Â© : `http://localhost:8000/health`).

---

## ÃƒÂ°Ã…Â¸Ã¢â‚¬Å“Ã…Â¡ Documentation du projet
* [Analyse des risques (T1)](docs/risques.md)
* [StratÃƒÆ’Ã‚Â©gie de branches (T2)](docs/adr/0001-strategie-branches.md)
* [RÃƒÆ’Ã‚Â¨gles de contribution et gestion (T3)](CONTRIBUTING.md)
* [Configuration GitHub (T3)](docs/config/README.md)
