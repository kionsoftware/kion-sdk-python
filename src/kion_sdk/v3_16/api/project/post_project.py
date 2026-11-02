from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_project_response_201 import PostProjectResponse201
from ...models.post_project_response_400 import PostProjectResponse400
from ...models.post_project_response_401 import PostProjectResponse401
from ...models.post_project_response_403 import PostProjectResponse403
from ...models.post_project_response_422 import PostProjectResponse422
from ...models.post_project_response_500 import PostProjectResponse500
from ...models.project_create import ProjectCreate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ProjectCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500 | None:
    if response.status_code == 201:
        response_201 = PostProjectResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostProjectResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostProjectResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostProjectResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostProjectResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostProjectResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate | Unset = UNSET,

) -> Response[PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500]:
    """ Creates a project in the application.

     NOTE: This endpoint is deprecated and only supports projects with spend plans.
    Use /v3/project/with-spend-plan to create a project when financial system settings are configured
    for Spend Plans.
    Use /v3/project/with-budget when when financial system settings are configured for Budget, even when
    budgets are not configured to be enforced.

    Args:
        body (ProjectCreate | Unset): ProjectCreate defines a project creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500]
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
    body: ProjectCreate | Unset = UNSET,

) -> PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500 | None:
    """ Creates a project in the application.

     NOTE: This endpoint is deprecated and only supports projects with spend plans.
    Use /v3/project/with-spend-plan to create a project when financial system settings are configured
    for Spend Plans.
    Use /v3/project/with-budget when when financial system settings are configured for Budget, even when
    budgets are not configured to be enforced.

    Args:
        body (ProjectCreate | Unset): ProjectCreate defines a project creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate | Unset = UNSET,

) -> Response[PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500]:
    """ Creates a project in the application.

     NOTE: This endpoint is deprecated and only supports projects with spend plans.
    Use /v3/project/with-spend-plan to create a project when financial system settings are configured
    for Spend Plans.
    Use /v3/project/with-budget when when financial system settings are configured for Budget, even when
    budgets are not configured to be enforced.

    Args:
        body (ProjectCreate | Unset): ProjectCreate defines a project creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500]
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
    body: ProjectCreate | Unset = UNSET,

) -> PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500 | None:
    """ Creates a project in the application.

     NOTE: This endpoint is deprecated and only supports projects with spend plans.
    Use /v3/project/with-spend-plan to create a project when financial system settings are configured
    for Spend Plans.
    Use /v3/project/with-budget when when financial system settings are configured for Budget, even when
    budgets are not configured to be enforced.

    Args:
        body (ProjectCreate | Unset): ProjectCreate defines a project creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectResponse201 | PostProjectResponse400 | PostProjectResponse401 | PostProjectResponse403 | PostProjectResponse422 | PostProjectResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
