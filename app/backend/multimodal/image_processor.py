from PIL import Image, ImageEnhance
from pathlib import Path


def process_image(image_path):

    image = Image.open(image_path)

    # Convert to RGB
    image = image.convert("RGB")

    # Resize large images
    max_size = (1200, 1200)
    image.thumbnail(max_size)

    # Improve contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.5)

    # Save processed image
    PROJECT_ROOT = Path(__file__).resolve().parents[3]

    processed_dir = PROJECT_ROOT / "data" / "processed"

    processed_dir.mkdir(parents=True, exist_ok=True)

    processed_path = processed_dir / f"processed_{Path(image_path).name}"

    image.save(processed_path)

    return str(processed_path)

