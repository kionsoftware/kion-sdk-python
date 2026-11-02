from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.aws_account_creation_config import AWSAccountCreationConfig
from ...models.put_aws_account_creation_config_response_200 import PutAWSAccountCreationConfigResponse200
from ...models.put_aws_account_creation_config_response_401 import PutAWSAccountCreationConfigResponse401
from ...models.put_aws_account_creation_config_response_403 import PutAWSAccountCreationConfigResponse403
from ...models.put_aws_account_creation_config_response_500 import PutAWSAccountCreationConfigResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AWSAccountCreationConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/app-config/aws-account-creation",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = PutAWSAccountCreationConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PutAWSAccountCreationConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutAWSAccountCreationConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PutAWSAccountCreationConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCreationConfig,

) -> Response[PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500]:
    """ Sets the account creation settings used for programmatically creating new AWS accounts

    Args:
        body (AWSAccountCreationConfig): AWSAccountCreationConfig represents the system settings
            for creating AWS accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500]
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
    body: AWSAccountCreationConfig,

) -> PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500 | None:
    """ Sets the account creation settings used for programmatically creating new AWS accounts

    Args:
        body (AWSAccountCreationConfig): AWSAccountCreationConfig represents the system settings
            for creating AWS accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCreationConfig,

) -> Response[PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500]:
    """ Sets the account creation settings used for programmatically creating new AWS accounts

    Args:
        body (AWSAccountCreationConfig): AWSAccountCreationConfig represents the system settings
            for creating AWS accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500]
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
    body: AWSAccountCreationConfig,

) -> PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500 | None:
    """ Sets the account creation settings used for programmatically creating new AWS accounts

    Args:
        body (AWSAccountCreationConfig): AWSAccountCreationConfig represents the system settings
            for creating AWS accounts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutAWSAccountCreationConfigResponse200 | PutAWSAccountCreationConfigResponse401 | PutAWSAccountCreationConfigResponse403 | PutAWSAccountCreationConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
