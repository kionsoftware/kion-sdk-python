from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.reset_webhook_delete_response_200 import ResetWebhookDeleteResponse200
from ...models.reset_webhook_delete_response_400 import ResetWebhookDeleteResponse400
from ...models.reset_webhook_delete_response_401 import ResetWebhookDeleteResponse401
from ...models.reset_webhook_delete_response_403 import ResetWebhookDeleteResponse403
from ...models.reset_webhook_delete_response_500 import ResetWebhookDeleteResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/webhook-delete-state/{id}/reset".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500 | None:
    if response.status_code == 200:
        response_200 = ResetWebhookDeleteResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ResetWebhookDeleteResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ResetWebhookDeleteResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ResetWebhookDeleteResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = ResetWebhookDeleteResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500]:
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

) -> Response[ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500]:
    """ Resets the state of a webhook delete in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500]
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

) -> ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500 | None:
    """ Resets the state of a webhook delete in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500]:
    """ Resets the state of a webhook delete in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500]
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

) -> ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500 | None:
    """ Resets the state of a webhook delete in an account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResetWebhookDeleteResponse200 | ResetWebhookDeleteResponse400 | ResetWebhookDeleteResponse401 | ResetWebhookDeleteResponse403 | ResetWebhookDeleteResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
