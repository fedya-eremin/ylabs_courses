from pydantic import BaseModel

from uuid import UUID


class CreateMenu(BaseModel):
    title: str
    description: str


class Menu(CreateMenu):
    id: UUID
    submenus_count: int
    dishes_count: int


class CreateSubmenu(BaseModel):
    title: str
    description: str
    menu_id: UUID


class Submenu(BaseModel):
    class Config:
        orm_mode = True
    id: UUID
    dishes_count: int


class CreateDish(BaseModel):
    title: str
    description: str
    price: float
    submenu_id: UUID


class Dish(CreateDish):
    class Config:
        orm_mode = True
    id: UUID
