from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_v1_post_spend_report_query_response_object import ApiV1PostSpendReportQueryResponseObject
from ...models.post_spend_report_query_response_401 import PostSpendReportQueryResponse401
from ...models.post_spend_report_query_response_403 import PostSpendReportQueryResponse403
from ...models.post_spend_report_query_response_500 import PostSpendReportQueryResponse500
from ...models.spend_report_query import SpendReportQuery
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SpendReportQuery | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/spend-report",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ApiV1PostSpendReportQueryResponseObject.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = PostSpendReportQueryResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostSpendReportQueryResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PostSpendReportQueryResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SpendReportQuery | Unset = UNSET,

) -> Response[PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject]]:
    """ Query spend data on multiple dimensions

     By adjusting the accept header, you can choose to receive the data in either JSON or CSV format.
    The default format is JSON.

    Start date is inclusive and end dates are exclusive
    {start_datecode: 202401, end_datecode: 202406 } will fetch data from Jan 2024 - May 2024

    Args:
        body (SpendReportQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject]]
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
    body: SpendReportQuery | Unset = UNSET,

) -> PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject] | None:
    """ Query spend data on multiple dimensions

     By adjusting the accept header, you can choose to receive the data in either JSON or CSV format.
    The default format is JSON.

    Start date is inclusive and end dates are exclusive
    {start_datecode: 202401, end_datecode: 202406 } will fetch data from Jan 2024 - May 2024

    Args:
        body (SpendReportQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SpendReportQuery | Unset = UNSET,

) -> Response[PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject]]:
    """ Query spend data on multiple dimensions

     By adjusting the accept header, you can choose to receive the data in either JSON or CSV format.
    The default format is JSON.

    Start date is inclusive and end dates are exclusive
    {start_datecode: 202401, end_datecode: 202406 } will fetch data from Jan 2024 - May 2024

    Args:
        body (SpendReportQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject]]
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
    body: SpendReportQuery | Unset = UNSET,

) -> PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject] | None:
    """ Query spend data on multiple dimensions

     By adjusting the accept header, you can choose to receive the data in either JSON or CSV format.
    The default format is JSON.

    Start date is inclusive and end dates are exclusive
    {start_datecode: 202401, end_datecode: 202406 } will fetch data from Jan 2024 - May 2024

    Args:
        body (SpendReportQuery | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSpendReportQueryResponse401 | PostSpendReportQueryResponse403 | PostSpendReportQueryResponse500 | list[ApiV1PostSpendReportQueryResponseObject]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
