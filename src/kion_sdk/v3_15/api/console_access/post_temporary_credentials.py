from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_temporary_credentials_response_200 import PostTemporaryCredentialsResponse200
from ...models.post_temporary_credentials_response_400 import PostTemporaryCredentialsResponse400
from ...models.post_temporary_credentials_response_401 import PostTemporaryCredentialsResponse401
from ...models.post_temporary_credentials_response_403 import PostTemporaryCredentialsResponse403
from ...models.post_temporary_credentials_response_422 import PostTemporaryCredentialsResponse422
from ...models.post_temporary_credentials_response_500 import PostTemporaryCredentialsResponse500
from ...models.role_info import RoleInfo
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: RoleInfo | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/temporary-credentials",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500 | None:
    if response.status_code == 200:
        response_200 = PostTemporaryCredentialsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostTemporaryCredentialsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostTemporaryCredentialsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostTemporaryCredentialsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostTemporaryCredentialsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostTemporaryCredentialsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RoleInfo | Unset = UNSET,

) -> Response[PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500]:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role.

    Args:
        body (RoleInfo | Unset): RoleInfo defines a IAM role name and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500]
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
    body: RoleInfo | Unset = UNSET,

) -> PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500 | None:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role.

    Args:
        body (RoleInfo | Unset): RoleInfo defines a IAM role name and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RoleInfo | Unset = UNSET,

) -> Response[PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500]:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role.

    Args:
        body (RoleInfo | Unset): RoleInfo defines a IAM role name and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500]
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
    body: RoleInfo | Unset = UNSET,

) -> PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500 | None:
    """ Generates a short-term access key (STAK) for an AWS account and IAM role.

    Args:
        body (RoleInfo | Unset): RoleInfo defines a IAM role name and and account number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTemporaryCredentialsResponse200 | PostTemporaryCredentialsResponse400 | PostTemporaryCredentialsResponse401 | PostTemporaryCredentialsResponse403 | PostTemporaryCredentialsResponse422 | PostTemporaryCredentialsResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
