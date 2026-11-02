from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_cloud_access_role_associations_response_200 import DeleteOUCloudAccessRoleAssociationsResponse200
from ...models.delete_ou_cloud_access_role_associations_response_400 import DeleteOUCloudAccessRoleAssociationsResponse400
from ...models.delete_ou_cloud_access_role_associations_response_401 import DeleteOUCloudAccessRoleAssociationsResponse401
from ...models.delete_ou_cloud_access_role_associations_response_403 import DeleteOUCloudAccessRoleAssociationsResponse403
from ...models.delete_ou_cloud_access_role_associations_response_404 import DeleteOUCloudAccessRoleAssociationsResponse404
from ...models.delete_ou_cloud_access_role_associations_response_422 import DeleteOUCloudAccessRoleAssociationsResponse422
from ...models.delete_ou_cloud_access_role_associations_response_500 import DeleteOUCloudAccessRoleAssociationsResponse500
from ...models.ou_cloud_access_role_associations import OUCloudAccessRoleAssociations
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OUCloudAccessRoleAssociations,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou-cloud-access-role/{id}/association".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOUCloudAccessRoleAssociationsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteOUCloudAccessRoleAssociationsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOUCloudAccessRoleAssociationsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOUCloudAccessRoleAssociationsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOUCloudAccessRoleAssociationsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteOUCloudAccessRoleAssociationsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteOUCloudAccessRoleAssociationsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500]:
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
    body: OUCloudAccessRoleAssociations,

) -> Response[DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500]:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (OUCloudAccessRoleAssociations): OUCloudAccessRoleAssociations defines the json
            structure for the OU cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500]
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
    body: OUCloudAccessRoleAssociations,

) -> DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500 | None:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (OUCloudAccessRoleAssociations): OUCloudAccessRoleAssociations defines the json
            structure for the OU cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500
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
    body: OUCloudAccessRoleAssociations,

) -> Response[DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500]:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (OUCloudAccessRoleAssociations): OUCloudAccessRoleAssociations defines the json
            structure for the OU cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500]
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
    body: OUCloudAccessRoleAssociations,

) -> DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500 | None:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (OUCloudAccessRoleAssociations): OUCloudAccessRoleAssociations defines the json
            structure for the OU cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUCloudAccessRoleAssociationsResponse200 | DeleteOUCloudAccessRoleAssociationsResponse400 | DeleteOUCloudAccessRoleAssociationsResponse401 | DeleteOUCloudAccessRoleAssociationsResponse403 | DeleteOUCloudAccessRoleAssociationsResponse404 | DeleteOUCloudAccessRoleAssociationsResponse422 | DeleteOUCloudAccessRoleAssociationsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
