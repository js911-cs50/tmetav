import cv2
import depthai as dai

# 1. Initialize the v3 Pipeline
pipeline = dai.Pipeline()

# 2. Create and build the unified Camera node
cam = pipeline.create(dai.node.Camera).build(boardSocket=dai.CameraBoardSocket.CAM_A)

# 3. Request a standard 640x480 BGR planar output stream
rgb_out = cam.requestOutput(size=(640, 480), type=dai.ImgFrame.Type.BGR888p, fps=30)

# 4. Create your output stream queue directly from the stream endpoint
q_rgb = rgb_out.createOutputQueue(maxSize=4, blocking=False)

# 5. Start and run the pipeline
pipeline.start()
print("Camera running! Press 'q' on the video window to exit.")

with pipeline:
    while pipeline.isRunning():
        # Fetch the frame from the queue
        in_rgb = q_rgb.get()
        frame = in_rgb.getCvFrame()
        
        # Display the live stream
        cv2.imshow("OAK-D Live Feed (v3 API)", frame)
        
        if cv2.waitKey(1) == ord('q'):
            break





cv2.destroyAllWindows()