from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_check_create import ComplianceCheckCreate
from ...models.post_compliance_check_bulk_response_201 import PostComplianceCheckBulkResponse201
from ...models.post_compliance_check_bulk_response_400 import PostComplianceCheckBulkResponse400
from ...models.post_compliance_check_bulk_response_401 import PostComplianceCheckBulkResponse401
from ...models.post_compliance_check_bulk_response_403 import PostComplianceCheckBulkResponse403
from ...models.post_compliance_check_bulk_response_422 import PostComplianceCheckBulkResponse422
from ...models.post_compliance_check_bulk_response_500 import PostComplianceCheckBulkResponse500
from typing import cast



def _get_kwargs(
    *,
    body: list[ComplianceCheckCreate],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/check/bulk-create",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceCheckBulkResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceCheckBulkResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceCheckBulkResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceCheckBulkResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostComplianceCheckBulkResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceCheckBulkResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ComplianceCheckCreate],

) -> Response[PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500]:
    """ Creates Compliance Checks by bulk.

    Args:
        body (list[ComplianceCheckCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500]
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
    body: list[ComplianceCheckCreate],

) -> PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500 | None:
    """ Creates Compliance Checks by bulk.

    Args:
        body (list[ComplianceCheckCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ComplianceCheckCreate],

) -> Response[PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500]:
    """ Creates Compliance Checks by bulk.

    Args:
        body (list[ComplianceCheckCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500]
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
    body: list[ComplianceCheckCreate],

) -> PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500 | None:
    """ Creates Compliance Checks by bulk.

    Args:
        body (list[ComplianceCheckCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckBulkResponse201 | PostComplianceCheckBulkResponse400 | PostComplianceCheckBulkResponse401 | PostComplianceCheckBulkResponse403 | PostComplianceCheckBulkResponse422 | PostComplianceCheckBulkResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
