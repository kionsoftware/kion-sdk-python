from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_program_create import ComplianceProgramCreate
from ...models.post_compliance_program_response_201 import PostComplianceProgramResponse201
from ...models.post_compliance_program_response_400 import PostComplianceProgramResponse400
from ...models.post_compliance_program_response_401 import PostComplianceProgramResponse401
from ...models.post_compliance_program_response_403 import PostComplianceProgramResponse403
from ...models.post_compliance_program_response_422 import PostComplianceProgramResponse422
from ...models.post_compliance_program_response_500 import PostComplianceProgramResponse500
from typing import cast



def _get_kwargs(
    *,
    body: ComplianceProgramCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/compliance/program",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceProgramResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceProgramResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceProgramResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceProgramResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostComplianceProgramResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceProgramResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceProgramCreate,

) -> Response[PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500]:
    """ Creates a Compliance Program.

    Args:
        body (ComplianceProgramCreate): ComplianceProgramCreate defines a Compliance Program
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500]
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
    body: ComplianceProgramCreate,

) -> PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500 | None:
    """ Creates a Compliance Program.

    Args:
        body (ComplianceProgramCreate): ComplianceProgramCreate defines a Compliance Program
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ComplianceProgramCreate,

) -> Response[PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500]:
    """ Creates a Compliance Program.

    Args:
        body (ComplianceProgramCreate): ComplianceProgramCreate defines a Compliance Program
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500]
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
    body: ComplianceProgramCreate,

) -> PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500 | None:
    """ Creates a Compliance Program.

    Args:
        body (ComplianceProgramCreate): ComplianceProgramCreate defines a Compliance Program
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceProgramResponse201 | PostComplianceProgramResponse400 | PostComplianceProgramResponse401 | PostComplianceProgramResponse403 | PostComplianceProgramResponse422 | PostComplianceProgramResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
