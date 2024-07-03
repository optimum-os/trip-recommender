# Projet Trip Recommender

L'objectif de l’application est de recommander des destinations avec les détails de voyage (prix vol, hotels) en fonction des préférences et des critères de l'utilisateur.

**Input de l’utilisateur**

- Ville de Départ
- Prix (budget) : vol + hotel
- Date Début/Fin exacte ou choisir les mois
- Distance :
 - Avec escale, sans escale
 - Heures de transport
- Thèmes
  - Plage, famille, Ski, golf

---

- Chercher des dataset existant/Scraping des données.
   - [x] Il faut des données des villes, vols et des hôtels.

- Algorithmes
  - Parties ML pour prédire les destinations.
    - Prédire le coût de séjour en parcourant chaque destination
      - [x] créer un modèle ML pour prédire le coût de Vol
      - [x] créer un modèle ML pour prédire le coût d'Hôtel
  - Sortir les destinations correspondant aux critères de l'utilisateur.
    - budget, distance, thèmes