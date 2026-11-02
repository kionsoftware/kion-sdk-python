from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_webhook_delete_state_response_200 import GetAccountWebhookDeleteStateResponse200
from ...models.get_account_webhook_delete_state_response_400 import GetAccountWebhookDeleteStateResponse400
from ...models.get_account_webhook_delete_state_response_401 import GetAccountWebhookDeleteStateResponse401
from ...models.get_account_webhook_delete_state_response_403 import GetAccountWebhookDeleteStateResponse403
from ...models.get_account_webhook_delete_state_response_500 import GetAccountWebhookDeleteStateResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/webhook-delete-state/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountWebhookDeleteStateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAccountWebhookDeleteStateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAccountWebhookDeleteStateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAccountWebhookDeleteStateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAccountWebhookDeleteStateResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500]:
    """ Gets the state of a webhook delete in an account. Will effectively start a delete.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500 | None:
    """ Gets the state of a webhook delete in an account. Will effectively start a delete.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500]:
    """ Gets the state of a webhook delete in an account. Will effectively start a delete.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500 | None:
    """ Gets the state of a webhook delete in an account. Will effectively start a delete.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountWebhookDeleteStateResponse200 | GetAccountWebhookDeleteStateResponse400 | GetAccountWebhookDeleteStateResponse401 | GetAccountWebhookDeleteStateResponse403 | GetAccountWebhookDeleteStateResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
