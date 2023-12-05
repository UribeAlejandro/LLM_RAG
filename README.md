# Clementine - Loka


## Data

The data is stored in the `datasets` folder. The data is stored in the following format:

```
datasets
├── raw
│   └── ...
├── interim
│   └── ...
└── processed
    └── ...
```

The `raw` folder contains the raw data. The `interim` folder contains the data after it has been cleaned. The `processed` folder contains the data after it has been processed and is ready for use in a model.

The data can be pulled from remote using the following command:

```bash
dvc pull
```

