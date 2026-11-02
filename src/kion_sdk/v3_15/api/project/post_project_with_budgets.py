from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_project_with_budgets_response_201 import PostProjectWithBudgetsResponse201
from ...models.post_project_with_budgets_response_400 import PostProjectWithBudgetsResponse400
from ...models.post_project_with_budgets_response_401 import PostProjectWithBudgetsResponse401
from ...models.post_project_with_budgets_response_403 import PostProjectWithBudgetsResponse403
from ...models.post_project_with_budgets_response_422 import PostProjectWithBudgetsResponse422
from ...models.post_project_with_budgets_response_500 import PostProjectWithBudgetsResponse500
from ...models.project_create_with_budgets import ProjectCreateWithBudgets
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ProjectCreateWithBudgets | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project/with-budget",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500 | None:
    if response.status_code == 201:
        response_201 = PostProjectWithBudgetsResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostProjectWithBudgetsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostProjectWithBudgetsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostProjectWithBudgetsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostProjectWithBudgetsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostProjectWithBudgetsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCreateWithBudgets | Unset = UNSET,

) -> Response[PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500]:
    """ Creates a project in the application when financial system settings are configured to use Budgets,
    whether or not budgets are configured to be enforced.

    Args:
        body (ProjectCreateWithBudgets | Unset): ProjectCreateWithBudgets defines a project
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500]
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
    body: ProjectCreateWithBudgets | Unset = UNSET,

) -> PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500 | None:
    """ Creates a project in the application when financial system settings are configured to use Budgets,
    whether or not budgets are configured to be enforced.

    Args:
        body (ProjectCreateWithBudgets | Unset): ProjectCreateWithBudgets defines a project
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCreateWithBudgets | Unset = UNSET,

) -> Response[PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500]:
    """ Creates a project in the application when financial system settings are configured to use Budgets,
    whether or not budgets are configured to be enforced.

    Args:
        body (ProjectCreateWithBudgets | Unset): ProjectCreateWithBudgets defines a project
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500]
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
    body: ProjectCreateWithBudgets | Unset = UNSET,

) -> PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500 | None:
    """ Creates a project in the application when financial system settings are configured to use Budgets,
    whether or not budgets are configured to be enforced.

    Args:
        body (ProjectCreateWithBudgets | Unset): ProjectCreateWithBudgets defines a project
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectWithBudgetsResponse201 | PostProjectWithBudgetsResponse400 | PostProjectWithBudgetsResponse401 | PostProjectWithBudgetsResponse403 | PostProjectWithBudgetsResponse422 | PostProjectWithBudgetsResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
