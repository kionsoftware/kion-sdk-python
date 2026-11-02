from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_budget_by_project_id_response_200 import GetBudgetByProjectIDResponse200
from ...models.get_budget_by_project_id_response_400 import GetBudgetByProjectIDResponse400
from ...models.get_budget_by_project_id_response_401 import GetBudgetByProjectIDResponse401
from ...models.get_budget_by_project_id_response_403 import GetBudgetByProjectIDResponse403
from ...models.get_budget_by_project_id_response_404 import GetBudgetByProjectIDResponse404
from ...models.get_budget_by_project_id_response_500 import GetBudgetByProjectIDResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project/{id}/budget".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBudgetByProjectIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetBudgetByProjectIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetBudgetByProjectIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBudgetByProjectIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetBudgetByProjectIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetBudgetByProjectIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500]:
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

) -> Response[GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500]:
    """ Returns all budgets for a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500 | None:
    """ Returns all budgets for a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500]:
    """ Returns all budgets for a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500 | None:
    """ Returns all budgets for a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBudgetByProjectIDResponse200 | GetBudgetByProjectIDResponse400 | GetBudgetByProjectIDResponse401 | GetBudgetByProjectIDResponse403 | GetBudgetByProjectIDResponse404 | GetBudgetByProjectIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
