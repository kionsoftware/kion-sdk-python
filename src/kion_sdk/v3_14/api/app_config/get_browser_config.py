from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_browser_config_response_200 import GetBrowserConfigResponse200
from ...models.get_browser_config_response_401 import GetBrowserConfigResponse401
from ...models.get_browser_config_response_403 import GetBrowserConfigResponse403
from ...models.get_browser_config_response_500 import GetBrowserConfigResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-config/browser",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBrowserConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetBrowserConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBrowserConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetBrowserConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500]:
    """ Gets the browser config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500 | None:
    """ Gets the browser config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500]:
    """ Gets the browser config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500 | None:
    """ Gets the browser config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBrowserConfigResponse200 | GetBrowserConfigResponse401 | GetBrowserConfigResponse403 | GetBrowserConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
