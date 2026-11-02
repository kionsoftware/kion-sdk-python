from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_standard_create import ComplianceStandardCreate
from ...models.post_compliance_standard_response_201 import PostComplianceStandardResponse201
from ...models.post_compliance_standard_response_400 import PostComplianceStandardResponse400
from ...models.post_compliance_standard_response_401 import PostComplianceStandardResponse401
from ...models.post_compliance_standard_response_403 import PostComplianceStandardResponse403
from ...models.post_compliance_standard_response_422 import PostComplianceStandardResponse422
from ...models.post_compliance_standard_response_500 import PostComplianceStandardResponse500
from typing import cast



def _get_kwargs(
    *,
    body: ComplianceStandardCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/standard",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceStandardResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceStandardResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceStandardResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceStandardResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostComplianceStandardResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceStandardResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceStandardCreate,

) -> Response[PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500]:
    """ Creates a Compliance Standard.

    Args:
        body (ComplianceStandardCreate): ComplianceStandardCreate defines a Compliance Standard
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500]
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
    body: ComplianceStandardCreate,

) -> PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500 | None:
    """ Creates a Compliance Standard.

    Args:
        body (ComplianceStandardCreate): ComplianceStandardCreate defines a Compliance Standard
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceStandardCreate,

) -> Response[PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500]:
    """ Creates a Compliance Standard.

    Args:
        body (ComplianceStandardCreate): ComplianceStandardCreate defines a Compliance Standard
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500]
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
    body: ComplianceStandardCreate,

) -> PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500 | None:
    """ Creates a Compliance Standard.

    Args:
        body (ComplianceStandardCreate): ComplianceStandardCreate defines a Compliance Standard
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceStandardResponse201 | PostComplianceStandardResponse400 | PostComplianceStandardResponse401 | PostComplianceStandardResponse403 | PostComplianceStandardResponse422 | PostComplianceStandardResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
