from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_budget_by_ouid_response_200 import GetBudgetByOUIDResponse200
from ...models.get_budget_by_ouid_response_400 import GetBudgetByOUIDResponse400
from ...models.get_budget_by_ouid_response_401 import GetBudgetByOUIDResponse401
from ...models.get_budget_by_ouid_response_403 import GetBudgetByOUIDResponse403
from ...models.get_budget_by_ouid_response_404 import GetBudgetByOUIDResponse404
from ...models.get_budget_by_ouid_response_500 import GetBudgetByOUIDResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou/{id}/budget".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBudgetByOUIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetBudgetByOUIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetBudgetByOUIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBudgetByOUIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetBudgetByOUIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetBudgetByOUIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500]:
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

) -> Response[GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500]:
    """ Returns all thresholds for an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500]
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

) -> GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500 | None:
    """ Returns all thresholds for an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500]:
    """ Returns all thresholds for an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500]
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

) -> GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500 | None:
    """ Returns all thresholds for an OU.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBudgetByOUIDResponse200 | GetBudgetByOUIDResponse400 | GetBudgetByOUIDResponse401 | GetBudgetByOUIDResponse403 | GetBudgetByOUIDResponse404 | GetBudgetByOUIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
