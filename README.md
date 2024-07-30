# LLM for Research - README

## Overview

This project leverages a Language Learning Model (LLM) to assist researchers by answering questions based on information extracted from 1-3 provided URLs. The user provides the URLs containing the source material, and the LLM processes the content to generate answers to user queries.

## Features

- **URL Input:** Users can input 1-3 URLs containing relevant information.
- **Content Extraction:** The LLM extracts and processes the content from the provided URLs.
- **Question Answering:** Users can ask questions based on the content of the provided URLs, and the LLM will generate responses.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- Pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/llm-research-tool.git
cd llm-research-tool
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

1. **Start the application:**

    ```bash
    python url-llm.py
    ```

2. **Input URLs:**

    You will be prompted to input 1-3 URLs. Ensure the URLs contain the relevant information for your research.

3. **Ask Questions:**

    Once the URLs are processed, you can start asking questions based on the content of the provided URLs.

### Example

```bash
$ python main.py
Please enter up to 3 URLs (comma-separated):
> https://example.com/article1, https://example.com/article2

You can now ask questions based on the provided URLs:
> What is the main conclusion of the first article?
Answer: The main conclusion of the first article is...
```

## Project Structure

- **main.py:** The main script to run the application.
- **requirements.txt:** Contains the list of dependencies.
- **llm_model.py:** Handles the LLM model operations, including loading and querying the model.
- **url_processor.py:** Contains functions for extracting and processing content from URLs.

## Contributing

We welcome contributions to this project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Create a pull request describing your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or feedback, please contact aniketdesh004@gmail.com.

---

Thank you for using LLM for Research! Happy researching!
