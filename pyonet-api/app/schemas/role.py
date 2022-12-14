from pydantic import BaseModel
from fastapi import Query
from typing import Optional 
from app.schemas.permission import PermissionModel   


class RoleModel(BaseModel):          
    roleid: Optional[int]  = Query(None, title="roleid", form_options={"optional":1,"display":0}) 
    name: str  = Query(..., title="name", max_length=32, form_options={}) 
    description: str  = Query(..., title="description", max_length=128, form_options={})

class RoleCreateModel(BaseModel):
    name: str  = Query(..., title="name", max_length=32, form_options={}) 
    description: str  = Query(..., title="description", max_length=128, form_options={})
    permissions: Optional[list[int]] = []

class RoleUpdateModel(BaseModel):
    name: Optional[str]  = Query(..., title="name", max_length=32, form_options={}) 
    description: Optional[str]  = Query(..., title="description", max_length=128, form_options={})
    permissions: Optional[list[int]] = []


class RoleJoinedModel(RoleModel):
    permissions: list[PermissionModel] = []