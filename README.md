# Hugging Face Daily Papers summarizer

This repository contains the source code for a Telegram bot designed to fetch, summarize, and deliver daily research papers from Hugging Face's Daily Papers API. The bot uses several libraries including `requests`, `json`, `telebot` for Telegram interactions, `schedule` for scheduling tasks, and `arxiv` for fetching academic papers.

## Overview

The bot performs the following operations:

- Fetches daily papers from Hugging Face's Daily Papers API based on the previous day's date.
- Searches for related papers on arXiv using the titles fetched from Hugging Face.
- Downloads and saves these papers locally.
- Converts the PDFs of these papers into plain text.
- Uses the Perplexity AI model (`llama-3.1-70b-instruct`) to generate a summary of the papers' contents.
- Schedules a daily reminder to send the summarized papers to subscribed users via Telegram.
- Updates a database with new subscribers and sends them the daily summary upon subscribing.

## Prerequisites

Before running the bot, ensure you have Python installed on your system. You will also need to install the required Python packages listed in the `requirements.txt` file. Additionally, you must obtain an API key for both Hugging Face and Perplexity AI, which should be stored in environment variables or directly in the script as placeholders.

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Obtain API keys for Hugging Face and Perplexity AI and replace the placeholders in the script with your actual keys.
4. Ensure you have a Telegram bot token; create one through the BotFather on Telegram if necessary.
5. Update the bot token in the script with your Telegram bot token.

## Usage

To run the bot, execute the script using Python:

```bash
python hf_daily_papers_bot.py
```

### Commands

- `/start`: Subscribes the user to receive daily summaries and sends them the latest summary.

### Scheduling and Notifications

The bot schedules a daily task at 14:00 UTC to send out the daily summaries to all subscribed users. It checks for new subscriptions and updates its internal database accordingly.

## Contributing

Contributions to improve the bot's functionality, efficiency, or user experience are welcome. Please submit pull requests or issues detailing your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
