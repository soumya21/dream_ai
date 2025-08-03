import json
import requests

def lambda_handler(event, context):
  agent = event.get('agent')
  function = event.get('function')
  actionGroup = event.get('actionGroup')
  parameters = event.get('parameters', {})

  # Extract parameters
  email_id = parameters.get('email_id')
  start_date = parameters.get('start_date')
  end_date = parameters.get('end_date')

  # Base URL for FastAPI application
  base_url = "https://7133-103-211-17-154.ngrok-free.app"  # Update with your FastAPI application URL
  apply_leave_url = f"{base_url}/apply-leave/"

  # Make API request to apply leave
  try:
    response = requests.post(apply_leave_url, json={
        "email_id": email_id,
        "start_date": start_date,
        "end_date": end_date
    })
    response_data = response.json()
      
    if response.status_code == 200:
      response_message = f"Leave applied successfully: {response_data}"
    else:
      response_message = f"Failed to apply leave: {response_data.get('detail', 'Unknown error')}"
  
  except Exception as e:
    response_message = f"Error applying leave: {str(e)}"

  #Prepare the response
  responseBody = {
    "TEXT": {
      "body": response_message
    }
  }

  action_response = {
    'actionGroup': actionGroup,
    'function': function,
    'functionResponse': {
      'responseBody': responseBody
    }
  }

  lambda_response = {
    'response': action_response,
    'messageVersion': event.get('messageVersion', '1.0')
  }

  print("Response: {}".format(lambda_response))

  return lambda_response
