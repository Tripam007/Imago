from PIL import Image, ImageEnhance, ImageFilter
import os

# Paths
path = './imgs'
pathOut = './editedImgs'

# Make sure output folder exists
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Menu of filters
print("\nChoose filters to apply (you can select multiple, separated by commas):")
print("1. Blur")
print("2. Gaussian Blur")
print("3. Contour")
print("4. Detail")
print("5. Edge Enhance")
print("6. Emboss")
print("7. Find Edges")
print("8. Smooth")
print("9. Sharpen")
print("10. Brightness")
print("11. Contrast")
print("12. Color (saturation)")
print("13. Sharpness (adjustable)")

# Take multiple choices
choices = input("\nEnter choice numbers (e.g., 9,11,12): ").split(",")

# Convert to integers & strip spaces
choices = [int(c.strip()) for c in choices if c.strip().isdigit()]

# Store factors for adjustable filters
factors = {}
for c in choices:
    if c in [10, 11, 12, 13]:  # needs factor
        factors[c] = float(input(f"Enter factor for filter {c}: "))

# Process images
for filename in os.listdir(path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        img = Image.open(f"{path}/{filename}")
        edit = img.copy()  # work on a copy

        # Apply filters in the order chosen
        for choice in choices:
            if choice == 1:
                edit = edit.filter(ImageFilter.BLUR)
            elif choice == 2:
                edit = edit.filter(ImageFilter.GaussianBlur(3))  # radius = 3
            elif choice == 3:
                edit = edit.filter(ImageFilter.CONTOUR)
            elif choice == 4:
                edit = edit.filter(ImageFilter.DETAIL)
            elif choice == 5:
                edit = edit.filter(ImageFilter.EDGE_ENHANCE_MORE)
            elif choice == 6:
                edit = edit.filter(ImageFilter.EMBOSS)
            elif choice == 7:
                edit = edit.filter(ImageFilter.FIND_EDGES)
            elif choice == 8:
                edit = edit.filter(ImageFilter.SMOOTH_MORE)
            elif choice == 9:
                edit = edit.filter(ImageFilter.SHARPEN)
            elif choice == 10:
                enhancer = ImageEnhance.Brightness(edit)
                edit = enhancer.enhance(factors[choice])
            elif choice == 11:
                enhancer = ImageEnhance.Contrast(edit)
                edit = enhancer.enhance(factors[choice])
            elif choice == 12:
                enhancer = ImageEnhance.Color(edit)
                edit = enhancer.enhance(factors[choice])
            elif choice == 13:
                enhancer = ImageEnhance.Sharpness(edit)
                edit = enhancer.enhance(factors[choice])

        # Save output
        clean_name = os.path.splitext(filename)[0]
        edit.save(f"{pathOut}/{clean_name}_edited.jpg")
        print(f"✅ Saved: {clean_name}_edited.jpg")

print("\n🎉 Done! All images processed with your chosen filters.")
