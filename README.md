# Azure FAQ Video Generator

This Python application uses Google to search for the most frequently asked questions related to the Azure portal and generates videos answering these questions. The app automates the process of finding popular queries and producing informative video content.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

## Configuration

Before running the script, you need to configure your Google API credentials and other settings. Create a `.env` file in the root directory and add the following:

```env
GOOGLE_API_KEY=your_google_api_key
CSE_ID=your_custom_search_engine_id
