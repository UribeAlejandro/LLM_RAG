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
├── test
│   └── ...
├── raw
│   └── ...
├── interim
│   └── ...
└── processed
    └── ...
```

The `raw` folder contains the raw data. The `interim` folder contains the data after it has been cleaned. The `processed` folder contains the data after it has been processed and is ready for use in a model. The `test` folder contains the data used for testing.

The data can be pulled from remote using the following command:

```bash
dvc pull
```

The data for testing can be pulled from remote using the following command:

```bash
dvc pull datasets/test
```

## Extract, transform, load

The ETL process consists of the following steps:

- `extract`: Reads the files matching the `datasets/raw/*.md` glob pattern.
- `transform`: The documents are split and chunked into a specified length. The chunks are then vectorized using the GPT4All embedding model.
- `load`: The embeddings are uploaded to a `Pinecone` index.

## Model experiments

Models are pre-trained, open-sourced and can be accessed using the `GPT4All` library. The model experiments and evaluation are logged in the MLFlow server. Two models were evaluated:

- `orca-mini-3b-gguf2-q4_0`: This model requires a machine with 4GB of RAM and its weights are about 1.84GB.
- `gpt4all-falcon-q4_0`: This model requires a machine with 8GB of RAM and its weights are about 3.92GB.

Further information about the models can be found in [GPT4All](https://gpt4all.io/index.html).

The models where evaluated using some example queries related to the content of the documents:

- What is SageMaker?
- What are all AWS regions where SageMaker is available?
- How to check if an endpoint is KMS encrypted?
- What are SageMaker Geospatial capabilities?

The following metrics were used to evaluate the models:

- `Latency`: The time it takes to get a response from the model.
- `Toxicity`: The toxicity of the response. It regards hate speech, offensive language, insults, and profanity.
- `ARI grade`: The ARI grade of the response. It regards the readability of the response. This test indicates the grade level at which readers can understand the text.
- `Flesch-Kincaid grade`: The Flesch-Kincaid grade of the response. It regards the readability, it is a test designed to indicate how difficult a passage in English is to understand
- `Output`: The output of the model. It is not a metric, but it is used to evaluate the quality of the response.

The `GPT falcon` model performed better than the `Orca model` in all metrics, but latency. The `GPT falcon` model was chosen to be used in the application.
