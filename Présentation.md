# TER

## Le but:

Créer un logiciel pour prédire l'ensoleillement pour l'utilisation de panneaux photovoltaïques

## Comment prédire ?

Machine learning

### En quelque mot, c'est quoi le machine learning ?

**Machine learning**: c'est un mécanisme qui permet de prédire une valeur à partir d'un ensemble de données.

## Nos outils

### Python

#### Les librairies

- Sklearn: propose des modèles de machine learning
- Pandas et NumPy: permet de manipuler des données
- Tkinter: permet de créer une interface graphique

### Les données

Date
GHI(Wh/m2)

## Comment ca marche ?

1. on traite nos données pour pouvoir utiliser avec la Sklearn
2. on choisit un modèle: model = RandomForestRegressor()
3. on entraîne le modèle: model.fit(X, y)
4. on obtient un résultat: model.score(X, y)
5. Si le résultat est bon on prédit l'ensoleillement: model.predict(X)
6. sinon on change de modèle

## présentation du logiciel

### structure du logiciel

### mode d'utilisation

## Démonstration
