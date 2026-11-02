from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_standard_project_response_200 import GetComplianceStandardProjectResponse200
from ...models.get_compliance_standard_project_response_401 import GetComplianceStandardProjectResponse401
from ...models.get_compliance_standard_project_response_403 import GetComplianceStandardProjectResponse403
from ...models.get_compliance_standard_project_response_500 import GetComplianceStandardProjectResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    ou_id: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["non_compliant"] = non_compliant

    params["detailed"] = detailed

    params["standard_id"] = standard_id

    params["check_id"] = check_id

    params["ou_id"] = ou_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/standard/project",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceStandardProjectResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceStandardProjectResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceStandardProjectResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetComplianceStandardProjectResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    ou_id: int | Unset = UNSET,

) -> Response[GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500]:
    """ Finds projects based on their compliance standards.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        ou_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500]
     """


    kwargs = _get_kwargs(
        non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
ou_id=ou_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    ou_id: int | Unset = UNSET,

) -> GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500 | None:
    """ Finds projects based on their compliance standards.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        ou_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500
     """


    return sync_detailed(
        client=client,
non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
ou_id=ou_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    ou_id: int | Unset = UNSET,

) -> Response[GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500]:
    """ Finds projects based on their compliance standards.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        ou_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500]
     """


    kwargs = _get_kwargs(
        non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
ou_id=ou_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    ou_id: int | Unset = UNSET,

) -> GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500 | None:
    """ Finds projects based on their compliance standards.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        ou_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceStandardProjectResponse200 | GetComplianceStandardProjectResponse401 | GetComplianceStandardProjectResponse403 | GetComplianceStandardProjectResponse500
     """


    return (await asyncio_detailed(
        client=client,
non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
ou_id=ou_id,

    )).parsed
