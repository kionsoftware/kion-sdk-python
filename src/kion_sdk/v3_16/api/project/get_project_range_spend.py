from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_range_spend_response_200 import GetProjectRangeSpendResponse200
from ...models.get_project_range_spend_response_400 import GetProjectRangeSpendResponse400
from ...models.get_project_range_spend_response_401 import GetProjectRangeSpendResponse401
from ...models.get_project_range_spend_response_403 import GetProjectRangeSpendResponse403
from ...models.get_project_range_spend_response_404 import GetProjectRangeSpendResponse404
from ...models.get_project_range_spend_response_500 import GetProjectRangeSpendResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    start_datecode: str,
    end_datecode: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start_datecode"] = start_datecode

    params["end_datecode"] = end_datecode


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project/{id}/spend/account/range".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectRangeSpendResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetProjectRangeSpendResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetProjectRangeSpendResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectRangeSpendResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectRangeSpendResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectRangeSpendResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500]:
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
    start_datecode: str,
    end_datecode: str,

) -> Response[GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500]:
    """ Finds the current month spend by project ID and date range from AWS billing reports.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
start_datecode=start_datecode,
end_datecode=end_datecode,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    start_datecode: str,
    end_datecode: str,

) -> GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500 | None:
    """ Finds the current month spend by project ID and date range from AWS billing reports.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500
     """


    return sync_detailed(
        id=id,
client=client,
start_datecode=start_datecode,
end_datecode=end_datecode,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    start_datecode: str,
    end_datecode: str,

) -> Response[GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500]:
    """ Finds the current month spend by project ID and date range from AWS billing reports.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
start_datecode=start_datecode,
end_datecode=end_datecode,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    start_datecode: str,
    end_datecode: str,

) -> GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500 | None:
    """ Finds the current month spend by project ID and date range from AWS billing reports.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectRangeSpendResponse200 | GetProjectRangeSpendResponse400 | GetProjectRangeSpendResponse401 | GetProjectRangeSpendResponse403 | GetProjectRangeSpendResponse404 | GetProjectRangeSpendResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start_datecode=start_datecode,
end_datecode=end_datecode,

    )).parsed
