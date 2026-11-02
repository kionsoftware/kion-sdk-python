from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.diagnostic_billing_report_list_response_200 import DiagnosticBillingReportListResponse200
from ...models.diagnostic_billing_report_list_response_400 import DiagnosticBillingReportListResponse400
from ...models.diagnostic_billing_report_list_response_401 import DiagnosticBillingReportListResponse401
from ...models.diagnostic_billing_report_list_response_403 import DiagnosticBillingReportListResponse403
from ...models.diagnostic_billing_report_list_response_500 import DiagnosticBillingReportListResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    month: int | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["Month"] = month

    json_billing_source_i_ds: list[int] | Unset = UNSET
    if not isinstance(billing_source_i_ds, Unset):
        json_billing_source_i_ds = billing_source_i_ds


    params["BillingSourceIDs"] = json_billing_source_i_ds

    params["Status"] = status

    params["Page"] = page

    params["Count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/beta/diagnostic/billing-report",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500 | None:
    if response.status_code == 200:
        response_200 = DiagnosticBillingReportListResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DiagnosticBillingReportListResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DiagnosticBillingReportListResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DiagnosticBillingReportListResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = DiagnosticBillingReportListResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    month: int | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> Response[DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500]:
    """ Returns a paginated list of Billing Report diagnostics.

    Args:
        month (int | Unset):
        billing_source_i_ds (list[int] | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500]
     """


    kwargs = _get_kwargs(
        month=month,
billing_source_i_ds=billing_source_i_ds,
status=status,
page=page,
count=count,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    month: int | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500 | None:
    """ Returns a paginated list of Billing Report diagnostics.

    Args:
        month (int | Unset):
        billing_source_i_ds (list[int] | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500
     """


    return sync_detailed(
        client=client,
month=month,
billing_source_i_ds=billing_source_i_ds,
status=status,
page=page,
count=count,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    month: int | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> Response[DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500]:
    """ Returns a paginated list of Billing Report diagnostics.

    Args:
        month (int | Unset):
        billing_source_i_ds (list[int] | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500]
     """


    kwargs = _get_kwargs(
        month=month,
billing_source_i_ds=billing_source_i_ds,
status=status,
page=page,
count=count,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    month: int | Unset = UNSET,
    billing_source_i_ds: list[int] | Unset = UNSET,
    status: str | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,

) -> DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500 | None:
    """ Returns a paginated list of Billing Report diagnostics.

    Args:
        month (int | Unset):
        billing_source_i_ds (list[int] | Unset):
        status (str | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiagnosticBillingReportListResponse200 | DiagnosticBillingReportListResponse400 | DiagnosticBillingReportListResponse401 | DiagnosticBillingReportListResponse403 | DiagnosticBillingReportListResponse500
     """


    return (await asyncio_detailed(
        client=client,
month=month,
billing_source_i_ds=billing_source_i_ds,
status=status,
page=page,
count=count,

    )).parsed
