# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T12:32:30+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity

app = MCPProxy(
    contact={'email': 'apisupport@zenoti.com', 'x-twitter': 'ZenotiSoftware'},
    description='Our API documentation has been moved to https://docs.zenoti.com. \n\n',
    title='Zenoti API',
    version='1.0.0',
    servers=[{'url': 'https://api.zenoti.com'}],
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
