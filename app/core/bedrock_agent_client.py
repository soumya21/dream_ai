# app/core/bedrock_client.py
import boto3
from app.core.config import settings
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from typing import Optional
from fastapi import FastAPI

class BedrockClient:
    def __init__(self, agent_id: str, alias_id: str):
        self.agent_id = agent_id
        self.alias_id = alias_id
        self.client = boto3.client("bedrock-agent-runtime", settings.bedrock_agent_region,
                                   aws_access_key_id=settings.aws_access_key_id,
                                   aws_secret_access_key=settings.aws_secret_access_key,)
        print(f"BedrockClient initialized with Agent ID: {self.agent_id}")

    def validate_agent(self, prompt=None):
        try:
            # Perform a Bedrock agent invocation to check the connection
            test_input = "Test input for Bedrock agent"
            response = self.client.invoke_agent(
                agentId=self.agent_id,
                agentAliasId=self.alias_id,  # Correct parameter for alias ID
                sessionId='test-session-id',  # Unique session ID
                inputText=prompt  # Adjust the body format as needed
            )
            print(f"Bedrock agent successfully invoked: {response}")
        except NoCredentialsError:
            print("Credentials not found.")
            raise
        except ClientError as e:
            print(f"Client error: {e}")
            if e.response['Error']['Code'] == 'InvalidRequestException':
                print(f"Invalid request: {e.response['Error']['Message']}")
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                print(f"Agent not found: {e.response['Error']['Message']}")
            else:
                print(f"Error occurred: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def invoke_bedrock_agent(self, user_input: str):
        completion = ""
        traces =[]
        try:
            response = self.client.invoke_agent(
                agentId=self.agent_id,
                agentAliasId=self.alias_id,
                sessionId="test",
                inputText=user_input,
            )
            for event in response.get("completion"):
                print(event)
                try:
                    trace = event["trace"]
                    traces.append(trace['trace'])
                except KeyError:
                    chunk = event["chunk"]
                    completion = completion + chunk["bytes"].decode()
                except Exception as e:
                    print(e)

        except ClientError as e:
            print(e)

        return completion, traces

# Global variable to hold the BedrockClient instance
bedrock_client: Optional[BedrockClient] = None

def init_bedrock_client():
    global bedrock_client
    if not bedrock_client:
        try:
            # Initialize Bedrock client using environment variables
            bedrock_client = BedrockClient(
                agent_id=settings.agent_id,
                alias_id=settings.alias_id
            )
            # Validate the Bedrock agent to ensure it's correctly set up
            bedrock_client.validate_agent("List of holidays?")
        except Exception as e:
            print(f"Failed to initialize Bedrock client: {e}")
            bedrock_client = None
            raise e