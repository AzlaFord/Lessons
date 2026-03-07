from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
# return a list of Results objects
results = model(["pizza.jpg", "plane.avif"])

for result in results:
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
