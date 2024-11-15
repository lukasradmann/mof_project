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
            "max": 1e-1
        },
        "batch_size": {
            "distribution": "q_log_uniform_values",
            "q": 8,
            "min": 32,
            "max": 256,
        },
        "n_layers": {
            "distribution": "int_uniform",
            "min": 2,
            "max": 4,
        },
        "n_units": {
            "distribution": "categorical",
            "values": [32, 64, 128],
        },
        "dropout": {
            "distribution": "uniform",
            "min": 0.2,
            "max": 0.5,
        }
    },
}