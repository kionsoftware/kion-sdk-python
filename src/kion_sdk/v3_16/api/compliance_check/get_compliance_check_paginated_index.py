from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_check_paginated_index_response_200 import GetComplianceCheckPaginatedIndexResponse200
from ...models.get_compliance_check_paginated_index_response_400 import GetComplianceCheckPaginatedIndexResponse400
from ...models.get_compliance_check_paginated_index_response_401 import GetComplianceCheckPaginatedIndexResponse401
from ...models.get_compliance_check_paginated_index_response_500 import GetComplianceCheckPaginatedIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    ou_id: int | Unset = UNSET,
    project_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    cloud_provider_id: int | Unset = UNSET,
    compliance_type_id: int | Unset = UNSET,
    managed_type: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["ou_id"] = ou_id

    params["project_id"] = project_id

    params["standard_id"] = standard_id

    params["account_id"] = account_id

    params["detailed"] = detailed

    params["non_compliant"] = non_compliant

    params["page"] = page

    params["count"] = count

    params["query"] = query

    params["cloud_provider_id"] = cloud_provider_id

    params["compliance_type_id"] = compliance_type_id

    params["managed_type"] = managed_type

    params["severity_type_id"] = severity_type_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/check",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceCheckPaginatedIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetComplianceCheckPaginatedIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetComplianceCheckPaginatedIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetComplianceCheckPaginatedIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ou_id: int | Unset = UNSET,
    project_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    cloud_provider_id: int | Unset = UNSET,
    compliance_type_id: int | Unset = UNSET,
    managed_type: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,

) -> Response[GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500]:
    """ Returns a paginated result of all Compliance Checks in the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        standard_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        cloud_provider_id (int | Unset):
        compliance_type_id (int | Unset):
        managed_type (int | Unset):
        severity_type_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
project_id=project_id,
standard_id=standard_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,
cloud_provider_id=cloud_provider_id,
compliance_type_id=compliance_type_id,
managed_type=managed_type,
severity_type_id=severity_type_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    ou_id: int | Unset = UNSET,
    project_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    cloud_provider_id: int | Unset = UNSET,
    compliance_type_id: int | Unset = UNSET,
    managed_type: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,

) -> GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500 | None:
    """ Returns a paginated result of all Compliance Checks in the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        standard_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        cloud_provider_id (int | Unset):
        compliance_type_id (int | Unset):
        managed_type (int | Unset):
        severity_type_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500
     """


    return sync_detailed(
        client=client,
ou_id=ou_id,
project_id=project_id,
standard_id=standard_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,
cloud_provider_id=cloud_provider_id,
compliance_type_id=compliance_type_id,
managed_type=managed_type,
severity_type_id=severity_type_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ou_id: int | Unset = UNSET,
    project_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    cloud_provider_id: int | Unset = UNSET,
    compliance_type_id: int | Unset = UNSET,
    managed_type: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,

) -> Response[GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500]:
    """ Returns a paginated result of all Compliance Checks in the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        standard_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        cloud_provider_id (int | Unset):
        compliance_type_id (int | Unset):
        managed_type (int | Unset):
        severity_type_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
project_id=project_id,
standard_id=standard_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,
cloud_provider_id=cloud_provider_id,
compliance_type_id=compliance_type_id,
managed_type=managed_type,
severity_type_id=severity_type_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    ou_id: int | Unset = UNSET,
    project_id: int | Unset = UNSET,
    standard_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    cloud_provider_id: int | Unset = UNSET,
    compliance_type_id: int | Unset = UNSET,
    managed_type: int | Unset = UNSET,
    severity_type_id: int | Unset = UNSET,

) -> GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500 | None:
    """ Returns a paginated result of all Compliance Checks in the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        standard_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        cloud_provider_id (int | Unset):
        compliance_type_id (int | Unset):
        managed_type (int | Unset):
        severity_type_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckPaginatedIndexResponse200 | GetComplianceCheckPaginatedIndexResponse400 | GetComplianceCheckPaginatedIndexResponse401 | GetComplianceCheckPaginatedIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
ou_id=ou_id,
project_id=project_id,
standard_id=standard_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,
cloud_provider_id=cloud_provider_id,
compliance_type_id=compliance_type_id,
managed_type=managed_type,
severity_type_id=severity_type_id,

    )).parsed
