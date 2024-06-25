import asyncio
import nats
from PIL import Image, ImageTk
import tkinter as tk
import io

class TkAsyncio:
    def __init__(self, root):
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.quit()
        self.root.destroy()
        asyncio.get_event_loop().stop()

    def run(self):
        asyncio.ensure_future(self.update_tk())
        asyncio.get_event_loop().run_forever()

    async def update_tk(self):
        while True:
            self.root.update()
            await asyncio.sleep(0.01)

async def main():
    # Connect to NATS
    nc = await nats.connect("demo.nats.io")

    # Subscribe to the camera.frames subject
    sub = await nc.subscribe("pc23")
    print("READY")

    async def receive_frame():
        while True:
            msg = await sub.next_msg()
            print("Received:", msg)
            # Decode JPEG frame
            buffer = io.BytesIO(msg.data)
            frame = Image.open(buffer)
            # Convert to PhotoImage for tkinter
            photo = ImageTk.PhotoImage(frame)
            # Update the tkinter label with the new frame
            label.config(image=photo)
            label.image = photo

    # Create a tkinter window
    root = tk.Tk()
    label = tk.Label(root)
    label.pack()

    # Create and start the tkinter/asyncio integration
    tk_asyncio = TkAsyncio(root)
    receiver_task = asyncio.create_task(receive_frame())

    # Start the combined event loop
    tk_asyncio.run()

    # Cleanup
    await receiver_task
    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
