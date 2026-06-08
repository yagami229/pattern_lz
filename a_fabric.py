import asyncio
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    async def render(self) -> str:
        """Отрисовка кнопки"""
        pass

class Checkbox(ABC):
    @abstractmethod
    async def render(self) -> str:
        """Отрисовка чекбокса"""
        pass
    
    @abstractmethod
    async def bind_to_button(self, button: Button) -> str:
        """Привязка чекбокса к кнопке"""
        pass

class LightButton(Button):
    async def render(self) -> str:
        await asyncio.sleep(0.01)
        return "[Light Button]"

class LightCheckbox(Checkbox):
    async def render(self) -> str:
        await asyncio.sleep(0.01)
        return "[Light Checkbox]"
        
    async def bind_to_button(self, button: Button) -> str:
        button_style = await button.render()
        return f"{button_style} скомпонован с [Light Checkbox]"

class DarkButton(Button):
    async def render(self) -> str:
        await asyncio.sleep(0.01)
        return "[Dark Button]"

class DarkCheckbox(Checkbox):
    async def render(self) -> str:
        await asyncio.sleep(0.01)
        return "[Dark Checkbox]"
        
    async def bind_to_button(self, button: Button) -> str:
        button_style = await button.render()
        return f"{button_style} скомпонован с [Dark Checkbox]"



class UI_Factory(ABC):
    @abstractmethod
    async def get_button(self) -> Button: pass
    
    @abstractmethod
    async def get_checkbox(self) -> Checkbox: pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass



class LightThemeFactory(UI_Factory):
    async def get_button(self) -> Button:
        return LightButton()
        
    async def get_checkbox(self) -> Checkbox:
        return LightCheckbox()

class DarkThemeFactory(UI_Factory):
    async def get_button(self) -> Button:
        return DarkButton()
        
    async def get_checkbox(self) -> Checkbox:
        return DarkCheckbox()


async def initialize_ui(factory: UI_Factory):
    async with factory as active_factory:
        btn_task = asyncio.create_task(active_factory.get_button())
        chkbx_task = asyncio.create_task(active_factory.get_checkbox())
        
        button = await btn_task
        checkbox = await chkbx_task
        
        print(f"Компонент 1: {await button.render()}")
        print(f"Компонент 2: {await checkbox.render()}")
        print(f"Связь: {await checkbox.bind_to_button(button)}")

async def main():
    print("--- Запуск Светлой темы ---")
    await initialize_ui(LightThemeFactory())
    
    print("\n--- Запуск Темной темы ---")
    await initialize_ui(DarkThemeFactory())

if __name__ == "__main__":
    asyncio.run(main())