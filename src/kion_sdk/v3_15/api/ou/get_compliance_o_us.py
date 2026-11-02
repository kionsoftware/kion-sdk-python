from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_o_us_response_200 import GetComplianceOUsResponse200
from ...models.get_compliance_o_us_response_400 import GetComplianceOUsResponse400
from ...models.get_compliance_o_us_response_401 import GetComplianceOUsResponse401
from ...models.get_compliance_o_us_response_403 import GetComplianceOUsResponse403
from ...models.get_compliance_o_us_response_500 import GetComplianceOUsResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["non_compliant"] = non_compliant

    params["detailed"] = detailed

    params["standard_id"] = standard_id

    params["check_id"] = check_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/ou",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceOUsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetComplianceOUsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetComplianceOUsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceOUsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetComplianceOUsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500]:
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

) -> Response[GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500]:
    """ Finds OUs based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500]
     """


    kwargs = _get_kwargs(
        non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,

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

) -> GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500 | None:
    """ Finds OUs based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500
     """


    return sync_detailed(
        client=client,
non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,

) -> Response[GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500]:
    """ Finds OUs based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500]
     """


    kwargs = _get_kwargs(
        non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,

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

) -> GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500 | None:
    """ Finds OUs based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceOUsResponse200 | GetComplianceOUsResponse400 | GetComplianceOUsResponse401 | GetComplianceOUsResponse403 | GetComplianceOUsResponse500
     """


    return (await asyncio_detailed(
        client=client,
non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,

    )).parsed
