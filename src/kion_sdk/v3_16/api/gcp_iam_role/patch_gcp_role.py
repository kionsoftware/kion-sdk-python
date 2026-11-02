from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_role_update import GCPRoleUpdate
from ...models.patch_gcp_role_response_200 import PatchGCPRoleResponse200
from ...models.patch_gcp_role_response_400 import PatchGCPRoleResponse400
from ...models.patch_gcp_role_response_401 import PatchGCPRoleResponse401
from ...models.patch_gcp_role_response_403 import PatchGCPRoleResponse403
from ...models.patch_gcp_role_response_404 import PatchGCPRoleResponse404
from ...models.patch_gcp_role_response_422 import PatchGCPRoleResponse422
from ...models.patch_gcp_role_response_500 import PatchGCPRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: GCPRoleUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/gcp-iam-role/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchGCPRoleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchGCPRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchGCPRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchGCPRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchGCPRoleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchGCPRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchGCPRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500]:
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
    body: GCPRoleUpdate,

) -> Response[PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500]:
    """ Updates an existing GCPIAMRole in the application.

    Args:
        id (int):
        body (GCPRoleUpdate): GCPRoleUpdate defines an GCP Role Definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500]
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
    body: GCPRoleUpdate,

) -> PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500 | None:
    """ Updates an existing GCPIAMRole in the application.

    Args:
        id (int):
        body (GCPRoleUpdate): GCPRoleUpdate defines an GCP Role Definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500
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
    body: GCPRoleUpdate,

) -> Response[PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500]:
    """ Updates an existing GCPIAMRole in the application.

    Args:
        id (int):
        body (GCPRoleUpdate): GCPRoleUpdate defines an GCP Role Definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500]
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
    body: GCPRoleUpdate,

) -> PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500 | None:
    """ Updates an existing GCPIAMRole in the application.

    Args:
        id (int):
        body (GCPRoleUpdate): GCPRoleUpdate defines an GCP Role Definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchGCPRoleResponse200 | PatchGCPRoleResponse400 | PatchGCPRoleResponse401 | PatchGCPRoleResponse403 | PatchGCPRoleResponse404 | PatchGCPRoleResponse422 | PatchGCPRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
