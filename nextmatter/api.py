import requests
from dotenv import load_dotenv
import os
from nextmatter.classes.file import File
from nextmatter.classes.image import Image
from nextmatter.classes.instance import Instance
from nextmatter.classes.workflow import Workflow
from nextmatter.classes.form_field import FormField
from nextmatter.exceptions import (
    NextMatterException,
    NextMatterCacheException,
    RatelimitBudgetExceeded,
    APIException,
    RecordNotFoundException,
    TooManyValuesException,
    SearchResponseLimitExceeded,
    InvalidQueryParamException
)

load_dotenv()

class NextMatterAPI:
    """
    Client for interacting with the NextMatter API.
    """

    def __init__(self, api_key: str = None):
        """
        Initialize the NextMatterAPI client.

        :param api_key: API key for authenticating with the NextMatter API.
        """
        try:
            self.api_key = api_key or os.getenv('NEXTMATTER_API_KEY')
            if not self.api_key:
                raise ValueError("API key must be provided or set in the environment variables.")
            
            self.base_url = "https://core.nextmatter.com/api/"
            self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            self.session = requests.Session()
            self.session.headers.update(self.headers)

            self.file = File(self)
            self.image = Image(self)
            self.instance = Instance(self)
            self.workflow = Workflow(self)
            self.form_field = FormField(self)
        except Exception as e:
            raise NextMatterException(f"Failed to initialize NextMatterAPI: {e} \n\n\nMore info: https://help.nextmatter.com/reference/intro/authentication")