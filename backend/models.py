from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

class TodoList(Model):
    id = fields.IntField(pk=True)
    item = fields.CharField(max_length=100, nullable=False)
    completed = fields.BooleanField(default=False)
    
# create  pydantic models
todo_list_pydantic = pydantic_model_creator(TodoList, name="TodoList")
todo_list_pydantic_in = pydantic_model_creator(TodoList, name="TodoListIn", exclude_readonly=True)