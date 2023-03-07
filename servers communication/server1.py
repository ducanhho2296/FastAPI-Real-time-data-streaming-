from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import fields
import tortoise
app = FastAPI()

# Define the database connection settings
DATABASE_URL = "postgres://user:password@localhost:5432/mydatabase"

# Define the database models
class MyModel(tortoise.models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    class Meta:

