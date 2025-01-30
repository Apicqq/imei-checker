import aiohttp


class HttpClient:
    """Client to persist opened aiohttp session."""

    session: aiohttp.ClientSession = None

    def start(self):
        """Start aiohttp session."""
        self.session = aiohttp.ClientSession()

    async def stop(self):
        """Close aiohttp session."""
        await self.session.close()
        self.session = None

    def __call__(self) -> aiohttp.ClientSession:
        """Return aiohttp session when called."""
        assert self.session is not None
        return self.session
