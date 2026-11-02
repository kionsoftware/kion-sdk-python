from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.webhook_owners import WebhookOwners
from ...models.webhook_remove_owners_response_200 import WebhookRemoveOwnersResponse200
from ...models.webhook_remove_owners_response_400 import WebhookRemoveOwnersResponse400
from ...models.webhook_remove_owners_response_401 import WebhookRemoveOwnersResponse401
from ...models.webhook_remove_owners_response_403 import WebhookRemoveOwnersResponse403
from ...models.webhook_remove_owners_response_404 import WebhookRemoveOwnersResponse404
from ...models.webhook_remove_owners_response_422 import WebhookRemoveOwnersResponse422
from ...models.webhook_remove_owners_response_500 import WebhookRemoveOwnersResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: WebhookOwners | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/webhook/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = WebhookRemoveOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = WebhookRemoveOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = WebhookRemoveOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = WebhookRemoveOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = WebhookRemoveOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = WebhookRemoveOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = WebhookRemoveOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500]:
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

) -> Response[WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500]
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

) -> WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500
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

) -> Response[WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500]
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

) -> WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the webhook in the application.

    Args:
        id (int):
        body (WebhookOwners | Unset): WebhookOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookRemoveOwnersResponse200 | WebhookRemoveOwnersResponse400 | WebhookRemoveOwnersResponse401 | WebhookRemoveOwnersResponse403 | WebhookRemoveOwnersResponse404 | WebhookRemoveOwnersResponse422 | WebhookRemoveOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
