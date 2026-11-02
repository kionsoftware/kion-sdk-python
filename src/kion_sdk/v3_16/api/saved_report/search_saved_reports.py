from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.saved_report_search import SavedReportSearch
from ...models.search_saved_reports_response_200 import SearchSavedReportsResponse200
from ...models.search_saved_reports_response_400 import SearchSavedReportsResponse400
from ...models.search_saved_reports_response_401 import SearchSavedReportsResponse401
from ...models.search_saved_reports_response_422 import SearchSavedReportsResponse422
from ...models.search_saved_reports_response_500 import SearchSavedReportsResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SavedReportSearch | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/saved-report/search",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500 | None:
    if response.status_code == 200:
        response_200 = SearchSavedReportsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SearchSavedReportsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = SearchSavedReportsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = SearchSavedReportsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = SearchSavedReportsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SavedReportSearch | Unset = UNSET,

) -> Response[SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500]:
    """ Gets a list of saved reports that match the search criteria.

    Args:
        body (SavedReportSearch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500]
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
    body: SavedReportSearch | Unset = UNSET,

) -> SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500 | None:
    """ Gets a list of saved reports that match the search criteria.

    Args:
        body (SavedReportSearch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SavedReportSearch | Unset = UNSET,

) -> Response[SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500]:
    """ Gets a list of saved reports that match the search criteria.

    Args:
        body (SavedReportSearch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500]
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
    body: SavedReportSearch | Unset = UNSET,

) -> SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500 | None:
    """ Gets a list of saved reports that match the search criteria.

    Args:
        body (SavedReportSearch | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchSavedReportsResponse200 | SearchSavedReportsResponse400 | SearchSavedReportsResponse401 | SearchSavedReportsResponse422 | SearchSavedReportsResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
