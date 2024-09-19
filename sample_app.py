import asyncio
import json
import uuid
from typing import List, Dict
from rick_and_morty_client import RickAndMortyClient


async def main():
    client = RickAndMortyClient()

    characters = await client.get_all_characters()
    locations = await client.get_all_locations()
    episodes = await client.get_all_episodes()

    await asyncio.gather(
        save_data_to_json('characters.json', characters),
        save_data_to_json('locations.json', locations),
        save_data_to_json('episodes.json', episodes)
    )

    print("\nEpisodes aired between 2017 and 2021:")
    print_episodes_between(episodes, 2017, 2021)


async def save_data_to_json(filename: str, data: List[Dict]):
    """Save data to a JSON file with the specified structure."""
    output = [
        {
            "id": str(uuid.uuid4()),
            "RawData": item
        }
        for item in data
    ]

    # Write to file asynchronously
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, write_json_file, filename, output)


def write_json_file(filename: str, data):
    """Write data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def print_episodes_between(episodes: List[Dict], start_year: int, end_year: int):
    """Print episode names that aired between the specified years."""
    for episode in episodes:
        air_date = episode.get('air_date', '')
        if air_date:
            try:
                air_year = int(air_date.split()[-1])
                if start_year <= air_year <= end_year:
                    print(f"- {episode['name']}")
            except ValueError:
                continue


if __name__ == '__main__':
    asyncio.run(main())
