from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.funding_source_spend_report_request import FundingSourceSpendReportRequest
from ...models.post_funding_source_report_response_200 import PostFundingSourceReportResponse200
from ...models.post_funding_source_report_response_400 import PostFundingSourceReportResponse400
from ...models.post_funding_source_report_response_401 import PostFundingSourceReportResponse401
from ...models.post_funding_source_report_response_403 import PostFundingSourceReportResponse403
from ...models.post_funding_source_report_response_404 import PostFundingSourceReportResponse404
from ...models.post_funding_source_report_response_500 import PostFundingSourceReportResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: FundingSourceSpendReportRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/spend-report/funding-source",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500 | None:
    if response.status_code == 200:
        response_200 = PostFundingSourceReportResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostFundingSourceReportResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostFundingSourceReportResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostFundingSourceReportResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostFundingSourceReportResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PostFundingSourceReportResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: FundingSourceSpendReportRequest | Unset = UNSET,

) -> Response[PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500]:
    """ Returns the spend report for a particular funding source.

    Args:
        body (FundingSourceSpendReportRequest | Unset): FundingSourceSpendReportRequest represents
            request parameters for a spend report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500]
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
    body: FundingSourceSpendReportRequest | Unset = UNSET,

) -> PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500 | None:
    """ Returns the spend report for a particular funding source.

    Args:
        body (FundingSourceSpendReportRequest | Unset): FundingSourceSpendReportRequest represents
            request parameters for a spend report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FundingSourceSpendReportRequest | Unset = UNSET,

) -> Response[PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500]:
    """ Returns the spend report for a particular funding source.

    Args:
        body (FundingSourceSpendReportRequest | Unset): FundingSourceSpendReportRequest represents
            request parameters for a spend report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500]
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
    body: FundingSourceSpendReportRequest | Unset = UNSET,

) -> PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500 | None:
    """ Returns the spend report for a particular funding source.

    Args:
        body (FundingSourceSpendReportRequest | Unset): FundingSourceSpendReportRequest represents
            request parameters for a spend report.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFundingSourceReportResponse200 | PostFundingSourceReportResponse400 | PostFundingSourceReportResponse401 | PostFundingSourceReportResponse403 | PostFundingSourceReportResponse404 | PostFundingSourceReportResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
