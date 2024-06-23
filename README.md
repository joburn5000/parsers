# PDF Parsing Evaluation Pipeline

## Overview

This repository contains a comprehensive evaluation pipeline for comparing the performance of various PDF parsing systems. The goal is to identify the best PDF parser for extracting tables and handling complex PDF content. The pipeline systematically evaluates multiple parsers using a diverse test dataset and provides detailed metrics to support the decision-making process.

## Installation

To install the necessary components for running the evaluation pipeline, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/joburn5000/parsers.git
    cd parsers
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. [in progress] Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    todo: add requirements.txt, add "You can find all the dependencies listed in the `requirements.txt` file."

## Dependencies

The project relies on the following Python libraries and tools:

- **pdfplumber**
- **Camelot-py**
- **PDFMiner**
(among others)
TODO add all libraries


## Contributing

We welcome contributions to improve the evaluation pipeline and expand its capabilities. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with descriptive messages:
    ```bash
    git commit -m "Description of the feature or fix"
    ```
4. Push your changes to your forked repository:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request to the main repository, describing the changes and the reason for them.

We appreciate your feedback and contributions to this project!
