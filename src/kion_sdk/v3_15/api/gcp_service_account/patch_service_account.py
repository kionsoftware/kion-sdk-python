from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.google_cloud_service_account_update import GoogleCloudServiceAccountUpdate
from ...models.patch_service_account_response_200 import PatchServiceAccountResponse200
from ...models.patch_service_account_response_400 import PatchServiceAccountResponse400
from ...models.patch_service_account_response_401 import PatchServiceAccountResponse401
from ...models.patch_service_account_response_403 import PatchServiceAccountResponse403
from ...models.patch_service_account_response_404 import PatchServiceAccountResponse404
from ...models.patch_service_account_response_422 import PatchServiceAccountResponse422
from ...models.patch_service_account_response_500 import PatchServiceAccountResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: GoogleCloudServiceAccountUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/gcp/service-account/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchServiceAccountResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchServiceAccountResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchServiceAccountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchServiceAccountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchServiceAccountResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchServiceAccountResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchServiceAccountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500]:
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
    body: GoogleCloudServiceAccountUpdate,

) -> Response[PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500]:
    """ Updates a GCPServiceAccount in the application.

    Args:
        id (int):
        body (GoogleCloudServiceAccountUpdate): GoogleCloudServiceAccountUpdate defines updating a
            Google Cloud service account on cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500]
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
    body: GoogleCloudServiceAccountUpdate,

) -> PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500 | None:
    """ Updates a GCPServiceAccount in the application.

    Args:
        id (int):
        body (GoogleCloudServiceAccountUpdate): GoogleCloudServiceAccountUpdate defines updating a
            Google Cloud service account on cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500
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
    body: GoogleCloudServiceAccountUpdate,

) -> Response[PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500]:
    """ Updates a GCPServiceAccount in the application.

    Args:
        id (int):
        body (GoogleCloudServiceAccountUpdate): GoogleCloudServiceAccountUpdate defines updating a
            Google Cloud service account on cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500]
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
    body: GoogleCloudServiceAccountUpdate,

) -> PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500 | None:
    """ Updates a GCPServiceAccount in the application.

    Args:
        id (int):
        body (GoogleCloudServiceAccountUpdate): GoogleCloudServiceAccountUpdate defines updating a
            Google Cloud service account on cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServiceAccountResponse200 | PatchServiceAccountResponse400 | PatchServiceAccountResponse401 | PatchServiceAccountResponse403 | PatchServiceAccountResponse404 | PatchServiceAccountResponse422 | PatchServiceAccountResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
