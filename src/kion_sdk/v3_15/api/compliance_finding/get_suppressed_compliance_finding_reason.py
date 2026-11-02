from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_suppressed_compliance_finding_reason_response_200 import GetSuppressedComplianceFindingReasonResponse200
from ...models.get_suppressed_compliance_finding_reason_response_400 import GetSuppressedComplianceFindingReasonResponse400
from ...models.get_suppressed_compliance_finding_reason_response_401 import GetSuppressedComplianceFindingReasonResponse401
from ...models.get_suppressed_compliance_finding_reason_response_403 import GetSuppressedComplianceFindingReasonResponse403
from ...models.get_suppressed_compliance_finding_reason_response_404 import GetSuppressedComplianceFindingReasonResponse404
from ...models.get_suppressed_compliance_finding_reason_response_500 import GetSuppressedComplianceFindingReasonResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/finding/suppressed/{id}/reason".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500 | None:
    if response.status_code == 200:
        response_200 = GetSuppressedComplianceFindingReasonResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetSuppressedComplianceFindingReasonResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetSuppressedComplianceFindingReasonResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetSuppressedComplianceFindingReasonResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetSuppressedComplianceFindingReasonResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetSuppressedComplianceFindingReasonResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500]:
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

) -> Response[GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500]:
    """ Returns the reason a compliance finding was suppressed.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500]
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

) -> GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500 | None:
    """ Returns the reason a compliance finding was suppressed.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500]:
    """ Returns the reason a compliance finding was suppressed.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500]
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

) -> GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500 | None:
    """ Returns the reason a compliance finding was suppressed.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSuppressedComplianceFindingReasonResponse200 | GetSuppressedComplianceFindingReasonResponse400 | GetSuppressedComplianceFindingReasonResponse401 | GetSuppressedComplianceFindingReasonResponse403 | GetSuppressedComplianceFindingReasonResponse404 | GetSuppressedComplianceFindingReasonResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
