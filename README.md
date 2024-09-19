# Rick and Morty API Integration

This Python project integrates with the Rick and Morty API to fetch and process data about characters, locations, and episodes. It demonstrates asynchronous API calls and data handling using Python's `aiohttp` library.

## Project Structure

- `rick_and_morty_client.py`: Contains the asynchronous API client class for interacting with the Rick and Morty API.
- `sample_app.py`: A sample application that uses the client module to fetch data and save it in separate JSON files.

## Features

- Asynchronous API requests.
- Pagination handling to fetch all available data.
- Data is saved into JSON files with a specific structure.
- Filtering and listing of episodes based on the air date.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://your-repository-url.git
   cd rick_and_morty_api_integration
   ```
   
2. **Install the Required Libraries**  
   * Install the poetry if needed:
      ```bash
      poetry install
      ```
   * Install requirements:
      ```bash
       poetry install
      ```

3. **Run the Sample Application**
   ```bash
    poetry run python sample_app.py
    ```
   
