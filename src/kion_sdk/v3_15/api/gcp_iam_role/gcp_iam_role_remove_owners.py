from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_iam_role_remove_owners_response_200 import GcpIAMRoleRemoveOwnersResponse200
from ...models.gcp_iam_role_remove_owners_response_400 import GcpIAMRoleRemoveOwnersResponse400
from ...models.gcp_iam_role_remove_owners_response_401 import GcpIAMRoleRemoveOwnersResponse401
from ...models.gcp_iam_role_remove_owners_response_403 import GcpIAMRoleRemoveOwnersResponse403
from ...models.gcp_iam_role_remove_owners_response_404 import GcpIAMRoleRemoveOwnersResponse404
from ...models.gcp_iam_role_remove_owners_response_422 import GcpIAMRoleRemoveOwnersResponse422
from ...models.gcp_iam_role_remove_owners_response_500 import GcpIAMRoleRemoveOwnersResponse500
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
        "url": "/v3/gcp-iam-role/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = GcpIAMRoleRemoveOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GcpIAMRoleRemoveOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GcpIAMRoleRemoveOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GcpIAMRoleRemoveOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GcpIAMRoleRemoveOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = GcpIAMRoleRemoveOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GcpIAMRoleRemoveOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500]:
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

) -> Response[GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the IAM role in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500]
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

) -> GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the IAM role in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500
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

) -> Response[GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the IAM role in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500]
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

) -> GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the IAM role in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GcpIAMRoleRemoveOwnersResponse200 | GcpIAMRoleRemoveOwnersResponse400 | GcpIAMRoleRemoveOwnersResponse401 | GcpIAMRoleRemoveOwnersResponse403 | GcpIAMRoleRemoveOwnersResponse404 | GcpIAMRoleRemoveOwnersResponse422 | GcpIAMRoleRemoveOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
