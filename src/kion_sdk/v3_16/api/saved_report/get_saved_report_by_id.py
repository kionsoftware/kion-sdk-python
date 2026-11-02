from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_saved_report_by_id_response_200 import GetSavedReportByIDResponse200
from ...models.get_saved_report_by_id_response_400 import GetSavedReportByIDResponse400
from ...models.get_saved_report_by_id_response_401 import GetSavedReportByIDResponse401
from ...models.get_saved_report_by_id_response_403 import GetSavedReportByIDResponse403
from ...models.get_saved_report_by_id_response_404 import GetSavedReportByIDResponse404
from ...models.get_saved_report_by_id_response_500 import GetSavedReportByIDResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/saved-report/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetSavedReportByIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetSavedReportByIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSavedReportByIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetSavedReportByIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSavedReportByIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetSavedReportByIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500]:
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

) -> Response[GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500]:
    """ Gets a saved report by saved report ID.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500]
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

) -> GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500 | None:
    """ Gets a saved report by saved report ID.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500]:
    """ Gets a saved report by saved report ID.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500]
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

) -> GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500 | None:
    """ Gets a saved report by saved report ID.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSavedReportByIDResponse200 | GetSavedReportByIDResponse400 | GetSavedReportByIDResponse401 | GetSavedReportByIDResponse403 | GetSavedReportByIDResponse404 | GetSavedReportByIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
