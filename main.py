import asyncio
from typing import Any
from DataObjects import *

import PySimpleGUI as sg


data_groups = [

    [PingResource()]

]




async def events(window: sg.Window) -> tuple[Any, dict, list, None]:
    while True:
        event, values = window.read(timeout=100, timeout_key="__TIMEOUT__")
        if event == "__TIMEOUT__":
            continue
        elif event == sg.WINDOW_CLOSED:
            break
        else:
            yield event, values
        await asyncio.sleep(.1)


if __name__ == '__main__':
    window = sg.Window()
