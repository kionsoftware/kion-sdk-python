from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.end_webhook_delete_response_200 import EndWebhookDeleteResponse200
from ...models.end_webhook_delete_response_400 import EndWebhookDeleteResponse400
from ...models.end_webhook_delete_response_401 import EndWebhookDeleteResponse401
from ...models.end_webhook_delete_response_403 import EndWebhookDeleteResponse403
from ...models.end_webhook_delete_response_500 import EndWebhookDeleteResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/webhook-delete-state/{id}/end".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500 | None:
    if response.status_code == 200:
        response_200 = EndWebhookDeleteResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = EndWebhookDeleteResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = EndWebhookDeleteResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = EndWebhookDeleteResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = EndWebhookDeleteResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500]:
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

) -> Response[EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500]:
    """ Mark the webhook delete as completed for the account/cloud rule/webhook/type.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500]
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

) -> EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500 | None:
    """ Mark the webhook delete as completed for the account/cloud rule/webhook/type.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500]:
    """ Mark the webhook delete as completed for the account/cloud rule/webhook/type.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500]
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

) -> EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500 | None:
    """ Mark the webhook delete as completed for the account/cloud rule/webhook/type.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EndWebhookDeleteResponse200 | EndWebhookDeleteResponse400 | EndWebhookDeleteResponse401 | EndWebhookDeleteResponse403 | EndWebhookDeleteResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
