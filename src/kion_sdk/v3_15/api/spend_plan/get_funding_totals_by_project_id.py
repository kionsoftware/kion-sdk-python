from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_funding_totals_by_project_id_response_200 import GetFundingTotalsByProjectIDResponse200
from ...models.get_funding_totals_by_project_id_response_401 import GetFundingTotalsByProjectIDResponse401
from ...models.get_funding_totals_by_project_id_response_403 import GetFundingTotalsByProjectIDResponse403
from ...models.get_funding_totals_by_project_id_response_404 import GetFundingTotalsByProjectIDResponse404
from ...models.get_funding_totals_by_project_id_response_500 import GetFundingTotalsByProjectIDResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project/{id}/spend-plan-with-totals".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetFundingTotalsByProjectIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetFundingTotalsByProjectIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetFundingTotalsByProjectIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetFundingTotalsByProjectIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetFundingTotalsByProjectIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500]:
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

) -> Response[GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500]:
    """ Finds the spend plan for a project by ID in the application, with total planned and total spend
    attached for all funding sources.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500]
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

) -> GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500 | None:
    """ Finds the spend plan for a project by ID in the application, with total planned and total spend
    attached for all funding sources.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500]:
    """ Finds the spend plan for a project by ID in the application, with total planned and total spend
    attached for all funding sources.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500]
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

) -> GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500 | None:
    """ Finds the spend plan for a project by ID in the application, with total planned and total spend
    attached for all funding sources.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFundingTotalsByProjectIDResponse200 | GetFundingTotalsByProjectIDResponse401 | GetFundingTotalsByProjectIDResponse403 | GetFundingTotalsByProjectIDResponse404 | GetFundingTotalsByProjectIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
