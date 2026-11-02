from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_suppressed_compliance_findings_response_200 import GetSuppressedComplianceFindingsResponse200
from ...models.get_suppressed_compliance_findings_response_400 import GetSuppressedComplianceFindingsResponse400
from ...models.get_suppressed_compliance_findings_response_401 import GetSuppressedComplianceFindingsResponse401
from ...models.get_suppressed_compliance_findings_response_403 import GetSuppressedComplianceFindingsResponse403
from ...models.get_suppressed_compliance_findings_response_422 import GetSuppressedComplianceFindingsResponse422
from ...models.get_suppressed_compliance_findings_response_500 import GetSuppressedComplianceFindingsResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    project_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["check_id"] = check_id

    params["standard_id"] = standard_id

    params["severity_type_id"] = severity_type_id

    params["page"] = page

    params["count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/finding/suppressed",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetSuppressedComplianceFindingsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetSuppressedComplianceFindingsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSuppressedComplianceFindingsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetSuppressedComplianceFindingsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = GetSuppressedComplianceFindingsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GetSuppressedComplianceFindingsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,

) -> Response[GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500]:
    """ Returns a paginated list of suppressed compliance findings matching the requested parameters.

    Args:
        project_id (int | Unset):
        check_id (int | Unset):
        standard_id (int | Unset):
        severity_type_id (int | Unset):
        page (int | Unset):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
check_id=check_id,
standard_id=standard_id,
severity_type_id=severity_type_id,
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
    project_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,

) -> GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500 | None:
    """ Returns a paginated list of suppressed compliance findings matching the requested parameters.

    Args:
        project_id (int | Unset):
        check_id (int | Unset):
        standard_id (int | Unset):
        severity_type_id (int | Unset):
        page (int | Unset):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500
     """


    return sync_detailed(
        client=client,
project_id=project_id,
check_id=check_id,
standard_id=standard_id,
severity_type_id=severity_type_id,
page=page,
count=count,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,

) -> Response[GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500]:
    """ Returns a paginated list of suppressed compliance findings matching the requested parameters.

    Args:
        project_id (int | Unset):
        check_id (int | Unset):
        standard_id (int | Unset):
        severity_type_id (int | Unset):
        page (int | Unset):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
check_id=check_id,
standard_id=standard_id,
severity_type_id=severity_type_id,
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
    project_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,

) -> GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500 | None:
    """ Returns a paginated list of suppressed compliance findings matching the requested parameters.

    Args:
        project_id (int | Unset):
        check_id (int | Unset):
        standard_id (int | Unset):
        severity_type_id (int | Unset):
        page (int | Unset):
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSuppressedComplianceFindingsResponse200 | GetSuppressedComplianceFindingsResponse400 | GetSuppressedComplianceFindingsResponse401 | GetSuppressedComplianceFindingsResponse403 | GetSuppressedComplianceFindingsResponse422 | GetSuppressedComplianceFindingsResponse500
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,
check_id=check_id,
standard_id=standard_id,
severity_type_id=severity_type_id,
page=page,
count=count,

    )).parsed
