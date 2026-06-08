import asyncio
from abc import ABC, abstractmethod

class SharedIcon(ABC):
    def __init__(self, texture_path: str):
        self.texture = texture_path

    @abstractmethod
    async def draw_at(self, coordinates: str) -> str:
        pass

class MapIcon(SharedIcon):
    async def draw_at(self, coordinates: str) -> str:
        await asyncio.sleep(0.5)
        return f"Иконка [{self.texture}] отображена в точке {coordinates}"

class IconRegistry:
    def __init__(self):
        self._loaded_icons: dict[str, SharedIcon] = {}

    async def get_icon(self, texture_path: str) -> SharedIcon:
        return self._loaded_icons.setdefault(texture_path, MapIcon(texture_path))

    @property
    def total_loaded(self) -> int:
        return len(self._loaded_icons)

class MapObject:
    def __init__(self, icon: SharedIcon, unique_id: str):
        self._icon = icon
        self.location = unique_id

    async def display(self) -> str:
        return await self._icon.draw_at(self.location)
    

async def main():
    registry = IconRegistry()

    tree_icon = await registry.get_icon("tree.png")
    stone_icon = await registry.get_icon("stone.png")
    another_tree_icon = await registry.get_icon("tree.png")

    game_objects = [MapObject(tree_icon, "X:10, Y:20"),
                    MapObject(stone_icon, "X:55, Y:12"),
                    MapObject(another_tree_icon, "X:12, Y:88"),]

    tasks = [asyncio.create_task(obj.display()) for obj in game_objects]
    outputs = await asyncio.gather(*tasks)
    
    for output in outputs:
        print(output)
        
    print("---")
    print(f"Всего тяжелых текстур в памяти: {registry.total_loaded}")

if __name__ == "__main__":
    asyncio.run(main())