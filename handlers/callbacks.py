async def callback_continue(callback):
    await callback.message.answer(text="Успешно вызван callbacks!")