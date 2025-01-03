# Configuration for hyperparameter tuning with wandb sweep

sweep_config = {
    "name": "sweepdemo",
    "method": "random",
    "metric": {
        "goal": "minimize", 
        "name": "valid/loss_epoch"
    },
    "parameters": {
        "learning_rate": {
            "distribution": "log_uniform_values",
            "min": 1e-4, 
            "max": 1e-2
        },
        "batch_size": {
            "distribution": "q_log_uniform_values",
            "q": 8,
            "min": 64,
            "max": 256,
        },
        "n_layers": {
            "value": 3
        },
        "n_units": {
            "distribution": "categorical",
            "values": [128],
        },
        "dropout": {
            "distribution": "uniform",
            "min": 0.1,
            "max": 0.4,
        },
    },
    "early_terminate": {
      "type" : "hyperband",
      "min_iter": 3,
      "eta": 3
    }
}