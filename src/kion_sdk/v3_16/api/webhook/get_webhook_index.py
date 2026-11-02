from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_webhook_index_response_200 import GetWebhookIndexResponse200
from ...models.get_webhook_index_response_401 import GetWebhookIndexResponse401
from ...models.get_webhook_index_response_403 import GetWebhookIndexResponse403
from ...models.get_webhook_index_response_500 import GetWebhookIndexResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/webhook",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetWebhookIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetWebhookIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetWebhookIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetWebhookIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500]:
    """ Returns a list of webhooks from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500]
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

) -> GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500 | None:
    """ Returns a list of webhooks from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500]:
    """ Returns a list of webhooks from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500]
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

) -> GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500 | None:
    """ Returns a list of webhooks from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookIndexResponse200 | GetWebhookIndexResponse401 | GetWebhookIndexResponse403 | GetWebhookIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
