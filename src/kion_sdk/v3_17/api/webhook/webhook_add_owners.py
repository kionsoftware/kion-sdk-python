from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.webhook_add_owners_response_200 import WebhookAddOwnersResponse200
from ...models.webhook_add_owners_response_400 import WebhookAddOwnersResponse400
from ...models.webhook_add_owners_response_401 import WebhookAddOwnersResponse401
from ...models.webhook_add_owners_response_403 import WebhookAddOwnersResponse403
from ...models.webhook_add_owners_response_404 import WebhookAddOwnersResponse404
from ...models.webhook_add_owners_response_422 import WebhookAddOwnersResponse422
from ...models.webhook_add_owners_response_500 import WebhookAddOwnersResponse500
from ...models.webhook_owners import WebhookOwners
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: WebhookOwners | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/webhook/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = WebhookAddOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = WebhookAddOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = WebhookAddOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = WebhookAddOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = WebhookAddOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = WebhookAddOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = WebhookAddOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500]:
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
    body: WebhookOwners | Unset = UNSET,

) -> Response[WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500]:
    """ Adds users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500]
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
    body: WebhookOwners | Unset = UNSET,

) -> WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500 | None:
    """ Adds users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500
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
    body: WebhookOwners | Unset = UNSET,

) -> Response[WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500]:
    """ Adds users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500]
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
    body: WebhookOwners | Unset = UNSET,

) -> WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500 | None:
    """ Adds users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookAddOwnersResponse200 | WebhookAddOwnersResponse400 | WebhookAddOwnersResponse401 | WebhookAddOwnersResponse403 | WebhookAddOwnersResponse404 | WebhookAddOwnersResponse422 | WebhookAddOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
