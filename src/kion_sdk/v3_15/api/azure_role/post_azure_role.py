from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_role_create import AzureRoleCreate
from ...models.post_azure_role_response_201 import PostAzureRoleResponse201
from ...models.post_azure_role_response_400 import PostAzureRoleResponse400
from ...models.post_azure_role_response_401 import PostAzureRoleResponse401
from ...models.post_azure_role_response_403 import PostAzureRoleResponse403
from ...models.post_azure_role_response_422 import PostAzureRoleResponse422
from ...models.post_azure_role_response_500 import PostAzureRoleResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AzureRoleCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/azure-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAzureRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAzureRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAzureRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAzureRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAzureRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAzureRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureRoleCreate,

) -> Response[PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500]:
    """ Creates an Azure Role in the application.

    Args:
        body (AzureRoleCreate): AzureRoleCreate defines an Azure Role Definition creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500]
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
    body: AzureRoleCreate,

) -> PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500 | None:
    """ Creates an Azure Role in the application.

    Args:
        body (AzureRoleCreate): AzureRoleCreate defines an Azure Role Definition creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureRoleCreate,

) -> Response[PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500]:
    """ Creates an Azure Role in the application.

    Args:
        body (AzureRoleCreate): AzureRoleCreate defines an Azure Role Definition creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500]
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
    body: AzureRoleCreate,

) -> PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500 | None:
    """ Creates an Azure Role in the application.

    Args:
        body (AzureRoleCreate): AzureRoleCreate defines an Azure Role Definition creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAzureRoleResponse201 | PostAzureRoleResponse400 | PostAzureRoleResponse401 | PostAzureRoleResponse403 | PostAzureRoleResponse422 | PostAzureRoleResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
