from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_service_range_spend_response_200 import GetProjectServiceRangeSpendResponse200
from ...models.get_project_service_range_spend_response_400 import GetProjectServiceRangeSpendResponse400
from ...models.get_project_service_range_spend_response_401 import GetProjectServiceRangeSpendResponse401
from ...models.get_project_service_range_spend_response_403 import GetProjectServiceRangeSpendResponse403
from ...models.get_project_service_range_spend_response_404 import GetProjectServiceRangeSpendResponse404
from ...models.get_project_service_range_spend_response_500 import GetProjectServiceRangeSpendResponse500
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
        "url": "/v3/project/{id}/spend/service/range".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectServiceRangeSpendResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetProjectServiceRangeSpendResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetProjectServiceRangeSpendResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectServiceRangeSpendResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectServiceRangeSpendResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectServiceRangeSpendResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500]:
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

) -> Response[GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500]:
    """ Returns a breakdown of spending across services in the project for the requested date range.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500]
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

) -> GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500 | None:
    """ Returns a breakdown of spending across services in the project for the requested date range.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500
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

) -> Response[GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500]:
    """ Returns a breakdown of spending across services in the project for the requested date range.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500]
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

) -> GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500 | None:
    """ Returns a breakdown of spending across services in the project for the requested date range.

    Args:
        id (int):
        start_datecode (str):
        end_datecode (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectServiceRangeSpendResponse200 | GetProjectServiceRangeSpendResponse400 | GetProjectServiceRangeSpendResponse401 | GetProjectServiceRangeSpendResponse403 | GetProjectServiceRangeSpendResponse404 | GetProjectServiceRangeSpendResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start_datecode=start_datecode,
end_datecode=end_datecode,

    )).parsed
