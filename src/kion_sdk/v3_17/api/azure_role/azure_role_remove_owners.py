from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_role_remove_owners_response_200 import AzureRoleRemoveOwnersResponse200
from ...models.azure_role_remove_owners_response_400 import AzureRoleRemoveOwnersResponse400
from ...models.azure_role_remove_owners_response_401 import AzureRoleRemoveOwnersResponse401
from ...models.azure_role_remove_owners_response_403 import AzureRoleRemoveOwnersResponse403
from ...models.azure_role_remove_owners_response_404 import AzureRoleRemoveOwnersResponse404
from ...models.azure_role_remove_owners_response_422 import AzureRoleRemoveOwnersResponse422
from ...models.azure_role_remove_owners_response_500 import AzureRoleRemoveOwnersResponse500
from ...models.policy_owners import PolicyOwners
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PolicyOwners,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/azure-role/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = AzureRoleRemoveOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = AzureRoleRemoveOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = AzureRoleRemoveOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = AzureRoleRemoveOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = AzureRoleRemoveOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = AzureRoleRemoveOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = AzureRoleRemoveOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500]:
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
    body: PolicyOwners,

) -> Response[AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the Azure Role Definition in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500]
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
    body: PolicyOwners,

) -> AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the Azure Role Definition in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500
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
    body: PolicyOwners,

) -> Response[AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the Azure Role Definition in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500]
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
    body: PolicyOwners,

) -> AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the Azure Role Definition in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AzureRoleRemoveOwnersResponse200 | AzureRoleRemoveOwnersResponse400 | AzureRoleRemoveOwnersResponse401 | AzureRoleRemoveOwnersResponse403 | AzureRoleRemoveOwnersResponse404 | AzureRoleRemoveOwnersResponse422 | AzureRoleRemoveOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
