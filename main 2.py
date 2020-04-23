#Encodes obj using the codec registered for encoding
import codecs
phrase = input("Enter Phrase you want to Encrypt or Decrypt: ")
# Apply codecs twice to get back original input
print(codecs.encode(phrase, 'rot_13'))