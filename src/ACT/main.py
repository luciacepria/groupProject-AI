import os
import time
from dotenv import load_dotenv
from src.ACT.crew import ACTCrew
from litellm.exceptions import RateLimitError

load_dotenv()

api_key4 = os.getenv('EDENAI_KEY')

def run():
    inputs = {
        'company_name': 'Tesla', 
    }

    crew_instance = ACTCrew()

    max_retries = 3
    for attempt in range(max_retries):
        try:
            crew_instance.crew().kickoff(inputs=inputs)
            break
        except RateLimitError as e:
            print(f"The number of attempts has been exceeded, retrying... {attempt + 1}/{max_retries}")
            time.sleep(2 ** attempt)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    run()
