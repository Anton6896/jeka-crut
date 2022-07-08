from pydantic import BaseModel


class User(BaseModel):
    """ instance of user in db """
    username: str
    data: str | None = None

    def get_table_name(self):
        return 'user_table'

    def serialize(self):
        return {
            'username': self.username,
            'data': self.data
        }
