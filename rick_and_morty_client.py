import asyncio
import aiohttp
from typing import List, Dict


class RickAndMortyClient:
    BASE_URL = 'https://rickandmortyapi.com/api'

    async def fetch_all(self, endpoint: str) -> List[Dict]:
        """Fetch all items from a given endpoint asynchronously."""
        results = []
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.BASE_URL}/{endpoint}') as response:
                data = await response.json()
                results.extend(data['results'])
                total_pages = data['info']['pages']

            tasks = [
                self.fetch_page(session, f'{self.BASE_URL}/{endpoint}?page={page}')
                for page in range(2, total_pages + 1)
            ]

            pages_data = await asyncio.gather(*tasks)
            for page_results in pages_data:
                results.extend(page_results)

        return results

    async def fetch_page(self, session: aiohttp.ClientSession, url: str) -> List[Dict]:
        """Fetch a single page of results."""
        async with session.get(url) as response:
            data = await response.json()
            return data['results']

    async def get_all_characters(self) -> List[Dict]:
        """Get all characters."""
        return await self.fetch_all('character')

    async def get_all_locations(self) -> List[Dict]:
        """Get all locations."""
        return await self.fetch_all('location')

    async def get_all_episodes(self) -> List[Dict]:
        """Get all episodes."""
        return await self.fetch_all('episode')
