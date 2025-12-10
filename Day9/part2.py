from PIL import Image, ImageDraw
from shapely.geometry import Polygon

# inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day9/example"
inputName = "/Users/debbieurquhart/code_projects/AOC-25/Day9/input"

points = []

with open(inputName) as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue

        x, y = line.split(",")
        points.append((int(x), int(y)))


def save_polygon_png(points, output_file="day9_polygon.png"):
    # Use Shapely to fix the polygon (correct ordering, remove self-crossings)
    poly = Polygon(points)

    # Extract the exterior ring (the valid usable outline)
    exterior = list(poly.exterior.coords)

    # Compute bounding box
    xs = [x for x, y in exterior]
    ys = [y for x, y in exterior]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    img_size = 2000
    padding = 50

    span_x = max_x - min_x
    span_y = max_y - min_y

    scale_x = (img_size - 2 * padding) / span_x
    scale_y = (img_size - 2 * padding) / span_y
    scale = min(scale_x, scale_y)

    # Create blank image
    img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)

    # Convert to image coordinates (flip Y to look like a grid)
    poly_pts = []
    for (x, y) in exterior:
        cx = padding + (x - min_x) * scale
        cy = padding + (y - min_y) * scale
        cy = img_size - cy
        poly_pts.append((cx, cy))

    # Draw filled polygon with red outline
    draw.polygon(poly_pts, fill=(200, 255, 200), outline="red")

    # Draw the red vertices
    r = 4
    for (cx, cy) in poly_pts:
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="red")

    img.save(output_file)
    print(f"Saved polygon image as: {output_file}")


# Call the function
save_polygon_png(points, "day9_polygon.png")
