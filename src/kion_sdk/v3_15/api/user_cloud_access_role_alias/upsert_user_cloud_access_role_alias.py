from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.upsert_user_cloud_access_role_alias_request import UpsertUserCloudAccessRoleAliasRequest
from ...models.upsert_user_cloud_access_role_alias_response_201 import UpsertUserCloudAccessRoleAliasResponse201
from ...models.upsert_user_cloud_access_role_alias_response_400 import UpsertUserCloudAccessRoleAliasResponse400
from ...models.upsert_user_cloud_access_role_alias_response_401 import UpsertUserCloudAccessRoleAliasResponse401
from ...models.upsert_user_cloud_access_role_alias_response_500 import UpsertUserCloudAccessRoleAliasResponse500
from typing import cast



def _get_kwargs(
    *,
    body: UpsertUserCloudAccessRoleAliasRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/user-cloud-access-role-alias",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500 | None:
    if response.status_code == 201:
        response_201 = UpsertUserCloudAccessRoleAliasResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = UpsertUserCloudAccessRoleAliasResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpsertUserCloudAccessRoleAliasResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = UpsertUserCloudAccessRoleAliasResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpsertUserCloudAccessRoleAliasRequest,

) -> Response[UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500]:
    """ Creates or updates a user cloud access role alias.

    Args:
        body (UpsertUserCloudAccessRoleAliasRequest): UpsertUserCloudAccessRoleAliasRequest
            contains the parameters for creating or updating a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500]
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
    body: UpsertUserCloudAccessRoleAliasRequest,

) -> UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500 | None:
    """ Creates or updates a user cloud access role alias.

    Args:
        body (UpsertUserCloudAccessRoleAliasRequest): UpsertUserCloudAccessRoleAliasRequest
            contains the parameters for creating or updating a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpsertUserCloudAccessRoleAliasRequest,

) -> Response[UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500]:
    """ Creates or updates a user cloud access role alias.

    Args:
        body (UpsertUserCloudAccessRoleAliasRequest): UpsertUserCloudAccessRoleAliasRequest
            contains the parameters for creating or updating a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500]
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
    body: UpsertUserCloudAccessRoleAliasRequest,

) -> UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500 | None:
    """ Creates or updates a user cloud access role alias.

    Args:
        body (UpsertUserCloudAccessRoleAliasRequest): UpsertUserCloudAccessRoleAliasRequest
            contains the parameters for creating or updating a user cloud access role alias.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpsertUserCloudAccessRoleAliasResponse201 | UpsertUserCloudAccessRoleAliasResponse400 | UpsertUserCloudAccessRoleAliasResponse401 | UpsertUserCloudAccessRoleAliasResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
