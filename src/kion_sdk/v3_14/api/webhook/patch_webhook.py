from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_webhook_response_200 import PatchWebhookResponse200
from ...models.patch_webhook_response_400 import PatchWebhookResponse400
from ...models.patch_webhook_response_401 import PatchWebhookResponse401
from ...models.patch_webhook_response_403 import PatchWebhookResponse403
from ...models.patch_webhook_response_404 import PatchWebhookResponse404
from ...models.patch_webhook_response_422 import PatchWebhookResponse422
from ...models.patch_webhook_response_500 import PatchWebhookResponse500
from ...models.webhook_update import WebhookUpdate
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: WebhookUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/webhook/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchWebhookResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchWebhookResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchWebhookResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchWebhookResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchWebhookResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchWebhookResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchWebhookResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500]:
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
    body: WebhookUpdate,

) -> Response[PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500]:
    """ Updates a webhook by ID in the application.

    Args:
        id (int):
        body (WebhookUpdate): WebhookUpdate defines a webhook update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: WebhookUpdate,

) -> PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500 | None:
    """ Updates a webhook by ID in the application.

    Args:
        id (int):
        body (WebhookUpdate): WebhookUpdate defines a webhook update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: WebhookUpdate,

) -> Response[PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500]:
    """ Updates a webhook by ID in the application.

    Args:
        id (int):
        body (WebhookUpdate): WebhookUpdate defines a webhook update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: WebhookUpdate,

) -> PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500 | None:
    """ Updates a webhook by ID in the application.

    Args:
        id (int):
        body (WebhookUpdate): WebhookUpdate defines a webhook update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchWebhookResponse200 | PatchWebhookResponse400 | PatchWebhookResponse401 | PatchWebhookResponse403 | PatchWebhookResponse404 | PatchWebhookResponse422 | PatchWebhookResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
