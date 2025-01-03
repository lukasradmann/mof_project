# Finding Metal Organic Frameworks for separating greenhouse gases

## Table of Contents

- [Project Structure](#project-structure)
- [Pre-requisites](#pre-requisites)
- [Installation](#pre-requisites)
## Project Structure

```

├── README.md                     <- The top-level README for developers using this project.
├── .gitignore                    <- The top-level README for developers using this project.
│
├── autogluon
│   ├── AutogluonModels           <- Saved autogluon models and generated reports.
│   ├── autogluon.py              <- Code for training an autogluon model.
│   └── requirements.txt          <- Required dependencies.
│
├── data
│   ├── preprocessing.ipynb       <- Code for preprocessing original dataset
│   ├── processed_MOFs.csv        <- Intermediate data that has been transformed.
│   ├── val_MOFs.csv              <- The final validation set.
│   ├── test_MOFs.csv             <- The final test set.
│   ├── train_MOFs.csv            <- The final training set.
│   └── requirements.txt          <- Required dependencies.
│
├── gcn
│   ├── gcn.ipynb                 <- Code for training graph neural network.
│   └── requirements.txt          <- Required dependencies.
│
├── neuralnet
│   ├── nn.ipynb                  <- Code for training neural network.
│   ├── sweep_config.py           <- Configurations for the hyperparameter search space.
│   └── requirements.txt          <- Intermediate data that has been transformed.
│
└──scikit
    ├── feature_engineering.ipynb <- Code for feature engineering.
    ├── model_selection.ipynb     <- Code for regression model selection.
    └── requirements.txt          <- Required dependencies.
```

## Pre-requisites

Before you begin, ensure you have met the following requirements:

- **Python**: Make sure you have Python installed.
- **Weights & Biases Account**: To train a neural network you need to create an account on Weights & Biases (W&B) for experiment tracking and logging.
- **CIF-file dataset for GCN**: To train a graph neural network you will need to download the CIF-file dataset form the following link https://archive.materialscloud.org/record/2018.0016/v3 and use it in the code in /gcn/gcn.ipynb

## Installation

Before running any script in a given folder, install the required packages using the following command:

```sh
pip install -r requirements.txt
```
--------

