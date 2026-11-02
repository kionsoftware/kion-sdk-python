from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.budget_update import BudgetUpdate
from ...models.put_budget_response_200 import PutBudgetResponse200
from ...models.put_budget_response_400 import PutBudgetResponse400
from ...models.put_budget_response_401 import PutBudgetResponse401
from ...models.put_budget_response_403 import PutBudgetResponse403
from ...models.put_budget_response_404 import PutBudgetResponse404
from ...models.put_budget_response_422 import PutBudgetResponse422
from ...models.put_budget_response_500 import PutBudgetResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: BudgetUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/budget/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500 | None:
    if response.status_code == 200:
        response_200 = PutBudgetResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutBudgetResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutBudgetResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutBudgetResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PutBudgetResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutBudgetResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutBudgetResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500]:
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
    body: BudgetUpdate | Unset = UNSET,

) -> Response[PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500]:
    """ Updates a budget by ID in the application.

    Args:
        id (int):
        body (BudgetUpdate | Unset): BudgetUpdate is used to update an existing project budget or
            OU threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500]
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
    body: BudgetUpdate | Unset = UNSET,

) -> PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500 | None:
    """ Updates a budget by ID in the application.

    Args:
        id (int):
        body (BudgetUpdate | Unset): BudgetUpdate is used to update an existing project budget or
            OU threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500
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
    body: BudgetUpdate | Unset = UNSET,

) -> Response[PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500]:
    """ Updates a budget by ID in the application.

    Args:
        id (int):
        body (BudgetUpdate | Unset): BudgetUpdate is used to update an existing project budget or
            OU threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500]
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
    body: BudgetUpdate | Unset = UNSET,

) -> PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500 | None:
    """ Updates a budget by ID in the application.

    Args:
        id (int):
        body (BudgetUpdate | Unset): BudgetUpdate is used to update an existing project budget or
            OU threshold.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutBudgetResponse200 | PutBudgetResponse400 | PutBudgetResponse401 | PutBudgetResponse403 | PutBudgetResponse404 | PutBudgetResponse422 | PutBudgetResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
