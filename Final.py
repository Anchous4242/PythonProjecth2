import cv2
from PIL import Image

image_path = 'mem.jpg'
glasses_path = 'glasses.png'
chain_path = 'necklace.png'
cascade_path = 'haarcascade_frontalcatface_extended.xml'
cat_face_cascade = cv2.CascadeClassifier(cascade_path)
image = cv2.imread(image_path)
cat = Image.open(image_path).convert("RGBA")
glasses = Image.open(glasses_path).convert("RGBA")
chain = Image.open(chain_path).convert("RGBA")
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
    resized_glasses = glasses.resize((w, int(h / 3)))
    cat.paste(resized_glasses, (x + 5, int(y + h / 3)), resized_glasses)
    resized_chain = chain.resize((w, int(h / 3)))
    chain_y = y + h
    cat.paste(resized_chain, (x, chain_y), resized_chain)
cat.save("cat_with_glasses_and_chain.png")
cat_with_accessories = cv2.imread("cat_with_glasses_and_chain.png")
cv2.imshow("Cat with Glasses and Chain", cat_with_accessories)
cv2.waitKey(0)
cv2.destroyAllWindows()