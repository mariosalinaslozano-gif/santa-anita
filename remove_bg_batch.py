from pathlib import Path
from rembg import remove

# Input/output folders
input_dir = Path(r"C:\Users\mario\santa-anita\public\Designs")
output_dir = Path(r"C:\Users\mario\santa-anita\public\Designs\no-bg")
output_dir.mkdir(parents=True, exist_ok=True)

# Supported image extensions
exts = {".png", ".jpg", ".jpeg", ".webp"}

for img_path in input_dir.iterdir():
    if img_path.suffix.lower() in exts and img_path.is_file():
        out_path = output_dir / f"{img_path.stem}-nobg.png"

        with img_path.open("rb") as f:
            input_data = f.read()

        output_data = remove(input_data)  # transparent background

        with out_path.open("wb") as f:
            f.write(output_data)

        print(f"Saved: {out_path}")

print("Done.")