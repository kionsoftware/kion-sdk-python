from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_access_role_info import CloudAccessRoleInfo
from ...models.post_temporary_credentials_role_name_response_200 import PostTemporaryCredentialsRoleNameResponse200
from ...models.post_temporary_credentials_role_name_response_400 import PostTemporaryCredentialsRoleNameResponse400
from ...models.post_temporary_credentials_role_name_response_401 import PostTemporaryCredentialsRoleNameResponse401
from ...models.post_temporary_credentials_role_name_response_403 import PostTemporaryCredentialsRoleNameResponse403
from ...models.post_temporary_credentials_role_name_response_422 import PostTemporaryCredentialsRoleNameResponse422
from ...models.post_temporary_credentials_role_name_response_500 import PostTemporaryCredentialsRoleNameResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CloudAccessRoleInfo | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/temporary-credentials/cloud-access-role",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500 | None:
    if response.status_code == 200:
        response_200 = PostTemporaryCredentialsRoleNameResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostTemporaryCredentialsRoleNameResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostTemporaryCredentialsRoleNameResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostTemporaryCredentialsRoleNameResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostTemporaryCredentialsRoleNameResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostTemporaryCredentialsRoleNameResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CloudAccessRoleInfo | Unset = UNSET,

) -> Response[PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500]:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role using the name of the cloud
    access role.

    Args:
        body (CloudAccessRoleInfo | Unset): CloudAccessRoleInfo defines a cloud access role name
            and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500]
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
    body: CloudAccessRoleInfo | Unset = UNSET,

) -> PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500 | None:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role using the name of the cloud
    access role.

    Args:
        body (CloudAccessRoleInfo | Unset): CloudAccessRoleInfo defines a cloud access role name
            and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CloudAccessRoleInfo | Unset = UNSET,

) -> Response[PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500]:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role using the name of the cloud
    access role.

    Args:
        body (CloudAccessRoleInfo | Unset): CloudAccessRoleInfo defines a cloud access role name
            and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500]
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
    body: CloudAccessRoleInfo | Unset = UNSET,

) -> PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500 | None:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role using the name of the cloud
    access role.

    Args:
        body (CloudAccessRoleInfo | Unset): CloudAccessRoleInfo defines a cloud access role name
            and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTemporaryCredentialsRoleNameResponse200 | PostTemporaryCredentialsRoleNameResponse400 | PostTemporaryCredentialsRoleNameResponse401 | PostTemporaryCredentialsRoleNameResponse403 | PostTemporaryCredentialsRoleNameResponse422 | PostTemporaryCredentialsRoleNameResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
