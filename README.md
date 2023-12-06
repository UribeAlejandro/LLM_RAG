# Clementine - Loka


## Installation

To install the project, run the following command:

```bash
make install
```

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

## Extract, transform, load

The ETL process consists of the following steps:

- `extract`: Reads the files matching the `datasets/raw/*.md` glob pattern.
- `transform`: The documents are split and chunked into a specified length. The chunks are then vectorized using an embedding model.
- `load`: The embeddings are uploaded to a `Pinecone` index.
