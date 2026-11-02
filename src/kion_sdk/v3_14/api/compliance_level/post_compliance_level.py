from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_level_create import ComplianceLevelCreate
from ...models.post_compliance_level_response_201 import PostComplianceLevelResponse201
from ...models.post_compliance_level_response_400 import PostComplianceLevelResponse400
from ...models.post_compliance_level_response_401 import PostComplianceLevelResponse401
from ...models.post_compliance_level_response_403 import PostComplianceLevelResponse403
from ...models.post_compliance_level_response_500 import PostComplianceLevelResponse500
from typing import cast



def _get_kwargs(
    *,
    body: ComplianceLevelCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/compliance/level",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceLevelResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceLevelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceLevelResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceLevelResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PostComplianceLevelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceLevelCreate,

) -> Response[PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500]:
    """ Creates a new Compliance Level in the application.

    Args:
        body (ComplianceLevelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500]
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
    body: ComplianceLevelCreate,

) -> PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500 | None:
    """ Creates a new Compliance Level in the application.

    Args:
        body (ComplianceLevelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceLevelCreate,

) -> Response[PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500]:
    """ Creates a new Compliance Level in the application.

    Args:
        body (ComplianceLevelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500]
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
    body: ComplianceLevelCreate,

) -> PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500 | None:
    """ Creates a new Compliance Level in the application.

    Args:
        body (ComplianceLevelCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceLevelResponse201 | PostComplianceLevelResponse400 | PostComplianceLevelResponse401 | PostComplianceLevelResponse403 | PostComplianceLevelResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
