from uuid import UUID

from pydantic import BaseModel


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


class Submenu(CreateSubmenu):
    class Config:
        from_attributes = True
    id: UUID
    dishes_count: int


class CreateDish(BaseModel):
    title: str
    description: str
    price: float


class Dish(CreateDish):
    class Config:
        from_attributes = True
    id: UUID
