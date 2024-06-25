import asyncio
import nats
from PIL import Image, ImageTk
import tkinter as tk
import io

async def main():
    # Connect to NATS
    nc = await nats.connect("demo.nats.io")

    # Subscribe to the camera.frames subject
    sub = await nc.subscribe("camera.frames")
    print("READY")
    async def receive_frame():
        while True:
            msg = await sub.next_msg()
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

    # Start the receiving task
    receiver_task = asyncio.create_task(receive_frame())

    # Run the tkinter main loop
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
    finally:
        # Cancel the receiving task and close the NATS connection
        receiver_task.cancel()
        await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
