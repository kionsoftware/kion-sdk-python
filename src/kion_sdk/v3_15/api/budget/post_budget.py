from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.budget_create import BudgetCreate
from ...models.post_budget_response_201 import PostBudgetResponse201
from ...models.post_budget_response_400 import PostBudgetResponse400
from ...models.post_budget_response_401 import PostBudgetResponse401
from ...models.post_budget_response_403 import PostBudgetResponse403
from ...models.post_budget_response_422 import PostBudgetResponse422
from ...models.post_budget_response_500 import PostBudgetResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BudgetCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/budget",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500 | None:
    if response.status_code == 201:
        response_201 = PostBudgetResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostBudgetResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostBudgetResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostBudgetResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostBudgetResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostBudgetResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BudgetCreate | Unset = UNSET,

) -> Response[PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500]:
    """ Creates a budget in the application.

    Args:
        body (BudgetCreate | Unset): BudgetCreate is used to create a new project budget or OU
            threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500]
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
    body: BudgetCreate | Unset = UNSET,

) -> PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500 | None:
    """ Creates a budget in the application.

    Args:
        body (BudgetCreate | Unset): BudgetCreate is used to create a new project budget or OU
            threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BudgetCreate | Unset = UNSET,

) -> Response[PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500]:
    """ Creates a budget in the application.

    Args:
        body (BudgetCreate | Unset): BudgetCreate is used to create a new project budget or OU
            threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500]
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
    body: BudgetCreate | Unset = UNSET,

) -> PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500 | None:
    """ Creates a budget in the application.

    Args:
        body (BudgetCreate | Unset): BudgetCreate is used to create a new project budget or OU
            threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostBudgetResponse201 | PostBudgetResponse400 | PostBudgetResponse401 | PostBudgetResponse403 | PostBudgetResponse422 | PostBudgetResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
