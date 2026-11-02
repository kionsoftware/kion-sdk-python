from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_user_cloud_access_role_alias_request import DeleteUserCloudAccessRoleAliasRequest
from ...models.delete_user_cloud_access_role_alias_response_200 import DeleteUserCloudAccessRoleAliasResponse200
from ...models.delete_user_cloud_access_role_alias_response_400 import DeleteUserCloudAccessRoleAliasResponse400
from ...models.delete_user_cloud_access_role_alias_response_401 import DeleteUserCloudAccessRoleAliasResponse401
from ...models.delete_user_cloud_access_role_alias_response_500 import DeleteUserCloudAccessRoleAliasResponse500
from typing import cast



def _get_kwargs(
    *,
    body: DeleteUserCloudAccessRoleAliasRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/user-cloud-access-role-alias",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteUserCloudAccessRoleAliasResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteUserCloudAccessRoleAliasResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteUserCloudAccessRoleAliasResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = DeleteUserCloudAccessRoleAliasResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteUserCloudAccessRoleAliasRequest,

) -> Response[DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500]:
    """ Deletes a user cloud access role alias.

    Args:
        body (DeleteUserCloudAccessRoleAliasRequest): DeleteUserCloudAccessRoleAliasRequest
            contains the parameters for deleting a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: DeleteUserCloudAccessRoleAliasRequest,

) -> DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500 | None:
    """ Deletes a user cloud access role alias.

    Args:
        body (DeleteUserCloudAccessRoleAliasRequest): DeleteUserCloudAccessRoleAliasRequest
            contains the parameters for deleting a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeleteUserCloudAccessRoleAliasRequest,

) -> Response[DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500]:
    """ Deletes a user cloud access role alias.

    Args:
        body (DeleteUserCloudAccessRoleAliasRequest): DeleteUserCloudAccessRoleAliasRequest
            contains the parameters for deleting a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DeleteUserCloudAccessRoleAliasRequest,

) -> DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500 | None:
    """ Deletes a user cloud access role alias.

    Args:
        body (DeleteUserCloudAccessRoleAliasRequest): DeleteUserCloudAccessRoleAliasRequest
            contains the parameters for deleting a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteUserCloudAccessRoleAliasResponse200 | DeleteUserCloudAccessRoleAliasResponse400 | DeleteUserCloudAccessRoleAliasResponse401 | DeleteUserCloudAccessRoleAliasResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
