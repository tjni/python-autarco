# pylint: disable=W0621
"""Asynchronous Python client for the Autarco API."""

import asyncio

from autarco import Autarco


async def main() -> None:
    """Show example on getting Autarco - account data."""
    async with Autarco(  # noqa: S106
        email="test@autarco.com",
        password="password",
    ) as client:
        public_key = await client.get_public_key()
        account = await client.account(public_key)
        print(account)


if __name__ == "__main__":
    asyncio.run(main())
