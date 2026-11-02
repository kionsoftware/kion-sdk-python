from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_compliance_check_scan_group_response_201 import PostComplianceCheckScanGroupResponse201
from ...models.post_compliance_check_scan_group_response_400 import PostComplianceCheckScanGroupResponse400
from ...models.post_compliance_check_scan_group_response_401 import PostComplianceCheckScanGroupResponse401
from ...models.post_compliance_check_scan_group_response_403 import PostComplianceCheckScanGroupResponse403
from ...models.post_compliance_check_scan_group_response_422 import PostComplianceCheckScanGroupResponse422
from ...models.post_compliance_check_scan_group_response_500 import PostComplianceCheckScanGroupResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/check/{id}/scan/group".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceCheckScanGroupResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceCheckScanGroupResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceCheckScanGroupResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceCheckScanGroupResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostComplianceCheckScanGroupResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceCheckScanGroupResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500]:
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

) -> Response[PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500]:
    """ Creates a Compliance Check Scan Group.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500]
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

) -> PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500 | None:
    """ Creates a Compliance Check Scan Group.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500]:
    """ Creates a Compliance Check Scan Group.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500]
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

) -> PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500 | None:
    """ Creates a Compliance Check Scan Group.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckScanGroupResponse201 | PostComplianceCheckScanGroupResponse400 | PostComplianceCheckScanGroupResponse401 | PostComplianceCheckScanGroupResponse403 | PostComplianceCheckScanGroupResponse422 | PostComplianceCheckScanGroupResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
