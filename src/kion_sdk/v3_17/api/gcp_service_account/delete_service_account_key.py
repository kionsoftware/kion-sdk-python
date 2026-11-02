from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_service_account_key_response_200 import DeleteServiceAccountKeyResponse200
from ...models.delete_service_account_key_response_401 import DeleteServiceAccountKeyResponse401
from ...models.delete_service_account_key_response_403 import DeleteServiceAccountKeyResponse403
from ...models.delete_service_account_key_response_404 import DeleteServiceAccountKeyResponse404
from ...models.delete_service_account_key_response_500 import DeleteServiceAccountKeyResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/gcp/service-account/{id}/key".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteServiceAccountKeyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteServiceAccountKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteServiceAccountKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteServiceAccountKeyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteServiceAccountKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500]:
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

) -> Response[DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500]:
    """ Deletes key associated to the specified gcp service account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500]
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

) -> DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500 | None:
    """ Deletes key associated to the specified gcp service account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500]:
    """ Deletes key associated to the specified gcp service account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500]
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

) -> DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500 | None:
    """ Deletes key associated to the specified gcp service account.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteServiceAccountKeyResponse200 | DeleteServiceAccountKeyResponse401 | DeleteServiceAccountKeyResponse403 | DeleteServiceAccountKeyResponse404 | DeleteServiceAccountKeyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
