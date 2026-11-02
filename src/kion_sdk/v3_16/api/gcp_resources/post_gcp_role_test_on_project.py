from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_role_test_on_project_body import GCPRoleTestOnProjectBody
from ...models.post_gcp_role_test_on_project_response_200 import PostGCPRoleTestOnProjectResponse200
from ...models.post_gcp_role_test_on_project_response_400 import PostGCPRoleTestOnProjectResponse400
from ...models.post_gcp_role_test_on_project_response_401 import PostGCPRoleTestOnProjectResponse401
from ...models.post_gcp_role_test_on_project_response_403 import PostGCPRoleTestOnProjectResponse403
from ...models.post_gcp_role_test_on_project_response_422 import PostGCPRoleTestOnProjectResponse422
from ...models.post_gcp_role_test_on_project_response_500 import PostGCPRoleTestOnProjectResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GCPRoleTestOnProjectBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp-resources/test-project",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500 | None:
    if response.status_code == 200:
        response_200 = PostGCPRoleTestOnProjectResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostGCPRoleTestOnProjectResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostGCPRoleTestOnProjectResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostGCPRoleTestOnProjectResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostGCPRoleTestOnProjectResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostGCPRoleTestOnProjectResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPRoleTestOnProjectBody,

) -> Response[PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500]:
    """ Verifies if the permissions provided can be applied to a specific GCP Project.

    Args:
        body (GCPRoleTestOnProjectBody): GCPRoleTestOnProjectBody defines the parameters needed to
            verify a set of IAM Permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500]
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
    body: GCPRoleTestOnProjectBody,

) -> PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500 | None:
    """ Verifies if the permissions provided can be applied to a specific GCP Project.

    Args:
        body (GCPRoleTestOnProjectBody): GCPRoleTestOnProjectBody defines the parameters needed to
            verify a set of IAM Permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPRoleTestOnProjectBody,

) -> Response[PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500]:
    """ Verifies if the permissions provided can be applied to a specific GCP Project.

    Args:
        body (GCPRoleTestOnProjectBody): GCPRoleTestOnProjectBody defines the parameters needed to
            verify a set of IAM Permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500]
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
    body: GCPRoleTestOnProjectBody,

) -> PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500 | None:
    """ Verifies if the permissions provided can be applied to a specific GCP Project.

    Args:
        body (GCPRoleTestOnProjectBody): GCPRoleTestOnProjectBody defines the parameters needed to
            verify a set of IAM Permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGCPRoleTestOnProjectResponse200 | PostGCPRoleTestOnProjectResponse400 | PostGCPRoleTestOnProjectResponse401 | PostGCPRoleTestOnProjectResponse403 | PostGCPRoleTestOnProjectResponse422 | PostGCPRoleTestOnProjectResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
