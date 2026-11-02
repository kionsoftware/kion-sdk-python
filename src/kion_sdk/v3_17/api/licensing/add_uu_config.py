from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.add_uu_config_response_201 import AddUUConfigResponse201
from ...models.add_uu_config_response_400 import AddUUConfigResponse400
from ...models.add_uu_config_response_422 import AddUUConfigResponse422
from ...models.add_uu_config_response_500 import AddUUConfigResponse500
from ...models.usage_unit_config import UsageUnitConfig
from typing import cast



def _get_kwargs(
    *,
    body: UsageUnitConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/license/usage-unit",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500 | None:
    if response.status_code == 201:
        response_201 = AddUUConfigResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = AddUUConfigResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 422:
        response_422 = AddUUConfigResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = AddUUConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UsageUnitConfig,

) -> Response[AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500]:
    """ Adds a usage unit to the application.

    Args:
        body (UsageUnitConfig): UsageUnitConfig contains a usage unit key to be added to the
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: UsageUnitConfig,

) -> AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500 | None:
    """ Adds a usage unit to the application.

    Args:
        body (UsageUnitConfig): UsageUnitConfig contains a usage unit key to be added to the
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UsageUnitConfig,

) -> Response[AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500]:
    """ Adds a usage unit to the application.

    Args:
        body (UsageUnitConfig): UsageUnitConfig contains a usage unit key to be added to the
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UsageUnitConfig,

) -> AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500 | None:
    """ Adds a usage unit to the application.

    Args:
        body (UsageUnitConfig): UsageUnitConfig contains a usage unit key to be added to the
            application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddUUConfigResponse201 | AddUUConfigResponse400 | AddUUConfigResponse422 | AddUUConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
