# Hugging Face Daily Papers summarizer

## Overview

This thing utomates the process of downloading academic papers from arXiv based on titles of Hugging Face daily papers, converting these papers into text, and then using a large language model to generate summaries of the papers' contents. It's designed to be a comprehensive tool for researchers and students looking to stay up-to-date with the latest developments in fields such as Artificial Intelligence, Machine Learning, and Large Language Models.

## Dependencies

To run this script, you need to have the following Python packages installed:

- `os`
- `time`
- `arxiv`
- `langchain_community` (including `vectorstores`, `document_loaders`, `chat_models`)
- `langchain` (including `prompts`, `pydantic_v1`, `schema`)
- `json`
- `requests`
- `datetime`
- `PyPDF2`

These dependencies can be installed via pip:

```bash
pip install os time arxiv langchain_community langchain json requests datetime PyPDF2
```

Note: Ensure you have the latest versions of these packages to avoid compatibility issues.

## Usage

1. **Set Up**: Before running the script, ensure you have set up your environment variables correctly, especially the `pplx_key` variable, which is required for authentication with the Perplexity API.

2. **Running the Script**: Execute the script by running:

   ```bash
   python main.py
   ```

   This will trigger the download of papers from the previous day, convert them into text, and generate summaries using the specified large language model.

## Functions

### `get_yesterday_date()`

Returns the date of the previous day in the format `YYYY-MM-DD`.

### `get_daily_papers()`

Fetches daily papers from Hugging Face's API and returns the raw JSON response.

### `get_paper_titles()`

Extracts the titles of the papers fetched by `get_daily_papers()` and prints them out.

### `save_papers(dirpath)`

Downloads and saves the papers related to the titles obtained from `get_paper_titles()` into the specified directory.

### `papers_to_text(dirpath)`

Converts the downloaded papers into text format and concatenates them into a single string.

### `llm_talkr(papers_text)`

Generates summaries of the papers' contents using a large language model and returns the summarized text.

### `main()`

The main function orchestrates the entire process, including creating directories for storing papers, saving papers, converting them to text, and generating summaries.

## Contributing

Contributions to this project are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
