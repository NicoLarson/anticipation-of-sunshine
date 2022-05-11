# Projet TER - L3 Informatique

## Le but du projet:

Créer un programme pour prédire l'ensoleillement grace à un modèle de machine learning.

## Installation des dépendances

```bash
pip install -r requirements.txt
```

## Démarrage du projet

```bash
python main.py
```

## Les modèles:

[List des modèles](https://scikit-learn.org/stable/index.html)

- [x] Linear Regression
- [x] svr
- [x] linear lasso

### Ajouter un modèle

Dans le fichier `modules/models.py`, ajouter:

```python
def nouveau_model(X_fit, Y_fit, X_predict, Y_predict):
    model = nouveau_model()
    fit = model.fit(X_fit, Y_fit)
    score_predict = model.score(X_predict, Y_predict)
    score_fit = fit.score(X_fit, Y_fit)
    return [score_predict, score_fit]
```

> A faire: système pour ajouter un modèle

## Fonctionnalité du programme

- Importer un fichier `csv` exemple dans `datas_test`
- Choisir si on veut faire un traitement avec clusters ou pas
- Choisir le modèle à utiliser
- Executer le traitement
- Affichage du résultat
