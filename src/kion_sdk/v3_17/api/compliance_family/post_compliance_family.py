from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_family_create import ComplianceFamilyCreate
from ...models.post_compliance_family_response_201 import PostComplianceFamilyResponse201
from ...models.post_compliance_family_response_400 import PostComplianceFamilyResponse400
from ...models.post_compliance_family_response_401 import PostComplianceFamilyResponse401
from ...models.post_compliance_family_response_403 import PostComplianceFamilyResponse403
from ...models.post_compliance_family_response_500 import PostComplianceFamilyResponse500
from typing import cast



def _get_kwargs(
    *,
    body: ComplianceFamilyCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/compliance/family",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceFamilyResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceFamilyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceFamilyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceFamilyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PostComplianceFamilyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceFamilyCreate,

) -> Response[PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500]:
    """ Creates a new Compliance Family in the application.

    Args:
        body (ComplianceFamilyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500]
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
    body: ComplianceFamilyCreate,

) -> PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500 | None:
    """ Creates a new Compliance Family in the application.

    Args:
        body (ComplianceFamilyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceFamilyCreate,

) -> Response[PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500]:
    """ Creates a new Compliance Family in the application.

    Args:
        body (ComplianceFamilyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500]
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
    body: ComplianceFamilyCreate,

) -> PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500 | None:
    """ Creates a new Compliance Family in the application.

    Args:
        body (ComplianceFamilyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceFamilyResponse201 | PostComplianceFamilyResponse400 | PostComplianceFamilyResponse401 | PostComplianceFamilyResponse403 | PostComplianceFamilyResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
