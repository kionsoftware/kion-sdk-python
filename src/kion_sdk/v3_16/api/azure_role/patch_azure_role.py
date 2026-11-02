from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_role import AzureRole
from ...models.patch_azure_role_response_200 import PatchAzureRoleResponse200
from ...models.patch_azure_role_response_400 import PatchAzureRoleResponse400
from ...models.patch_azure_role_response_401 import PatchAzureRoleResponse401
from ...models.patch_azure_role_response_403 import PatchAzureRoleResponse403
from ...models.patch_azure_role_response_404 import PatchAzureRoleResponse404
from ...models.patch_azure_role_response_422 import PatchAzureRoleResponse422
from ...models.patch_azure_role_response_500 import PatchAzureRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AzureRole,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/azure-role/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchAzureRoleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchAzureRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAzureRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAzureRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchAzureRoleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchAzureRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchAzureRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500]:
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
    body: AzureRole,

) -> Response[PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500]:
    """ Updates an Azure Role Definition by ID in the application.

    Args:
        id (int):
        body (AzureRole): AzureRole defines an Azure Role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500]
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
    body: AzureRole,

) -> PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500 | None:
    """ Updates an Azure Role Definition by ID in the application.

    Args:
        id (int):
        body (AzureRole): AzureRole defines an Azure Role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500
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
    body: AzureRole,

) -> Response[PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500]:
    """ Updates an Azure Role Definition by ID in the application.

    Args:
        id (int):
        body (AzureRole): AzureRole defines an Azure Role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500]
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
    body: AzureRole,

) -> PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500 | None:
    """ Updates an Azure Role Definition by ID in the application.

    Args:
        id (int):
        body (AzureRole): AzureRole defines an Azure Role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAzureRoleResponse200 | PatchAzureRoleResponse400 | PatchAzureRoleResponse401 | PatchAzureRoleResponse403 | PatchAzureRoleResponse404 | PatchAzureRoleResponse422 | PatchAzureRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
