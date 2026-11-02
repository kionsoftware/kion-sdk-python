from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.google_cloud_service_account_key_update import GoogleCloudServiceAccountKeyUpdate
from ...models.patch_service_account_key_response_200 import PatchServiceAccountKeyResponse200
from ...models.patch_service_account_key_response_401 import PatchServiceAccountKeyResponse401
from ...models.patch_service_account_key_response_403 import PatchServiceAccountKeyResponse403
from ...models.patch_service_account_key_response_404 import PatchServiceAccountKeyResponse404
from ...models.patch_service_account_key_response_500 import PatchServiceAccountKeyResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: GoogleCloudServiceAccountKeyUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/gcp/service-account/{id}/key".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchServiceAccountKeyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PatchServiceAccountKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchServiceAccountKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchServiceAccountKeyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PatchServiceAccountKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500]:
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
    body: GoogleCloudServiceAccountKeyUpdate,

) -> Response[PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500]:
    """ Updates the key associated to the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyUpdate): GoogleCloudServiceAccountKeyUpdate defines
            updating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500]
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
    body: GoogleCloudServiceAccountKeyUpdate,

) -> PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500 | None:
    """ Updates the key associated to the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyUpdate): GoogleCloudServiceAccountKeyUpdate defines
            updating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500
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
    body: GoogleCloudServiceAccountKeyUpdate,

) -> Response[PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500]:
    """ Updates the key associated to the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyUpdate): GoogleCloudServiceAccountKeyUpdate defines
            updating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500]
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
    body: GoogleCloudServiceAccountKeyUpdate,

) -> PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500 | None:
    """ Updates the key associated to the specified gcp service account.

    Args:
        id (int):
        body (GoogleCloudServiceAccountKeyUpdate): GoogleCloudServiceAccountKeyUpdate defines
            updating a key attached to a google cloud service account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServiceAccountKeyResponse200 | PatchServiceAccountKeyResponse401 | PatchServiceAccountKeyResponse403 | PatchServiceAccountKeyResponse404 | PatchServiceAccountKeyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
