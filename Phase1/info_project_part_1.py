# -*- coding: utf-8 -*-
"""Info Project Part 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NoEQzp31EpVFVVvTR8XcfZlvikxramS1

# Setup

Importing file
"""

from google.colab import files


text_file = files.upload()

"""1. Computing an estimate of the
probabilities of the different English characters (symbols) in this text
file
"""

# saving the text in the file in a string
text = text_file["Test_text_file.txt"]

text = str(text)
text = text[2:len(text)-1]

# create dictionary with character and their coressponding probability
char_probability = {}
for i in range(97, 123):
    char_probability[chr(i)] = 0
char_probability['('] = 0
char_probability[')'] = 0
char_probability['.'] = 0
char_probability[','] = 0
char_probability['/'] = 0
char_probability['-'] = 0
char_probability[' '] = 0

for c in text:
    char_probability[c] += 1
for x in char_probability:
    char_probability[x] = char_probability[x]/len(text)
print(char_probability)

"""2. Calculating the entropy"""

import math
entropy = 0
for c in char_probability:
    entropy += -char_probability[c] * math.log2(char_probability[c])

entropy

"""3. Calculating the number of bits/symbol in a fixed length
code and its effeciency
"""

bits_fixed_length =  math.ceil(math.log2(len(char_probability)))
effeciency_fixed_length = entropy/bits_fixed_length
print("fixed length code\t "+ str(bits_fixed_length) + " bits/symbol\n", "effeciency\t\t", effeciency_fixed_length*100, " %")

"""# Huffman

4. Encoder
"""

# creating class for tree node
class Node:
    def __init__(self, char=None, probability=0):
        self.char = char
        self.probability = probability
        self.left = None
        self.right = None

# initializing nodes
tree = []
for x in char_probability:
    tree.append(Node(x, char_probability[x]))

# creating tree
while(len(tree) > 1):
    tree.sort(key = lambda p: -p.probability)  # sort probabilities descendingly
    left = tree.pop()
    right = tree.pop()
    node = Node('*',left.probability + right.probability)
    node.right = right
    node.left = left
    tree.append(node)



# creating code
char_code = {}
for x in char_probability:
    char_code[x] = ""

def code(node, node_code):
    if node:
        if node.char != '*':
            char_code[node.char] = node_code
        code(node.left, node_code + "0")
        code(node.right, node_code  + "1")

code(tree[0],'')

def encode_huffman(text):
    encoded_text = ""
    for s in text:
        encoded_text += char_code[s]

    return encoded_text

huffman_encoded_text = encode_huffman(text)

"""5. Decoder"""

# Decode the Huffman encoded text directly
def decode_huffman(encoded_text, root):
    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        # If a leaf node is reached, append the character and reset to root
        if current_node.char != '*':  # Leaf node
            decoded_text += current_node.char
            current_node = root  # Reset to root for the next character

    return decoded_text

# Decode the encoded text
decoded_text = decode_huffman(huffman_encoded_text, tree[0])

# Print the decoded text
print("Decoded Text:")
print(decoded_text)

with open("decode_file.txt", "w") as file:
    file.write(decoded_text)

"""comparing decoded stream with the original stream"""

def CompareTexts(text1, text2):
  if len(text1) != len(text2):
    return False
  for i in range(0, len(text1)):
    if text1[i] != text2[i]:
      print(i)
      return False
  return True

print("Texts are the same") if CompareTexts(text, decoded_text) else print("Texts are not the same")

"""6. Calculating the efficiency of the Huffman code"""

def CalculateEfficiencyHuffman():
  average_code_length = 0
  for code in char_code:
    average_code_length += len(char_code[code]) * char_probability[code]
  return entropy / average_code_length

print("Huffman code efficiency: ", CalculateEfficiencyHuffman())

"""# Shannon-Fano

7. Encoder
"""

from pprint import pprint
def ShannonFanoEncoder(symbols):
  codes = {}
  assignCodes(symbols, "", codes)
  return codes

def assignCodes(symbols, prefix, codes):
    if len(symbols) == 1:
        codes[symbols[0][0]] = prefix
        return

    splitPoint = findSplitPoint(symbols)
    firstGroup = symbols[:splitPoint + 1]
    secondGroup = symbols[splitPoint + 1:]

    assignCodes(firstGroup, prefix + "0", codes)
    assignCodes(secondGroup, prefix + "1", codes)


def findSplitPoint(symbols):
    totalFrequency = 0
    for i in range(0, len(symbols)):
        totalFrequency += symbols[i][1]

    cumulativeFrequency = 0
    half_total = totalFrequency / 2
    for i in range(0, len(symbols)):
        cumulativeFrequency += symbols[i][1]
        if cumulativeFrequency >= half_total:
          return i if (abs(cumulativeFrequency - half_total) < abs(cumulativeFrequency - (half_total + symbols[i][1]))) else i - 1


    return len(symbols) - 1

def EncodeText(text, codes):
  encoded_text = ""
  for char in text:
    encoded_text += codes[char]
  return encoded_text


char_probability1 = {
    'a': 0.3,
    'b': 0.25,
    'c': 0.2,
    'd': 0.15,
    'e': 0.1
}
text1 = "abcdabcdabdd"

sorted_char_probability = sorted(char_probability.items(), key=lambda x: x[1],  reverse=True)
codes = ShannonFanoEncoder(sorted_char_probability)
encoded_text = EncodeText(text, codes)

"""Decoder"""

def ShannonFanoDecoder(encoded_text, codes):
    decoded_text = ""
    current_code = ""
    for char in encoded_text:
        current_code += char
        for code in codes:
            if codes[code] == current_code:
                decoded_text += code
                current_code = ""
                break
    return decoded_text


decoded_text = ShannonFanoDecoder(encoded_text, codes)

"""comparing decoded stream with the original stream"""

def CompareTexts(text1, text2):
  if len(text1) != len(text2):
    return False
  for i in range(0, len(text1)):
    if text1[i] != text2[i]:
      print(i)
      return False
  return True

print("Texts are the same") if CompareTexts(text, decoded_text) else print("Texts are not the same")

"""Calculating the efficiency of the Shannon-Fano code"""

def CalculateEfficiencyShannon():
  average_code_length = 0
  for code in codes:
    average_code_length += len(codes[code]) * char_probability[code]
  return entropy / average_code_length

print("Shannon-Fano code efficiency: ", CalculateEfficiencyShannon())

"""**8-Efficiency Comparison: Shannon-Fanovs. Huffman Codes**"""

# Comparison Function using pre-computed variables
def compare_coding_methods(fixed_avg_length, huffman_avg_length, shannon_fano_avg_length,
                           fixed_efficiency, huffman_efficiency, shannon_fano_efficiency):
    # Display Results
    print(f"{'Method':<15} {'Average Length':<20} {'Efficiency (%)':<20}")
    print(f"{'Fixed-Length':<15} {fixed_avg_length:<20.4f} {fixed_efficiency * 100:<20.2f}")
    print(f"{'Huffman':<15} {huffman_avg_length:<20.4f} {huffman_efficiency * 100:<20.2f}")
    print(f"{'Shannon-Fano':<15} {shannon_fano_avg_length:<20.4f} {shannon_fano_efficiency * 100:<20.2f}")

# Call the function with the pre-computed values
compare_coding_methods(bits_fixed_length, math.ceil(CalculateEfficiencyHuffman()*entropy), math.ceil(CalculateEfficiencyShannon()*entropy),
                       effeciency_fixed_length, CalculateEfficiencyHuffman(), CalculateEfficiencyShannon())