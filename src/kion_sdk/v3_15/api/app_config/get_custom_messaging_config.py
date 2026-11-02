from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_custom_messaging_config_response_200 import GetCustomMessagingConfigResponse200
from ...models.get_custom_messaging_config_response_401 import GetCustomMessagingConfigResponse401
from ...models.get_custom_messaging_config_response_403 import GetCustomMessagingConfigResponse403
from ...models.get_custom_messaging_config_response_500 import GetCustomMessagingConfigResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-config/custom-messaging",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCustomMessagingConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCustomMessagingConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCustomMessagingConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetCustomMessagingConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500]:
    """ Gets the custom messaging config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500]
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

) -> GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500 | None:
    """ Gets the custom messaging config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500]:
    """ Gets the custom messaging config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500]
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

) -> GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500 | None:
    """ Gets the custom messaging config settings

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCustomMessagingConfigResponse200 | GetCustomMessagingConfigResponse401 | GetCustomMessagingConfigResponse403 | GetCustomMessagingConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
