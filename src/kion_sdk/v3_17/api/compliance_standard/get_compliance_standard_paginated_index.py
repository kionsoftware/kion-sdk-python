from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_standard_paginated_index_response_200 import GetComplianceStandardPaginatedIndexResponse200
from ...models.get_compliance_standard_paginated_index_response_400 import GetComplianceStandardPaginatedIndexResponse400
from ...models.get_compliance_standard_paginated_index_response_401 import GetComplianceStandardPaginatedIndexResponse401
from ...models.get_compliance_standard_paginated_index_response_500 import GetComplianceStandardPaginatedIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    ou_id: int | Unset = UNSET,
    project_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    cloud_rule_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    query: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["ou_id"] = ou_id

    params["project_id"] = project_id

    params["check_id"] = check_id

    params["cloud_rule_id"] = cloud_rule_id

    params["account_id"] = account_id

    params["detailed"] = detailed

    params["non_compliant"] = non_compliant

    params["page"] = page

    params["count"] = count

    params["query"] = query


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/standard",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceStandardPaginatedIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetComplianceStandardPaginatedIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetComplianceStandardPaginatedIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetComplianceStandardPaginatedIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500]:
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
    check_id: int | Unset = UNSET,
    cloud_rule_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    query: str | Unset = UNSET,

) -> Response[GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500]:
    """ Returns a paginated list of Compliance Standards from the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        check_id (int | Unset):
        cloud_rule_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
project_id=project_id,
check_id=check_id,
cloud_rule_id=cloud_rule_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,

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
    check_id: int | Unset = UNSET,
    cloud_rule_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    query: str | Unset = UNSET,

) -> GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Compliance Standards from the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        check_id (int | Unset):
        cloud_rule_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500
     """


    return sync_detailed(
        client=client,
ou_id=ou_id,
project_id=project_id,
check_id=check_id,
cloud_rule_id=cloud_rule_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ou_id: int | Unset = UNSET,
    project_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    cloud_rule_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    query: str | Unset = UNSET,

) -> Response[GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500]:
    """ Returns a paginated list of Compliance Standards from the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        check_id (int | Unset):
        cloud_rule_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,
project_id=project_id,
check_id=check_id,
cloud_rule_id=cloud_rule_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,

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
    check_id: int | Unset = UNSET,
    cloud_rule_id: int | Unset = UNSET,
    account_id: int | Unset = UNSET,
    detailed: int | Unset = UNSET,
    non_compliant: int | Unset = UNSET,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    query: str | Unset = UNSET,

) -> GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Compliance Standards from the application.

    Args:
        ou_id (int | Unset):
        project_id (int | Unset):
        check_id (int | Unset):
        cloud_rule_id (int | Unset):
        account_id (int | Unset):
        detailed (int | Unset):
        non_compliant (int | Unset):
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardPaginatedIndexResponse200 | GetComplianceStandardPaginatedIndexResponse400 | GetComplianceStandardPaginatedIndexResponse401 | GetComplianceStandardPaginatedIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
ou_id=ou_id,
project_id=project_id,
check_id=check_id,
cloud_rule_id=cloud_rule_id,
account_id=account_id,
detailed=detailed,
non_compliant=non_compliant,
page=page,
count=count,
query=query,

    )).parsed
