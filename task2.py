from PIL import Image
import argparse

def xor_encrypt_decrypt(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Convert key to a repeating pattern
    key = [ord(char) for char in key]
    key_length = len(key)

    # Process the image pixels
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            key_value = key[(x + y) % key_length]
            r ^= key_value
            g ^= key_value
            b ^= key_value
            pixels[x, y] = (r, g, b)

    return img

def main():
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt an image using XOR.')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform')
    parser.add_argument('image', help='certificate.jpg')
    parser.add_argument('key', help='Encryption/Decryption key')

    args = parser.parse_args()

    img = xor_encrypt_decrypt(args.image, args.key)

    # Save the result
    if args.action == 'encrypt':
        img.save('encrypted_image.png')
    elif args.action == 'decrypt':
        img.save('decrypted_image.png')


if __name__ == "__main__":
    main()